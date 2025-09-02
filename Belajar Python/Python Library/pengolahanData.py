#pandas  library pengolahan dan analisis data
import pandas as pd

data = {
    'nama' : ['gagah','herry','yanti','deson'],
    'umur' : [20,21,22,23],
    'pekerjaan':['mahasiswa','mahasiswa','dokter','engginer'] 
}

hasil = pd.DataFrame(data)
print(hasil)

#numpy  library array or matrix
import numpy
matriks = numpy.array([[1,2,3],[4,5,6],[7,8,9]])
print(matriks)

#Matplotlib    library visualisasi data
import matplotlib.pyplot as plt

x = [1,2,3,4,5]
y = [5,6,7,8,9]

visual_data = plt.plot(x,y)
plt.title("Contoh Plot Garis")
plt.xlabel("Sumbu X")
plt.ylabel("Sumbu Y")

plt.show

#Seaborn visualisasi data sama seperti matplotlib. Bahkan library seaborn dibangun berdasarkan pada library matplotlib.
import seaborn as sns
import matplotlib.pyplot as plt
 
# Contoh data
tips = sns.load_dataset('tips')  # Memuat dataset tips dari Seaborn
 
# Contoh plot histogram
sns.histplot(tips['total_bill'], kde=True)
plt.title('Histogram Total Bill')
plt.xlabel('Total Bill')
plt.ylabel('Frequency')
plt.show()