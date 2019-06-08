def daftarnama():
    print("Daftar Nama: ")
    for orang in names:
        print(orang)



names = [ ]
siswa = "asd"

while True:
    print("Ketik 1 untuk menambahkan nama siswa")
    print("Ketik 2 untuk menghapus nama siswa yang terakhir")
    print("Ketik 3 untuk melihat daftar nama siswa")
    print("Ketik 9 untuk keluar")
    pilihan = input()
    if pilihan == "1":
        print("Masukkan nama:")
        print("(ketik exit untuk keluar)")
        siswa = input()
        while siswa.lower() != "exit":
            names.append(siswa.capitalize())

            daftarnama()

            print("Masukkan nama:")
            print("(ketik exit untuk keluar)")
            siswa = input()

    elif pilihan == "3":
        daftarnama()

    elif pilihan == "2":
        names.pop()
        daftarnama()

    elif pilihan == "9":
        break

    else:
        pass



            






