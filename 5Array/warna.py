colors = ["green","blue","red","yellow"]

colors.append("brown")      # append untuk menambahkan brown di dalam list warna kita 

colors.insert(0,"brown")    # brown dimasukkan menjadi di awal dari sebuah list 
colors.pop()                # sekarang brown ada di awal dan di akhir lalu dengan menggunakan pop akan menghapus brown yang di akhir
del colors[0]               # lalu kita akan mendelete list yang awal
colors.reverse()            # untuk menukar urutan dari list

print ('List Warna: ' + str(colors))    # untuk menampilkan list warna yang tersisa
print ('Jumlah warna : ' + str(len(colors)))    #untuk menampilkan jumlah list yang tersisa
