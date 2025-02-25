# 📱 iPhone App Extractor Pro

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg) ![License](https://img.shields.io/badge/License-MIT-green.svg) ![Status](https://img.shields.io/badge/Status-Stable-brightgreen.svg)

Benvenuto in **iPhone App Extractor Pro**, uno strumento Python progettato per estrarre l'elenco delle applicazioni installate su un iPhone connesso via USB a un computer Windows 11. Questo programma è pensato per analisti forensi che vogliono identificare spyware, malware e altre app sospette in modo rapido e affidabile! 🚨

Con questo tool, puoi:
- 📋 Estrarre l’elenco completo delle app installate.
- 🔍 Identificare app legittime, sospette e malevole usando database locali.
- 🖨️ Salvare i risultati in un file TXT con metadati del dispositivo (IMEI, modello, versione iOS, ecc.).
- 🎨 Visualizzare avvisi colorati nel terminale per app pericolose.

---

## ✨ Funzionalità Principali

- **Connessione USB**: Collega il tuo iPhone a un PC Windows 11 via USB e analizza le app installate.
- **Database Locali**:
  - `legitimate_apps.json`: Elenco di app considerate sicure (es. app di sistema Apple e app comuni).
  - `illegitimate_apps.json`: Elenco di app malevole note (es. spyware come mSpy o FlexiSpy).
- **Classificazione**:
  - ✅ **Legitimate**: App presenti nel database delle app sicure.
  - 🚨 **Malicious**: App elencate come malevole (con nome noto, se disponibile).
  - ⚠️ **Suspicious**: App non riconosciute, con controllo di anomalie (es. nome mancante, Bundle ID strano).
- **Metadati del Dispositivo**: Include IMEI, modello, versione iOS, numero di serie e timestamp dell’analisi.
- **Output Colorato**: Evidenziazione visiva nel terminale con rosso per app malevole e giallo per sospette con anomalie.
- **File di Output**: Risultati salvati in `installed_apps.txt` con dettagli chiari e leggibili.

---

## 🛠️ Come Funziona

### 1. **Estrazione delle App**
Il programma usa la libreria `pymobiledevice3` per connettersi all’iPhone tramite USB e recuperare l’elenco delle app installate con il servizio `InstallationProxyService`. Per ogni app, estrae:
- Nome (`CFBundleName`).
- Bundle ID (`CFBundleIdentifier`).

### 2. **Classificazione**
- Confronta ogni Bundle ID con:
  - `legitimate_apps.json`: Se presente, l’app è "Legitimate".
  - `illegitimate_apps.json`: Se presente, l’app è "Malicious" e mostra il nome noto (es. "mSpy").
  - Se non è in nessuno dei due, diventa "Suspicious".
- Controlla anomalie nei metadati per app sospette/malevole (es. nome mancante o Bundle ID non convenzionale).

### 3. **Metadati del Dispositivo**
Recupera informazioni dall’iPhone usando `LockdownClient`:
- IMEI.
- Modello (es. "iPhone14,5").
- Versione iOS (es. "18.3").
- Numero di serie.
- Timestamp dell’analisi.

### 4. **Output**
- **Terminale**: Mostra avvisi colorati:
  - Rosso (`Fore.RED`) per app malevole.
  - Giallo (`Fore.YELLOW`) per app sospette con anomalie.
- **File TXT**: Salva tutto in `installed_apps.txt` con un’intestazione dettagliata.

---

## 📦 Prerequisiti

- Sistema operativo: **Windows 11**.
- Python: **3.9 o superiore**.
- iPhone connesso via USB, sbloccato e autorizzato ("Fidati" del computer).

### Dipendenze
- `pymobiledevice3`: Per comunicare con l’iPhone.
- `colorama`: Per l’evidenziazione dei colori nel terminale.

---

## 🚀 Installazione

1. **Clona il Repository**:
   ```bash
   git clone https://github.com/marcko80/iphone-app-extractor-pro.git
   cd iphone-app-extractor-pro

## 📝 Guida Passo-Passo per Utilizzare iPhone App Extractor Pro
Segui questa guida per configurare ed eseguire lo script iphone_app_extra_pro.py sul tuo computer Windows 11 e analizzare le applicazioni installate su un iPhone. Ogni passo è descritto minuziosamente per garantirti un’esperienza senza intoppi! 🚀

1. Preparazione dell’Ambiente
Prima di eseguire lo script, assicurati di avere tutto il necessario installato sul tuo PC.
Verifica il Sistema Operativo:
Assicurati di usare Windows 11. Lo script è ottimizzato per questo sistema.
Installa Python:
Scarica Python (versione 3.9 o superiore) da python.org.
Durante l’installazione, seleziona "Add Python to PATH" per abilitare l’uso dal terminale.
Verifica l’installazione aprendo un terminale (Prompt dei comandi o PowerShell) e digitando:
bash
python --version
Dovresti vedere qualcosa come Python 3.11.2.

Installa le Dipendenze Python:
Apri il terminale e installa le librerie necessarie:
bash
pip install pymobiledevice3 colorama
pymobiledevice3: Comunica con l’iPhone.
colorama: Abilita i colori nel terminale.
Installa libimobiledevice:
Usa Scoop, un gestore di pacchetti per Windows:
Apri PowerShell come amministratore e installa Scoop:
powershell
iwr -useb get.scoop.sh | iex
Installa libimobiledevice:
powershell
scoop install libimobiledevice
Questo è necessario per far funzionare pymobiledevice3.

3. Download dello Script
Ottieni il codice sorgente e preparalo per l’esecuzione.
Scarica lo Script:
Se hai Git installato:
bash
git clone https://github.com/marcko/iphone-app-extractor-pro.git
cd iphone-app-extractor-pro
Altrimenti, scarica il file iphone_app_extra_pro.py manualmente dal repository e salvalo in una cartella (es. D:\Progetti\iPhoneAnalyzer).
Verifica la Directory:
Apri il terminale e naviga nella cartella dello script:
bash
cd D:\Progetti\iPhoneAnalyzer

5. Configurazione dei Database
Lo script usa due file JSON per classificare le app. Configurali prima dell’esecuzione.
Database delle App Legittime (legitimate_apps.json):
Se non esiste, lo script lo crea automaticamente con un elenco di default (es. Photos, WhatsApp).
Puoi modificarlo manualmente aggiungendo altre app sicure. Esempio:
json
{
    "com.apple.mobilesafari": "Safari",
    "com.google.chrome": "Chrome"
}
Database delle App Malevole (illegitimate_apps.json):
Se non esiste, viene creato vuoto.
Popolalo con Bundle ID di app malevole note. Esempio:
json
{
    "com.mspy": "mSpy",
    "com.worldwidelogic": "FlexiSpy"
}
Salva il file nella stessa directory dello script.

7. Collegamento dell’iPhone
Prepara il dispositivo per l’analisi.
Connetti l’iPhone:
Usa un cavo USB per collegare l’iPhone al PC.
Sblocca e Autorizza:
Sblocca l’iPhone con il codice.
Quando appare il popup "Vuoi autorizzare questo computer?", tocca "Fidati".

9. Esecuzione dello Script
Esegui lo script e analizza le app installate.
Apri il Terminale:
Usa Prompt dei comandi o PowerShell.
Vai nella directory dello script (se non ci sei già):
bash
cd D:\Progetti\iPhoneAnalyzer
Avvia lo Script:
Digita:
bash
python iphone_app_extra_pro.py
Premi Invio e attendi.
Osserva l’Output nel Terminale:
Vedrai messaggi colorati:
Verde: App preinstallate Apple (es. Photos).
Rosso: App malevole (es. mSpy).
Giallo: App sospette con anomalie (es. nome mancante).
Esempio:
Collega il tuo iPhone tramite USB e assicurati che sia sbloccato...
[Verde]INFO: App preinstallata Apple - Photos (com.apple.mobileslideshow)[Normale]
[Rosso]ATTENZIONE: Trovata app malevola - mSpy (com.mspy) | Nota: mSpy[Normale]
Elenco salvato con successo in installed_apps.txt
10. Analisi dei Risultati
Controlla i risultati generati dallo script.
Apri il File di Output:
Cerca installed_apps.txt nella directory dello script.
Aprilo con un editor di testo (es. Blocco Note, Notepad++).
Leggi il Contenuto:
Troverai:
Metadati: Timestamp, IMEI, modello, versione iOS, numero di serie.
Elenco App: Nome, Bundle ID, stato (Legitimate, Malicious, Suspicious), note e anomalie.
Esempio:

Analisi eseguita il: 2025-02-25 18:30:00
IMEI: 123456789012345
Modello: iPhone14,5
Versione iOS: 18.3
Numero di serie: ABC123XYZ456
Elenco delle applicazioni installate:
Photos | Bundle ID: com.apple.mobileslideshow | Status: Legitimate
mSpy | Bundle ID: com.mspy | Status: Malicious | Nota: mSpy

7. Risoluzione dei Problemi
Se qualcosa va storto, ecco come correggere i problemi più comuni.
"No device found":
Controlla che l’iPhone sia collegato, sbloccato e autorizzato.
Verifica che libimobiledevice sia installato (scoop install libimobiledevice).
Colori non visibili:
Assicurati che colorama sia installato (pip install colorama).
Usa PowerShell invece del Prompt dei comandi per una migliore resa dei colori.
Errore JSON:
Apri legitimate_apps.json o illegitimate_apps.json e controlla la sintassi (es. virgole mancanti).
Usa un validatore online (es. jsonlint.com) per correggere.

8. Personalizzazione (Opzionale)
Adatta lo script alle tue esigenze.
Aggiorna i Database:
Aggiungi nuove app a legitimate_apps.json o illegitimate_apps.json con un editor di testo.
Modifica i Colori:
Cambia Fore.GREEN, Fore.RED, o Fore.YELLOW in get_installed_apps() con altri colori di colorama (es. Fore.BLUE).
