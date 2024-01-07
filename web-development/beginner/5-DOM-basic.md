# Basic DOM (Document Object Model)

### Ngoding Stylish dengan JavaScript DOM: Bawa Website-mu ke Next Level!

Halo Komanders! Udah pada tau belum nih, kalo JavaScript DOM itu
kuncinya buat bikin website makin kece dan interaktif? Kalo belum,
gausah khawatir! Kita bakal ngasih tau nih tentang JavaScript DOM biar
webseit makin seru dan ga bosenin!

### DOM Itu Apa Sih?

DOM stands for Document Object Model. Jadi, DOM ini kayak peta buat
ngasih tahu browser gimana struktur dan relasi antar elemen di dalam
HTML, CSS, dan JavaScript. Jadi, kita bisa ngerubah kontennya, gayanya,
atau apa aja deh langsung dari JavaScript.

Sebelum memulai, alangkah baiknya kita siapkan berkas html berikut ini :

```html
<html lang="en">

<head>

    <meta charset="UTF-8">

    <meta name="viewport" content="width=device-width,
initial-scale=1.0">

    <title>Document<title>

</head>

<body>

    <h3 id="judul">BELAJAR DOM BARENG KOMANDRO</h3>

    <p class="teks">Ternyata DOM gampang banget looooh</p>

</body>

</html>
```

Dari berkas diatas akan menghasilkan web sederhana seperti ini :

![image1](https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/995711a3-a931-4609-8623-294a18b45914)

### Seleksi Elemen: Pilih yang Keren!

Pertama-tama, kita harus tahu cara seleksi elemen di HTML pake
JavaScript. Ini kunci utama, coy! Pake metode document.querySelector,
document.getElementById, atau document.getElementsByClassName.

Ayo kita mulai menuliskan codingan Javascriptnya. Kalian bisa langsung
saja isi menggunakan tag script di file html kalian tadi!

-   ```document.querySelector``` memilih elemen pertama yang cocok dengan
    selector CSS-nya. Misalnya, kalo mau pilih elemen dengan ID
    'judul', kita bisa pake kodemu kayak gini:

    ```const judulKeren = document.querySelector(\'#judul\');```

-   ```document.getElementById``` lebih spesifik, langsung pilih elemen
    berdasarkan ID-nya. Contohnya:
    
    ```const judulKeren = document.getElementById(\'judul\');```

-   ```document.getElementsByClassName``` memilih semua elemen dengan nama
    kelas tertentu. Misalnya, kalo mau pilih semua elemen dengan kelas
    'teks', kita bisa pake kodemu kayak gini:

    ```const teksKeren = document.getElementsByClassName(\'teks\');```

Berdasarkan penjelasan diatas, maka kalian bisa menambahkan codingan
pada tag script menjadi seperti ini

```html
<script>
        const judulKeren = document.getElementById('judul');
        const teksKeren = document.getElementsByClassName('teks');
</script>
```
### Manipulasi Elemen: Bikin Keren!

Setelah kita seleksi elemennya, kita bisa mengubah isi atau gayanya
sesuai keinginan. Kita bisa memanipulasi elemen tersebut mulai dari
properti, atribut, dan masih banyak lagi. Ayo sekarang kita coba
mengotak-atik elemen judul dan teks kita!

-   Misalnya, kita mau bikin warna judul website kita jadi biru:

    ```judulKeren.style.color = 'blue';``` 

-   Kita juga bisa membuat elemen baru menggunakan DOM. Contohnya kali
    ini kita akan membuat elemen tombol atau button

    ```js
    const tombolKeren = document.createElement('button');
    tombolKeren.textContent = 'Ini tombol cuy!';
    document.body.appendChild(tombolKeren);
    ```

Maka, setelah kita mencoba mengotak-atik elemennya, codingan tag script
kita bertambah menjadi seperti ini

```html
<script>

        const judulKeren = document.getElementById('judul');

        const teksKeren = document.getElementsByClassName('teks');

        judulKeren.style.color = 'blue';

        const tombolKeren = document.createElement('button');

        tombolKeren.textContent = 'Ini tombol cuy!';

        document.body.appendChild(tombolKeren);

</script>
```

Coba kalian save, dan liat perubahan membagongkan apa yang terjadi pada
web kalian

![image2](https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/c7d41870-c315-40d6-ab07-4a15918213f0)

Voila sekarang elemen judul berubah menjadi warna biru dan ada tambahan
elemen baru, yaitu tombol. Sangat mudah sekali bukan?

### Event Listeners buat Aksi Keren

Nah, yang paling bikin keren dari DOM itu aksinya! Pake event listeners,
lu bisa nangkep aksi user kayak klik, hover, atau apa aja deh. Contoh
sederhana nih:

```js
        tombolKeren.addEventListener('click', function () {

            alert('Tombolnya ke-klik cuuuy!');

        });
```

Coba kalian tambahkan code diatas ke dalam tag script kalian, lalu save,
dan coba klik tombol kalian sekarang!

![image3](https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/602ee43a-007d-4690-97e8-9d1a926640a2)


Mantap, sekarang ketika kalian meng-klik tombol maka pesan alert akan
muncul. Keren banget kan? Dengan teknik EventListener ini kalian bisa
membuat web kalian lebih interaktif kepada usernya.

### Teknik Parallax yang Kece

Pernahkah kalian berpikir, gimana jadinya kalau web kalian mempunyai
animasi 3D? Sangat amat menarik bukan? Fun factnya salah satu teknik
animasi 3D mudah yang memanfaatkan penggunaan DOM adalah teknik
Parallax.

Parallax merupakan efek visual yang diciptakan dengan memanfaatkan
perbedaan kecepatan pergerakan antara elemen-elemen di latar depan dan
latar belakang. Efek ini memberikan ilusi kedalaman dan gerakan 3D pada
sebuah tampilan.

Kalian pasti sangat penasaran untuk mencobanya, nih aku kasih tau salah
satu project youtube yang dijamin bikin kalian jago DOM dan Parallax
dibawah 30 menit.

<https://youtu.be/1wfeqDyMUx4?si=JT36Xa8NrxPrn6nz>

Eiits jangan males dong! Coba kalian ikutin tutorial dari link tersebut.
Dari link tersebut kita bisa belajar banyak mulai dari logic DOM itu
sendiri hingga logic dari teknik Parallax.

### Kesimpulan

Jadi, JavaScript DOM itu kunci buat bikin website kalian jadi makin
interaktif dan kece. Seleksi elemen, manipulasi kontennya, kerennya lagi
kalian tambahin aksi-aksi kece pake event listeners. Semua itu bisa
kalian lakuin dengan JavaScript DOM. Mulai sekarang, bikin website lu
makin kece pake DOM, yuk!

##
author : Ihza  
markdown : Ifarra
