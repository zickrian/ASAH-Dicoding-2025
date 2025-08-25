#pada array kita dapat melakukan operasi  list comprehension
# ...existing code...
import array

# gunakan typecode satu karakter, 'i' = signed int
arr = array.array('i', [1, 2, 3, 4, 5])
print(arr)  # array('i', [1, 2, 3, 4, 5])

# contoh list comprehension
var_list = [i for i in range(10)]
print(var_list)

arr_list = [1,2,3,4,5,6]
print(arr_list[2]) # output nya 3


print("\n")

var = [1,2,3,4,5]  # dimana panjang dari array ini adalah 5

for i in range(len(var)):
    current_var = var[i]
    next_var = i + 1

    if next_var < len(var):
        next_variabel = var[next_var]
    else:
        next_var = None

    print(f'Current Number : {current_var} , Next Number is {next_variabel}')

