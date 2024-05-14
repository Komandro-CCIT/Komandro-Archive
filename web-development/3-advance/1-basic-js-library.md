# Pengenalan dasar library js

![libjs](https://getflywheel.com/layout/wp-content/uploads/2019/02/The_Best_Java_Script_Libraries_1800x500-1-1280x356.jpg)

## Apa Itu JS Library?

JS Library (JavaScript Library) adalah kumpulan fungsi dan fitur yang telah ditulis sebelumnya dalam bahasa pemrograman JavaScript. Library ini dapat digunakan untuk mempermudah pengembangan aplikasi web dengan menyediakan berbagai fungsionalitas yang umum digunakan, seperti manipulasi DOM, animasi, komunikasi dengan server, dan masih banyak lagi.

## Manfaat JS Library

Menggunakan JS Library memiliki beberapa manfaat, antara lain:

1. **Efisiensi Pengembangan**: Dengan menggunakan JS Library, pengembang dapat menghemat waktu dan usaha dalam menulis kode dari awal. Library sudah menyediakan fungsi-fungsi yang telah dioptimalkan dan teruji, sehingga pengembang tidak perlu mengulang proses yang sama.

2. **Kualitas dan Keandalan**: JS Library yang populer biasanya telah melalui pengujian dan pengembangan yang intensif oleh komunitas pengembang. Hal ini dapat meningkatkan kualitas dan keandalan kode yang digunakan dalam proyek.

3. **Kompatibilitas Lintas Peramban**: Library JavaScript umumnya dirancang agar dapat berfungsi dengan baik di berbagai peramban web modern. Ini memungkinkan pengembang untuk menghindari perhatian yang terlalu mendalam terhadap perbedaan implementasi di antara peramban.

4. **Dokumentasi yang Kaya**: Library populer cenderung memiliki dokumentasi yang lengkap dan rinci. Dokumentasi ini memberikan panduan penggunaan yang jelas, contoh kode, dan penjelasan yang membantu pengembang memahami cara menggunakan library tersebut.

## Contoh JS Library Populer

Berikut adalah beberapa contoh JS Library yang populer:

1. **React**: React adalah library JavaScript yang digunakan untuk membangun antarmuka pengguna (UI) yang interaktif. React menggunakan konsep komponen yang dapat digunakan kembali untuk memisahkan logika aplikasi dan tampilan.

2. **Vue**: Vue adalah library JavaScript yang serupa dengan React. Vue juga digunakan untuk membangun UI interaktif dan menawarkan pendekatan yang lebih ringan dan mudah dipelajari.

3. **jQuery**: jQuery adalah library JavaScript yang populer dan banyak digunakan. jQuery menyederhanakan manipulasi DOM, penanganan acara, animasi, dan berbagai fungsi lainnya yang memudahkan pengembangan aplikasi web.

4. **Lodash**: Lodash adalah library utilitas JavaScript yang kaya fitur, yang menyediakan banyak fungsi berguna untuk memanipulasi dan mengelola data.

5. **Axios**: Axios adalah library JavaScript yang digunakan untuk melakukan permintaan HTTP ke server. Axios menyediakan antarmuka yang sederhana dan kuat untuk berkomunikasi dengan API.

## Pengenalan dasar jQuery

![](https://upload.wikimedia.org/wikipedia/commons/thumb/d/d3/Logo_jQuery.svg/1200px-Logo_jQuery.svg.png)

Salah satu JS library yang populer adalah jQUery, jQuery mempermudah developer web untuk mengembangkan aplikasi web mereka, dengan mempersingkat pengetikan dom dan banyak fitur fitur lain yang tersedia.

jQuery adalah sebuah library JavaScript yang populer dan banyak digunakan dalam pengembangan aplikasi web. Library ini dirancang untuk menyederhanakan manipulasi DOM (Document Object Model), penanganan acara, animasi, dan komunikasi dengan server.

### Manfaat Penggunaan jQuery

Penggunaan jQuery memiliki beberapa manfaat, di antaranya:

1. **Sintaks yang Ringkas**: jQuery menggunakan sintaks yang ringkas dan mudah dipahami. Dengan menggunakan jQuery, pengembang dapat melakukan manipulasi dan interaksi dengan elemen-elemen DOM dengan lebih mudah dan efisien dibandingkan dengan menggunakan JavaScript murni.

2. **Kompatibilitas Lintas Browser**: jQuery dirancang untuk bekerja secara konsisten di berbagai peramban web yang umum digunakan. Dengan menggunakan jQuery, pengembang dapat menghindari perhatian yang mendalam terhadap perbedaan implementasi di antara browser dan fokus pada pengembangan fungsionalitas aplikasi.

3. **Fungsi yang Kaya**: jQuery menyediakan pustaka fungsi JavaScript yang kaya dan tangguh. Fungsi-fungsi ini mencakup manipulasi DOM, penanganan acara, animasi, komunikasi AJAX, efek visual, dan banyak lagi. Penggunaan pustaka fungsi ini mempercepat pengembangan aplikasi web dengan menyediakan solusi yang siap pakai.

4. **Dokumentasi yang Lengkap**: jQuery memiliki dokumentasi resmi yang lengkap dan terperinci. Dokumentasi ini menyediakan panduan penggunaan, contoh kode, dan penjelasan yang membantu pengembang memahami cara menggunakan fungsi-fungsi jQuery dengan benar.

### Contoh Penggunaan jQuery

Berikut adalah beberapa contoh penggunaan jQuery:

1. **Manipulasi DOM**: jQuery memudahkan manipulasi elemen-elemen DOM, seperti menambah, menghapus, atau mengubah atribut suatu elemen. Contohnya, dengan jQuery, pengembang dapat dengan mudah menambahkan elemen baru ke halaman atau mengubah tampilan elemen yang ada.

2. **Penanganan Event**: jQuery menyediakan metode yang mudah digunakan untuk menangani acara, seperti klik mouse, pengisian formulir, atau perubahan ukuran jendela. Dengan jQuery, pengembang dapat menambahkan responsifitas dan interaktivitas ke aplikasi web dengan lebih mudah.

3. **AJAX**: jQuery menyediakan metode yang sederhana untuk melakukan permintaan HTTP ke server dan memperbarui bagian halaman secara dinamis. Dengan jQuery, pengembang dapat mengirim permintaan AJAX dan mengolah respons server dengan mudah.

4. **Animasi**: jQuery menyediakan fungsi animasi yang kuat untuk membuat efek visual yang menarik. Pengembang dapat menggunakan fungsi animasi jQuery untuk membuat elemen bergerak, memudar, atau berubah ukuran secara halus.

### Contoh implementasi jQuery untuk manipulasi DOM

Pertama kita harus menambahkan link dari jQuery untuk memulai menggunakan jquery :

```html
<script src="https://code.jquery.com/jquery-3.7.1.min.js" integrity="sha256-/JqT3SQfawRcv/BIHPThkBvs0OEvtFFmqPF/lYI/Cxo=" crossorigin="anonymous"></script>
```

setelah itu kalian dapat menggunakan tag `<script>` untuk menulis kode js ke dalam file html kalian, kalian juga dapat menggunakan eksternal js untuk menggunakan jQuery.


### 1. Menambahkan Element Baru ke Halaman

```javascript
// Menambahkan elemen <p> baru ke dalam elemen dengan id "container"
$("#container").append("<p>Ini adalah teks baru yang ditambahkan menggunakan jQuery!</p>");
```

### 2. Mengubah Teks pada Elemen

```javascript
// Mengubah teks pada elemen dengan id "judul" menjadi "Selamat Datang!"
$("#judul").text("Selamat Datang!");
```

### 3. Menghapus Element

```javascript
// Menghapus elemen dengan class "hapus"
$(".hapus").remove();
```

### 4. Mengubah Atribut Element

```javascript
// Mengubah atribut src pada elemen gambar dengan id "logo"
$("#logo").attr("src", "gambar-baru.png");
```

### 5. Menambahkan atau Menghapus Kelas pada Element

```javascript
// Menambahkan kelas "aktif" pada elemen dengan id "menu"
$("#menu").addClass("aktif");

// Menghapus kelas "aktif" dari elemen dengan id "menu"
$("#menu").removeClass("aktif");
```

### 6. Menangani Event Klik

```javascript
// Menambahkan penanganan Event klik pada elemen dengan id "tombol"
$("#tombol").click(function() {
  alert("Tombol diklik!");
});
```

### 7. Animasi Element

```javascript
// Menganimasikan elemen dengan id "kotak" untuk bergerak ke kanan sejauh 200 piksel dalam 1 detik
$("#kotak").animate({left: "200px"}, 1000);
```

### 8. Mengambil Nilai Inputan

```javascript
// Mengambil nilai inputan pada elemen dengan id "nama"
var nilaiNama = $("#nama").val();
console.log("Nama yang diinputkan: " + nilaiNama);
```

Dalam contoh-contoh di atas, kita menggunakan sintaks jQuery yang ringkas dan mudah dipahami. Manipulasi DOM seperti menambah, mengubah, atau menghapus elemen, serta mengatur atribut, kelas, dan acara menjadi lebih sederhana dengan bantuan jQuery. Animasi dan pengambilan nilai inputan juga dapat dilakukan dengan mudah menggunakan fungsi-fungsi yang disediakan oleh jQuery.

Dengan menggunakan jQuery, pengembang dapat dengan efisien melakukan manipulasi DOM dalam aplikasi web dengan lebih mudah dan cepat.

## Kesimpulan

Sama seperti menggunakan bootstrap dengan css, menggunakan javascript library seperti jQuery dapat mempermudah dan mempercepat pengembangan web, ada berbagai macam fungsi dan jenis library yang kita dapat implementasikan kedalam web kita, di kasus ini, jQuery dapat kita gunakan untuk mengurus urusan front-end dan juga back-end.

Dengan menggunakan js library, kita dapat membuka luas posibiibitas yang sebelumya dengan hanya menggunakan js saja akan memakan waktu yang lama untuk mengimplementasikan ide yang kita miliki.

---

Author: Ifarra
