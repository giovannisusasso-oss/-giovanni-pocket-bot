import asyncio
import os

from pocket_option import PocketOptionClient

PO_SESSION = os.getenv("PO_SESSION")
PO_UID = os.getenv("PO_UID")

ASSET = "EURUSD_otc"


async def main():
    print("Giovanni Pocket Bot avviato!")
    print("Scanner pronto.")
    print("Asset:", ASSET)

    while True:
        print("Bot attivo...")
        await asyncio.sleep(60)


if __name__ == "__main__":
    asyncio.run(main())






    
    

    
        
        


    
