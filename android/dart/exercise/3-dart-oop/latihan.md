# Soal 1: Penerapan Inheritance dan Polimorfisme

Buatlah program Dart yang menangani berbagai jenis bentuk geometri. Program ini harus dapat menghitung luas dari beberapa jenis bentuk seperti lingkaran dan persegi panjang. Gunakan konsep inheritance dan polimorfisme untuk mencapai ini. Program harus menggunakan kelas abstrak sebagai dasar untuk bentuk-bentuk ini, dan setiap bentuk harus mengimplementasikan metode untuk menghitung luasnya.

### Instruksi:

1. Buat kelas abstrak `Shape` dengan metode abstrak `double area()` yang mengembalikan luas dari bentuk.

2. Buat dua kelas `Circle` dan `Rectangle` yang mengimplementasikan Shape.

    - Kelas `Circle` harus memiliki atribut `radius` dan mengimplementasikan metode `area()` untuk menghitung luas lingkaran.

    - Kelas `Rectangle` harus memiliki atribut `width` dan `height` serta mengimplementasikan metode `area()` untuk menghitung luas persegi panjang.

3. Dalam fungsi `main()`, buat objek `Circle` dan `Rectangle`, lalu cetak luas dari masing-masing objek menggunakan polimorfisme.

# Soal 2: Penerapan Encapsulation dan Named Parameters
Buatlah program Dart yang menyimpan informasi tentang karyawan, termasuk nama, umur, dan posisi mereka. Gunakan konsep enkapsulasi untuk melindungi properti kelas dan gunakan named parameters untuk meningkatkan keterbacaan kode. Program harus menyediakan metode untuk menampilkan informasi karyawan dan memastikan bahwa data yang diberikan valid.

### Instruksi:
1. Buat kelas `Employee` dengan properti privat `_name`, `_age`, dan `_position`.

2. Buat konstruktor dengan named parameters untuk menginisialisasi properti `Employee`.

2. Sediakan getter dan setter untuk setiap properti, dengan validasi untuk memastikan `age` positif dan `position` tidak kosong.

3. Tambahkan metode `displayInfo()` untuk menampilkan informasi karyawan.

4. Dalam fungsi `main()`, buat objek `Employee` dan gunakan getter dan setter untuk mengakses dan mengubah properti, lalu panggil metode `displayInfo()`.

Selamat mengerjakan !
