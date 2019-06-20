user = "kolla"
pw = "kollaborasi"
a = 1

user_input = input("masukkan username anda")
pw_input = input("masukkan password anda") 

while user_input != "kolla" and pw_input != "kollaborasi": 
    a += 1
    user_input = input("masukkan username anda")
    pw_input = input("masukkan password anda") 

    if a < 5:
        print("salah")
    elif a == 5:
        print("you've exceedeed your tries")
        break

if user_input == 'kolla' and pw_input == 'kollaborasi':
    print('benar')