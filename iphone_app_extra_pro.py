import os
import json
from datetime import datetime
from pymobiledevice3.lockdown import create_using_usbmux
from pymobiledevice3.services.installation_proxy import InstallationProxyService
from colorama import init, Fore, Style

# Inizializza colorama per supportare i colori su Windows
init()

# Nomi dei file dei database locali
LEGITIMATE_APPS_FILE = "legitimate_apps.json"
ILLEGITIMATE_APPS_FILE = "illegitimate_apps.json"

def load_legitimate_apps_database(filename=LEGITIMATE_APPS_FILE):
    """
    Carica il database locale di app legittime da un file JSON.
    Se il file non esiste, crea uno di default con alcune app.
    """
    default_apps = {
        "com.apple.mobileslideshow": "Photos",
        "com.apple.camera": "Camera",
        "com.apple.mobilemail": "Mail",
        "com.apple.mobilecal": "Calendar",
        "com.apple.mobilesafari": "Safari",
        "com.apple.Preferences": "Settings",
        "com.apple.MobileSMS": "Messages",
        "com.apple.mobilephone": "Phone",
        "com.whatsapp": "WhatsApp",
        "org.telegram.messenger": "Telegram",
        "com.google.chrome": "Chrome",
        "com.google.gmail": "Gmail"
    }
    
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(default_apps, f, indent=4)
        print(f"Creato database di default: {filename}")
        return default_apps
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception as e:
        print(f"Errore nel caricamento del database legittimo: {e}. Uso database di default.")
        return default_apps

def load_illegitimate_apps_database(filename=ILLEGITIMATE_APPS_FILE):
    """
    Carica il database locale di app malevole da un file JSON.
    Se il file non esiste, crea uno vuoto.
    """
    default_apps = {}
    
    if not os.path.exists(filename):
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(default_apps, f, indent=4)
        print(f"Creato database vuoto per app malevole: {filename}")
        return default_apps
    
    try:
        with open(filename, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return {bundle_id: "App malevola sconosciuta" for bundle_id in data}
            return data
    except Exception as e:
        print(f"Errore nel caricamento del database malevolo: {e}. Uso database vuoto.")
        return default_apps

def is_app_legitimate(bundle_id, legitimate_apps, illegitimate_apps):
    """
    Verifica lo stato dell'app:
    - Legitimate: presente nel database legittimo
    - Malicious: presente nel database malevolo
    - Suspicious: non presente in nessuno dei due
    """
    if bundle_id in legitimate_apps:
        return "Legitimate"
    if bundle_id in illegitimate_apps:
        return "Malicious"
    return "Suspicious"

def has_suspicious_behavior(app_data):
    """
    Controlla se un'app ha comportamenti anomali basati sui metadati disponibili.
    """
    if isinstance(app_data, dict):
        bundle_id = app_data.get("CFBundleIdentifier", "Sconosciuto")
        app_name = app_data.get("CFBundleName", bundle_id)
        
        if app_name == "Sconosciuto" or app_name == bundle_id:
            return "Nome mancante o incoerente"
        if not bundle_id.startswith("com.") and not bundle_id.startswith("org."):
            return "Bundle ID non convenzionale"
        return None
    return "Dati insufficienti"

def get_installed_apps():
    try:
        # Carica i database locali
        legitimate_apps = load_legitimate_apps_database()
        illegitimate_apps = load_illegitimate_apps_database()
        
        # Crea una connessione al dispositivo iOS tramite USB
        lockdown = create_using_usbmux()
        app_service = InstallationProxyService(lockdown=lockdown)

        # Recupera metadati del dispositivo
        device_info = {
            "imei": lockdown.get_value(key="InternationalMobileEquipmentIdentity") or "Non disponibile",
            "model": lockdown.get_value(key="ProductType") or "Non disponibile",
            "ios_version": lockdown.get_value(key="ProductVersion") or "Non disponibile",
            "serial": lockdown.get_value(key="SerialNumber") or "Non disponibile",
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        # Estrai l'elenco delle applicazioni installate
        apps = app_service.get_apps()

        # Crea una lista di dizionari con nome, Bundle ID, stato e anomalie
        app_list = []
        for app in apps:
            if isinstance(app, dict):
                bundle_id = app.get("CFBundleIdentifier", "Sconosciuto")
                app_name = app.get("CFBundleName", bundle_id)
            elif isinstance(app, str):
                bundle_id = app
                app_name = "Sconosciuto"
            else:
                continue

            # Verifica lo stato dell'app
            status = is_app_legitimate(bundle_id, legitimate_apps, illegitimate_apps)

            # Controlla comportamenti sospetti solo per app Suspicious o Malicious
            anomaly = has_suspicious_behavior(app) if status != "Legitimate" else None

            # Evidenziazione visiva nel terminale con colorama
            if status == "Malicious":
                print(f"{Fore.RED}ATTENZIONE: Trovata app malevola - {app_name} ({bundle_id}) | Nota: {illegitimate_apps.get(bundle_id)}{Style.RESET_ALL}")
            elif status == "Suspicious" and anomaly:
                print(f"{Fore.YELLOW}NOTA: App sospetta con anomalia - {app_name} ({bundle_id}) | Anomalia: {anomaly}{Style.RESET_ALL}")

            app_list.append({
                "name": app_name,
                "bundle_id": bundle_id,
                "status": status,
                "anomaly": anomaly,
                "known_name": illegitimate_apps.get(bundle_id) if status == "Malicious" else None
            })

        return app_list, device_info

    except Exception as e:
        print(f"Errore durante l'estrazione delle app o dei metadati: {e}")
        return [], {"imei": "Non disponibile", "model": "Non disponibile", "ios_version": "Non disponibile", "serial": "Non disponibile", "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}

def save_to_file(app_list, device_info, filename="installed_apps.txt"):
    try:
        with open(filename, "w", encoding="utf-8") as file:
            file.write(f"Analisi eseguita il: {device_info['timestamp']}\n")
            file.write(f"IMEI: {device_info['imei']}\n")
            file.write(f"Modello: {device_info['model']}\n")
            file.write(f"Versione iOS: {device_info['ios_version']}\n")
            file.write(f"Numero di serie: {device_info['serial']}\n")
            file.write("-" * 50 + "\n")
            if not app_list:
                file.write("Nessuna applicazione trovata o errore di connessione.\n")
            else:
                file.write("Elenco delle applicazioni installate:\n")
                file.write("-" * 50 + "\n")
                for app in app_list:
                    line = f"{app['name']} | Bundle ID: {app['bundle_id']} | Status: {app['status']}"
                    if app["known_name"] and app["status"] == "Malicious":
                        line += f" | Nota: {app['known_name']}"
                    if app["anomaly"]:
                        line += f" | Anomalia: {app['anomaly']}"
                    file.write(line + "\n")
        print(f"Elenco salvato con successo in {filename}")
    except Exception as e:
        print(f"Errore durante il salvataggio del file: {e}")

def main():
    print("Collega il tuo iPhone tramite USB e assicurati che sia sbloccato...")
    apps, device_info = get_installed_apps()
    save_to_file(apps, device_info)

if __name__ == "__main__":
    main()