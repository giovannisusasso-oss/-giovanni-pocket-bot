import os
import time
import threading
from http.server import HTTPServer, BaseHTTPRequestHandler

PORT = int(os.environ.get("PORT", "10000"))


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


print("GIOVANNI POCKET BOT AVVIATO", flush=True)
print("SCANNER PRONTO - EURUSD_otc", flush=True)

threading.Thread(target=server, daemon=True).start()

while True:
    print("BOT ATTIVO", flush=True)
    time.sleep(30)
    

    
        
        


    
