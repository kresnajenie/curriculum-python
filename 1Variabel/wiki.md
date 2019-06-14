# Python
## Table of Content:

01. Introduction
    - a. Summary
    - b. Getting started
    - c. Road map
02. Objectives
    - a. Know
    - b. Understand
    - c. Do
    - d. Certification
03. Requirements
    - a. Prerequisites
    - b. Tools
05. Syntax & Grammar
    - a. Anatomy
    - b. Style guide
    - c. Comment
06. Variable & Constant
    - a. Declare
    - b. Scope
07. Input
    - a. String
    - b. Integer
08. Data Types
    - a. Primitive 
    - b. Non Primitive
    - c. Conversion
09. Operator
    - a. Arithmetic
    - b. Comparisons
    - c. Logical
10. Conditional
    - a. if
    - b. elif
    - c. else
11. Loop
    - a. while
    - b. for
12. Function
13. Debugging
14. OOP
    - a. Class
15. Readability
16. Functionality
17. Performance
18. Security
19. Accessibility
20. Framework
21. Project
22. Certification
23. References

## Introduction
1. ### Summary
2. ### Getting Started
3. ### Road Map

## Objectives
1. ### Know
2. ### Understand
3. ### Do
4. ### Certification
## Requirements
1. ### Prerequisites
2. ### Tools
    - __Visual Studio Code__
    - __Install Python__
    - __Install Pip__
    - __Install Github__
    - __Install Homebrew (Mac)__
    - __Install Cmder (Win)__  
    link: https://cmder.net/
## Code Style Guide
## Syntax and Grammar
## Variable
### Declare
Dalam Python, menyatakan variabel bisa secara langsung.
```python
nama = "Kresna"

print(nama)
```
Output:
> Kresna

Dengan kode `nama = "Kresna"`, variabel nama dinyatakan dan berisikan `"Kresna"`

### Types
- #### String
Tipe _String_ berisi kata-kata dan dinyatakan dengan petik satu `' '` atau petik dua `" "`
```python
nama = 'Kresna' #string
nama_panjang = "Kresna Jenie" #string

print(nama)
print(nama_panjang)
```
Output:
> Kresna  
> Kresna Jenie
+ #### Integer
Tipe _Integer_ berisi angka yang bisa dipakai untuk operasi hitung. Dinyatakan tanpa petik.
```python
a = 1       # integer
b = 3       # integer
c = a + b   # integer

print(a)
print(b)
print(c)
```
Output: 
> 1  
3   
4
- #### Float
Tipe _Float_ berisi angka desimal yang bisa dipakai juga untuk operasi hitung. Dinyatakan dengan angka desimal (titik dibelakang angka).
```python
a = 1.5     # float
b = 3.2     # float
c = a + b   # float

print(a)
print(b)
print(c)
```
Output: 
> 1.5  
3.2  
4.7
## Operators
- ### Arithmatic
    - __Penjumlahan__   
    Gunakan tanda tambah `+` untuk penjumlahan.
    Penjumlahan bisa digunakan untuk string, integer, dan float.
        1. __String__  
        Penjumlahan __*String*__ dengan tanda `+` tidak akan menciptakan spasi diantara kedua string.    

            ```python
            nama_depan = 'Kresna '  #string
            nama_belakang = 'Jenie' #string

            nama = (nama_depan + nama_belakang) # string + string
            print(nama)
            ```

            Output:
            > Kresna Jenie  
        
        2. __Integer__  
        Penjumlahan __*Integer*__ dengan tanda `+` akan menjumlahkan angka yang diberikan

            ```python
            x = 20  #integer
            y = 15  #integer

            z = (x + y) # integer + integer
            print(z)
            ```

            Output:
            > 35  

            Jika ada __*Integer*__ yang ingin dijadikan string bisa memakai `str()`

            ```python
            x = 20  #integer
            y = 15  #integer

            z = (str(x) + str(y)) # string + string
            print(z)
            ```

            Output:
            > 2015
        3. __Float__  
            Penjumlahan __*Float*__ dengan __*Float*__ dengan tanda `+` akan menghasilkan __*Float*__

            ```python
            x = 20.2    #float
            y = 15.3    #float
            z = (x + y) # float + float
            print(z)    #35.5 => menjadi float
            ```
            
            Output: 
            > 35.5

            Penjumlahan __*Float*__ dengan __*Integer*__ dengan tanda `+` akan menghasilkan __*Float*__

            ```python
            x = 20.2        #float
            y = 15          #integer
            z = (x + y)     # float + integer
            print(z)        #35.2 => jadi float
            ```
            Output: 
            > 35.2

        4. __Campuran__  
            Untuk mengembalikan hasil yang terdiri dari berbagai tipe dapat dilakukan juga dengan tanda `+`.

            ```python
            nama = "Kresna" #string
            umur = 15       #integer
            uang = 15500.5

            print(nama + " yang berumur " + umur + ", mempunyai uang " + uang)
            ```

            Output:
            > Kresna yang berumur 15, mempunyai uang 15500.5

            Namun, dengan cara ini tipe __*Integer*__ dan __*Float*__ harus dijadikan __*String*__ dengan `str()`.  
            
            Agar lebih mudah bisa menggunakan `%`

            ```python
            nama = "Kresna" #string
            umur = 15       #integer
            uang = 15500.5

            print("%s yang berumur %d, mempunyai uang %r" % (nama, umur, uang))
            ```

            Output:
            > Kresna yang berumur 15, mempunyai uang 15500.5

            | Symbol | Type    |
            |--------|---------|
            | %s     | String  |
            | %d     | Integer |
            | %r     | Float   |

    - __Pengurangan__  
        Gunakan tanda `-` untuk pengurangan. Pengurangan dapat dilakukan untuk __*Integer*__ dan __*Float*__
        1. __Integer__  
            ```python
            x = 20      #integer
            y = 15      #integer

            z = x - y   # integer + integer
            print(z)
            ```

            Output:
            > 5

        2. __Float__  

            ```python
            x = 20.4  #float
            y = 15.5  #float

            z = x - y # float + float
            print(z)
            ```

            Output:
            > 4.9

        3. __Campuran__

            ```python
            x = 20      #integer
            y = 15.5    #float

            z = x - y   # integer + float
            print(z)    #float
            ```

            Output:
            > 4.5
        
    - __Perkalian__  
    Gunakan tanda `*` untuk perkalian. Perkalian dapat digunakan untuk __*String*__, __*Integer*__, dan __*Float*__

        1. __String__  
        Saat ada __*String*__ seperti `nama = "Kresna"` dan nama itu dikalikan `print(nama * 5)`, maka nama itu akan diulang lima kali.

            ```python
            nama = 'Kresna' #string

            print(nama * 5)
            ```

            Output:
            > KresnaKresnaKresnaKresnaKresna
        
        2. __Integer__

            ```python
            x = 4   #integer
            y = 3   #integer
            print(x * y) #12 => akan menjadi integer
            ```
            Output:
            > 12

        3. __Float__

            ```python
            x = 4.3     #float
            y = 3.4     #float
            print(x * y)  #14.62 => akan menjadi float
            ```

            Output:
            > 14.62
        
        4. __Campuran__  
            __*Integer*__ saat dikalikan dengan  __*Float*__ akan menjadi __*Float*__.

            ```python
            x = 4.2     #float
            y = 3       #integer
            print(x * y)  #12.6 => akan menjadi float
            ```

            Output:
            > 12.6

    - __Pembagian__  
        Gunakan tanda `/` untuk perkalian. Perkalian dapat digunakan untuk __*Integer*__ dan __*Float*__

        1. __Integer__  
            Pembagian __*Integer*__ yang tidak habis akan berubah tipe menjadi float

            ```python
            x = 4   #integer
            y = 3   #integer
            print(x * y) #1.3333 => akan menjadi float
            ```
            Output:
            > 1.33333333

            Jika hasil yang diberikan ingin dijadikan __*Integer*__ maka bisa memakai `int()`

            ```python
            x = 4   #integer
            y = 3   #integer
            print(int(x * y)) #1 => akan menjadi integer
            ```
            Output:
            > 1

        2. __Float__  
            Hasil pembagian __*Float*__  akan tetap menjadi tipe __*Float*__
            ```python
            x = 4.3     #float
            y = 3.4     #float
            print(x / y)  #1,2647058824 => akan menjadi float
            ```

            Output:
            > 1,2647058824

- ### Comparison
- ### Logical
## Input  
Input digunakan untuk mendapatkan respon dari pengguna.  

```python
nama = input('Siapa nama kamu?')

print('Nama: %s' % (nama.capitalize())) 
# .upper() => huruf besar semua, .lower() => huruf kecil semua
```
Output:
> Siapa nama kamu? '  
    *__Kresna__*  
Nama: Kresna

Dengan kode ini akan ditanyakan `Siapa nama kamu?`. Respon yang diketik oleh pengguna, dalam kasus ini yaitu `Kresna`, akan dimasukkan kedalam variable `nama`.  
  
Input akan secara otomatis merubah hasil menjadi __*String*__. Untuk variabel bisa tipe __*Integer*__ bisa menggunakan `int()` dan untuk tipe __*Float*__ bisa menggunakan `float()`.

```python
nama = input('Siapa nama kamu? ')
umur = int(input('Berapa umurmu? '))
uang = float(input('Berapa uang yang kamu punya?'))

print('Nama: %s, Umur: %d, Uang: %r' % (nama.capitalize(), umur, uang))
```
Output: 
>Siapa nama kamu?  
__*Kresna*__  
Berapa umurmu?  
__*15*__  
Berapa uang yang kamu punya?  
__*20.5*__  
Nama: Kresna, Umur: 15, Uang: 20.5

## Debugging
## Conditional
- ### __Logical operator :__
    - Sama dengan: `a == b`
    - Tidak sama dengan: `a != b`
    - Kurang dari: `a < b`
    - Kurang dari atau sama dengan: `a <= b`
    - Besar dari: `a > b`
    - Besar dari atau sama dengan: `a >= b`

    Operator ini biasa digunakan pada `if` dan loop.
- ### if
    Pernyataan __*If*__ ditulis dengan menuliskan `if`.

    ```python
    a = 200
    b = 300

    if a < b:
        print('a lebih kecil dari b')
    ```

    Output:
    > a lebih kecil dari b

- ### elif
    __Elif__ digunakan untuk menambahkan kondisi lain yang diperlukan dengan menuliskan `elif`.
    ```python
    a = 200
    b = 300
    c = 400

    if a < b:
        print('a lebih kecil dari b')
    elif b < c:
        print('b lebih kecil dari c')
    elif a != c:
        print('a tidak sama dengan c')
    ```

    Output:
    > a lebih kecil dari b  
    b lebih kecil dari c  
    a tidak sama dengan c
- ### else
    __Else__ digunakan untuk kondisi lain selain kondisi-kondisi sebelumnya yang ditulisakn dengan `else`.

    ```python
    a = 400
    b = 300

    if a < b:
        print('a lebih kecil dari b')
    elif a == b:
        print('a sama dengan b')
    else:
        print('a lebih besar dari b')
    ```

    Output:
    > a lebih besar dari b

## Collection
Terdapat empat koleksi data yang ada di dalam bahasa pemrograman __Python__:



| Collection | Ordered | Changeable | Indexed | Allow Duplicate |
|------------|---------|------------|---------|-----------------|
| __List__       | Yes     | Yes        | Yes     | Yes             |
| __Tuple__      | Yes     | No         | Yes     | Yes             |
| __Set__        | No      | Yes        | No      | No              |
| __Dictionary__ | No      | Yes        | Yes     | No              |
  
Sangat berguna untuk mengerti tipe-tipe __*Collection*__ agar dapat menggunakan tipe yang benar dalam berbagai kondisi tertentu.
### Lists
__List__ adalah suatu koleksi yang urut dan bisa diubah. Dalam __Python__, __List__ ditulis dengan kurung siku `[]`.

```python
alat_tulis = ["bulpen", "pensil", "penghapus", "penggaris"]

print(alat_tulis)
```
Output:
> ['bulpen', 'pensil', 'penghapus', 'penggaris']

### Dictionary
__Dictionary__ adalah sebuah koleksi yang tidak berurutan, dapat diganti, dan berindeks.
```python
dictionary = {
    "nama":"Kresna",
    "kelas": "10A",
    "nomor": "20"
}
print(dictionary)
```

Output:

> {'nama': 'Kresna', 'kelas': '10A', 'nomor': '20' }

__Mengambil Item__ dapat dilakukan dengan 2 cara :

```python
kelas = dictionary["kelas"]
```
atau  
```python
kelas = dictionary.get["kelas]
```

__Mengubah Item__ dapat dilakukan dengan cara :

```python
dictionary["nama"] = "Jeremy" 
```

__Menambahkan Item__ dapat dilakukan dengan cara :

```python
dictionary["nis"] = "1813553"
```
__Menghilangkan Item__ dapat dilakukan dengan cara :

```python
dictionary.pop("nomor")
```
atau

```python
del dictionary["nomor"]
```

#### __Mengakses Item__  
Setiap item dapat diakses dengan nomor indeks masing-masing. Nomor indeks mulai dengan `0`.

```python
alat_tulis = ["bulpen", "pensil", "penghapus", "penggaris"]

print(alat_tulis[0])
print(alat_tulis[1])
print(alat_tulis[2])
print(alat_tulis[3])
```
Output:
> bulpen  
pensil  
penghapus  
penggaris

Setiap item dalam __List__ juga bisa diakses dengan __Loop__.

```python
alat_tulis = ["bulpen", "pensil", "penghapus", "penggaris"]

for alat in alat_tulis:
    print(alat)
```
Output:
> bulpen  
pensil  
penghapus  
penggaris

#### Menambahkan Item

Gunakan `append()` untuk menambahkan item di akhir __List__.

```python
alat_tulis = ["bulpen", "pensil", "penghapus", "penggaris"]

alat_tulis.append("jangka")
print(alat_tulis)
```

Output:
> ['bulpen', 'pensil', 'penghapus', 'penggaris', 'jangka']

Gunakan `insert()` untuk menambahkan item pada posisi yang spesifik dengan nomor indeks.

```python
alat_tulis = ["bulpen", "pensil", "penghapus", "penggaris"]

alat_tulis.insert(1, "jangka")
print(alat_tulis)
```
Output:
> ['bulpen', 'jangka', 'pensil', 'penghapus', 'penggaris']

Untuk belajar lebih lanjut mengenai list: https://www.w3schools.com/python/python_lists.asp


### Tuples
### Sets
### Dictionaries
## Loop
- ### while
    __While__ digunakan untuk menjalankan pernyataaan selama kondisi yang dituliskan tercapai.
    ```python
    a = 1
    while a < 7:
        print(a)
    a += 1
    ```
    Output:
    > 1  
    2  
    3  
    4  
    5  
    6  

    - __Break__  
     __Break__ digunakan untuk menghentikan __Loop__ walaupun kondisi yang dituliskan benar  .

        ```python
        a = 1
        while a < 7:
            print(a)
            if a == 5:
                break
            a += 1
        ```

        Output:
        > 1  
        2  
        3  
        4  
        5  

    - __Continue__  
    __Continue__ digunakan untuk mengulang __Loop__ tanpa menjalan pernyataan yang berada dibawahnya.
        ```python
        a = 1
        while a < 7:
            a += 1
            if a == 5:
                continue
            print(a)
        ```
        Output:  

        > 2  
        3  
        4  
        6  

- ### for  
    __For__ digunakan untuk mengulang sebuah urutan contohnya seperti list, tuple, set, dictionary, dan string.

    ```python
    siswa =["Kresna","Jeremy","Vannes"]

    for x in siswa:
        print(x)
    ```
    Output:

    > Kresna  
    Jeremy  
    Vannes

    - __Break__  
      
        ```python
        siswa =["Kresna","Jeremy","Vannes"]

        for x in siswa:
            if x == "Jeremy":
                break
        print(x)
        ```

        Output :
        >Kresna

    - __Continue__

        ```python
        siswa =["Kresna","Jeremy","Vannes"]

        for x in siswa:
            if x == "Kresna":
                continue
        print(x)
        ```
        Output :
        > Jeremy  
        Vannes

    - __Nested Loop__  

        ```python
        sifat = ["pintar","tinggi","ganteng"]
        siswa = ["Kresna","Jeremy","Vannes"]

        for x in siswa:
            for y in sifat:
                print (x ,y)
        ```
        Output :
        >Kresna pintar  
        Kresna tinggi  
        Kresna ganteng  
        Jeremy pintar  
        Jeremy tinggi  
        Jeremy ganteng  
        Vannes pintar  
        Vannes tinggi  
        Vannes ganteng  

## Function
## OOP
## Wand
- ### Installation
    Install Wand using pip  
      
    - Windows
      
        ```
        pip install Wand
        ```
    - Mac
      
        ```
        pip3 install Wand
        ```
    Wand menggunakan modul python bernama ImageMagic. Jadi ImageMagick juga perlu diinstall.
    - Windows   
      
        https://imagemagick.org/script/download.php  
          
    - Mac  
      
        ```
        brew install imagemagick
        ```
    
- ### Membuka Image
    ```python
    from wand.image import Image
    from wand.display import display

    image_background = "./scorebola.jpg"
    filename_output = "./score-output.png"

    with Image(filename=background) as img_background:
        display(img_background)
        img_background.format = "png"
        img_background.save(filename=filename_output)
    ```

    `image_background` adalah lokasi dari gambar background yang ingin dibuka. Lokasi file berbeda-beda tergantung tempatnya.

    `filename_output` adalah nama dan lokasi yang diinginkan dari file gambar yang akan di save. Nama file dapat diubah sesuai kebutuhan.

    ---
    ```python 
    with Image(filename=background) as img_background:
    ```
    Kode ini membuka gambar dari `background` dan menamakannya sebagai `img_background`. Nama `img_background` dapat diubah sesuai kebutuhan.

    ```python 
    display(img_background)
    ```
    Kode ini akan menampilkan gambar dari `img_background`.

    ```python
    img_background.format = "png"
    img_background.save(filename=filename_output)
    ```

    Kode ini akan menyimpan file ke lokasi `filename_output` dan menyimpan file sebagai `png`. Tipe file dapat diubah sesuai kebutuhan.

- ### Menulis pada Image
    Kita akan menulis angka `4` pada image yang tadi.

    ```python
    from wand.image import Image
    from wand.color import Color
    from wand.drawing import Drawing
    from wand.display import display

    background = "./scorebola.jpg"
    filename = "score-output.png"
    font_text = "./oswald.ttf"

    body_text = "4"

    with Image(filename=background) as img_background:
        with Drawing() as context:
            context.font = font_text
            context.fill_color = Color('white')
            context.font_size = 300
            metrics = context.get_font_metrics(img_background, body_text, multiline=True)
            context.text(
                x=800,
                y=900,
                body=body_text)
            context(img_background)
        img_background.format = "png"
        img_background.save(filename=filename)
    ```
    `font_text` adalah jenis font yang digunakan untuk menulis pada gambar tersebut.

    `body_text` adalah tulisan yang akan kita tuliskan pada gambar.

    ```python
    with Drawing() as context:
            context.font = font
            context.fill_color = Color('white')
            context.font_size = 300
            metrics = context.get_font_metrics(img_background, body, multiline=True)
            context.text(
                x=800,
                y=900,
                body=body_text)
            context(img_background)
    ```
    ----
    ```python
    with Drawing() as context
    ``` 
    Untuk memanggil function drawing yang diambil dari Wand, yang kemudian kita namakan sebagai context. Context adalah objek yang akan ditulis.

    ```python
    context.font = font_text
    ```
    `context.font` adalah fungsi agar objek __context__ memakai font yang berada di variable `font_text`

    ```python
    context.fill_color = Color('white')
    ```
    `context.fill_color` adalah fungsi untuk objek __context__ memakai warna font putih dari `white`. Warna dalam `Color(<warna>)` dapat diubah sesuai kebutuhan.

    ```python
    context.font_size = 300
    ```
    `context.font_size` adalah fungsi agar objek __context__ mempunyai ukuran `300`. Ukuran dapat diubah sesuai kebutuhan.

    ```python
    metrics = context.get_font_metrics(img_background, body, multiline=True)
    ```
    `context.get_font_metrics` digunakan untuk mendapatkan ukuran dari tulisan yang digambar.

    ```python
    context.text(
    x=0,
    y=700,
    body=body_text)
    ```
    `context.text()` adalah fungsi untuk menentukan posisi dan isi dari objek __context__.  
      
    `x = <posisi>` untuk menentukan posisi koordinat sumbu x. `posisi` dapat diubah sesuai kebutuhan.  
      
    `y = <posisi>` untuk menentukan posisi koordinat sumbu y. `posisi` dapat diubah sesuai kebutuhan.  
      
    `body = body_text` untuk menentukan isi tulisan yang akan ditulis. `body_text` dapat diubah sesuai kebutuhan.

    ```python
    context(img_background)
    ```

    `context(img_background)` adalah fungsi untuk menuliskan objek __context__ pada gambar img_background. Objek __context__ memiliki font, font size, font color, posisi, dan isi yang telah kita berikan di kode sebelumnya.

- ### Menggambar pada Image
    Kita akan menggambar logo Chelsea yang terdapat di `./logo-chelsea.png`

    ```python
    from wand.image import Image
    from wand.color import Color
    from wand.drawing import Drawing
    from wand.display import display

    background = "./scorebola.jpg"
    filename = "score-output.png"
    font_text = "./oswald.ttf"
    filename_logo = "./logo-chelsea.png"

    body_text = "4"

    with Image(filename=background) as img_background:
        with Drawing() as context:
            context.font = font_text
            context.fill_color = Color('white')
            context.font_size = 300
            metrics = context.get_font_metrics(img_background, body_text, multiline=True)
            context.text(
                x=800,
                y=900,
                body=body_text)
            context(img_background)
        with Image(filename=filename_logo) as logo:
            img_background.composite(logo, left=80, top=570)
        img_background.format = "png"
        img_background.save(filename=filename)
    ```

    `filename_logo` adalah lokasi file logo yang dituju

    ```python
    with Image(filename=filename_logo) as logo:
    ```

    Memanggil fungsi `Image()` dari __Wand__ untuk membuka gambar `filename_logo` yang dinamakan sebagai `logo`.

    ```python
    img_background.composite(logo, left=80, top=570)
    ```

    Memanggil fungsi `composite()` untuk menggambar `logo` pada `img_background` dan menetapkan posisinya melalui `left` dan `top`.  
      
    `left` adalah koordinat sumbu x. Dapat diubah sesuai kebutuhan.  
      
    `top` adalah koordinat sumbu y. Dapat diubah sesuai kebutuhan.


## Flask
    Flask adalah sebuah *micro-web framework* yang ditulis dengan Python. Flask tidak membutuhkan library tertentu.
## Certification
## References
