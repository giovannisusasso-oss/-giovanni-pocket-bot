import os
import time
import threading
import requests
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", "10000"))

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
TELEGRAM_CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Giovanni Pocket Bot OK")

    def log_message(self, format, *args):
        return


def server():
    httpd = HTTPServer(("0.0.0.0", PORT), Handler)
    print("WEB SERVER OK - PORTA", PORT, flush=True)
    httpd.serve_forever()


def send_telegram(message):
    if not TELEGRAM_TOKEN or not TELEGRAM_CHAT_ID:
        print("TELEGRAM CONFIG MANCANTE", flush=True)
        return

    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"

    data = {
        "chat_id": TELEGRAM_CHAT_ID,
        "text": message
    }

    try:
        response = requests.post(url, data=data, timeout=15)
        print("TELEGRAM:", response.status_code, flush=True)
    except Exception as e:
        print("ERRORE TELEGRAM:", e, flush=True)


print("GIOVANNI POCKET BOT AVVIATO", flush=True)
print("SCANNER PRONTO - EURUSD_otc", flush=True)

threading.Thread(target=server, daemon=True).start()

send_telegram("🟢 Giovanni Pocket Bot online!\nScanner EURUSD OTC avviato.")

while True:
    print("BOT ATTIVO", flush=True)
    time.sleep(30)
