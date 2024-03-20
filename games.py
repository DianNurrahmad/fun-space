def main():
    print("Pilih Salah Satu!")
    print("1. Kertas")
    print("2. Batu")
    print("3. Gunting")
    pilih = int(input("Masukkan Pilihan Anda: "))
    import random
    comp = random.randint(1,3)
    if pilih == 1:
        if comp == 1:
            print("Kamu Memilih Kertas")
            print("Komputer Memilih Kertas")
            print("Seri!")
        elif comp == 2:
            print("Kamu Memilih Kertas")
            print("Komputer Memilih Batu")
            print("Komputer Menang!")
        else:
            print("Kamu Memilih Kertas")
            print("Komputer Memilih Gunting")
            print("Kamu Menang!")
    elif pilih == 2:
        if comp == 1:
            print("Kamu Memilih Batu")
            print("Komputer Memilih Kertas")
            print("Kamu Menang!")
        elif comp == 2:
            print("Kamu Memilih Batu")
            print("Komputer Memilih Batu")
            print("Seri!")
        else:
            print("Kamu Memilih Batu")
            print("Komputer Memilih Gunting")
            print("Komputer Menang!")
    elif pilih == 3:
        if comp == 1:
            print("Kamu Memilih Gunting")
            print("Komputer Memilih Kertas")
            print("Komputer Menang!")
        elif comp == 2:
            print("Kamu Memilih Gunting")
            print("Komputer Memilih Batu")
            print("Kamu Menang!")
        else:
            print("Kamu Memilih Gunting")
            print("Komputer Memilih Gunting")
            print("Seri!")
    
    elif pilih == 4:
        print("Terima Kasih")
        exit()
    else:
        print("Pilihan Tidak Tersedia")

main()