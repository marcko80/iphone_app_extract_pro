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

   
