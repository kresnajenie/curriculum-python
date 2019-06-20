students = []

student = {}

student["nama"] = "Kresna"
student["umur"] = 15
student["sekolah"] = "CC"
student["alamat"] = "Kedoya"
students.append(student)

student = {}

student["nama"] = "Vincent"
student["umur"] = 14
student["laptop"] = "Mac"
student["sekolah"] = "Laurensia"
students.append(student)

student = {}

student["nama"] = "Aldo"
student["umur"] = 18
student["alamat"] = "Surabaya"
student["sekolah"] = "HKUST"

students.append(student)

for murid in students:
    print("Nama: " + murid["nama"])
    print("Umur: " + str(murid["umur"]))
    print("Daerah tinggal: " + murid["alamat"])
    print("Sekolah: " + murid["sekolah"])
    print("")