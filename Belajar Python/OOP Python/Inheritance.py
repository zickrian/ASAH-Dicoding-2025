class MobilBasic():
    def __init__(self,merk,warna,kecepatan):
        self.warna = warna
        self.merk = merk
        self.kecepatan = kecepatan

    def tambah_kecepatan(self): #self merupakan ciri2 dari method
        self.kecepatan += 10

class Ferari(MobilBasic):  #seluruh artribut yang ada pada MobilBasic di turunkan ke Ferari
    def turbo_mode(self):
        self.kecepatan += 150


#output dari mobilBasic

Toyota = MobilBasic('toyota', 'hitam', 80)
print(Toyota.kecepatan)

F1 = Ferari('honda', 'merah', 150)
print(F1.kecepatan)

F1.turbo_mode() #menambahkan 150 ke kecepatan
print(F1.kecepatan)