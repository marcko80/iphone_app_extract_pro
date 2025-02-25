📱 iPhone App Extractor Pro
Python License Status
Benvenuto in iPhone App Extractor Pro, uno strumento Python progettato per estrarre l'elenco delle applicazioni installate su un iPhone connesso via USB a un computer Windows 11. Questo programma è pensato per analisti forensi che vogliono identificare spyware, malware e altre app sospette in modo rapido e affidabile! 🚨
Con questo tool, puoi:
📋 Estrarre l’elenco completo delle app installate.
🔍 Identificare app legittime, sospette e malevole usando database locali.
🖨️ Salvare i risultati in un file TXT con metadati del dispositivo (IMEI, modello, versione iOS, ecc.).
🎨 Visualizzare avvisi colorati nel terminale per app pericolose.
✨ Funzionalità Principali
Connessione USB: Collega il tuo iPhone a un PC Windows 11 via USB e analizza le app installate.
Database Locali:
legitimate_apps.json: Elenco di app considerate sicure (es. app di sistema Apple e app comuni).
illegitimate_apps.json: Elenco di app malevole note (es. spyware come mSpy o FlexiSpy).
Classificazione:
✅ Legitimate: App presenti nel database delle app sicure.
🚨 Malicious: App elencate come malevole (con nome noto, se disponibile).
⚠️ Suspicious: App non riconosciute, con controllo di anomalie (es. nome mancante, Bundle ID strano).
Metadati del Dispositivo: Include IMEI, modello, versione iOS, numero di serie e timestamp dell’analisi.
Output Colorato: Evidenziazione visiva nel terminale con rosso per app malevole e giallo per sospette con anomalie.
File di Output: Risultati salvati in installed_apps.txt con dettagli chiari e leggibili.
🛠️ Come Funziona
1. Estrazione delle App
Il programma usa la libreria pymobiledevice3 per connettersi all’iPhone tramite USB e recuperare l’elenco delle app installate con il servizio InstallationProxyService. Per ogni app, estrae:
Nome (CFBundleName).
Bundle ID (CFBundleIdentifier).
2. Classificazione
Confronta ogni Bundle ID con:
legitimate_apps.json: Se presente, l’app è "Legitimate".
illegitimate_apps.json: Se presente, l’app è "Malicious" e mostra il nome noto (es. "mSpy").
Se non è in nessuno dei due, diventa "Suspicious".
Controlla anomalie nei metadati per app sospette/malevole (es. nome mancante o Bundle ID non convenzionale).
3. Metadati del Dispositivo
Recupera informazioni dall’iPhone usando LockdownClient:
IMEI.
Modello (es. "iPhone14,5").
Versione iOS (es. "18.3").
Numero di serie.
Timestamp dell’analisi.
4. Output
Terminale: Mostra avvisi colorati:
Rosso (Fore.RED) per app malevole.
Giallo (Fore.YELLOW) per app sospette con anomalie.
File TXT: Salva tutto in installed_apps.txt con un’intestazione dettagliata.
📦 Prerequisiti
Sistema operativo: Windows 11.
Python: 3.9 o superiore.
iPhone connesso via USB, sbloccato e autorizzato ("Fidati" del computer).
Dipendenze
pymobiledevice3: Per comunicare con l’iPhone.
colorama: Per l’evidenziazione dei colori nel terminale.
🚀 Installazione
Clona il Repository:
bash
git clone https://github.com/marcko80/iphone_app_extract_pro.git
cd iphone-app-extractor-pro
Installa Python (se non già presente):
Scarica da python.org e assicurati di aggiungere Python al PATH.
Installa le Dipendenze:
bash
pip install pymobiledevice3 colorama
Installa libimobiledevice (necessario per pymobiledevice3):
Usa Scoop (gestore di pacchetti per Windows):
powershell
iwr -useb get.scoop.sh | iex
scoop install libimobiledevice
🖥️ Procedura di Utilizzo
Prepara i Database:
Il programma crea automaticamente:
legitimate_apps.json (app sicure di default, es. Photos, WhatsApp).
illegitimate_apps.json (vuoto, da popolare).
Aggiorna illegitimate_apps.json con app malevole note. Esempio:
json
{
    "com.mspy": "mSpy",
    "com.worldwidelogic": "FlexiSpy"
}
Collega l’iPhone:
Connetti l’iPhone al PC via USB.
Sblocca il dispositivo e seleziona "Fidati" quando richiesto.
Esegui il Programma:
Apri un terminale (Prompt dei comandi o PowerShell) nella directory del progetto.
Esegui:
bash
python iphone_app_extra_pro.py
Analizza i Risultati:
Terminale: Cerca avvisi in rosso (malevole) o giallo (sospette).
File: Apri installed_apps.txt per l’elenco completo.
📄 Esempio di Output
Terminale
Collega il tuo iPhone tramite USB e assicurati che sia sbloccato...
[Rosso]ATTENZIONE: Trovata app malevola - mSpy (com.mspy) | Nota: mSpy[Normale]
[Giallo]NOTA: App sospetta con anomalia - UnknownApp (com.unknown.app) | Anomalia: Nome mancante o incoerente[Normale]
Elenco salvato con successo in installed_apps.txt
installed_apps.txt
Analisi eseguita il: 2025-02-25 17:00:00
IMEI: 123456789012345
Modello: iPhone14,5
Versione iOS: 18.3
Numero di serie: ABC123XYZ456
--------------------------------------------------
Elenco delle applicazioni installate:
--------------------------------------------------
Photos | Bundle ID: com.apple.mobileslideshow | Status: Legitimate
WhatsApp | Bundle ID: com.whatsapp | Status: Legitimate
mSpy | Bundle ID: com.mspy | Status: Malicious | Nota: mSpy
UnknownApp | Bundle ID: com.unknown.app | Status: Suspicious | Anomalia: Nome mancante o incoerente
⚙️ Personalizzazione
Aggiungi App Legittime: Modifica legitimate_apps.json con nuovi Bundle ID e nomi.
Aggiorna App Malevole: Espandi illegitimate_apps.json con spyware o malware noti.
Modifica Output: Cambia i colori in get_installed_apps (es. Fore.GREEN per "Legitimate").
🐛 Risoluzione dei Problemi
Errore "No device found": Assicurati che l’iPhone sia sbloccato, autorizzato e che libimobiledevice sia installato.
Colori non visibili: Verifica che colorama sia installato (pip install colorama).
Errore JSON: Controlla la sintassi di legitimate_apps.json e illegitimate_apps.json (usa un validatore online se necessario).
📜 Licenza
Questo progetto è rilasciato sotto la licenza MIT (LICENSE). Usalo liberamente e contribuisci se vuoi! 🌟
🤝 Contributi
Hai suggerimenti o vuoi aggiungere funzionalità? Apri una PR o un issue! Adoro collaborare! 💡
⭐ Ringraziamenti
Grazie a pymobiledevice3 per il supporto ai dispositivi iOS.
A colorama per rendere il terminale più vivace.
E a te per aver provato questo tool! 🙌
Sostituisci tuo-username nel comando git clone con il tuo nome utente GitHub effettivo. Questo README è dettagliato, user-friendly e pronto per attirare l’attenzione sul tuo repository! Fammi sapere se vuoi modifiche o aggiunte! 😊
