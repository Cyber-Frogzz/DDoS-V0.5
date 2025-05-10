import os

def banner():
    os.system("clear")
    print("""
       =============================
       |         Welcome To        |
       |      Tools By Frogzz      |
|=========================================|
|  TikTok: @phantomguardfrogzz            |
|  GitHub: github.com/PhantomGuard-Frogzz |
===========================================
    """)

def menu():
    print("\n[1] DDoS Attack")
    print("[2] IP Tracker")
    print("[3] Check Server SA:MP")
    print("[4] Spam Otp")
    print("[5] DDoS 7 Layers")
    choice = input("\nPilih menu: ")

    if choice == "1":
        os.system("python AllTools.py")
    elif choice == "2":
        os.system("python AllTools.py track")
    elif choice == "3":
        os.system("python check-server.py")
    elif choice == "4":
        os.system("python fngstp.py menu")
    elif choice == "5":
        os.system("python dos7lyrs.py attack_start")
    else:
        print("Pilihan tidak valid!")

if __name__ == "__main__":
    banner()
    menu()