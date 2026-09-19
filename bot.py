import os
import time
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

PORT = int(os.environ.get("PORT", 10000))


class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Giovanni Pocket Bot is running!")

    def log_message(self, format, *args):
        pass


def start_server():
    server = HTTPServer(("0.0.0.0", PORT), Handler)
    print(f"Server attivo sulla porta {PORT}")
    server.serve_forever()


print("Giovanni Pocket Bot avviato!")
print("Scanner pronto.")
print("Asset: EURUSD_otc")

Thread(target=start_server, daemon=True).start()

while True:
    print("Bot attivo...")
    time.sleep(60)
    

    
        
        


    
