class Mobil:
    #artribut
    warna = "merah"
    roda = 4

mobil = Mobil() #cara pemangilan class di oop mirip dengan fungsi
print(mobil.warna, 'dan beroda: ', mobil.roda)


class Montor:
    def __init__(self): #setiap kali menetapkan sesuatu di awali dengan nama dari paremeter itu misal self ya self.merek
        self.warna = 'blue'
        self.merk = 'yeho'


montor_1 = Montor()
print(montor_1.warna , montor_1.merk)


class Mobils:
    def __init__(self,warna,merk,kecepatan):   #paremeter harus di isi ketika di pangil
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan
 
    def tambah_speed(self): #object method
        self.kecepatan += 10

    #menambahkann static method
    @staticmethod
    def call_merek():
        print("merk mobil ini sesuai apa yang di isikan")

    @classmethod
    def call_mereks(cls):
        pass

Mobo = Mobils('merah','honda',250) #mengisi parameter yang ada
print(Mobo.warna, Mobo.merk, Mobo.kecepatan) #merah honda 250

Mobo.tambah_speed()  #ini adalah cara untuk eanggil metod
#setelah di tambahakan metod
print(Mobo.kecepatan) #260 karna sebelumnya memangil metod add speed sebesar 10 

Mobo.call_merek()
Mobils.call_merek() #kita bisa memanggil tanpa harus membuat artribut dulu (lanngsung)