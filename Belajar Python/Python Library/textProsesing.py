
'''
PIP
PIP adalah package manager resmi dari Python yang dapat digunakan untuk mengunduh, 
menginstal, menghapus, dan mengelola package Python dari Python Package Index (PyPI) 
dan repositori lainnya.


Conda
Selain pip yang termasuk package manager resmi dari Python, ada juga conda yang 
merupakan package manager dan environment manager untuk Python. 

'''

import re #regex utk mengecek pola tulisan

pola = '^[^@]+@[^@]+'
string = 'firdaus@gmail.com'

hasil = re.match(pola, string)

if hasil:
    print('sudah sama')
else:
    print('Ada perbedaaan format pada teks')