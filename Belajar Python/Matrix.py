#di dalam matriks kita dapat menggunakan list biasa dan juga library numpy

import numpy as np
import sys #mengecek bit yang di gunakan

list = [[1,2,3],[4,5,6],[7,8,9]]
for i in list:
    print(i,"\n")

#mencoba menggunakan numpy

matriks = np.array([[1,2,3],[4,5,6],[7,8,9]])
print('Jumlah Bit yang di gunakan pada Matriks = ', matriks.size * matriks.itemsize) #numpy menggunakan 72 bit 
print('Jumlah Bit yang di gunakan pada List = ', sys.getsizeof(list * len(list))) #list biasa menghabiskan 128 bit

for i in matriks:
    print(i,"\n")

#kita jga bisa mengisi matriks mengunakan list comprehension
var_matriks = [[0 for j in range(3)] for i in range(4)]

for i in var_matriks:
    print(i, '\n')

#cara indexing pada matriks
'''
[0, 0, 0]

[0, 0, 0]

[0, 0, 0]

[0, 0, 0]
'''
matriks1 = [[1,2,3], #0    
            [4,5,6], #1
            [7,8,9]] #2
            #0 1 2

#semisal ingin print angka 6 maka yang pertama kita lihat baris ke berapa 6 berada di baris ke 1 lalu dia ada kolom berapa,
#kolom disini berarti yang ada di dalam [ 4,5,6] dia ada di 2  karna matriks di mulai dari 0
'''
    [1,4,7]
    [2,5,8]
    [3,6,9]

'''
var_1 = matriks1[2][1]
print(var_1)

matriks1[1][2]=9

print(matriks1)

print(matriks1[0][2])
#[[1, 2, 3], [4, 5, 9], [7, 8, 9]]
#jadi 0 itu berari beradaa di matriks pertama [1,2,3] lalu 2 itu di dalam matriks pertama yakni 3



#cara menghitung perkalian dengan matriks tanpa numpy

var = [[1,2,3 ],
       [4,5,6]]

var_result= [[0 for j in range(3)] for i in range(2)]

for i in range(len(var)): #len var berisi 0 dan juga 1
    for j in range(len(var[0])): #len var[0] berisi 0 1 2 
        var_result[i][j] = var[i][j]*2

print(var_result) 

#cara menggunakan numpy

var_before = np.array( [[1,2,3],[4,5,6]])

result =  var_before * 2
print(result)

#cek bits
print("ukuran bit dari result menggunakan matrix Pake Numpy: ", var_before.size * var_before.itemsize )
print("ukuran bit dari result menggunakan matrix Manual pake List: ", sys.getsizeof(var * len(var)))


