import addContact as tambah_kontak #menggunakan addContact yg sdh dibuat agar bs digunakan

customers = [] #PENTING, list diluar agar tidak ter-override/terhapus setiap kali melakukan loop

while True:
    print('---------------------------------------------')
    print('input 0 to see contacts')
    print('input 1 to add contact')
    print('input 9 to exit')
    print('---------------------------------------------')
    respond = input()
    if respond == "0":
        for customer in customers:  #Python akan memeriksa memory
                                    #Python akan melihat dictionary siapa saja yang sudah di input
            print("-----------\nNama: %s\nAge: %d\nBerat: %d\nTipe:%s\n-------" % (customer["name"],customer["age"],customer["weight"],customer["type"]))

    elif respond == "1":
        while True:
            try:
                name = input('Masukkan nama anda : ')
                umur = int(input('Masukkan umur anda : '))
                berat = int(input('Masukkan berat anda : '))
                data = tambah_kontak.AddContact(name, umur, berat)
                customers.append(data) #menambahkan data customer yang baru diinput ke list customers
                print("Nama: "+data["name"])
                print("Umur: "+str(data["age"]))
                print("Berat: "+str(data["weight"]))
                break
            except ValueError: #Agar program tidak crash ketika python menemukan kesalahan di input
                print('Please enter the correct data')
    elif respond == "9":
        break

    else:
        pass

