# Penjelasan singkat dan contoh operasi pada array/list di Python.

import array  # modul 'array' menyediakan struktur array tipe-homogen (lebih ringkas dari list untuk tipe primitif)

# Membuat array bertipe signed int (typecode 'i') dan menampilkannya.
# Typecode harus satu karakter: 'i' untuk int, 'f' untuk float, dll.
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)  # contoh keluaran: array('i', [1, 2, 3, 4, 5])

# Contoh list comprehension: membuat list berisi angka 0..9
var_list = [i for i in range(10)]
print(var_list)  # output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Contoh indexing pada list: ambil elemen indeks ke-2 (nilai ketiga)
arr_list = [1, 2, 3, 4, 5, 6]
print(arr_list[2])  # output: 3

print("\n")

# Iterasi dengan akses index: menampilkan current dan next element.
# Catatan: hati-hati agar variable untuk "next" selalu terdefinisi; jika tidak ada elemen berikutnya, gunakan None.
var = [1, 2, 3, 4, 5]  # panjang list = 5

for i in range(len(var)):
    current_var = var[i]          # elemen saat ini
    next_index = i + 1            # indeks elemen berikutnya (bukan nilainya)

    # periksa apakah indeks berikutnya masih dalam rentang list
    if next_index < len(var):
        next_variabel = var[next_index]  # ambil nilai elemen berikutnya
    else:
        # tidak ada elemen berikutnya -> gunakan None sebagai penanda
        next_variabel = None

    # tampilkan current dan next (jika ada)
    print(f'Current Number : {current_var} , Next Number is {next_variabel}')


# Contoh sederhana mencari nilai maksimum dengan dua-pointer (left_pointer menyimpan nilai terbesar sementara).
var_arr = [1, 2, 7, 89, 40, 5]
left_pointer = var_arr[0]  # inisialisasi dengan elemen pertama

for i in range(1, len(var_arr)):
    right_pointer = var_arr[i]    # elemen di posisi i
    # jika elemen di kanan lebih besar, perbarui left_pointer menjadi nilai yang lebih besar
    if right_pointer > left_pointer:
        left_pointer = right_pointer

print(left_pointer)  # hasil: nilai maksimum dari daftar (89)


"""
SOAL
"""
#semisal kita punya array dari 0  -100
var_array = [i for i in range(100+1)]
#lakukan pertambahan di seluruh array dan cari rata2 nya
total = 0
for i in var_array: 
    total += i    #menambahkan seluruh elemen array lalu di masukan ke dalam total

result = total / len(var_array)

print(result) # rata2 dari seluruh array yakni 5050 lalu di bagi dengan panjang array itu sendiri 100 
# hasilnya 50.0
