from flask import Flask, jsonify
import sqlite3
import os

app = Flask(__name__)

# Route für die API, um Benutzerdaten abzurufen
@app.route('/api/user', methods=['GET'])
def get_user():
    # Verbindung zur SQLite-Datenbank über den Datenbank-Container
    conn = sqlite3.connect(os.getenv('DB_PATH'))  # Verbindung zur SQLite-Datenbank über Volume
    user = conn.execute('SELECT * FROM users WHERE name = ?', ('Karim',)).fetchone()
    conn.close()
    return jsonify({'id': user[0], 'name': user[1]})  # Benutzerinformationen als JSON zurückgeben

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)  # API auf Port 5000 starten
