# Tag Semantic

author : HasthoRahtomo   
markdown: Ifarra

---

Tag semantic adalah tag HTML yang memberikan arti tertentu kepada
elemen-elemen dalam dokumen web. Ini membantu menggambarkan struktur dan
konten dokumen dengan cara yang lebih bermakna, bukan hanya sebagai
presentasi visual.

contoh penggunaan Tag semantic Output kode:

1. `<header>`:
    Elemen `<header>` digunakan untuk mendefinisikan bagian kepala dokumen atau bagian dari sebuah halaman. Biasanya, elemen ini berisi judul halaman, logo, menu navigasi, atau elemen-elemen lain yang menggambarkan bagian atas dokumen atau halaman tersebut. Contoh penggunaan elemen `<header>` adalah sebagai berikut:
    
    ```html
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
    ```

1. `<nav>`:
    Elemen `<nav>` digunakan untuk menandai bagian yang berisi navigasi, seperti menu. Elemen ini membantu dalam mengidentifikasi bagian dokumen yang berfungsi sebagai navigasi utama. Contoh penggunaan elemen `<nav>` adalah sebagai berikut:
    
    ```html
    <nav>
      <ul>
        <li><a href="#">Beranda</a></li>
        <li><a href="#">Tentang</a></li>
        <li><a href="#">Kontak</a></li>
      </ul>
    </nav>
    ```

3. `<article>`:
    Elemen `<article>` digunakan untuk menandai konten independen yang dapat berdiri sendiri, seperti artikel atau posting blog. Elemen `<article>` sering digunakan untuk mengelompokkan informasi yang merupakan entitas lengkap, yang dapat dijadikan objek untuk dibagikan atau digunakan secara terpisah. Contoh penggunaan elemen `<article>` adalah sebagai berikut:
    
    ```html
    <article>
      <h2>Judul Artikel</h2>
      <p>Isi artikel...</p>
    </article>
    ```

4. `<section>`:
    Elemen `<section>` digunakan untuk menandai bagian dari dokumen, seringkali dengan judul atau subjudul. Elemen ini membantu dalam mengelompokkan konten yang terkait menjadi bagian yang lebih besar. Contoh penggunaan elemen `<section>` adalah sebagai berikut:
    
    ```html
    <section>
      <h2>Bagian 1</h2>
      <p>Isi bagian 1...</p>
    </section>
    
    <section>
      <h2>Bagian 2</h2>
      <p>Isi bagian 2...</p>
    </section>
    ```

5. `<aside>`:
    Elemen `<aside>` digunakan untuk menandai konten yang berhubungan dengan konten di sekitarnya, seperti sidebar atau catatan pada bagian bawah. Elemen ini sering digunakan untuk menampilkan konten tambahan atau pendukung yang tidak terlalu terkait dengan konten utama. Contoh penggunaan elemen `<aside>` adalah sebagai berikut:
    
    ```html
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
    ```

6. `<footer>`:
    Elemen `<footer>` digunakan untuk menandai bagian kaki dokumen atau bagian dari sebuah halaman. Elemen ini berisi informasi tambahan seperti informasi hak cipta, tautan ke halaman terkait, atau informasi kontak. Contoh penggunaan elemen `<footer>` adalah sebagai berikut:
    
    ```html
    <footer>
      <p>Hak Cipta &copy; 2023 Nama Perusahaan</p>
      <nav>
        <ul>
          <li><a href="#">Kebijakan Privasi</a></li>
          <li><a href="#">Syarat dan Ketentuan</a></li>
        </ul>
      </nav>
    </footer>
    ```

7. `<main>`:
    Elemen `<main>` digunakan untuk menandai konten utama dari sebuah dokumen. Elemen ini hanya boleh digunakan sekali dalam satu dokumen dan berfungsi untuk mengidentifikasi konten utama yang relevan untuk dokumen tersebut. Contoh penggunaan elemen `<main>` adalah sebagai berikut:
    
    ```html
    <main>
      <h1>Selamat Datang di Situs Kami</h1>
      <p>Selamat datang di situs kami. Kami menyediakan berbagai informasi menarik untuk Anda.</p>
    </main>
    ```

8. `<figure>` dan `<figcaption>`:
    Elemen `<figure>` digunakan untuk menandai elemen yang berhubungan dengan gambar atau ilustrasi. Elemen ini sering digunakan untuk mengelompokkan gambar atau media lainnya bersama dengan keterangan yang menjelaskan kontennya. Elemen `<figcaption>` digunakan sebagai keterangan atau deskripsi untuk elemen `<figure>`. Contoh penggunaan elemen `<figure>` dan `<figcaption>` adalah sebagai berikut:
    
    ```html
    <figure>
      <img src="gambar.jpg" alt="Gambar Deskripsi">
      <figcaption>Gambar ilustrasi untuk contoh.</figcaption>
    </figure>
    ```

9. `<time>`:
    Elemen `<time>` digunakan untuk menandai elemen yang berisi informasi waktu atau tanggal. Elemen ini membantu dalam menyajikan informasi terkait waktu secara terstruktur. Contoh penggunaan elemen `<time>` adalah sebagai berikut:
    
    ```html
    <p>Artikel dipublikasikan pada <time datetime="2023-12-26">26 Desember 2023</time>.</p>
    ```


Di dalam contoh di atas, atribut `datetime` pada elemen `<time>` digunakan untuk memberikan informasi waktu dalam format yang dapat dibaca oleh mesin.

Itulah penjelasan lengkap beserta contoh kode untuk setiap elemen yang Anda sebutkan. Semoga penjelasan ini membantu Anda memahami penggunaan dan fungsionalitas masing-masing elemen tersebut dalam HTML.
Perlu diingat bahwa tag sematic berisi sebenarnya sama seperti \<div\>
biasa, kita tetap harus mengaturnya kembali melalui .CSS . Penggunaan
tag semantic dapat membantu seseorang dalam membaca kode yang kita buat.
