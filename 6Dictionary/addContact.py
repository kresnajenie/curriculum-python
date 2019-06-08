def AddContact(nama, umur, berat): #Parameter nama umur berat hanya permisalan, yang sebenarnya ada di file ContactProject
    try:
        customer_data = {}
        customer_data["name"] = nama
        customer_data["age"] = umur
        customer_data["weight"] = berat
        berat = customer_data["weight"]
        if berat > 100:
            customer_data["type"] = "Gendut"
        elif berat < 40:
            customer_data["type"] = "Kurang makan"
        else:
            customer_data["type"] = "Normal"

        return customer_data #Agar data yang sudah di input dapat diambil kembali ketika diperlukan
    except ValueError:
        print('Please enter the field correctly')
    except:
        print('Please try again')