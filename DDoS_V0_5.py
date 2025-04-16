import threading
import time
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
