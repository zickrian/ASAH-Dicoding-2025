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

    def tambah_kecepatan(self):
        self.kecepatan += 20   #OVERRIDDE atau MENIMPA

f1 = Ferari('honda','merah',100)
f1.tambah_kecepatan()
print(f1.kecepatan)