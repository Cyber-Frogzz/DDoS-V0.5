import os

def menu():
    os.system('clear')
    print('''
Welcome To Tools Frogzz

[My Tiktok  : your_tiktok]
[My Github  : https://github.com/Cyber-Frogzz/DDoS-V0.5]
[My YouTube : your_youtube]

[1] DDoS V0.5
''')
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        ip = input("IP Target (contoh: http://1.2.3.4): ")
        jumlah = input("Jumlah Packet: ")
        os.system(f'python DDoS-V0.5.py {ip} {jumlah}')
        input("Tekan Enter untuk kembali ke menu...")
        menu()

menu()