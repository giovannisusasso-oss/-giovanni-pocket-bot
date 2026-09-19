import asyncio
import os
from http.server import BaseHTTPRequestHandler, HTTPServer
from threading import Thread

from pocket_option import PocketOptionClient

PO_SESSION = os.getenv("PO_SESSION")
PO_UID = os.getenv("PO_UID")

ASSET = "EURUSD_otc"
PORT = int(os.getenv("PORT", "10000"))


class HealthHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Giovanni Pocket Bot is running!")

    def log_message(self, format, *args):
        pass


def start_server():
    server = HTTPServer(("0.0.0.0", PORT), HealthHandler)
    server.serve_forever()


async def main():
    Thread(target=start_server, daemon=True).start()

    print("Giovanni Pocket Bot avviato!")
    print("Scanner pronto.")
    print("Asset:", ASSET)

    while True:
        print("Bot attivo...")
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())




    
    

    
        
        


    
