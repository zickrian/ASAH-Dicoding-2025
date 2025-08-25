#basic looping and if else
stock = "tersedia"

if stock == "tersedia":
    print("ibu membeli ayam")

nilai  = 90

if nilai>=85:
    print("selamat kamu lulus")
else:
    print("kamu lulus tapi di ambang batas")

nilai = 79

if nilai>=85:
    nHuruf = "A"
elif nilai >= 80:
    nHuruf = "AB"
elif nilai >= 75:
    nHuruf = "B"
else:
    nHuruf = "C"

print(nHuruf)

nilai = 89
kepribadian = 'kurang'

if nilai >= 85 and kepribadian == "baik":
    print("Kamu mempunyai kepribadian dan nilai yang sempurna")
elif nilai >=85 and kepribadian != "baik":
    print("nilai kamu bagus tapi tolong perbaiki kepribadian kamu")
else:
    print(" ")

#ternary Operator
#merupakan baris if else dalam one-line
#block_code_benar if kondisi else block_code_salah
lulus = True

print("selamattt atas kelulusan") if lulus  else print("jangan patah semangat")
print("kamu hebat") if nilai >= 85 else print("Belajar lagi ya")

#Ternary tuples
#(block_code_jika_salah) (block_code_jika_bnr)[kondisi]

utbk = "lulus"
pengecekan = ("Jangan patah semangat","Selamat kamu lulus")[utbk == "lulus"]
print(pengecekan)