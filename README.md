# Zootopia - Tier-Informationen Website Generator

Ein Python-Projekt, das automatisch eine HTML-Website mit detaillierten Informationen über Tiere generiert. Die Daten werden in Echtzeit von der API-Ninjas Animals API abgerufen.

## Inhaltsverzeichnis

- [Features](#features)
- [Installation](#installation)
- [API-Setup](#api-setup)
- [Verwendung](#verwendung)
- [Projektstruktur](#projektstruktur)
- [Technologien](#technologien)

## Features

- Suche nach beliebigen Tieren oder Tierrassen
- Automatische Generierung einer responsiven HTML-Website
- Anzeige von Tierinformationen:
  - Name
  - Ernährungsweise (Diet)
  - Standort (Location)
  - Typ (Type)
- Sichere API-Key-Verwaltung mit `.env`-Datei
- Fehlerbehandlung bei nicht existierenden Tieren

## Installation

### Voraussetzungen

- Python 3.7 oder höher
- pip (Python Package Manager)

### Schritt 1: Repository klonen oder herunterladen

```bash
cd /pfad/zu/deinem/projekt
```

### Schritt 2: Virtuelles Environment erstellen (empfohlen)

```bash
python -m venv .venv
```

### Schritt 3: Virtuelles Environment aktivieren

**macOS/Linux:**
```bash
source .venv/bin/activate
```

**Windows:**
```bash
.venv\Scripts\activate
```

### Schritt 4: Dependencies installieren

```bash
pip install -r requirements.txt
```

## API-Setup

### 1. API-Key besorgen

1. Besuche [API-Ninjas](https://api-ninjas.com/)
2. Erstelle einen kostenlosen Account
3. Kopiere deinen API-Key aus dem Dashboard

### 2. .env-Datei erstellen

Erstelle eine neue Datei mit dem Namen `.env` im Root-Verzeichnis des Projekts:

```bash
touch .env
```

Füge deinen API-Key in die `.env`-Datei ein:

```env
API_KEY=dein_api_key_hier
```

**Wichtig:** Keine Leerzeichen um das `=` und keine Anführungszeichen!

### 3. .gitignore überprüfen

Stelle sicher, dass die `.env`-Datei in der `.gitignore` aufgeführt ist, um deinen API-Key nicht versehentlich zu committen:

```gitignore
.env
__pycache__/
*.pyc
.venv/
```

## Verwendung

### Programm starten

```bash
python animals_web_generator.py
```

### Beispiel-Session

```
Enter an animal or an animal-race: lion

######## - WEBSITE WAS SUCCESSFULLY GENERATED TO "animal.html" - ########
```

Die generierte Website findest du unter `animals.html` im Projektverzeichnis. Öffne sie einfach in deinem Browser!

### Weitere Beispiele

```bash
# Suche nach einem Tiger
python animals_web_generator.py
> tiger

# Suche nach einer Hunderasse
python animals_web_generator.py
> golden retriever

# Suche nach einem Vogel
python animals_web_generator.py
> eagle
```

## Projektstruktur

```
zootopia_with_api/
│
├── animals_web_generator.py    # Hauptprogramm - generiert die HTML-Website
├── data_fetcher.py              # Ruft Tierdaten von der API ab
├── animals_template.html        # HTML-Template für die Website
├── animals.html                 # Generierte Website (wird erstellt)
├── requirements.txt             # Python-Dependencies
├── .env                         # API-Key Konfiguration (nicht im Repo)
├── .gitignore                   # Git-Ignore-Datei
└── README.md                    # Diese Datei
```

## Technologien

- **Python 3.x** - Hauptprogrammiersprache
- **requests** - HTTP-Anfragen an die API
- **python-dotenv** - Laden von Umgebungsvariablen aus `.env`
- **API-Ninjas Animals API** - Tierdaten-Quelle

## Wie es funktioniert

1. **Benutzereingabe:** Der Nutzer gibt einen Tiernamen ein
2. **API-Anfrage:** `data_fetcher.py` sendet eine Anfrage an die API-Ninjas Animals API
3. **Datenverarbeitung:** Die erhaltenen Tierdaten werden verarbeitet und in HTML konvertiert
4. **HTML-Generierung:** Das Template wird mit den Tierdaten gefüllt
5. **Website-Erstellung:** Eine fertige `animals.html` Datei wird generiert

## Troubleshooting

### "python-dotenv could not parse statement"

- Überprüfe, dass deine `.env`-Datei das Format `API_KEY=wert` verwendet (nicht `API_KEY: 'wert'`)
- Keine Leerzeichen um das Gleichheitszeichen

### "No API data returned"

- Überprüfe, ob dein API-Key korrekt in der `.env`-Datei eingetragen ist
- Stelle sicher, dass `load_dotenv()` aufgerufen wird

### Tier nicht gefunden

- Die API gibt nur Daten für existierende Tiere zurück
- Versuche alternative Schreibweisen oder englische Namen

## Entwickler

Erstellt von Bastian Westholt als Teil des Masterschool-Projekts

## Lizenz

Dieses Projekt ist für Bildungszwecke erstellt.
