# PENJELASAN LENGKAP NOTEBOOK SISTEM REKOMENDASI FILM

## [1] Markdown - Header
Judul section untuk import library

## [2] Code - Import Library
Import semua library yang dibutuhkan:
* numpy & pandas: manipulasi data
* matplotlib & altair: visualisasi
* sklearn: machine learning utilities
* tensorflow v1: untuk membangun model collaborative filtering
* collections: struktur data tambahan

## [3] Code - Setup Altair
Konfigurasi Altair untuk visualisasi interaktif di Google Colab:
* Enable transformer untuk handle dataset besar
* Enable renderer untuk Colab environment

## [4] Markdown - Header
Judul section untuk data loading

## [5] Code - Download Dataset
Download dataset MovieLens 100k dari internet:
* 943 users
* 1682 movies
* 100,000 ratings
Dataset di-extract ke folder lokal

## [6] Code - Load Dataset
Membaca 3 file CSV:
1. users: data pengguna (user_id, age, sex, occupation, zip_code)
2. ratings: data rating (user_id, movie_id, rating, timestamp)
3. movies: data film (movie_id, title, release_date, genre dalam format biner)

## [7] Code - Cek Jumlah Data
Menampilkan statistik dataset:
* 1682 film unik
* 943 pengguna unik
* 100,000 rating total

## [8] Code - Preprocessing ID
Mengubah ID agar dimulai dari 0 (bukan 1):
* user_id: 1-943 → 0-942
* movie_id: 1-1682 → 0-1681
* Ekstraksi tahun rilis dari tanggal
* Konversi rating ke float

## [9] Code - Hitung Genre
Menghitung jumlah kemunculan setiap genre:
* Drama paling banyak (725 film)
* Comedy (505 film)
* Action & Thriller (masing-masing 251 film)

## [10] Code - Fungsi Mark Genres
Membuat fungsi untuk menggabungkan genre:
* get_random_genre(): pilih 1 genre random dari film
* get_all_genres(): gabungkan semua genre dengan tanda "-"
Contoh output: "Action-Adventure-Thriller"

## [11] Code - Tampilkan All Genres
Menampilkan kolom all_genres yang berisi kombinasi genre setiap film

## [12] Code - Merge Dataset
Menggabungkan 3 dataset (ratings, movies, users) menjadi 1 dataframe lengkap bernama "movielens"

## [13] Markdown - Header
Judul section untuk eksplorasi data

## [14] Code - Setup Helper Functions
Membuat fungsi utility untuk eksplorasi:
* mask(): filter dataframe berdasarkan kondisi
* flatten_cols(): flatten multi-level column names
* Set display options pandas (max 10 rows, 3 decimal)

## [15] Code - Deskripsi Users
Menampilkan statistik deskriptif dataset users:
* Rata-rata umur: 34 tahun
* Mayoritas: Male (670 dari 943)
* Pekerjaan terbanyak: student (196 orang)

## [16] Code - Visualisasi Occupation Filter
Membuat chart interaktif Altair:
* Bar chart occupation
* Filter interaktif untuk slicing data
* Fungsi filtered_hist() untuk histogram terfilter

## [17] Code - Analisis User Ratings
Agregasi rating per user:
* rating_count: jumlah rating per user
* rating_mean: rata-rata rating per user
Visualisasi dengan 3 chart:
1. Histogram jumlah rating per user
2. Histogram rata-rata rating per user
3. Bar chart occupation (dengan filter interaktif)

## [18] Code - Analisis Movie Ratings
Agregasi rating per film:
* rating count: jumlah rating per film
* rating mean: rata-rata rating per film
Visualisasi dengan 3 chart berdasarkan genre (dengan filter interaktif)

## [19] Code - Film Rating Terbaik
Menampilkan 10 film dengan rating terbaik (minimal 20 rating)
Filter untuk menghindari film dengan rating terlalu sedikit

## [20] Code - Fungsi Split Dataset
Membuat fungsi untuk split data train/test:
* Default: 90% train, 10% test
* Menggunakan random sampling

## [21] Markdown - Penjelasan SparseTensor
Dokumentasi tentang tf.SparseTensor:
* Indices: koordinat elemen non-nol [N, ndims]
* Values: nilai elemen non-nol [N]
* dense_shape: bentuk lengkap tensor [ndims]

## [22] Code - Fungsi Build SparseTensor
Membuat fungsi untuk convert ratings DataFrame ke SparseTensor:
* indices: [user_id, movie_id]
* values: rating
* dense_shape: [jumlah_user, jumlah_movie]

## [23] Markdown - Penjelasan Loss Function
Dokumentasi tentang fungsi loss yang akan dibuat menggunakan Mean Squared Error

## [24] Code - Fungsi Loss MSE
Implementasi sparse mean squared error:
* Prediksi: U × V^T (matrix multiplication)
* Loss: MSE antara rating asli vs prediksi
* Hanya menghitung loss untuk rating yang ada (sparse)

## [25] Markdown - Penjelasan Parameter
Dokumentasi 3 parameter fungsi loss:
1. sparse_ratings: matriks rating [N, M]
2. user_embeddings: embedding user U [N, k]
3. movie_embeddings: embedding movie V [M, k]

## [26] Code - Class CFModel
Class untuk Collaborative Filtering Model:
* __init__(): inisialisasi model
* embeddings: property untuk akses embedding
* train(): fungsi training dengan:
  - Gradient Descent Optimizer
  - Tracking metrics (train_error, test_error)
  - Plotting hasil training
  - Iterasi default: 100, learning rate: 1.0

## [27] Code - Fungsi Build Model
Membuat model collaborative filtering:
1. Split data train/test
2. Convert ke SparseTensor
3. Inisialisasi embedding U dan V (distribusi normal)
4. Hitung train_loss dan test_loss
5. Return CFModel object

## [28] Markdown - Header
Judul section untuk training

## [29] Code - Training Model
Melatih model dengan:
* embedding_dim = 30 (dimensi vektor embedding)
* init_stddev = 0.5 (standar deviasi inisialisasi)
* num_iterations = 1000
* learning_rate = 10.0
Output: grafik train_error vs test_error

## [30] Markdown - Penjelasan Similarity
Dokumentasi tentang 2 metode similarity:
* DOT product
* COSINE similarity

## [31] Code - Fungsi Compute Scores
Menghitung skor kesamaan:
* DOT: u · V^T
* COSINE: (u/||u||) · (V/||V||)^T
Return: array skor untuk semua item

## [32] Code - Fungsi User Recommendations
Menghasilkan rekomendasi film untuk user tertentu (user 942):
1. Hitung skor similarity antara user dan semua film
2. Buat DataFrame dengan skor, judul, genre
3. Hapus film yang sudah di-rating (jika exclude_rated=True)
4. Sort berdasarkan skor tertinggi
5. Tampilkan top-k rekomendasi

## [33] Markdown - Penjelasan User Recommendations
Dokumentasi cara kerja fungsi user_recommendations:
* Menghitung similarity
* Membuat DataFrame hasil
* Filter film yang sudah di-rating
* Mengurutkan dan menampilkan top-k

## [34] Markdown - Header
Judul untuk melihat output rekomendasi

## [35] Code - Generate Rekomendasi User
Menjalankan rekomendasi untuk user 942:
* Dengan COSINE similarity (top 5)
* Dengan DOT product (top 5)
Set USER_RATINGS = True untuk enable fungsi

## [36] Markdown - Penjelasan Movie Neighbors
Dokumentasi tentang rekomendasi berdasarkan kemiripan film

## [37] Code - Fungsi Movie Neighbors
Mencari film serupa berdasarkan judul:
1. Cari film berdasarkan substring judul
2. Hitung similarity dengan semua film lain
3. Sort berdasarkan skor
4. Tampilkan top-k film serupa
Berguna untuk "users who liked this also liked..."

## [38] Code - Generate Movie Neighbors
Mencari film serupa dengan "Star Wars":
* Dengan DOT product
* Dengan COSINE similarity
Menampilkan film-film dengan genre/karakteristik serupa
