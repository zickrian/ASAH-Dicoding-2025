# ...existing code...
"""
Penjelasan singkat:
- try: tempat menaruh kode yang berpotensi menyebabkan exception (kesalahan)
- except: menangkap dan menangani exception. Bisa beberapa blok except untuk tipe yang berbeda.
- else: dijalankan hanya jika blok try selesai tanpa exception.
- finally: selalu dijalankan, baik terjadi exception atau tidak (berguna untuk pembersihan resource).
"""


'''
# Contoh penggunaan dengan komentar di samping setiap bagian
try:
    # blok ini dicoba terlebih dahulu — jika ada error, Python lompat ke except yang sesuai
    x = int(input("Masukkan angka pembagi: "))
    hasil = 10 / x  # bisa memicu ZeroDivisionError jika x == 0
except ValueError:
    # menangani kasus input yang bukan angka
    print("Input tidak valid: masukkan angka bulat.")
except ZeroDivisionError:
    # menangani pembagian dengan nol
    print("Kesalahan: tidak boleh membagi dengan nol.")
except Exception as e:
    # menangani exception lain yang tidak terduga (umum)
    print("Terjadi kesalahan:", e)
else:
    # dijalankan hanya jika blok try sukses tanpa exception
    print("Hasil pembagian adalah:", hasil)
finally:
    # selalu dijalankan — cocok untuk menutup file, koneksi, atau membersihkan variabel
    print("Proses selesai. Terima kasih.")
# ...existing code...'''
'''
'''

var = -1

if var < 5:
    raise ValueError("Harus angka positif")
else:
 for i in range(var):
  print(i)
