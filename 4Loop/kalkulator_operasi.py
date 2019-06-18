import kalkulator_operasi as kode

def operasi_plus(tambah1, tambah2):
    try:
        tambah1 = int(input('Angka pertama : '))
        tambah2 = int(input('Angka kedua : '))
        hasiltambah = kode.tambah(tambah1, tambah2)
        return hasiltambah
    except:
        print('Try again')


def operasi_minus(kurang1,kurang2):
    try:
        kurang1 = int(input('Angka pertama: '))
        kurang2 = int(input('Angka kedua: '))
        hasilkurang = kode.kurang(kurang1, kurang2)
        return hasilkurang
    except:
        print('Try again')

def operasi_asterisk(kali1, kali2):
    try:
        kali1 = int(input('Angka pertama: '))
        kali2 = int(input('Angka kedua: '))
        hasilkali = kode.kali(kali1, kali2)
        return hasilkali
    except:
        print('Try again')

def operasi_slash(bagi1,bagi2):
    try:
        bagi1 = int(input('Angka pertama: '))
        bagi2 = int(input('Angka kedua: '))
        hasilbagi = kode.bagi(bagi1, bagi2)
        return hasilbagi
    except:
        print('Try again')