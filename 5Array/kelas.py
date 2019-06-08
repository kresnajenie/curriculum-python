

names = [ ]

print ("Jika telah selesai ketik Exit ") 
siswa = input("Tolong masukkan nama siswa: ") # untuk memasukkan nama siswa  


while siswa.lower() != "exit" : #selama yang diinput bukan Exit maka perintah untuk memasukkan nama akan selalu muncul
    names.append(siswa.capitalize())  # untuk menambahkan nama siswa ke list 

    print ("Nama : ")

    for name in names:
        print(name)

    siswa = input("Tolong masukkan nama siswa: ") # untuk memasukkan nama siswa








