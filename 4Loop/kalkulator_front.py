import kalkulator as kode
#Gak pakai file kalkulator_operasi
while True:
    print('Apakah anda ingin memakai kalkulator? (ya/tidak)')
    pilihan = input()
    if pilihan.lower() == 'ya': #.lower agar pilihan tidak sensitif terhadap Upper/Lower case
        print("""
                Hi, here is how you use the calculator
                to start, choose the operation you want to use.
                Klik + untuk penjumlahan
                Klik - untuk pengurangan
                Klik * untuk perkalian
                KLik / untuk pembagian
                """)
        print('Pilih simbol')
        operasi = input()
        print('Masukkan angka pertama : ')
        try:
            a = int(input())
        except ValueError:
            print('Please try again')
            break #Break agar tidak timbul pesan yang ter-loop
        print('Masukkan angka kedua : ')
        try:
           b = int(input())
        except ValueError:
            print('Please try again')
            break # sama kyk diatas
        while True: #Agar bisa diulang terus
            if operasi == "+":
                try:
                    hasiltambah = kode.tambah(a, b)
                    print(hasiltambah)
                    break
                except:
                    print('Try again')
            elif operasi == "-":
                try:
                    hasilkurang = kode.kurang(a,b)
                    print(hasilkurang)
                    break
                except:
                    print('Try again')
            elif operasi == "*":
                try:
                    hasilkali = kode.kali(a,b)
                    print(hasilkali)
                    break
                except:
                    print('Try again')
            elif operasi == "/":
                if b == 0:
                    print("Can't divide by zero")
                    break
                try:
                    hasilbagi = kode.bagi(a,b)
                    print(hasilbagi)
                    break
                except:
                    print('Try Again')
            else:
                print('Incorrect value')
                break
    else:
        print('Ok bye')
        break

