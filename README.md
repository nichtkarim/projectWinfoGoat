# Geteilte Podman Webapp

Dieses Projekt zeigt eine Webanwendung, die mit Podman in drei separate Container aufgeteilt ist:

- **Backend (Python API)**: Flask-API, die Benutzerdaten aus einer SQLite-Datenbank abruft.
- **Datenbank (SQLite)**: Datenbankcontainer, der die Benutzerdaten bereitstellt.
- **Frontend (Apache)**: Apache-Webserver, der die HTML-Seite hostet.

## Voraussetzungen

- [Podman](https://podman.io/getting-started/installation)
- [Podman Compose](https://github.com/containers/podman-compose)

## Anleitung

### 1. Projekt klonen

```bash
git clone <repository-url>
cd my_webapp
```

### 2. Anwendung starten

```bash
podman-compose up --build
```

### 3. Auf die Anwendung zugreifen

- Frontend ist unter `http://localhost:8080` erreichbar.
- Die API läuft auf `http://localhost:5000`.

## Projektstruktur

```plaintext
my_webapp/
├── backend/                # Python API Container
│   ├── app.py
│   └── Dockerfile
├── database/               # SQLite Datenbank Container
│   ├── users.db
│   └── Dockerfile
├── frontend/               # Frontend mit Apache Webserver
│   ├── index.html
│   └── Dockerfile
├── podman-compose.yml      # Podman Compose Datei
└── README.md               # Projekt-Dokumentation
```

## Lizenz

Dieses Projekt steht unter der MIT-Lizenz.
