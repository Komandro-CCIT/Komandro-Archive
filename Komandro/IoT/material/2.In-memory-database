# 2 - In Memory Database

---

## Overview

Setelah kalian membaca Introduction di bab sebelumnya, next step kalian bisa lanjutin di materi IMBD berikut ini :

In-memory database adalah sistem manajemen basis data yang menyimpan data secara eksklusif di memori utama komputer. Ini berbeda dengan sistem manajemen basis data tradisional, yang menyimpan data di disk. In-memory database menawarkan sejumlah keunggulan dibandingkan sistem manajemen basis data tradisional, mulai dari:

- Performa yang lebih cepat: Data yang disimpan di memori dapat diakses jauh lebih cepat daripada data yang disimpan di disk. Ini karena memori memiliki waktu akses yang jauh lebih cepat daripada disk.

- Efisiensi yang lebih tinggi: In-memory database dapat menggunakan memori lebih efisien daripada sistem manajemen basis data tradisional. Ini karena in-memory database tidak perlu mem-buffer data di disk.
- Scalability yang lebih baik: In-memory database dapat menskala dengan lebih baik daripada sistem manajemen basis data tradisional. Ini karena in-memory database dapat didistribusikan ke sejumlah server.

Berikut adalah beberapa contoh in-memory database:

- **Couchbase** adalah in-memory NoSQL database yang mendukung berbagai jenis data, termasuk dokumen, kunci-nilai, dan array. Couchbase digunakan oleh berbagai perusahaan, termasuk IBM, Cisco, dan PayPal.

- **MemSQ**L adalah in-memory SQL database yang menawarkan performa yang sangat tinggi untuk transaksi dan analisis. MemSQL digunakan oleh berbagai perusahaan, termasuk Netflix, Spotify, dan Amazon.

- **Redis** adalah in-memory key-value store yang sangat populer. Redis digunakan oleh berbagai perusahaan, termasuk Twitter, GitHub, dan Stack Overflow.

Berikut adalah beberapa contoh penggunaan in-memory database:

- Fraud detection. In-memory database dapat digunakan untuk mendeteksi penipuan secara real-time dengan menganalisis data transaksi secara cepat.

- Online trading. In-memory database dapat digunakan untuk menyediakan data harga saham secara real-time kepada para trader.

- Chat rooms. In-memory database dapat digunakan untuk menyimpan pesan chat secara real-time agar dapat diakses dengan cepat oleh para pengguna.

- Shopping carts. In-memory database dapat digunakan untuk menyimpan informasi tentang produk yang dipilih oleh pengguna dalam sebuah shopping cart.

In-memory database adalah teknologi yang sangat powerful untuk aplikasi yang membutuhkan akses data yang cepat dan real-time. Namun, in-memory database juga memiliki beberapa keterbatasan, seperti kapasitas yang terbatas dan biaya yang lebih tinggi.In-memory database masih merupakan teknologi yang relatif baru. Namun, popularitasnya meningkat karena semakin banyak aplikasi yang membutuhkan kinerja yang tinggi.

**Perbedaan IMDB dan SQL**

In-memory database (IMDB) dan SQL adalah dua teknologi yang berbeda yang dapat digunakan untuk menyimpan dan mengelola data. IMDB menyimpan data di memori utama komputer, sedangkan SQL adalah bahasa pemrograman yang digunakan untuk mengakses dan memanipulasi data dalam basis data.Berikut adalah beberapa perbedaan utama antara IMDB dan SQL:



Secara umum, IMDB menawarkan kinerja yang lebih cepat dan efisiensi memori yang lebih baik daripada SQL. Namun, IMDB juga lebih kompleks dan memiliki tingkat konsistensi data yang lebih rendah.Berikut adalah beberapa contoh penggunaan IMDB dan SQL:

- IMDB cocok untuk aplikasi yang membutuhkan kinerja yang tinggi, seperti aplikasi transaksional dan analisis. Misalnya, IMDB dapat digunakan untuk menyimpan data transaksi e-commerce atau data analitik untuk data warehouse.
- SQL cocok untuk aplikasi yang membutuhkan skalabilitas dan konsistensi data yang tinggi, seperti aplikasi data warehouse dan manajemen dokumen. Misalnya, SQL dapat digunakan untuk menyimpan data dokumen atau data transaksional untuk aplikasi perbankan.

Pada akhirnya, pilihan antara IMDB dan SQL tergantung pada kebutuhan spesifik aplikasi.

## Redis

**Apa itu Redis?**

Redis adalah database NoSQL yang menggunakan memori utama. Redis adalah singkatan dari "Remote Dictionary Server". Redis sendiri merupakan system data key- value berbasis memory (RAM) yang diriilis pada tahun 2009 sebagai project open source.

Dan itulah mengapa redis tidak dipakai sebagai database utama karena ketika redis mati, data otomatis akan hilang.



Note :

- Redis juga bisa menyimpan data di disk, tetapi hanya sebagai back up ketika redis sedang berjalan.

- Redis hanya akan memanipulasi data ke memory (RAM) ketika berjalan.

Berikut adalah beberapa fitur utama Redis:

- Penyimpanan cache: Redis dapat digunakan untuk menyimpan data yang sering diakses, seperti data produk atau data pengguna. Hal ini dapat meningkatkan kinerja aplikasi web.

- Database nilai-kunci: Redis dapat digunakan untuk menyimpan data dalam format nilai-kunci. Hal ini dapat digunakan untuk menyimpan data seperti token otentikasi atau data konfigurasi.

- Pub/sub: Redis dapat digunakan untuk mengirim pesan dari satu proses ke proses lain. Hal ini dapat digunakan untuk membangun sistem real-time, seperti sistem notifikasi atau sistem obrolan.

- Streaming: Redis dapat digunakan untuk mengalirkan data dari satu proses ke proses lain. Hal ini dapat digunakan untuk membangun sistem real-time, seperti sistem analisis data atau sistem streaming media.

Redis adalah database yang serbaguna dan dapat digunakan untuk berbagai aplikasi. Redis adalah pilihan yang baik untuk aplikasi yang membutuhkan kinerja yang tinggi dan fleksibilitas.

**Hubungan IMDB dan Redis**

In-memory database (IMDB) dan Redis adalah dua teknologi yang berbeda yang dapat digunakan untuk menyimpan dan mengelola data. IMDB menyimpan data di memori utama komputer, sedangkan Redis adalah database NoSQL yang menggunakan memori utama.Redis dapat digunakan sebagai IMDB, tetapi ada beberapa perbedaan penting antara keduanya.

IMDB biasanya dirancang untuk aplikasi transaksional dan analitik, sedangkan Redis lebih umum digunakan untuk aplikasi yang membutuhkan kinerja yang tinggi untuk operasi tertentu, seperti penyimpanan cache atau kunci-nilai.

**Kapan dan Mengapa Butuh Redis?**

Redis seringkali menjadi pilihan utama dalam pengembangan aplikasi Internet of Things (IoT) karena sejumlah alasan yang membuatnya sangat sesuai dengan kebutuhan dan karakteristik unik dari lingkungan IoT. Berikut adalah beberapa alasan utama:

- Ketika database utama lambat : Redis disini akan sengat membantu ketika traffic dari user sangat banyak dan akan membebani database utama, dan disini redis berfungsi menyimpan data sementara sehingga ketika ada ada user lain request hal yang sama maka tidak harus ke database utama.

- Kinerja Tinggi dan Responsif: Redis dirancang untuk memberikan kinerja tinggi dan responsif. Dengan menyimpan data di dalam memori utama (in-memory storage), Redis dapat memberikan latensi yang rendah dalam mengakses dan menyimpan data. Hal ini sangat penting dalam skenario IoT di mana kecepatan respons sistem adalah faktor kunci.

- Skema Data Sederhana dan Fleksibel:Redis menggunakan struktur data sederhana seperti string, hash, list, set, dan sorted set. Ini memberikan fleksibilitas dalam menyimpan dan mengambil data, yang dapat sesuai dengan kebutuhan variasi data yang mungkin ditemui dalam aplikasi IoT.

- Pub/Sub (Publish/Subscribe) untuk Komunikasi Real-Time:Redis memiliki fitur pub/sub yang memungkinkan komunikasi real-time antara berbagai komponen dalam sistem IoT. Ini sangat berguna untuk mendukung sinkronisasi dan peringatan yang cepat berdasarkan perubahan status atau peristiwa tertentu.

- Data Caching:Redis dapat digunakan sebagai sistem caching untuk menyimpan sementara data yang sering diakses. Dalam konteks IoT, di mana data seringkali dihasilkan dengan cepat dan perlu diakses secara instan, mekanisme caching ini sangat bermanfaat untuk mengurangi beban pada sistem dan meningkatkan responsifitas.

- Persistensi Opsi yang Dapat Dikonfigurasi:Meskipun Redis secara umum adalah basis data in-memory, ia juga menyediakan opsi persistensi yang dapat dikonfigurasi. Hal ini memungkinkan pengguna untuk memilih apakah data harus disimpan hanya di dalam memori atau juga di disk, sesuai dengan kebutuhan aplikasi IoT tertentu.

- Ringan dan Mudah Dikonfigurasi:Redis memiliki overhead yang rendah dan mudah dikonfigurasi, membuatnya cocok untuk perangkat IoT dengan sumber daya terbatas. Kemudahan konfigurasi ini juga memudahkan integrasi dengan aplikasi IoT yang beragam.

Dukungan Komunitas yang Kuat:Redis memiliki komunitas pengguna yang besar dan aktif. Ini berarti ada banyak sumber daya, dokumentasi, dan dukungan komunitas yang dapat diandalkan untuk membantu pengembang IoT saat menghadapi masalah atau mencari solusi. Ketika membangun aplikasi IoT, pengembang sering mencari solusi yang dapat menangani volume data tinggi dengan latensi rendah, dan Redis memenuhi kriteria tersebut dengan baik.

**Install Redis**

Redis merupakan aplikasi yang dibuat menggunakan Bahasa pemrograman C, untuk menggunakan Redis kita harus kompilasi kode program redisnya. Oleh karena itu disarankan menggunakan OS Linux atau Mac karena sudah ada compiler C. Jika menggunakan Windows kalian bisa pakai Docker yang sudah menyediakan distribusi bawaan untuk Bahasa pemrograman C.

Sebelumnya kami sangat membebaskan pilihan kalian dalam penginstallannya akan tetapi akan lebih baik jika menggunakan Rasberry PI dalam pembuatannya, namun tidak perlu khawatir karena tidak ada kita bisa menggunakan Virtual Machine yang di dalamnya kita Install OS Raspberry.

https://www.youtube.com/watch?v=y3QF7DrUIg0&ab\_channel=DestryHutagaol

**Syntax sederhana**

Kalau temen temen masih ingat tadi redis adalah system basis data key- value berbasis memory.

Dalam Redis, "key-value" merujuk pada struktur data dasar yang digunakan untuk menyimpan dan mengambil data. Redis adalah basis data yang memanfaatkan model key-value ini, di mana setiap nilai (value) disimpan dengan menggunakan kunci (key) yang unik.

Dalam Redis, kunci **(key)** adalah string yang digunakan untuk mengidentifikasi dan mengakses nilai (value) terkait. Kunci dapat berupa string apa pun, termasuk teks, angka, atau kombinasi keduanya. Penting untuk memilih kunci yang deskriptif dan unik agar memudahkan dalam mengelola dan mencari data.

Nilai **(value)** dalam Redis dapat berbagai jenis data, termasuk string, angka, daftar (list), himpunan (set), hash, dan struktur data lainnya. Redis mendukung berbagai jenis operasi pada nilai-nilai ini, seperti menetapkan nilai baru untuk kunci, mengambil nilai yang terkait dengan kunci, dan melakukan manipulasi data terperinci berdasarkan jenis nilai yang digunakan.

**Contoh penggunaan key-value dalam Redis:**

**Disc** : semua contoh disini kami menggunakan Bahasa phyton dalam contoh pembuatannya

**Menetapkan nilai untuk kunci:**

SET mykey "Hello Redis"

**Mendapatkan nilai yang terkait dengan kunci:**

GET mykey

**Menambahkan daftar nilai ke kunci:**

LPUSH mylist "element1"

LPUSH mylist "element2"

**Mendapatkan semua nilai dalam daftar berdasarkan kunci:**

LRANGE mylist 0 -1

**Menambahkan anggota ke dalam himpunan berdasarkan kunci:**

SADD myset "member1"

SADD myset "member2"

**Mendapatkan semua anggota dalam himpunan berdasarkan kunci:**

SMEMBERS myset

Dengan menggunakan struktur data key-value ini, Redis memungkinkan pengguna untuk menyimpan dan mengambil data dengan cepat dan efisien. Redis juga menyediakan berbagai operasi dan fitur yang kuat untuk memanipulasi dan mengelola nilai-nilai ini, menjadikannya solusi yang populer untuk caching, antrian pesan, dan berbagai skenario penggunaan lainnya.

### Membuat koneksi Redis:

**Membuat koneksi Redis**

import redis

r = redis.Redis(host='localhost', port=6379, db=0)

Pada syntax di atas, kita menggunakan modul redis untuk membuat koneksi dengan Redis. Kita menginisialisasi objek Redis dengan parameter host (alamat server Redis), port (nomor port Redis), dan db (nomor basis data Redis yang akan digunakan).

#### Menyimpan dan Mengambil Nilai:

**Menyimpan nilai menggunakan metode set**

r.set('key', 'value')

**Mengambil nilai menggunakan metode get**

value = r.get('key')

Dalam contoh di atas, kita menggunakan metode set untuk menyimpan nilai dengan menggunakan kunci 'key' dan nilai 'value'. Kemudian, kita menggunakan metode get untuk mengambil nilai yang terkait dengan kunci 'key'.

#### Menghapus Nilai:

**Menghapus nilai menggunakan metode delete**

r.delete('key')

Dalam contoh di atas, kita menggunakan metode delete untuk menghapus nilai yang terkait dengan kunci 'key'.

#### Mengatur Waktu Kadaluwarsa: 

**Menyimpan nilai dengan waktu kadaluwarsa (dalam detik)**

r.setex('key', 60, 'value')

Dalam contoh di atas, kita menggunakan metode setex untuk menyimpan nilai dengan waktu kadaluwarsa. Nilai tersebut akan otomatis dihapus setelah waktu yang ditentukan (dalam detik) telah berlalu.

#### Menambahkan Nilai ke Dalam Set:

**Menambahkan nilai ke dalam set menggunakan metode sadd**

r.sadd('set_key', 'value1', 'value2', 'value3')

Dalam contoh di atas, kita menggunakan metode sadd untuk menambahkan nilai ke dalam set dengan menggunakan kunci 'set_key'.

#### Mendapatkan Nilai dari Set:

**Mendapatkan semua nilai dalam set menggunakan metode smembers**

values = r.smembers('set_key')

Dalam contoh di atas, kita menggunakan metode smembers untuk mendapatkan semua nilai dalam set yang terkait dengan kunci 'set_key'.

Itu adalah beberapa contoh syntax awal yang umum digunakan dalam Redis. Redis menyediakan banyak perintah dan fitur lainnya yang dapat temen-temen eksplorasi lebih lanjut berdasarkan kebutuhan aplikasi kalian.

#### Contoh lain:

**Membuat koneksi Redis**

r = redis.Redis(host='localhost', port=6379, db=0)

**Menyimpan data dalam memori menggunakan Redis**

r.set('user:1:name', 'John Doe')

r.set('user:1:email', 'johndoe@example.com')

**Mendapatkan data dari Redis**

name = r.get('user:1:name')

email = r.get('user:1:email')

print(name.decode()) # Mengubah byte menjadi string

print(email.decode())

#### Menghapus data dari Redis

r.delete('user:1:name')

r.delete('user:1:email')

Pada contoh di atas, kami menggunakan Redis untuk menyimpan data pengguna (nama dan email) dengan menggunakan kunci-kunci yang terstruktur (user:1:name dan user:1:email). Kami menggunakan metode set untuk menyimpan nilai, dan metode get untuk mengambil nilai dari Redis. Metode delete digunakan untuk menghapus data dari Redis.

Tentu saja, ini hanya contoh sederhana dan Redis memiliki berbagai fitur dan perintah lainnya yang dapat digunakan untuk membangun aplikasi yang lebih kompleks dan efisien. Anda dapat merujuk ke dokumentasi Redis untuk mempelajari lebih lanjut tentang sintaksis dan fitur yang disediakan oleh Redis

#### Another ex;

**Contoh lain penggunaan Redis untuk menyimpan dan mengambil data dalam memori:**

#### Membuat koneksi Redis

r = redis.Redis(host='localhost', port=6379, db=0)

**Menambahkan data ke dalam set**

r.sadd('fruits', 'apple')

r.sadd('fruits', 'banana')

r.sadd('fruits', 'orange')

**Mendapatkan semua anggota set**

fruits = r.smembers('fruits')

print(fruits)

**Menambahkan data ke dalam hash**

r.hset('person:1', 'name', 'John Doe')

r.hset('person:1', 'age', 30)

r.hset('person:1', 'city', 'New York')

**Mendapatkan nilai dari hash**

name = r.hget('person:1', 'name')

age = r.hget('person:1', 'age')

city = r.hget('person:1', 'city')

print(name.decode())

print(int(age.decode()))

print(city.decode())

Pada contoh di atas, kita menggunakan Redis untuk menyimpan data dalam bentuk himpunan (set) dan hash. Data buah-buahan disimpan dalam himpunan "fruits" menggunakan metode sadd, dan kemudian kita mendapatkan semua anggota himpunan menggunakan metode smembers.

Selanjutnya, kita menggunakan hash untuk menyimpan data seputar seorang "person:1". Kita menggunakan metode hset untuk menambahkan nilai ke dalam hash, dan metode hget untuk mendapatkan nilai dari hash berdasarkan kunci.

Anda dapat mengeksplorasi lebih banyak fitur dan perintah Redis, seperti sorted set, list, dan operasi lainnya sesuai dengan kebutuhan aplikasi Anda.

# Exercise

1\.Buatlah koneksi Redis:

- Import modul Redis.

- Buat objek Redis dengan koneksi ke server Redis.

2\.Tambahkan data film ke dalam Redis:

- Simpan data film "The Shawshank Redemption" dengan informasi judul, tahun rilis, dan genre menggunakan struktur data hash.

- Simpan data film "The Godfather" dengan informasi yang sama.

3\.Ambil data film dari Redis:

- Dapatkan informasi film "The Shawshank Redemption" dari Redis menggunakan kunci yang sesuai.

- Dapatkan informasi film "The Godfather" dari Redis menggunakan kunci yang sesuai.

4\.Perbarui data film di Redis:

- Perbarui tahun rilis film "The Shawshank Redemption" menjadi tahun baru.

- Perbarui genre film "The Godfather" menjadi "Crime, Drama".

5\.Hapus data film dari Redis:

- Hapus data film "The Shawshank Redemption" dari Redis.

- Hapus data film "The Godfather" dari Redis.

### Keep your head high!!:p

