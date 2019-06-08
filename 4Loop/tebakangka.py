angka_tebakan = 25 #Ini adalah angka yg benar
tebakan = 0 #Untuk menyatakan ada variabel tebakan

while tebakan != 25:
    tebakan = int(input("Masukkan tebakan anda: ")) #Pengguna memasukkan tebakan yang nanti akan dievaluasi oleh program
    if tebakan < angka_tebakan:
        print("terlalu kecil")
    if tebakan > angka_tebakan:
        print("terlalu besar")
print ("anda benar!")