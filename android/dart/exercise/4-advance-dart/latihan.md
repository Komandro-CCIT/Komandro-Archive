# Soal 1: Penerapan Generic dan Koleksi dalam Dart
Buatlah program Dart yang menggunakan konsep generic untuk membuat struktur data stack yang dapat menyimpan berbagai tipe data. Program ini juga harus menggunakan koleksi `List` untuk mengimplementasikan stack. Selain itu, buat beberapa operasi dasar pada stack seperti push, pop, dan peek.

### Instruksi:
1. Buat kelas generic `Stack` yang menggunakan parameter tipe `T`.

2. Gunakan koleksi `List` untuk menyimpan elemen stack.

3. Implementasikan metode `push()` untuk menambahkan elemen ke stack.
Implementasikan metode `pop()` untuk menghapus elemen dari stack dan mengembalikannya.

4. Implementasikan metode `peek()` untuk melihat elemen teratas dari stack tanpa menghapusnya.

5. Dalam fungsi `main()`, buat instance dari `Stack` dengan berbagai tipe data (`int`, `String`, `double`), dan lakukan beberapa operasi dasar pada stack.

# Soal 2: Penerapan Asynchronous Programming dalam Dart
Buatlah program Dart yang melakukan operasi asinkron untuk membaca data dari server dan memproses data tersebut. Gunakan `Future` dan `async`/`await` untuk mengelola operasi asinkron. Program ini juga harus menangani kemungkinan kesalahan yang terjadi selama operasi asinkron.

### Instruksi:
1. Buat fungsi asinkron `fetchDataFromServer()` yang mengembalikan `Future<String>` dan mensimulasikan pengambilan data dari server dengan delay 2 detik.

2. Buat fungsi asinkron `processData()` yang menerima `String` sebagai parameter dan memproses data tersebut dengan delay 1 detik, mengembalikan hasil sebagai `String`.

3. Dalam fungsi `main()`, panggil `fetchDataFromServer()` dan `processData()` menggunakan await, dan tangani kemungkinan kesalahan dengan blok try-catch.