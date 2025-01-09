```bash
[Unit]
Description=Run Python Script
After=network.target

[Service]

ExecStart=/usr/bin/python3 /root/mmbbs/run.py #Pfad zum auszuführenden Python-Skript

WorkingDirectory=/root/mmbbs # Arbeitsverzeichnis des Dienstes

User=root # Benutzer, unter dem der Dienst läuft

Restart=always # Dienst wird bei Fehlern immer neu gestartet
Environment=PYTHONUNBUFFERED=1

[Install]

WantedBy=multi-user.target # Dienst wird im Multi-User-Ziel installiert
```