'''
Library web scraping adalah jenis library untuk membantu pengguna mengumpulkan data dari halaman web. 
Proses ini disebut sebagai “web scraping” atau “web crawling”. Anda bisa menggunakan fungsi dan
metode pada library ini untuk mengekstraksi informasi dari situs web dan menyimpannya dalam
format yang dapat diakses dan digunakan dalam analisis atau aplikasi lainnya. 
'''
#Beautifulsoup
from urllib.request import urlopen
from bs4 import BeautifulSoup
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Membuat objek BeautifulSoup
soup = BeautifulSoup(html, "html.parser")
 
# Mencetak judul halaman
print(soup.title)

#Urllib
from urllib.request import urlopen
 
# Pengambilan konten
url = "http://python.org/"
page = urlopen(url)
html = page.read().decode("utf-8")
 
# Mencari indeks awal dan akhir
start_index = html.find("<title>") + len("<title>")
end_index = html.find("</title>")
 
# Mengekstrak dan mencetak judul halaman
title = html[start_index:end_index]
print(title)
