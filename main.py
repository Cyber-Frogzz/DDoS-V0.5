import os

def banner():
    print("""



 ______  _                    _                      _____                          _ 
 | ___ \| |                  | |                    |  __ \                        | |
 | |_/ /| |__    __ _  _ __  | |_   ___   _ __ ___  | |  \/ _   _   __ _  _ __   __| |
 |  __/ | '_ \  / _` || '_ \ | __| / _ \ | '_ ` _ \ | | __ | | | | / _` || '__| / _` |
 | |    | | | || (_| || | | || |_ | (_) || | | | | || |_\ \| |_| || (_| || |   | (_| |
 \_|    |_| |_| \__,_||_| |_| \__| \___/ |_| |_| |_| \____/ \__,_| \__,_||_|    \__,_|
                                                                                      
                                                                                      




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