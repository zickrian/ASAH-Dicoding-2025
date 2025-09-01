# fungsi dalam python

# Fungsi untuk menghitung luas persegi panjang dengan parameter panjang dan lebar
def luas_persegi_panjang(panjang, lebar):
    result  = panjang * lebar  # Menghitung hasil perkalian panjang dan lebar
    return result  # Mengembalikan hasil perhitungan

# Memanggil fungsi dengan positional argument (berdasarkan urutan parameter)
persegi_panjang1 = luas_persegi_panjang(10, 2)  # Menghitung luas persegi panjang dengan panjang=10 dan lebar=2
print(persegi_panjang1)  # Menampilkan hasil perhitungan

# Memanggil fungsi dengan keyword argument (menyebutkan nama parameter secara eksplisit)
print("hasil dari persegi panjang2 adalah: ", luas_persegi_panjang(lebar=10, panjang=3))  # Menghitung luas dengan parameter terbalik


# Fungsi dengan parameter positional atau keyword
def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan  # Mengembalikan pesan sapaan

# Memanggil fungsi dengan positional argument
print(greeting("Dicoding", "Selamat pagi!"))  # Menampilkan sapaan dengan nama dan pesan

# Memanggil fungsi dengan keyword argument
print(greeting(pesan="Selamat sore!", nama="Dicoding"))  # Menampilkan sapaan dengan parameter terbalik


# Fungsi dengan parameter positional-only (hanya bisa dipanggil berdasarkan urutan)
def penjumlahan(a, b, /):
    return a + b  # Mengembalikan hasil penjumlahan dua angka

# Memanggil fungsi dengan positional argument
print(penjumlahan(3, 5))  # Menampilkan hasil penjumlahan 3 + 5


# Fungsi dengan parameter keyword-only (hanya bisa dipanggil dengan menyebutkan nama parameter)
def greeting(*, nama, pesan):
    return "Halo, " + nama + "! " + pesan  # Mengembalikan pesan sapaan

# Memanggil fungsi dengan keyword argument
print(greeting(pesan="Selamat sore!", nama="Dicoding"))  # Menampilkan sapaan dengan nama dan pesan


# Fungsi dengan variadic positional arguments (*args)
def hitung_total(*args):
    print(type(args))  # Menampilkan tipe data args (tuple)
    total = sum(args)  # Menghitung total dari semua angka dalam args
    return total  # Mengembalikan hasil penjumlahan

# Memanggil fungsi dengan sejumlah angka sebagai argumen
print(hitung_total(1, 2, 3))  # Menampilkan total dari 1 + 2 + 3


# Fungsi dengan variadic keyword arguments (**kwargs)
def cetak_info(**kwargs):
    info = ""  # Inisialisasi string kosong untuk menyimpan informasi
    for key, value in kwargs.items():  # Iterasi melalui pasangan key-value dalam kwargs
        info += key + ': ' + value + ", "  # Menambahkan informasi ke string
    return info  # Mengembalikan string informasi

# Memanggil fungsi dengan sejumlah pasangan key-value
print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))  # Menampilkan informasi


# Fungsi lambda untuk operasi pertambahan
pertambahan = lambda sisi, hasil: sisi + sisi  # Fungsi lambda untuk menambahkan sisi dua kali
print(pertambahan(10, 10))  # Menampilkan hasil pertambahan 10 + 10


