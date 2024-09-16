FROM python:3.8-slim

# Arbeitsverzeichnis erstellen
WORKDIR /app

# Kopiere die Python-App ins Arbeitsverzeichnis
COPY app.py .

# Flask installieren
RUN pip install Flask

# Exponiere Port 5000 für die API
EXPOSE 5000

# Starte die Anwendung
CMD ["python", "app.py"]
