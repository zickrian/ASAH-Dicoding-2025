#Slicing
program = "ASAH DICODING"
print(program[5:]) #memulai dari huruf ke 5
print(program[0:4]) #ASAH

#Formated String
print(f"Halo saya sedang mengikuti program {program}")

#List
list = ["Monitor", "leptop", "handphone", "mouse", "keyboard"]
print(list)
print(list[2:]) #dia memulai dari array ke 2 daari kiri dan menulis full setelahnya
print(list[:2]) #melakukan output dari 0  sampai 2 
print(list[1:5]) #melakukan output dari array 1 sebanyak 5 array
print(list[0:5:2]) # menambahkan agar print kelipatan 2

#daapat melakukan perubahan dalam list
list[0] = "modif"
print(list)

#tuple
tuple = (90, "nilai", "ujian", 100)
print(tuple)

#set 
set1 = {1,2,3,4,5}
set2 = {4,5,6,7,8}
#union dan intersection
unions =  set1.union(set2) #pengabungan dari kedua set
print(unions)
intersection = set1.intersection(set2) #irisan dari kedua set
print(intersection)

#Dictionary
dict = {'Name': 'Firdaus',
        'Age' : 20,
        'Status' : 'student',
        'Major' : 'commputer science'
        }

print(dict)
print(dict['Age']) #print lebih spesifik
#menambah
dict['Learn'] = "Machine Learning"
print(dict)
#menghapus
del dict["Age"]
print(dict)
#memodifikasi
dict['Name'] = "Adenka"
print(dict)

