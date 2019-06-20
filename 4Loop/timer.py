import time 

print("Masukkan jam: ")
waktu_jam = int(input())
print("Masukkan menit: ")
waktu_menit = int(input())
print("Masukkan detik: ")
waktu_detik = int(input())

waktu_total = (waktu_jam*3600) + (waktu_menit*60) + (waktu_detik)

for x in reversed(range(waktu_total + 1 )):
    print(x, "detik tersisa")
    '''
    waktu_total = waktu_total - 1
    '''
    time.sleep(1)

print("Selesai!!")