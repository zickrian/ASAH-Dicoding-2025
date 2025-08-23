#UPPER membuat text menjadi huruf besar 
word = "hello"
wordUp = word.upper()

print(wordUp)

#lower membuat text menjadi kecil 
word = "HELLO BRO"
wordLo = word.lower()

print(wordLo)

#Strip merupakan cara untuk menghilangkan whitespace

#lstrip left (menghilangkan di bagian kiri)
greeting = "   good morning"
greet = greeting.lstrip()
print(greeting)
print(greet)
print(greeting.lstrip()) #tanpa harus menetapkan di dalam suatu variabel terlebih dahulu

#rstrip (right)
eat = "Burger   "
eats = eat.rstrip()
print(eats)

#strip (menghilangkan di kanan dan kiri)
night = "  MOON  "
print(night.strip())
print(night.strip().lower()) #kombinasi lower and strip

night = "MoonHello worldmoonmoon"
print(night.strip("moon"+ "Moon")) #double word

#startwith melaukukan pengecekan di kata awal
platform = "asah dicoding"
check = platform.startswith("asah")
print(check)
#endwith melakukan pengecekan di kata ahir 
check = platform.endswith("asah")
print(check)

'''
Memisahkan dan Mengabungkan String
'''
#join di gunakan utk mengabungkan
print(' dan '.join(['aku', 'kita', 'dia', 'bersama'])) #dan pada kata sebelum .join di gunakan untuk batas antar array yang di gabungkan jadi semisal di isi dengan ' ' maka akan menciptakan spasi alias whitespace
#split di gunakan utk memisahkan
print("aku kamu dia bersama".split())

'''
Mengganti Elemen String
'''
#replace atau menganti
platform = "asah dicoding"
asah = platform.replace("asah","indonesia") #menganti asah dengan indonesia
print(asah)

'''
Pengecekan String
'''
#isupper untuk mengecek apakah nilainya besar semua  ini akan mengembalikan true or false
print("KIMONO".isupper()) #true
#islower untuk mengecek apakah nilainya kecil semua              ~~  ::  ~~
print('kimono'.islower()) #true
#isalpha untuk mengecek apakah nilainya alpabet alias huruf semua, kalau ada angka maka akan false
print('alphas10'.isalpha()) #false
#isalnum untuk mengecek apakan ada kombinasi antara huruf dan angka (bisa salah satu bisa keduanya) kalau iya maka true
print('tesmic123'.isalnum()) #true
#isdecimal untuk mengecek decimal
print('44.4'.isdecimal()) #false karna bukan numerik atau angka  cth: 1 2 3 maka akan true
#isspace untuk mengecek Space 
print("      ".isspace()) # true
#istittle utk mengecek apakah tiap huruf di awal kata mengunakan huruf besar atau tidak
print('Hello World'.istitle()) #true

'''
Formatting pada String
'''
#zfill untuk memastikan bahwa jumlah kata sesuai dengan jumlah yang di tetapkan
program = "ASAH"
print(program.zfill(5)) #output berupa 0ASAH karna zfill memastikan bahwa nilai pada string trsbt adalah 5

#rjust sama seperti zfill tetapi membuat text rata kanan
print(program.rjust(20)) #memastikan jumlah tetap 20 termasuk 'asah'
print(program.rjust(20, '1')) 
#ljust membuat text rata kiri
#center (tengah)
print(program.center(8, '!'))
#cara penulisan python
'''
\' Single quote
\" Double quote
\t Tab
\n Newline (line break)
\\ Backslash
'''