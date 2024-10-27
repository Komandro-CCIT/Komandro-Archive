# 5. Introduction to QA and Manual Testing

Author: Hudya (@perogeremmer)


## Overview

Quality Assurance (QA) adalah proses sistematis untuk memastikan bahwa suatu produk atau layanan memenuhi standar kualitas yang ditentukan. 

Dalam konteks pengembangan perangkat lunak, QA bertujuan untuk:
- Menemukan dan memperbaiki bug atau kesalahan
- Memastikan produk berfungsi sesuai dengan spesifikasi
- Meningkatkan kepuasan pengguna
- Mengurangi risiko dan biaya yang terkait dengan masalah kualitas

## Manual Testing

Dalam menjalankan tugasnya, QA akan melakukan testing salah satunya dengan metode manual testing. Manual testing adalah metode pengujian perangkat lunak di mana seorang tester secara langsung menjalankan test cases tanpa menggunakan alat otomatis. 

Mengapa disebut manual testing?

- Dilakukan oleh manusia (tester)
- Memungkinkan pengujian yang lebih mendalam dan intuitif
- Cocok untuk pengujian eksploratori dan usability testing
- Memerlukan waktu dan tenaga yang lebih banyak dibandingkan automated testing


Dalam melakukan manual testing, seorang QA akan membuat test cases. Test cases adalah serangkaian langkah, kondisi, dan parameter yang dirancang untuk menguji fungsionalitas tertentu dari sebuah aplikasi. 

## Komponen Test Case

Komponen *test case* meliputi:
- ID test case
- Deskripsi
- Prasyarat
- Langkah-langkah pengujian
- Data input
- Hasil yang diharapkan
- Hasil aktual
- Status (Pass/Fail)


## Jenis Testing

Dalam melakukan pengujian atau testing, ada beberapa jenis, diantaranya:

### Functional Testing 

Functional Testing adalah seperti seorang detektif yang teliti memeriksa setiap fitur aplikasi satu per satu. Bayangkan seorang QA tester sedang membuka aplikasi e-commerce baru. 

QA mulai dengan mencoba login, memastikan bahwa username dan password yang benar membuka pintu ke akun pengguna. Kemudian, QA beralih ke kotak pencarian, mengetik berbagai kata kunci untuk melihat apakah hasil yang muncul sesuai. 

Akhirnya, QA memasukkan beberapa item ke keranjang belanja dan melalui proses checkout, memastikan setiap langkah berjalan mulus seperti yang diharapkan. Tujuannya sederhana: memastikan bahwa setiap tombol, setiap form, dan setiap fitur dalam aplikasi bekerja persis seperti yang dijanjikan kepada pengguna.

### Non-functional Testing

Non-functional Testing di sisi lain, adalah seperti melihat aplikasi melalui berbagai lensa khusus. Pertama, tester kita memakai "kacamata kecepatan", menguji performa aplikasi. 

QA membanjiri situs dengan ratusan pengguna simultan, melihat apakah server bisa menangani beban tanpa melambat atau crash. 

Kemudian, QA mengenakan "topi keamanan", mencoba berbagai trik hacker untuk melihat apakah data pengguna aman dari ancaman. 

Terakhir, QA memakai "sarung tangan pengalaman pengguna", menavigasi situs dengan mata pengguna awam, memastikan bahwa setiap langkah intuitif dan mudah diikuti. Melalui pengujian non-fungsional ini, tester memastikan bahwa aplikasi tidak hanya bekerja, tetapi bekerja dengan baik, aman, dan nyaman digunakan.


### Regression Testing

Regression Testing adalah seperti seorang penjaga gawang yang waspada. Setiap kali tim pengembang melakukan perubahan pada aplikasi, entah itu memperbaiki bug atau menambahkan fitur baru, sang tester kembali ke lapangan. 

Dia mengulangi semua tes yang pernah dilakukan sebelumnya, memastikan bahwa perbaikan di satu area tidak merusak fungsionalitas di area lain. Misalnya, setelah update terbaru pada aplikasi e-commerce kita, tester memeriksa kembali proses login, pencarian, dan checkout. 

Tujuannya adalah memastikan bahwa perubahan baru tidak menimbulkan masalah baru atau membangkitkan kembali bug lama yang sudah diperbaiki.

### Integration Testing

Integration Testing bisa dibayangkan seperti seorang konduktor orkestra. Dalam pengujian ini, tester memastikan bahwa semua instrumen (atau dalam hal ini, komponen aplikasi) dapat bermain harmonis bersama. Misalnya, ketika pengguna menambahkan item ke keranjang belanja (frontend), informasi ini harus tersimpan dengan benar di database (backend). 

Tester memeriksa apakah data mengalir lancar antara berbagai modul aplikasi, memastikan bahwa frontend dan backend berkomunikasi tanpa hambatan, dan bahwa integrasi dengan layanan pihak ketiga (seperti gateway pembayaran) berfungsi sempurna.

### System Testing

System Testing adalah seperti melakukan uji terbang sebelum pesawat benar-benar lepas landas. Di sini, tester melihat aplikasi sebagai satu kesatuan utuh, bukan sebagai komponen-komponen terpisah. Mereka menguji aplikasi dalam lingkungan yang mirip dengan dunia nyata, memeriksa semua aspek dari perspektif pengguna akhir. 

Ini termasuk menguji skenario end-to-end, seperti melakukan pembelian lengkap di aplikasi e-commerce dari browsing produk hingga menerima konfirmasi pesanan. 

Tujuannya adalah memastikan bahwa seluruh sistem berfungsi sebagaimana mestinya dan memenuhi semua persyaratan yang telah ditentukan.

### User Acceptance Testing (UAT)

User Acceptance Testing (UAT) adalah babak final, seperti preview film sebelum peluncuran resmi. Di sini, bukan lagi tim QA yang menguji, melainkan perwakilan dari pengguna akhir atau klien. 

Bayangkan sekelompok pelanggan potensial diundang untuk mencoba aplikasi e-commerce baru. Mereka akan menggunakan aplikasi seperti yang akan mereka lakukan dalam kehidupan sehari-hari - mencari produk, membandingkan harga, melakukan pembelian. 

Feedback mereka sangat berharga karena mereka melihat aplikasi dari sudut pandang pengguna nyata. Mungkin mereka menemukan bahwa proses checkout terlalu rumit, atau desain kurang intuitif. 

UAT adalah kesempatan terakhir untuk memastikan bahwa aplikasi tidak hanya memenuhi spesifikasi teknis, tetapi juga benar-benar memenuhi kebutuhan dan harapan pengguna sebelum diluncurkan ke pasar.

## Teknik Pengujian

Dalam melakukan testing ada tiga teknik utama yang bisa dilakukan, diantaranya adalah sebagai berikut.

### Black Box Testing

Black Box Testing adalah metode pengujian perangkat lunak yang memeriksa fungsionalitas aplikasi tanpa melihat struktur kode internal. Tester hanya fokus pada input dan output.

### White Box Testing

White Box Testing, juga dikenal sebagai pengujian struktural atau pengujian kotak kaca, melibatkan pengujian struktur internal dan kode aplikasi.

### Gray Box Testing

Gray Box Testing adalah pendekatan hybrid yang menggabungkan elemen dari Black Box dan White Box Testing. Tester memiliki pengetahuan terbatas tentang struktur internal sistem.

### Perbedaan Teknik Pengujian

Masih gak paham ya? Mari kita simak cerita berikut.

Bayangkan ada sebuah kotak ajaib yang bisa mengubah buah-buahan menjadi jus. Tiga orang tester datang untuk memeriksa kotak ini, masing-masing dengan pendekatan yang berbeda.

#### Black Box Testing

Ana, tester pertama, adalah seorang Black Box Tester. Dia tidak peduli bagaimana mesin di dalam kotak bekerja. Ana hanya fokus pada apa yang bisa dilakukan kotak itu. Dia memasukkan berbagai jenis buah - apel, jeruk, anggur - dan memeriksa jus yang dihasilkan. Ana memastikan bahwa ketika dia memasukkan apel, yang keluar adalah jus apel, bukan jus jeruk. Dia juga mencoba memasukkan benda yang bukan buah, seperti batu, untuk melihat bagaimana kotak bereaksi. Ana tidak pernah membuka kotak atau mencoba memahami mekanisme di dalamnya. Baginya, yang penting adalah input yang diberikan menghasilkan output yang benar dan sesuai harapan.

#### White Box Testing

Budi, tester kedua, adalah seorang White Box Tester. Berbeda dengan Ana, Budi sangat tertarik dengan cara kerja internal kotak. Dia membuka kotak, mempelajari setiap gear, pipa, dan komponen di dalamnya. Budi memeriksa jalur yang dilalui buah, bagaimana buah dipotong, bagaimana jusnya diekstrak, dan bagaimana sistem membersihkan diri setelah setiap penggunaan. Dia bahkan mempelajari kode program yang mengontrol mesin. Dengan pengetahuan ini, Budi dapat merancang tes yang sangat spesifik, mencoba berbagai skenario yang mungkin tidak terpikirkan oleh seseorang yang hanya melihat dari luar.

#### Gray Box Testing

Citra, tester ketiga, mengambil pendekatan Gray Box Testing. Dia memiliki pengetahuan umum tentang cara kerja kotak tanpa mengetahui setiap detail. Citra tahu bahwa ada proses pemotongan, penggilingan, dan ekstraksi, tapi dia tidak mempelajari setiap komponen secara mendalam. Dengan pengetahuan ini, Citra dapat merancang tes yang lebih terarah dibanding Ana, tapi tidak serumit Budi. Misalnya, dia tahu bahwa kotak memiliki sistem pembersihan otomatis, jadi dia menguji bagaimana kotak menangani perubahan dari buah manis ke buah asam, memastikan tidak ada kontaminasi rasa.

#### Perbedaan Utama

- Ana (Black Box) hanya fokus pada input dan output, tanpa pengetahuan tentang cara kerja internal.
- Budi (White Box) memiliki pengetahuan mendalam tentang struktur internal dan kode, memungkinkan pengujian yang sangat mendetail.
- Citra (Gray Box) memiliki pemahaman umum tentang sistem internal, yang memungkinkan pengujian yang lebih terarah daripada Black Box, tapi tidak sedetail White Box.

Setiap pendekatan memiliki kelebihannya sendiri. Black Box Testing bagus untuk meniru pengalaman pengguna akhir, White Box Testing sempurna untuk menemukan bug tersembunyi dan mengoptimalkan kinerja internal, sedangkan Gray Box Testing menawarkan keseimbangan antara keduanya, memungkinkan pengujian yang efisien dengan pengetahuan terbatas tentang sistem internal.

## Tools untuk QA

Dalam menjalankan tugasnya, tentu QA memerlukan tools dalam pekerjaannya. Terdapat dua tools yang bisa digunakan yaitu Bug Tracking Tools dan Automation Tools.

### Bug Tracking Tools 

Bug Tracking Tools adalah perangkat lunak yang digunakan untuk melacak, mengelola, dan melaporkan bug atau masalah dalam pengembangan perangkat lunak.

Contoh: Trello, Google Sheet, Jira, Clickup


### Automation Tools 

Automation Tools adalah perangkat lunak yang memungkinkan otomatisasi pengujian, mengurangi kebutuhan akan pengujian manual yang berulang. 

Contoh: Selenium, Appium, Playwright