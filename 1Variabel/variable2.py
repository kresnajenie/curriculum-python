nama = 'Kresna' #string
umur = 15       #integer
uang = 13555.55 #float

print('Nama saya adalah ' + nama + '. Umur saya ' + str(umur) + '. Uang saya Rp' + str(uang) + '.') #harus dijadiin string
print('Nama saya adalah %s. Umur saya %d. Uang saya Rp%r.' % (nama, umur, uang) ) #%s untuk sting, %d untuk integer, %r untuk float