import os

def menu():
    os.system('clear')
    print('''
        Welcome To Tools PhantomGuard Frogzz

===============================================
[1] Simulasi Traffic (700 request/10 detik)
===============================================
    ''')
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        ip = input("Target (contoh: http://1.2.3.4): ")
        os.system(f'python DDoS-V0.5.py {ip}')
        input("Selesai! Tekan Enter untuk keluar.")

menu()