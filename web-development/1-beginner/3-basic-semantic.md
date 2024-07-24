| **Author**       | **Editor** |
|------------------|------------|
| HasthoRahtomo    | Ifarra     |
---

- [Tag Semantic](#tag-semantic)
  - [Tag  `<header>`](#tag--header)
  - [Tag `<nav>`](#tag-nav)
  - [Tag `<article>`](#tag-article)
  - [Tag ](#tag-)
  - [Tag `<aside>`](#tag-aside)
  - [Tag `<footer>`](#tag-footer)
  - [Tag `<main>`](#tag-main)
  - [Tag `<figure>` dan `<figcaption>`](#tag-figure-dan-figcaption)
  - [Tag `<time>`](#tag-time)

# Tag Semantic

Tag semantic adalah tag HTML yang memberikan arti tertentu kepada elemen-elemen dalam dokumen web. Ini membantu menggambarkan struktur dan konten dokumen dengan cara yang lebih bermakna, bukan hanya sebagai
presentasi visual.

## Tag  `<header>`

Elemen `<header>` digunakan untuk mendefinisikan bagian kepala dokumen atau bagian dari sebuah halaman. Biasanya, elemen ini berisi judul halaman, logo, menu navigasi, atau elemen-elemen lain yang menggambarkan bagian atas dokumen atau halaman tersebut. Contoh penggunaan elemen `<header>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Header</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        header {
            background-color: #333;
            color: #fff;
            padding: 20px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        header h1 {
            margin: 0;
            font-size: 2em;
        }
        nav {
            margin-top: 10px;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
            display: flex;
        }
        nav ul li {
            margin-right: 20px;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
        nav ul li a:hover {
            background-color: #575757;
        }
    </style>
</head>
<body>
    <header>
        <h1>Halaman Utama</h1>
        <nav>
            <ul>
                <li><a href="#">Beranda</a></li>
                <li><a href="#">Tentang</a></li>
                <li><a href="#">Kontak</a></li>
            </ul>
        </nav>
    </header>
</body>
</html>
```

## Tag `<nav>`

Elemen `<nav>` digunakan untuk menandai bagian yang berisi navigasi, seperti menu. Elemen ini membantu dalam mengidentifikasi bagian dokumen yang berfungsi sebagai navigasi utama. Contoh penggunaan elemen `<nav>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Navigasi</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        nav {
            background-color: #333;
            padding: 10px;
            border-radius: 5px;
            margin-bottom: 20px;
        }
        nav ul {
            list-style-type: none;
            padding: 0;
            margin: 0;
            display: flex;
        }
        nav ul li {
            margin-right: 20px;
        }
        nav ul li a {
            color: #fff;
            text-decoration: none;
            padding: 5px 10px;
            border-radius: 3px;
        }
        nav ul li a:hover {
            background-color: #575757;
        }
    </style>
</head>
<body>
    <nav>
        <ul>
            <li><a href="#">Beranda</a></li>
            <li><a href="#">Tentang</a></li>
            <li><a href="#">Kontak</a></li>
        </ul>
    </nav>
</body>
</html>
```

## Tag `<article>`

Elemen `<article>` digunakan untuk menandai konten independen yang dapat berdiri sendiri, seperti artikel atau posting blog. Elemen `<article>` sering digunakan untuk mengelompokkan informasi yang merupakan entitas lengkap, yang dapat dijadikan objek untuk dibagikan atau digunakan secara terpisah. Contoh penggunaan elemen `<article>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Artikel</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        article {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        article h2 {
            color: #333;
        }
        article p {
            color: #555;
        }
    </style>
</head>
<body>
    <article>
        <h2>Judul Artikel</h2>
        <p>Aliqua ex esse exercitation amet eiusmod velit pariatur ex nulla elit cupidatat irure. Reprehenderit excepteur velit officia voluptate quis. Nostrud nisi duis ipsum magna ipsum adipisicing quis sit proident minim. Irure esse deserunt mollit commodo qui esse amet fugiat.</p>
    </article>
</body>
</html>

```

## Tag <section>

Elemen `<section>` digunakan untuk menandai bagian dari dokumen, seringkali dengan judul atau subjudul. Elemen ini membantu dalam mengelompokkan konten yang terkait menjadi bagian yang lebih besar. Contoh penggunaan elemen `<section>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Section</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        section {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        section h2 {
            color: #333;
        }
        section p {
            color: #555;
        }
    </style>
</head>
<body>
    <section>
        <h2>Bagian 1</h2>
        <p>Velit dolor nulla incididunt fugiat amet nostrud. Deserunt laborum adipisicing Lorem cupidatat tempor nulla sint esse et ea proident fugiat reprehenderit eu. Exercitation amet exercitation ipsum ut adipisicing consectetur.</p>
    </section>

    <section>
        <h2>Bagian 2</h2>
        <p>Ex sint aute tempor voluptate ad ad dolore eu irure tempor magna culpa. Nostrud do eiusmod aute id et magna elit reprehenderit culpa occaecat ullamco non. Tempor dolor id deserunt esse dolore exercitation in dolore Lorem labore elit do. Pariatur aliquip laboris ipsum occaecat ad elit. Tempor aliquip commodo quis sint occaecat id ipsum. Sunt enim non in enim cupidatat id cillum duis.</p>
    </section>
</body>
</html>
```

## Tag `<aside>`

Elemen `<aside>` digunakan untuk menandai konten yang berhubungan dengan konten di sekitarnya, seperti sidebar atau catatan pada bagian bawah. Elemen ini sering digunakan untuk menampilkan konten tambahan atau pendukung yang tidak terlalu terkait dengan konten utama. Contoh penggunaan elemen `<aside>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Artikel dengan Aside</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        article {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
            margin-bottom: 20px;
        }
        article h2 {
            color: #333;
        }
        article p {
            color: #555;
        }
        aside {
            background-color: #f9f9f9;
            padding: 15px;
            border-radius: 5px;
            margin-top: 20px;
        }
        aside h3 {
            color: #333;
        }
        aside ul {
            list-style: none;
            padding: 0;
        }
        aside ul li {
            margin: 5px 0;
        }
        aside ul li a {
            color: #007BFF;
            text-decoration: none;
        }
        aside ul li a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <article>
        <h2>Judul Artikel</h2>
        <p>Isi artikel...</p>

        <aside>
            <h3>Artikel Terkait</h3>
            <ul>
                <li><a href="#">Artikel 1</a></li>
                <li><a href="#">Artikel 2</a></li>
                <li><a href="#">Artikel 3</a></li>
            </ul>
        </aside>
    </article>
</body>
</html>
```

## Tag `<footer>`

Elemen `<footer>` digunakan untuk menandai bagian kaki dokumen atau bagian dari sebuah halaman. Elemen ini berisi informasi tambahan seperti informasi hak cipta, tautan ke halaman terkait, atau informasi kontak. Contoh penggunaan elemen `<footer>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Footer</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        footer {
            background-color: #333;
            color: #fff;
            padding: 20px;
            text-align: center;
            border-radius: 5px;
            margin-top: 20px;
        }
        footer p {
            margin: 0;
        }
        footer nav ul {
            list-style: none;
            padding: 0;
            margin: 10px 0 0 0;
        }
        footer nav ul li {
            display: inline;
            margin: 0 10px;
        }
        footer nav ul li a {
            color: #fff;
            text-decoration: none;
        }
        footer nav ul li a:hover {
            text-decoration: underline;
        }
    </style>
</head>
<body>
    <footer>
        <p>Hak Cipta &copy; 2023 Nama Perusahaan</p>
        <nav>
            <ul>
                <li><a href="#">Kebijakan Privasi</a></li>
                <li><a href="#">Syarat dan Ketentuan</a></li>
            </ul>
        </nav>
    </footer>
</body>
</html>
```

## Tag `<main>`

Elemen `<main>` digunakan untuk menandai konten utama dari sebuah dokumen. Elemen ini hanya boleh digunakan sekali dalam satu dokumen dan berfungsi untuk mengidentifikasi konten utama yang relevan untuk dokumen tersebut. Contoh penggunaan elemen `<main>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Selamat Datang di Situs Kami</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
            background-color: #f4f4f4;
        }
        main {
            background-color: #fff;
            padding: 20px;
            border-radius: 5px;
            box-shadow: 0 0 10px rgba(0, 0, 0, 0.1);
        }
        h1 {
            color: #333;
        }
        p {
            color: #555;
        }
    </style>
</head>
<body>
    <main>
        <h1>Selamat Datang di Situs Kami</h1>
        <p>Selamat datang di situs kami. Kami menyediakan berbagai informasi menarik untuk Anda.</p>
    </main>
</body>
</html>
```

## Tag `<figure>` dan `<figcaption>`

Elemen `<figure>` digunakan untuk menandai elemen yang berhubungan dengan gambar atau ilustrasi. Elemen ini sering digunakan untuk mengelompokkan gambar atau media lainnya bersama dengan keterangan yang menjelaskan kontennya. Elemen `<figcaption>` digunakan sebagai keterangan atau deskripsi untuk elemen `<figure>`. Contoh penggunaan elemen `<figure>` dan `<figcaption>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Penggunaan Elemen Figure</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            line-height: 1.6;
            margin: 20px;
        }
        article {
            border: 1px solid #ddd;
            padding: 20px;
            border-radius: 5px;
            background-color: #f9f9f9;
        }
        h1 {
            color: #333;
        }
        figure {
            margin: 20px 0;
            text-align: center;
        }
        figcaption {
            margin-top: 10px;
            font-style: italic;
            color: #666;
        }
    </style>
</head>
<body>
    <article>
        <h1>Judul Artikel</h1>
        <p>Ini adalah contoh artikel yang memiliki gambar ilustrasi.</p>
        
        <figure>
            <img src="https://via.placeholder.com/600x400" alt="Gambar Deskripsi">
            <figcaption>Gambar ilustrasi untuk contoh.</figcaption>
        </figure>
        
        <p>Di dalam contoh di atas, elemen <code>&lt;figure&gt;</code> digunakan untuk mengelompokkan gambar dan keterangan gambar, sedangkan elemen <code>&lt;figcaption&gt;</code> memberikan deskripsi atau keterangan untuk gambar tersebut.</p>
    </article>
</body>
</html>
```

## Tag `<time>`

Elemen `<time>` digunakan untuk menandai elemen yang berisi informasi waktu atau tanggal. Elemen ini membantu dalam menyajikan informasi terkait waktu secara terstruktur. Contoh penggunaan elemen `<time>` adalah sebagai berikut:

```html
<!DOCTYPE html>
<html lang="id">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Penggunaan Elemen Time</title>
</head>
<body>
    <article>
        <h1>Judul Artikel</h1>
        <p>Ini adalah contoh artikel yang dipublikasikan pada tanggal tertentu.</p>
        <p>Artikel dipublikasikan pada <time datetime="2023-12-26">26 Desember 2023</time>.</p>
        <p>Di dalam contoh di atas, atribut <code>datetime</code> pada elemen <code>&lt;time&gt;</code> digunakan untuk memberikan informasi waktu dalam format yang dapat dibaca oleh mesin.</p>
    </article>
</body>
</html>
```

Itulah penjelasan lengkap beserta contoh kode untuk setiap elemen yang Anda sebutkan. Semoga penjelasan ini membantu Anda memahami penggunaan dan fungsionalitas masing-masing elemen tersebut dalam HTML. Perlu diingat bahwa tag semantik berfungsi serupa dengan `<div>` biasa, tetapi kita tetap harus mengaturnya kembali melalui CSS. Penggunaan tag semantik dapat membantu seseorang dalam membaca kode yang kita buat.
