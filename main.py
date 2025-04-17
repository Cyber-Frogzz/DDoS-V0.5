import os

def menu():
    os.system('clear')
    print('''
        Welcome To Tools Cyber-Frogzz

===============================================

[My Tiktok  : Frogzz]
[My Github  : https://github.com/Cyber-Frogzz/DDoS-V0.5]
[My YouTube : frogzzsamp-88]

                  ⚠️WARNING⚠️
          
          Hati Hati Saat Menggunakannya

===============================================
                  Pilihan Menu

[1] DDoS V0.5
''')
    pilihan = input("Pilih menu: ")

    if pilihan == '1':
        ip = input("IP Target (contoh: http://1.2.3.4): ")
        
        # Menjalankan DDoS dengan 50.000 request
        os.system(f'python DDoS-V0.5.py {ip}')
        
        input("Tekan Enter untuk kembali ke menu...")
        menu()

menu()