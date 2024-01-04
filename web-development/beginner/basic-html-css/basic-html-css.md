# Paduan Dasar Untuk HTML dan CSS

**Document writer:  Hastho Rahtomo**

**Markdown by: Muhammad Fauzan Arrafi**

**17 October 2023**

# **Chapter 1: Pengenalan**

Pernah kah kamu membuka website pada gadget mu? Kamu pasti pernah mengakses website hiburan seperti Spotify dan Youtube, jejaring sosial seperti Twitter dan Instagram maupun website untuk belajar seperti Ruang Guru dan Brainly. Mereka dibuat menggunakan bahasa pemograman ***HTML***, namun apa itu HTML?

## **HTML**

![](https://lh3.googleusercontent.com/pw/ADCreHeqKHqBNHEly80exzyISunSN13tomYfmRSc_f50RaZ4zRHu49EXR651fCPV3C7_3lNoxr1cImjFnBLXypjoFL8zl6zRlb3-hlxBzW16yDHIpcsgIFKW0Xf1iqkftigHbF-Tl4wih5trXv9kw6fBc4s=w586-h199-s-no)

HTML singkatan dari HyperText Markup Language, yang dalam bahasa Indonesia dapat diartikan sebagai \"Bahasa Markup Hiperteks.\" HTML adalah bahasa pemrograman yang digunakan untuk membuat halaman web dan struktur dasar dari konten di dalamnya. Ini adalah komponen kunci dari web, karena digunakan untuk mengatur teks, gambar, tautan, media, dan elemen-elemen lainnya dalam sebuah halaman web.

HTML bekerja dengan cara menandai atau \"markup\" berbagai elemen pada halaman web dengan menggunakan tag-tag khusus yang ditempatkan di dalam dokumen HTML. Tag-tag ini memberi petunjuk kepada browser web tentang cara menampilkan konten pada halaman.

Namun, HTML Tidak dapat bekerja sendiri. HTML membutuhkan bantuan dari bahasa lain seperti CSS (Cascading Style Sheet) dan JS (JavaScript) yang memiliki berbagai fungsi untuk membantu HTML, CSS berfungsi untuk "menghias" website yang tersedia dan JS untuk mengatur logic dari website yang telah dibuat. Kali ini kita akan belajar bagaimana cara menggunakan HTML dan CSS untuk membuat sebuah website statis.

## **CSS**

CSS adalah singkatan dari Cascading Style Sheets, yang dalam bahasa Indonesia dapat diterjemahkan sebagai \"Lembar Gaya Berkaskelana.\" CSS adalah bahasa pemrograman yang digunakan untuk mengontrol tampilan dan format dari elemen-elemen yang ditandai dalam sebuah dokumen HTML, seperti teks, gambar, tautan, dan elemen-elemen lainnya dalam halaman web.

Kita akan menggunakan ***Text Editor*** untuk membantu kita dalam menggunakan bahasa pemograman HTML dan CSS. Terdapat banyak text editor yang dapat kamu gunakan, seperti Atom, Notepad++ dan Visual Studio Code tetapi untuk kali ini kita akan menggunakan Visual Studio Code. Kamu dapat mengakses website Visual Studio Code lewat link berikut,
<https://code.visualstudio.com/>

## **Visual Studio Code**

Visual Studio Code (biasanya disingkat sebagai VS Code) adalah sebuah text editor kode sumber terbuka (open-source) yang dikembangkan oleh Microsoft. VS Code dirancang khusus untuk pengembangan perangkat lunak.

Setelah kamu mendownload Visual Studio Code, ayo kita mulai.

# **Chapter 2: Base**

Hal pertama yang harus kamu lakukan untuk membuat website adalah membuat file untuk website mu terlebih dahulu serta menyiapkan file file yang diperlukan.

## **Membuat Folder dan File**

Step 1: Buka aplikasi visual studio mu lalu klik "file" pada bagian kiri atas.

![](https://lh3.googleusercontent.com/pw/ADCreHeVW2NMENLiaoqYbUId_LJHApmMzWNbw0F0urmkjlzjC3Ns2dex5sZ-i3hvVRu0GToOE6TdndrkOaedqAT3LIEAKSeUZHxmawdePVl79XnA05lB2leTWm_XgqV_jqKbJUTQ2nyk38QvY0LSpHV8FOA=w1215-h683-s-no)

Step 2: Klik "open folder"

![](https://lh3.googleusercontent.com/pw/ADCreHeYCuk1phqCBRWI_fhOYSA2s5t5FAgfnjAjAkg37b7WsNwETUHv9zKdgyRK6YD20VMCJ6YoP5RHnmYrXFXJyb3lAKQD-Rv--b0Dh2sLXqFIwFkrdTeWTC3-AgTmq50asc0c4tuIyBR_my2JOB5k5Y8=w1215-h683-s-no)

Step 3: Pilih letak dimana folder mu ingin dibuat, lalu buat folder baru dengan meng-klik kanan pada mouse lalu memilih new -\> folder kemudian beri nama folder mu.

![](https://lh3.googleusercontent.com/pw/ADCreHeu_9qF33C84dWxAkPGwX6JW7X7gwtaL8ket8Sc0vP6wQ2aVldXxoPe4u6lk84PFC_7WYA3EXwrAhydyb3EQVb1FVWH0pAJRpNsri7rMkN0mTEr0kT4wSTAJ60J724POjYmm85c1E4ONvSTZOfM1oQ=w1215-h683-s-no)

Step 4: klik kiri satu kali pada Folder yang sudah dibuat kemudian klik "select folder". Visual studio akan membuka folder yang telah kamu pilih, isinya masih kosong namun jangan khawatir. Selanjutnya kita akan mengisi folder tersebut.

![](https://lh3.googleusercontent.com/pw/ADCreHeGmrLtxH2OmBFYY--nfLN_Ior374_0g7NN2IwilIIESe-EoxgYVLf6Hh3ljsOaWzvGUFubfMMg6mbDdBdWtXywYtBsm5FNI3_WGFJXKVIqYTDTPmf2E3NzUi2JzzkkZvXdPZX5n_h5um65Duojws4=w1215-h683-s-no)

Step 5: Klik kanan pada bagian titik merah kemudian pilih "new file"

![](https://lh3.googleusercontent.com/pw/ADCreHfGdnMdg-pTpal0fx0qEUQJofDp2sVVCJcI8GRkXKJOqNvdTWNOdU6QiHL6FwoojZGk16ZGr7Kn0XwmmmZV4gNNvbDEGjNTlkWM7iki93QDx5eeGxPENpNpMRhL33RQiVvcdPwbGb7vJPvVY8UYf3U=w1215-h683-s-no)

Step 6: Beri nama folder mu "index.html" seperti berikut, ulangi step 5 namun berikan nama folder nya "style.css".

![](https://lh3.googleusercontent.com/pw/ADCreHdUuYdK9MoVqV49W-k2495PDaB0YaLPSKE0YFoh3-YkDc5LtQzFORpobiE6USOtegVoHIS5r6bW6Po8z6eXKkB70-UX2Dm59rASria2IA2QPnMtYVJZb4OltYb8JIMpqUHcbx9BgjXW5k1lXHi6rco=w189-h63-s-no)

Step 7: hasil akhirnya akan seperti ini, selamat kamu sudah membuat file HTML dan CSS.

![](https://lh3.googleusercontent.com/pw/ADCreHdhEU4KsjoTSRBmD4z6mKghNzQx_6j8gOUhOaE7DF5zO6SSUYqis9kjrgfnXoeqlcHHr-MGtBM0TG2CvU_GE7saqyckSRZkTpRfzI4MuTQQ9Mx1mPmnbCoc5LNS7r54t014fg-aS8sewFJ4yYGkcb8=w190-h63-s-no)

## **Membuat dasar pada HTML**

Langkah selanjutnya setelah kamu membuat folder dan file projek mu adalah mengisi file projek mu dengan kode-kode. Namun kamu harus mempersiapkan file tersebut agar kode yang kamu masukan dapat dikenal oleh file mu. Kamu dapat mencoba hal berikut.

Buka file index.html -\> ketik "doc" tanpa petik dua (") kemudian enter. Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHc5C5gvUHMxDrANbOCoU1ltbBps2XaLVB-J7Ox61WbLZHxAA7gvQrBBZyyB4wp8TNNVMHaRdFJR00DGcKGY9mNqML6ILwo_qPimvxqVG7UjD2PFxS4AJaso4_0a01lIqLlQLV5dnKr02LRU5blxTQc=w637-h219-s-no?authuser=1)

File html mu sudah siap dimasukan kode kode, kamu dapat mencobanya dengan menulis "hello world" pada bagian dalam \<body\> kemudian save seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHdgAzmOfJ2kOtD21SmorY_fsZC3z3rdSXotCSfGwNp1Os6Ndd1NY3aeMja-25LuihzxjSWEBl2MWjfYgxNLaFO7qr2FyIvlWQSw-idi0NT6UKG5U0W-3P72ueC0JF3ci3o2IWlGPeNAM-HelOmSGGM=w589-h198-s-no?authuser=4)

Selanjutnya kamu dapat membuka file yang telah kamu buat menggunakan browser. Ini adalah hasil nya.

![](https://lh3.googleusercontent.com/pw/ADCreHf5aJHLMU40HY-XOqAqCOlAQaufPf4uXyDO5D-OcxsUOreq2uD8S0DpcvhwtscRa7gVu580pIFh-9gxqOPglozB3HTncWm4HHc4E1FdsmuGjuGd6lwTjicj6w4gSAZC3fedg6WwT1nQdrpF6VvHjG4=w747-h491-s-no?authuser=4)

Selamat, ini adalah website pertama mu. Pada chapter selanjutnya kita akan mulai mengisi file HTML yang telah kamu buat.

# **Chapter 3: Isi Base HTML**

Kamu telah membuat folder untuk menampung projek mu, kamu juga telah mengisinya dengan index.html dan style.css. Selanjutnya kita akan mulai mengisi file index.html mu dengan kode kode berikut.

## **Head \<head\> dan Body \<body\>**

![](https://lh3.googleusercontent.com/pw/ADCreHf32f6_VByNlVa05B-_RPHrgLLO62G0IiyOhVHpLl13ZRpN7gzsLQrsmvzY6WpX4MNWXAPgAuh3Yke1M3H-a3B0HW9o4vsaCKQq5zfoqghJ-saDyIewjdghlCde9MkXXl1dPEnO2aradpLbwKeCVnQ=w290-h391-s-no?authuser=4)

Coba bayangkan seorang manusia normal, ia memiliki kepala dan badan. Begitu pula dengan kode HTML. Head \<head\> berfungsi untuk mengatur body, head tidak akan ditampilkan pada output website. Sebaliknya, body <body\> merupakan tempat dari elemen elemen yang akan ditampilkan pada output. Tanda dari akhir bagian heda dan body dapat dilihat dengan adanya kode \</head\> dan \</body\> seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHfKlC0ndRwABARrNp3Ngg6n7Z_wRaT9r13HxfzJTTIMYaSuW0z_17MYSn7vxKXC7pYkJu4wsYmX9_ct94MPPtXpx6hkFGIFKEsV2kQDq_UrwY9unKwNA8wrraxArfgkuePsXtb3eD7_HP5ZMtJmfQM=w669-h288-s-no?authuser=4)

Bagian berwarna ungu adalah daerah dari \<head\> dan bagian berwarnkuning adalah daerah \<body\>, akhir dari setiap daerah dapat dikenali dengan penggunaan tanda tutup \</kode yang sama dengan pembuka\>. Maka dapat disimpulkan rumus dari kode yang digunakan adalah seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHeY-lGmWT1iQTWa964meaCmRh4rC3tygvRY8TKiVfujQdJrjhATlc_8ccg6GYicaK6Up4j_AbsjxVKwTsjadwA6seRimDYuJfnD79WRPKVH3As_cBMdYEQqnoYg0T3t6aN4_YSvmv4OAcdMshQ7SF4=w151-h73-s-no?authuser=4)

Kamu dapat memperhatikan contoh berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHdGB2qP2e5lI7LSJl1URuIngOv_pUvvPDy_NnO0pkeMzMx9X413_9Nzs11YgHlb9jpxgyC-Eu5F00VK98V4VxT-JrR7tbYBsdsDReiOJI885iZPg0KKlT-7EfPGMjhu3-nAAX6suK51diZku0--Z6w=w164-h70-s-no?authuser=4)

kode \<kode\> memiliki isi yaitu "aku ganteng" karena "aku ganteng" berada dalam daerah \<kode\> otomatis "aku ganteng" akan menjadi value dari \<kode\>

## **Header \<h\>**

Tag HTML \<h\> yang Anda sebutkan tidak merupakan tag standar dalam HTML. Biasanya, tag untuk judul (heading) dalam HTML adalah \<h1\>, \<h2\>, \<h3\>, \<h4\>, \<h5\>, atau \<h6\>, di mana angka yang mengikuti \"h\" menunjukkan tingkat kepentingan atau ukuran teks yang berbeda. Kamu dapat mencobanya dengan memasukan kode berikut kedalam \<body\>.

```html
<body>

<h1>Ini adalah h1</h1>

<h2> Ini adalah h2</h2>

<h3> Ini adalah h3 </h3>

<h4> Ini adalah h4</h4>

<h5> Ini adalah h5 </h5>

<h6> Ini adalah h6 </h6>

</body>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHflf9_I829arSl-punGGB6G5cfxBD4bUEjtXE-kJg3eJQTuIWLFTnh863RRQQwGKJKhArfe1G15XNqN-iiR43xAdF1fP9hEM5tU8YTaBjimbW9UqwQhJy3sia7if6AXhqIEW7ipTtpHmmSABfnQO-Y=w679-h355-s-no?authuser=4)

## **Paragraf \<p\>**

Adalah isi dari Header, paragraf dipakai untuk memuat banyak text sekaligus karena ukurannya lebih kecil dari header. Kamu dapat mencoba kode berikut.

```html
<body>

<h1>Ini adalah h1</h1>

<p> ini adalah paragraf. ini adalah paragraf.ini adalah paragraf. </p>

</body>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHfYOkN2W_CMJAJXIvVvcmnyZtJIzyIYU_rq5TRom5EK9MD3XaUf6mNygK_xSSPa5Dwv7c2Qko9FMeuWYPO-Oo0MfKfNieXnvb-VOU790UL7-VwOc34aDjP6d12kfK-qLWqKPzCONM11V3GhOaXMZ8E=w404-h107-s-no?authuser=4)

## **Break \<br\>**

Break dipakai untuk membuat baris baru atau jeda yang dapat dipakai didalam sebuah elemen maupun sebagai pembatas antar elemen. Break tidak memiliki kode penutup. Untuk penjelasan lebih jelas, perhatikan kode berikut.

```html
<body>

<h1>Ini adalah h1</h1>

<p> ini adalah paragraf. <br> ini adalah paragraf. <br> ini adalah
paragraf. </p>

</body>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHdBh4Iw4EhyhgVdHRlXkO58V32GJyMyyqeXQZ88oFugUEs0BZTTx1Q2ugw51N1tRkHIl26pZY_lIng9txjKMTrBs_keb_UcE451wgmE7eDKJ8D9Mhqy8Ey3DyfG6TOHExcWBUEePioWRPEEFmGIMWM=w197-h127-s-no?authuser=4)

## **Bold \<b\>, Underline \<u\> dan Italic \<i\>**

Ketiga kode tersebut memiliki kesamaan, yaitu memberikan efek pada text. Bold menjadikan text tersebut tebal, underline memberikan garis bawah dan italic memberikan efek miring pada text. Perhatikan kode berikut.

```html
<body>

<h1>Ini adalah h1</h1>

<p> <b>ini adalah bold.</b>
<br> <u>ini adalah underline.</u>
<br> <i>ini adalah italic.</i></p>

</body>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHeJoWd7yLhy597CDYqypWxUWfVy1LBZGKzDBbyYSDuV_EZSZQETzNzW8z7acK9RHKUtRF_LcjewmdipoRZK_6Hm7Z0VzL61uLx0zlVLu9LetIuEd0YgCzrCKdIoHesMobtcGmiy96ysLR2nGVeEHa8=w200-h129-s-no?authuser=4)

## **List**

Terdapat 2 tipe list yang dapat kamu gunakan, yaitu:

**ordered list \<ol\>**, adalah sebuah list dimana data yang kamu masukan akan terurut menggunakan angka/huruf.

```html
<ol>

<li>Item pertama</li>

<li>Item kedua</li>

<li>Item ketiga</li>

</ol>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHe0uhKfYygQuBqeO2BgwWnUOK3dHqgtlZLNzGyoeRMZCPc2gqmUtKmJP526CAKHa1nnfttG8HkKySo8lEHdML5mz1pKYlbs4xRgOUv_PPp565rLK-3_3rIKe8h6eLuqlYiVm3-2xxC_rRhhrsVBJms=w143-h89-s-no?authuser=4)

**Unordered list \<ul\>**, adalah sebuah list yang tidak mengurutkan data yang dimasukan dan hanya menggunakan dot/bullet sebagai indikator.

```html
<ul>

<li>Item A\</li>

<li>Item B\</li>

<li>Item C\</li>

</ul>
```

Hasilnya akan menjadi seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHe_L08KQ5NU5Mj5VtJvC2v3j9nV4boQFAEJqw_0oIfuu7KSoV0tk1fjO1XgJzgaLOEI--OC9_tT6ka4-htjtjlqEX1CJtloHRb8x2m3dJdVZSirl_7T9PFiWaI_sDJi4j_ALOWU792EzBkJEoH97HE=w103-h87-s-no?authuser=4)

## **Div \<div\>**

Berfungsi sebagai wadah untuk menyatukan elemen elemen yang ada didalamnya menjadi satu kelompok, perlu diingat bahwa div tidak memiliki pengaruh visual maupun efek secara langsung, div sendiri tidak memiliki warna dan menyesuaikan ukurannya dengan elemen yang ada didalamnya.

```html
<div>

<h1>Judul Halaman </h1>

<p>Ini adalah paragraf pertama. </p>

<p>Ini adalah paragraf kedua. </p>

</div>
```

## **Image \<img\>**

Memiliki fungsi untuk memasukan gambar pada html. Image memiliki format kode sebagai berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHd6G0ab82AQXuTMGAk1rpwyUFzWj0avfl1KwWrOTuI2isvsENaszEiK-76oDSQalrtb-CizKHYvwkx4cCkHyA_R0wHLLaca2J6kaWz_zq30Rm1te7zAjIAO-cKT0ZGSincGPxvBub3zBV4f8nPpyrE=w551-h36-s-no?authuser=4)

Atau kamu dapat mencontoh kode berikut ini

```html
<img src="https://upload.wikimedia.org/wikipedia/en/e/e7/Steve\_%28Minecraft%29.png" alt="steve">
```

Hasilnya akan menjadi seperti berikut.

![](https://upload.wikimedia.org/wikipedia/en/e/e7/Steve\_%28Minecraft%29.png)
![](https://lh3.googleusercontent.com/pw/ADCreHcHlan-ibXDwCU8ZeEZQf9_Elbs7KPIK0unCsSNyO3MwC5uDaiU55Zft0dJMZWBJVLzE2S0LiI4385b3i5nlmHyF2uTHwbedKF33KhnPU6pNUDt4GXYj4NRuffyHymqxvhRkmnIBmAUNJAETrtPLOM=w678-h416-s-no?authuser=4)

## **Button \<button\>**

Digunakan untuk membuat tombol dalam halaman web. Tombol ini biasanya berfungsi untuk memicu tindakan atau peristiwa tertentu saat diklik oleh pengguna. Tombol ini dapat digunakan untuk mengirim formulir, memulai skrip JavaScript, atau menjalankan berbagai tindakan sesuai dengan kebutuhan anda, Perhatikan kode berikut dan perhatikan outputnya.

```html
<body>

<button>Klik Saya</button>

</body>
```

## **Anchor \<a\>**

Digunakan untuk membuat tautan ke halaman web lain, berkas, atau alamat URL lainnya. Ini memungkinkan pengguna untuk mengeklik tautan dan beralih ke lokasi yang dituju. Elemen \<a\> sering digunakan untuk membuat tautan teks atau gambar. Untuk mencobanya, ikuti langkah langkah berikut:

Step 1: buat file "contohAnchor.html" pada folder projek mu

Step 2: masukan kode \<a href=\"contohAnchor.html\"\> Ini adalah tautan
ke contohAnchor \</a\> pada index.html

Step 3: perhatikan output nya.

![](https://lh3.googleusercontent.com/pw/ADCreHfoFZ71qVNTYRwprv1e0aXPMNNcHxZD9N1PFi8YJkRycFMirPMkIrMCpO6BBAKSEdQyahbWlyI9QXj-ZFpPtLJQOzCEwn87y3yiv90A4VTQ8NSrBQWCb0YKVr_b3PHg_blrNMvQXueS_N2-dAVPDtc=w669-h97-s-no?authuser=4)

Kamu akan mengakses file contohAnchor.html apabila mengklik link tersebut. Anchor sangat membantu apabila website mu terdiri dari berbagai file HTML yang harus dihubungkan.

# **Chapter 4: Styling**

Ini adalah chapter terakhir untuk membuat website statis, pada chapter ini kamu akan belajar mengenai CSS untuk menghias file HTML mu. Terdapat banyak kode yang menghasilkan beragam efek yang dapat kamu gunakan. Mari kita mulai!

## **Menghubungkan HTML dengan CSS**

Langkah pertama yang harus kita lakukan untuk dapat menggunakan HTML dengan CSS adalah dengan menghubungkan keduanya menggunakan kode berikut. Terdapat dua cara untuk menggunakan CSS untuk file HTML mu, inline dan eksternal CSS.

### **Eksternal CSS**

Eksternal CSS menggunakan file terpisah untuk men-style file HTML mu.

![](https://lh3.googleusercontent.com/pw/ADCreHfuMjkvurntBdGi8GIFYJL2EYmAzMn6dUgjaSylWdV1NGmfGqmhAk9NwPf1Zqq2IeLKbTl8N69qDPjWmFwfvBVwgQMXtBgbIdLBy4_AQQwQF5Fbm4kUmLxVFJjD60JUPXxC84cUaCXeFX61wq8LAQY=w179-h94-s-no?authuser=4)

Kamu dapat memperhatikan kode dibawah ini.

``<link rel="stylesheet" type="text" href="style.css">``

Kamu dapat mengcopy kode tersebut dan menaruhnya didalam \<head\>, seperti berikut:

![](https://lh3.googleusercontent.com/pw/ADCreHevnDjcItzgI3fqiflg45gBBXzDqs87X6xF2M0LJKjnUW2vHXfSdreXivwdWW-baDFKj7nU_txwASU0lti3kxhOr9tOfFMqWxouIuIS9CQtJUFDWapnvqcJPk67gaWwieIzqS66730xyfcRLAZRQHM=w583-h160-s-no?authuser=4)

Sekarang, kamu telah menghubungkan file HTML mu dengan CSS.

### **Internal CSS**

Berbeda dengan styling secara eksternal, internla css mengarah kepada tag \<style\> yang bisa kalian tulis di didalam \<head\> tag, berikut adalah contohd dari penggunaan internal css

```html
<head>
<title>Tutorial web satis part 1</title>
<style>
.gambar {
border-radius: 10px;
}
</style>
</head>
```

### **Inline CSS**

Berbeda dari eksternal CSS, inline css tidak membutuhkan file eksternal untuk digunakan. Kita dapat menggunakan "style" seperti contoh berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHehIx2jjxtsAG5TafXCW9qlJtOm1gmkRktpYNnkST5WiXbVpMjIlZML8elBkHX8DbCPMgC3yPStowtggeWSOge1xGG80beUo349LluzxyhSWnHuDGQTmVNE5vqoR_7DSa3qQYDlyNBNW1UUIRjyWnk=w367-h62-s-no?authuser=4)

## **Font Family**

Font-family adalah kode CSS pertama yang akan kamu pelajari, font-family digunakan untuk mengubah gaya font/model font untuk web HTML mu. Terdapat banyak tipe font yang dapat kamu pakai, seperti "arial", "sans-serif", "serif", "helvetica", dll. Kamu juga dapat menggunakan font dari internet. Perhatikan kode berikut.

```html
<body>

<h2>Komandro</h2>

<h2 style="font-family: Helvetica;">Komandro</h2>

</body>
```

![](https://lh3.googleusercontent.com/pw/ADCreHeW7yudEj56n8TVqrRVi3RiI8w-pUC2JIRqHOi3Z4tQ6S8UFb-Qt_wj2ddYkuBxuF1mi7MGesmDQRFfnuF2rdH1Y12gnlxXKjbCwuUue40KTO_66FZg_BtMDEC-c-BP0l8AJty298XchivvzRPxPqk=w142-h90-s-no?authuser=4)

Hasilnya adalah seperti berikut.

Dapat kamu lihat perbedaan dari tipe font pertama dan kedua, teks pertama adalah teks yang tidak menggunakan "font-family" dan yang kedua menggunakannya, font yang dipilih adalah "Helvetica".

## **Font Size**

Digunakan untuk mengatur ukuran dari text, kamu dapat mencoba kode
berikut.

```html
<body>

<h2>Komandro</h2>

<h2 style="font-size: 40px;">Komandro</h2>

</body>
```

Hasilnya adalah seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHe0uNy_glKvtW6UyGHRTIpqnOkHav8lNWQwhVKDDen8ucZUkFu9gAvsRkSVPvPSvidU8Zxgra0olgDgft4BxhJ4zaJL36LLjM9iuf1yjJXPw5RprmyWM5JgW9bxEehLCGjDClTblcknoljuaczBlMA=w238-h143-s-no?authuser=4)

## **Font Weight**

Digunakan untuk mengatur Ketebalan dari text, kamu dapat memilih ketebalan text dari light hingga bold, kamu juga dapat memasukan satuan ukuran.

```html
<body>

<h2>Komandro</h2>

<h2 style="font-weight: 400;">Komandro</h2>

</body>
```

Hasilnya adalah seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHcABSe8rGbwmDGbj_EpYrHcyiRq_LQHhfUgPS6N7zTYR-Cg2fjIWMPw67ZUzOD0piHtheH-mm0e63ZY1gPHjX58D_bySDVjuEAiBptm6hD_gwk3DNjMD-G-J42ag7XhKxfx-LmkdJykVx4vaB4qmH4=w131-h78-s-no?authuser=4)

## **Text-align**

Digunakan untuk mengatur posisi dari text, kamu dapat mencoba kode berikut.

```html
<h2>Komandro</h2>

<h2 style="text-align: center;">Komandro</h2>

<h2 style="text-align: right;">Komandro</h2>
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHdDy4JaquhIzU8L7QBMxyObkt0cEZjzc7jw1SEegyy3B_ly7a9cc5yrDvBbblqCRutWGZ7gZt18656WpWk8jqGODkJY5H-DxVzfils-2oFJmWreWzuOkoqSutoeuTvFQpFHOXZbNLgnzbGdg4-TLFE=w1366-h178-s-no?authuser=4)

## **Color**

Digunakan untuk mengubah warna dari font mu.

```html
<body>

<h2>Komandro</h2>

<h2 style="color: green;">Komandro</h2>

</body>
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHfD90_x_d2ftkHKpGlcEncyECwMdxqrmSAfu-c93PFvTNzPad1ICdaKOrMtWnB3TSfd0j11BDJYr9ZFDUr_7jCbipHxuNAEhJ-eUmon0uKLJfLJY8grgDLOL10VHwsBfI8doX9FVh-L4SEp8k61moc=w127-h74-s-no?authuser=4)

## **Background-color**

Digunakan untuk mengubah warna latar belakang dari elemen.

```html
<body>

<h2 style="background-color: green;">Komandro</h2>

</body>
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHcNqQ0_oF9KbWZv1bW6MfSjEJiVeu_HaAzd8NGjirsEoptfka-21M4HGmNW5iWl0WxZJEj271GiFQ85jrJ3eITzzcHIn-27nq697gHyoKZ0g4R19FmwkuARjR24iZt4JmSCleWI6ylIkU3NV-jDvtA=w231-h45-s-no?authuser=4)

## **Background-image**

Digunakan untuk menjadikan gambar yang kita inginkan menjadi background untuk elemen yang kita inginkan. Perhatikan kode berikut dan lihat hasilnya.

```html
<h2 style="background-image:
url(https://cdn.oneesports.gg/cdn-data/2022/01/GenshinImpact_Zhongli_drinking_tea.jpg);">

komandro<br>

komandro<br>

komandro<br>

komandro<br>

</h2>
```

## **Border**

Digunakan untuk membuat batas border pada ujung element, banyak tipe border yang dapat kamu gunakan, berikut adalah beberapa contoh border yang dapat kamu gunakan dan cara menggunakannya.

  **border**
  
  ``<h2 style="border: 1px solid black;"> Komandro</h2>``
  
  ![enter image description here](https://lh3.googleusercontent.com/pw/ADCreHfzUsWgiRPc1ZPLBlS9YLmRvVv7SjT-FTfAQ-YXAWmsVfBNNBTtFLqw_Zxu0W3wjeve7juiMX51x35jHr_nYHN79ho2FxrbonXmjrgxOyN3gxgZObIhQ6lQcF7rqS7ULAT8dnMDThQZOKebZ31ni_0=w154-h37-s-no?authuser=4)

  **dash**
  
  `` <h2 style="border: 2px dashed black;"> Komandro</h2> ``
  
  ![enter image description here](https://lh3.googleusercontent.com/pw/ADCreHfWdT4oXDCxwIQ6v7nzXBIvfpYKy7uSm2uQygKKjuv__OrOjYAjP4Z1lcwbcGuMKilY8404UYAShDvlkho-5zK8iH-OV4p-N8HHNNEKbJpFNV4noGUvL7UAm8ZNHFn_rULM0tQENUshoDBSqVbJ9lU=w141-h44-s-no?authuser=4)
  
  **dotted**
  
  ``<h2 style="border: 2px dotted black;"> Komandro</h2>``  
  
![enter image description here](https://lh3.googleusercontent.com/pw/ADCreHf8FUtxcHermSEQ4PZ8RokWztdrgkEklOqJAWxNlOo92oQuw-niKGrPToF61QX3okVLfAoA8wGgsbeYx-6o9TpohZmEbdIo6cq_rdbo-AczS-EtFpAHkSllsiRN6SnST1jLbPTdEnZc6y0T64Q6qe8=w149-h39-s-no?authuser=4)

**double**

 ``\<h2 style=\"border: 3px double black;\"\> Komandro\</h2\>``

![enter image description here](https://lh3.googleusercontent.com/pw/ADCreHeE41AYjNbausPTX5t3IPrYE4pP2lWH1Y9VEN4gdl8Nmz8CxySo7gc_UiuFZdgQ1Gr36fSPoF2zxIKIsSp3qm4vuymYJCu2ewBXocVs5RWJZq-WO0egCP6zKuGA-ONNuwwdbBxC3WnY09N1N3gcYI8=w160-h41-s-no?authuser=4)

  ---------------------------------------------------------------------------------------------------------------------------------------------------

## **Margin dan Padding**

Margin adalah kode untuk mengatur jarak antara elemen dengan elemen lain diluarnya, sedangkan padding adalah kode untuk mengatur jarak antara pembungkus dan elemennya.

![](https://lh3.googleusercontent.com/pw/ADCreHebSZHJgjNbqpgrgtL1cNvGdNuPKMG0le5XH3TQKKASidOtmjDplaPTPmD1Ev2RKeL51XtivusqfNEMeZgL-R5YWYBs3gtYcLEcDoXS2Dgget8L8EudmK_SeyOE8hD0sno23lqNaIH0IF3P3wd13jQ=w409-h188-s-no?authuser=4)

Terdapat 4 arah untuk menentukan ukuran margin dan padding.

- Top: mengatur jarak pada arah atas.

- left: mengatur jarak pada arah kiri.

- bottom: mengatur jarak pada arah bawah.

- right: mengatur jarak pada arah kanan.

Kamu dapat menggunakannya adalah seperti contoh berikut.

- Margin-top
- Margin-bottom  
- Margin-left

- Padding-top
- Padding-right
- Padding-bottom

Untuk penjelasan yang lebih jelas perhatikan kode berikut.

```
<body>

<h2 style="border: 3px solid black; padding: 20px;"> Komandro</h2>

<h2 style="border: 3px solid black; margin: 20px;"> Komandro</h2\>

</body>
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHflNfXdvpt_rPWekllWyD9vwqX8iC-rEzzvoPnieExS2jljzFMyUqwghr72thY9XANNwqtCr-jPlScPLrlWWBs5j61cJO9upBPOnTCWiTIB9d3rpa9SO1wBXqpem2jZiMIjSAuF08hVbu4KmhEHA6o=w339-h161-s-no?authuser=4)

## **Width dan Height**

Adalah kode yang dipakai untuk mengatur lebar dan tinggi dari sebuah elemen.

  Width, adalah kode untuk mengatur kelebaran yang bersifat statis                                                                                                           (tidak akan berubah valuenya).  
  
 ``                                                                                           <img   src=""    alt="" width="100px">
 ``

  Height, adalah kode untuk mengatur Ketinggian yang bersifat statis (tidak akan berubah valuenya).
  ``
  <img src=""  alt="" height="50px">
  ``

## **Min dan Max**

Kamu juga dapat mengatur ukuran minimal dan maksimal dari suatu elemen,
kamu dapat memilih kode kode berikut.

  Min-Width, digunakan untuk mengatur Min-width: ukuran bebas;
  batas kelebaran minimal untuk suatu
  elemen.

  Max-Width, digunakan untuk mengatur Max-width: ukuran bebas;
  batas kelebaran maksimal untuk
  suatu elemen.

  Min-height, digunakan untuk         Min-height: ukuran bebas;
  mengatur batas ketinggian minimal
  untuk suatu elemen.

  Max-height, digunakan untuk         Max-height: ukuran bebas;
  mengatur batas ketinggian maksmal
  untuk suatu elemen.

  -----------------------------------------------------------------------

## **Class dan ID**

Kamu dapat menggunakan class dan id untuk memanggil/selector variabel
yang terkandung didalamnya. Untuk ini kita membutuhkan style.CSS dan
index.HTML (pastikan file HTML dan CSS mu sudah terhubung). Perhatikan
kode berikut.

Index.HTML

  ```html
  <body>

<h2 class="iniClass">Class Komandro</h2>

<h2 id="iniId">ID Komandro</h2>

</body>

Style.CSS

.iniClass {

color: red;

}

#iniId {

color: blue;

}
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHdGd-QK2Lhf0euC7Jrx4ddZf9x2aNuJAdOodZ6IXzI8uac3-mmtWjL3w6urBxB4AKaM8ZOhWzLrRp-SydcEyh5yuASrlQd2MQUfIMVFc54ES5N8GBQOpB2eV3aD_EasHhXPCvbkazwXwsmz4Y95voI=w196-h111-s-no?authuser=4)

Secara fungsi, class dan Id memiliki fungsi yang sama. Kamu dapat
memilih salah satu nya untuk dipakai pada website projek mu.

## **Hover**

Mengacu pada keadaan ketika pengguna mengarahkan kursor mouse mereka ke elemen HTML tertentu, seperti tautan (link) atau elemen yang dapat diinteraksi. Saat pengguna mengarahkan kursor ke elemen tersebut, terkadang tindakan atau perubahan visual khusus dapat terjadi, dan ini disebut \"hover effect". Perhatikan kode berikut.

Index.HTML

```html
<body>

<h2> Class Komandro</h2>

</body>

Style.CSS

h2{

color: green;

}

h2:hover{

color:yellow;

}
```

Hasilnya akan seperti berikut.

![](https://lh3.googleusercontent.com/pw/ADCreHck1tLNeXDU97AVeiKF7pstmtNs0zB-1ywBoeMDsgVk7aUtl4Qf_bBMZgMIr_JKmcdJvX6XJeT5wo0_RFGbpcBe-DSvWNzeFlnZHg7kJr5ar50A6kxWg2kIcyDnWm15pptP2J6-wG61LjD7It9LyJo=w209-h151-s-no?authuser=4)

![](https://lh3.googleusercontent.com/pw/ADCreHel7RxfO7Un7Cdu3jJflDsE6mqffw5gL8iQV7pht0oyY9x2Ke_PRc5r2FQSocAiFfuTItiIePc1Up-sJ8XmnY-ixFvUmz1_Y6i_w8soE2nOpoHz-Nzhs8_251oY1qjIHFSnavobCZ61-E52RxYnOtQ=w213-h134-s-no?authuser=4)

## **Menentukan Posisi Item**

Kita dapat mengatur posisi elemen dengan menghitung ukuran elemen dan ukuran layar kita. Berikut adalah poin poin penting dalam menentukan posisi item:

\- Apabila kita menggunakan satuan persen sebagai ukuran (%), pastikan total keseluruhannya adalah 100%.

\- Apabila kita menggunakan satuan pixel (px), pastikan total keseluruhannya sesuai dengan lebah layar mu.

Untuk penjelasan lebih detail, perhatikan kode berikut.

```
<img src="https://www.ligagame.tv/templates/yootheme/cache/genshin-impact-zhongli_10461-ccede73b.webp"
width="30%" style="margin-left: 35%; margin-right: 35%;">
```

Hasilnya akan seperti berikut:

![](https://lh3.googleusercontent.com/pw/ADCreHeL6C80ObXHnAVvsCZjmKoLESTC3ohpo-PgyKD0JcuTfnPXvUUV-fwLZqiLNbV1-A4LQBGe0cFUlZ7HDlv8iS_degKL-kaKrQZ1pkOoxnFJIkSzUaF0NXVPybHzde6jfj1mGKiR36rlmgI2GcZxWHQ=w1366-h300-s-no?authuser=4)

Mengapa gambarnya menjadi ditengah? Karena margin kiri bernilai 35%, gambar berukuran 30% dan margin kanan bernilai 35% seperti gambar dibawah ini.

![](https://lh3.googleusercontent.com/pw/ADCreHe5bkOmKIbgseqAxwzhAqqjJoxav9hTTN0qdhupiWzDYRkCYmgHgSMy-hSqxXpYK7AMt4TL5-CDeIs1lNa9D-kF3ZtFev-ZHucHC4QopvVqoq_V-lgEhOCuuxSzXtbUD8en_FomcTjx4mydXF2E-BA=w1364-h315-s-no?authuser=4)

Margin kanan dan kiri dapat mengubah posisi gambar menjadi ditengah.

Ayo mencoba

Ubah posisi agar gambar berada di arah kanan lalu ubah gambar ke arah kiri. Sebagai clue, kamu dapat melihat pada bagian "margin" dan "width" pada kodingan mu!

Untuk implementasi dari materi ini, kalian bisa cek di bagian Mini project!
