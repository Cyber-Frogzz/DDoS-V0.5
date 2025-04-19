import os

def menu():
    os.system('clear')
    print('''
     Welcome To Tools PhantomGuard Frogzz

[Author : Frogzz            ]
[Community : 𝙋𝙝𝙖𝙣𝙩𝙤𝙢𝙂𝙪𝙖𝙧𝙙𓆃 ]


===============================================
                Pilihan Menu

[1] DDoS Free Proxy

===============================================
    ''')
    pilihan = input("Pilih menu: ")
    if pilihan == '1':
        ip = input("Target (contoh: http://1.2.3.4): ")
        os.system(f'python DDoS-V0.5.py {ip}')
        input("Selesai! Tekan Enter untuk keluar.")
 ]
menu()