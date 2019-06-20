import kalkulator_back

res = 3

while res != 9:
    print("-------------------")
    print("KALKULATOR")
    print("-------------------")
    print("masukkan 0 untuk penjumlahan")
    print("masukkan 1 untuk pengurangan")
    print("masukkan 9 untuk keluar")
    print("-------------------")

    res = int(input())

    first_number = int(input("Masukkan angka pertama:\n"))
    second_number = int(input("Masukkan angka kedua:\n"))

    if res == 0:
        hasil = kalkulator_back.tambah(first_number, second_number)
    elif res == 1:
        hasil = kalkulator_back.kurang(first_number, second_number)
    elif res == 9:
        break
    else: 
        pass

    print("Hasil adalah"+str(hasil))
