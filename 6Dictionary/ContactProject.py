import addContact as tambah_kontak

while True:
    print('---------------------------------------------')
    print('input 0 to see contacts')
    print('input 1 to add contact')
    print('input 9 to exit')
    print('---------------------------------------------')
    respond = input()
    customers = []
    if respond == "0":
        for x in customers:
            print(x)

    elif respond == "1":
            while True:
                try:
                    name = input('Masukkan nama anda : ')
                    umur = int(input('Masukkan umur anda : '))
                    berat = int(input('Masukkan berat anda : '))
                    data = tambah_kontak.AddContact(name, umur, berat)
                    customers.append(data)
                    print(data["name"])
                    print(data["age"])
                    print(data["weight"])
                    break
                except ValueError:
                    print('Please enter the correct data')
    elif respond == "9":
        pass

    else:
        pass

