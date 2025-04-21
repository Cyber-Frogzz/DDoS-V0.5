import requests

def cek_status_server(ip_port):
    url = f"https://samp-api.tk/server/{ip_port}"
    try:
        response = requests.get(url, timeout=5)
        data = response.json()

        if data.get("status") == "online":
            print(f"Status Server : \033[92mOnline\033[0m")
            print(f"Ping Server   : {data.get('ping')} ms")
            print(f"Player Online : {data.get('players')}/{data.get('maxplayers')}")
        else:
            print(f"Status Server : \033[91mOffline\033[0m")
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    ip_port = input("Masukkan IP+Port Server (contoh: 123.456.78.90:7777): ")
    cek_status_server(ip_port)