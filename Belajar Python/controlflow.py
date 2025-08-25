# basic branching (if/elif/else) and simple conditional expressions

# Contoh 1: pengecekan sederhana menggunakan if
stock = "tersedia"  # status barang

if stock == "tersedia":
    # jika kondisi terpenuhi, jalankan blok ini
    print("ibu membeli ayam")

# Contoh 2: if-else untuk mengecek nilai
nilai = 90

if nilai >= 85:
    # kondisi benar
    print("selamat kamu lulus")
else:
    # kondisi salah
    print("kamu lulus tapi di ambang batas")

# Contoh 3: if-elif-else untuk menentukan grade huruf
nilai = 79  # ubah nilai untuk melihat cabang berbeda

if nilai >= 85:
    nHuruf = "A"
elif nilai >= 80:
    # dieksekusi jika nilai < 85 tapi >= 80
    nHuruf = "AB"
elif nilai >= 75:
    nHuruf = "B"
else:
    # nilai < 75
    nHuruf = "C"

print(nHuruf)  # cetak grade huruf yang ditentukan

# Contoh 4: kombinasi kondisi dengan operator logika (and, or, !=)
nilai = 89
kepribadian = 'kurang'

if nilai >= 85 and kepribadian == "baik":
    # kedua kondisi harus True
    print("Kamu mempunyai kepribadian dan nilai yang sempurna")
elif nilai >= 85 and kepribadian != "baik":
    # nilai bagus tapi kepribadian bukan 'baik'
    print("nilai kamu bagus tapi tolong perbaiki kepribadian kamu")
else:
    # kondisi lainnya
    print(" ")

# Ternary Operator (conditional expression)
# Bentuk singkat if-else: <expr_true> if <condition> else <expr_false>
lulus = True

print("selamattt atas kelulusan") if lulus else print("jangan patah semangat")
print("kamu hebat") if nilai >= 85 else print("Belajar lagi ya")

# Ternary tuple (trik menggunakan tuple dan boolean sebagai indeks)
# struktur: (hasil_salah, hasil_benar)[kondisi_boolean]
utbk = "lulus"
pengecekan = ("Jangan patah semangat", "Selamat kamu lulus")[utbk == "lulus"]
print(pengecekan)

#perulangan
#FOR
#for <var>  in <inerable>

list = [1,2,3,4,5]
for i in list:
    print(i, end=" ")
print("\n")
for i in range(10):
    print(i, end=" ")  #range di mulai dari 0 jadi oputput = 0 - 9
print("\n")
#format range ( start, end , step)
for i in range ( 1,10,2):
    print(i, end=" ")

#while
print("\n")
i = 1 #angka awal dari while
while i <=5:
    print(i)
    i += 1 #menambahkan 1 untuk setiap kali di jalankan sampai memenuhi <=5

#nedted loop atau loop di dalam loop

for i in range(1,3):   # ini akan berjalan  1 - 2 maka dari itu output nya adalah 1 1 2 2
    for j in range(1,3): # ini berjalan di dalam loop output adalah 12 12
        print(i,j)

for i in range(1,4):  #code ini seharusnya menampilkan 1 -3 tetapi dia terseret kalau menurut saya dengan loop di dalam
    #sehingga yang awalnya 1 2 3 menjadi atau mengikuti loop di dalam
    for j in range(1,6): # output dari loop ini 1 - 5 
        print(i,j)
"""
output 
1-3
1-5
terbawa sampai 5
11
12
13
14
15    jadi setelah tingkatan pertama jalan untuk pertama kali , yakni 1 dia akan membiarkan tingkatan 2 habis yakni sampai 5 kalau sudah abis maka dia kembali ke tingkatan pertama lagi untuk melakukan ulang
21
22
23
24
25
31
32
33
34
35

semisal di loop dalam 1- 4 maka loop utama akann mengulagi 4x terlebih dahulu sebelum masuk kedalam loop kedua
jadi 
1
1
1
1
2
2
2
2

like that
"""

for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)

# akan menjalankan for pertama 0, lalu lanjut ke tingkat kedua 0 - 9 baru balik lagi mennuju ke tingkat pertama untuk 1 yang kedia 

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print(f'Huruf saat ini: {huruf}')


# for else
num = [1,2,3,4,5]

for i in num:
    if i == 4:
        print("angka di temukan")
        print(i)
else:
    print("angka tidak di temukan")
#while else
counter = 0

while counter < 3:
    print("ASAH")
    counter += 1
else:
    print("tidak kurang dari 3") # kenapa ini juga di jalankan? karna asah == 3 seharusnya <3


#List Comprehension
list = [1,2,3,4]
pangkat = [] # akan di isi pake append

for n in list:
    pangkat.append(n**2)  #mengisi pangkat dengan n berpangkat 2, dan n itu di dapat dari list karna for n in list
print(pangkat)
print("\n")
list=[1,2,3,4]
pangkat = [n**2 for n in list] #melakukan di one-line
print(pangkat)

