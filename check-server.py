import requests

def cek_status_server(ip_port):
    url = f"https://api.open.mp/server/{ip_port}"
    try:
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        try:
            data = response.json()
            if data.get("online"):
                print("\n\033[92m[+] Server SA:MP Ditemukan!\033[0m")
                print("-" * 35)
                print(f" IP Server : {ip_port}")
                print(f" Status Server : \033[92mOnline\033[0m")
                print(f" Player Online : {data.get('players')}/{data.get('maxplayers')}")
                print("-" * 35)
            else:
                print("\n\033[91m[-] Server tidak ditemukan atau offline.\033[0m")
        except ValueError as e:
            print(f"Terjadi kesalahan saat mengurai JSON: {e}")
    except requests.RequestException as e:
        print(f"Terjadi kesalahan: {e}")

if __name__ == "__main__":
    print("=== Cek Status Server SA:MP ===")
    ip_port = input("Masukkan IP+Port Server (contoh: 123.456.78.90:7777): ")
    cek_status_server(ip_port)