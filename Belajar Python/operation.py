#Operasi pada List, Set, dan String

#len() menghitung panjang
list = [1,2,3,4,5,6,7]
print(list)
print(len(list))

set = {1,2,2,4,5,1,3,7,8,9,4} #set secara otomatis menghilangkan duplikat 
print(set)
print(len(set))

#min dan max
grade = [50,60,75,85,90,99]
print(min(grade)) #terkecil
print(max(grade)) #terbesar

#count
platform = "Dicoding"
print(platform.count("i")) #menghitung jumlah i

print(list.count(4)) #menghitung angka 4 di dalam list, count tidak bisa di lakukan pada set 

tuple = (88,44, 5, 44, 44, 49)
print(tuple.count(44))

#in dan not in

university = "dian nuswantoro university"
print('dian' in university) #true

print('semarang ' not in university) #true


#sort (mengurutkan)
trans = ["bandung", "semarang", "jakarta", "surabaya"]
trans.sort()  # mengurutkan list secara ascending (A-Z)
print(trans)

trans.sort(reverse=True)  # mengurutkan list secara descending (Z-A)
print(trans)

# Jika ingin mendapatkan list baru yang sudah diurutkan tanpa mengubah list asli:
trans = ["bandung", "semarang", "jakarta", "surabaya"]
sorted_trans = sorted(trans)
print(sorted_trans)
