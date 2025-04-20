import os

def banner():
    print("""
=============================
|     Welcome To Frogzz     |
|   Tool By PhantomGuard    |
|===========================|
|  TikTok: @cyberfrogzz     |
|  GitHub: github.com/PhantomGuard-Frogzz |
=============================
""")

def menu():
    print("[1] DDoS Website")

def run():
    banner()
    menu()
    choice = input("Pilih menu: ")
    if choice == "1":
        os.system("python DDoS-V0.5.py")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    run()