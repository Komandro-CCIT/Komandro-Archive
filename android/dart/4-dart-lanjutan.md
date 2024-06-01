# Advance Dart

<br />

# Generic 
Generic adalah fitur dalam Dart yang memungkinkan Anda untuk membuat kelas, fungsi, dan tipe yang dapat bekerja dengan tipe data yang berbeda. Dengan menggunakan generic, Anda dapat menulis kode yang lebih fleksibel dan dapat digunakan kembali, sekaligus mempertahankan keamanan tipe.

### Kapan Menggunakan Generic?
Generic digunakan ketika Anda ingin membuat kelas atau fungsi yang dapat bekerja dengan berbagai tipe data tanpa mengorbankan keamanan tipe. Ini sangat berguna saat Anda bekerja dengan koleksi seperti `List`, `Set`, dan `Map`, atau saat Anda membuat struktur data yang kompleks.

- Generic memungkinkan Anda mendefinisikan tipe parameter yang akan digunakan dalam kelas atau fungsi.

- Ini memberikan fleksibilitas dalam mendefinisikan tipe data yang dapat digunakan tanpa harus mendefinisikan ulang kelas atau fungsi untuk setiap tipe data.

- Generic juga membantu mengurangi duplikasi kode dan meningkatkan keterbacaan serta pemeliharaan kode.

```dart
// Mendefinisikan kelas generic
class Box<T> {
  T content;

  Box(this.content);

  void showContent() {
    print('Content: $content');
  }
}

void main() {
  // Membuat instance dari Box dengan tipe String
  Box<String> stringBox = Box('Hello, Dart!');
  stringBox.showContent(); // Output: Content: Hello, Dart!

  // Membuat instance dari Box dengan tipe int
  Box<int> intBox = Box(123);
  intBox.showContent(); // Output: Content: 123

  // Membuat instance dari Box dengan tipe double
  Box<double> doubleBox = Box(3.14);
  doubleBox.showContent(); // Output: Content: 3.14
}
```
Dalam contoh di atas, kita mendefinisikan kelas `Box` yang menggunakan parameter tipe generic `T`. Kelas ini memiliki properti content yang bertipe `T` dan sebuah metode `showContent()` untuk menampilkan konten. Dalam fungsi `main()`, kita membuat instance dari Box dengan berbagai tipe data (`String`, `int`, dan `double`) dan memanggil metode` showContent()` pada masing-masing instance untuk menampilkan konten.

Penggunaan generic memungkinkan kita untuk menggunakan kelas `Box` dengan berbagai tipe data tanpa harus mendefinisikan ulang kelas tersebut untuk setiap tipe data yang berbeda. Ini memberikan fleksibilitas dan keamanan tipe yang lebih baik dalam penulisan kode.

# Collection (Koleksi)
Dart menyediakan berbagai jenis koleksi (collections) seperti `List`, `Set`, dan `Map` yang digunakan untuk menyimpan dan mengelola kumpulan data. Koleksi ini memiliki metode dan properti bawaan yang memudahkan pengelolaan data. Berikut adalah penjelasan dan contoh penggunaannya.

- ### List
    `List` adalah jenis koleksi dalam Dart yang terurut dan dapat diakses menggunakan indeks. Ini berarti setiap elemen dalam `List` memiliki posisi yang ditentukan, yang memungkinkan akses langsung ke elemen berdasarkan indeksnya. Salah satu fitur yang paling berguna dari `List` adalah kemampuannya untuk menyimpan elemen-elemen yang sama atau berbeda tipe, memungkinkan fleksibilitas dalam penggunaannya. Selain itu, `List` juga memungkinkan adanya duplikat elemen, yang artinya Anda dapat menyimpan nilai yang sama beberapa kali dalam `List`.

    #### Kapan Menggunakan List?
    `List` sangat berguna ketika Anda memiliki kumpulan data yang perlu diorganisir dalam urutan tertentu dan dapat diakses secara langsung menggunakan indeks. Misalnya, Anda dapat menggunakan `List` untuk menyimpan daftar nama, hasil dari pencarian, atau item dalam keranjang belanja.

    Dalam `List`, setiap elemen dapat diakses menggunakan indeksnya. Indeks dimulai dari 0 untuk elemen pertama, 1 untuk elemen kedua, dan seterusnya. Anda dapat menambahkan elemen baru ke `List` menggunakan metode `add()`, mengubah nilai elemen dengan langsung mengaksesnya menggunakan indeks, dan menghapus elemen menggunakan metode `remove()`. `List` juga mendukung berbagai operasi lain seperti mencari elemen, mengurutkan, dan memodifikasi secara dinamis.

   >Note
   <br/>
   `List` dapat dideklarasikan dengan atau tanpa tipe, namun disarankan untuk menyertakan tipe data elemen jika memungkinkan, karena ini membantu mencegah kesalahan dan meningkatkan kejelasan kode.
   >

   #### Contoh Penggunaan List
   ```dart
    void main() {
    // Mendeklarasikan List of Strings
    List<String> fruits = ['Apple', 'Banana', 'Mango'];

    // Menambahkan elemen baru ke List
    fruits.add('Orange');

    // Mengakses elemen List menggunakan indeks
    print(fruits[0]); // Output: Apple

    // Mengubah nilai elemen List
    fruits[1] = 'Blueberry';

    // Menghapus elemen dari List
    fruits.remove('Mango');

    // Menampilkan semua elemen List
    for (var fruit in fruits) {
        print(fruit);
    }

    }
    ```
    Dalam contoh di atas, kita mendeklarasikan sebuah `List` dengan tipe data `String`, kemudian menambahkan, mengakses, mengubah, dan menghapus elemen dari `List` tersebut. Kemudian, kita menggunakan loop `for` untuk menampilkan semua elemen `List`.

- ### Set
    `Set` adalah jenis koleksi dalam Dart yang mirip dengan `List`, namun memiliki perbedaan utama: `Set` tidak mengizinkan duplikat elemen. Dengan kata lain, setiap elemen dalam `Set` harus unik. `Set` juga tidak terurut, yang berarti tidak ada jaminan elemen akan berada dalam urutan tertentu saat diakses.

    #### Kapan Menggunakan Set?
    `Set` berguna ketika Anda perlu menyimpan elemen yang unik dan tidak perlu peduli tentang urutan elemen. Misalnya, ketika Anda ingin menghilangkan duplikat dari kumpulan data atau menyimpan kumpulan kata kunci unik.

    `Set` dalam Dart didefinisikan dengan menggunakan kurung kurawal `{}`. Anda dapat menambahkan elemen ke Set menggunakan metode `add()`, menghapus elemen dengan metode `remove()`, atau membersihkan seluruh Set dengan metode `clear()`. Karena Set tidak terurut, tidak ada cara langsung untuk mengakses elemen menggunakan indeks.

    #### Contoh Penggunaan Set
    ```dart
    void main() {
    // Mendeklarasikan Set of Strings
    Set<String> uniqueWords = {'apple', 'banana', 'apple', 'orange'};

    // Menambahkan elemen baru ke Set
    uniqueWords.add('grape');

    // Menghapus elemen dari Set
    uniqueWords.remove('banana');

    // Menampilkan semua elemen Set
    for (var word in uniqueWords) {
        print(word);
    }

    }
    ```
    Dalam contoh di atas, kita mendeklarasikan sebuah `Set` dengan tipe data `String`. Karena `Set` tidak mengizinkan duplikat, `apple` dan `banana` hanya muncul sekali dalam `Set`, meskipun ditambahkan beberapa kali. Setelah itu, kita menambahkan elemen baru, menghapus elemen `banana`, dan menampilkan semua elemen dalam `Set`.

- ### Map
    `Map` adalah jenis koleksi dalam Dart yang terdiri dari pasangan kunci-nilai yang terkait. Setiap elemen dalam `Map` terdiri dari dua bagian: kunci dan nilai yang terkait dengannya. Kunci harus unik dalam sebuah `Map`, tetapi nilai tidak perlu.

    #### Kapan Menggunakan Map?
    `Map` sangat berguna ketika Anda perlu menghubungkan satu set data dengan nilai-nilai tertentu. Misalnya, ketika Anda ingin menyimpan daftar nama dan umur, daftar kata kunci dan terjemahannya, atau detail kontak pengguna.

    Dalam Map, setiap elemen adalah pasangan kunci-nilai yang direpresentasikan sebagai `key: value`. Kunci digunakan untuk mengakses nilai yang terkait dengannya. Anda dapat menambahkan pasangan baru ke `Map` dengan menggunakan sintaks `{key: value}`, mengakses nilai dengan cara `mapName[key]`, mengubah nilai dengan cara yang sama, dan menghapus pasangan dengan metode `remove()`.

    #### Contoh penggunaan Map
    ```dart
    void main() {
    // Mendeklarasikan Map of Strings (nama dan umur)
    Map<String, int> ages = {'John': 30, 'Alice': 25, 'Bob': 35};

    // Menambahkan pasangan kunci-nilai baru ke Map
    ages['Emily'] = 28;

    // Mengakses nilai berdasarkan kunci
    print('Umur John: ${ages['John']}');

    // Mengubah nilai yang terkait dengan kunci tertentu
    ages['Alice'] = 26;

    // Menghapus pasangan kunci-nilai dari Map
    ages.remove('Bob');

    // Menampilkan semua pasangan kunci-nilai dalam Map
    ages.forEach((name, age) {
        print('$name berumur $age tahun');
    });

    }
    ```
    Dalam contoh di atas, kita mendeklarasikan sebuah `Map` dengan tipe data `String` untuk kunci dan tipe data `int` untuk nilai. Kita menambahkan, mengakses, mengubah, dan menghapus pasangan kunci-nilai dari `Map`, serta menampilkan semua pasangan kunci-nilai menggunakan metode `forEach()`.

# Exception Handling (penanganan pengecualian) 
**Exception Handling** (penanganan pengecualian) adalah teknik yang digunakan dalam pemrograman untuk mengatasi kesalahan atau kondisi tak terduga yang mungkin terjadi saat menjalankan suatu program. Dalam Dart, **exception handling** memungkinkan Anda untuk menangani kesalahan secara elegan dan menghindari kegagalan yang tidak terduga dalam aplikasi Anda.

### Kapan Menggunakan Exception Handling?
Anda harus menggunakan **exception handling** ketika Anda memiliki potensi kesalahan atau situasi tak terduga dalam kode Anda. Misalnya, ketika Anda membaca file dari sistem file yang mungkin tidak ditemukan, atau ketika Anda melakukan operasi matematika yang dapat menghasilkan hasil yang tidak valid.

Dalam Dart, Anda dapat menggunakan blok `try`, `catch`, dan `finally` untuk menangani exception. Blok `try` digunakan untuk menandai bagian kode yang mungkin menyebabkan exception. Blok `catch` digunakan untuk menangkap exception yang terjadi, sementara blok `finally` digunakan untuk mengeksekusi kode apa pun yang perlu dilakukan, terlepas dari apakah exception terjadi atau tidak.

### Contoh Penggunaan Exception Handling
```dart
void main() {
  try {
    // Menjalankan kode yang mungkin menimbulkan exception
    var result = 10 ~/ 0; // Pembagian dengan nol akan menyebabkan exception
    print('Hasil: $result'); // Tidak akan pernah dicetak
  } catch (e) {
    // Menangkap dan menangani exception
    print('Terjadi kesalahan: $e');
  } finally {
    // Mengeksekusi kode ini terlepas dari apakah exception terjadi atau tidak
    print('Program selesai');
  }
}
```
Dalam contoh di atas, kita mencoba melakukan operasi pembagian dengan nol, yang akan menyebabkan exception. Kita menangkap exception tersebut dengan menggunakan blok `catch`, dan mencetak pesan kesalahan. Blok `finally` dieksekusi setelahnya, terlepas dari apakah exception terjadi atau tidak. Ini memberikan kesempatan untuk membersihkan sumber daya atau mengeksekusi tindakan terakhir sebelum program berakhir.

# Asynchronous Programming
Asynchronous programming adalah paradigma pemrograman di mana beberapa tugas dapat berjalan secara independen dari satu sama lain, sehingga memungkinkan untuk mengeksekusi beberapa operasi secara bersamaan tanpa harus menunggu operasi sebelumnya selesai. Dalam Dart, asynchronous programming memungkinkan Anda untuk menjalankan operasi-operasi yang membutuhkan waktu lama, seperti membaca data dari sistem file atau melakukan panggilan jaringan, tanpa menghentikan eksekusi program secara keseluruhan.

### Perbedaan antara Asynchronous dan Synchronous Programming
- #### Synchronous programming
    Adalah paradigma pemrograman di mana setiap tugas dieksekusi secara berurutan, satu per satu. Dalam **synchronous programming**, setiap tugas harus menunggu tugas sebelumnya selesai sebelum dapat dieksekusi. Ini menyebabkan blok atau pembekuan pada aplikasi jika ada operasi yang membutuhkan waktu lama.

- #### Asynchronous programming
    Dalam **asynchronous programming**, tugas-tugas yang membutuhkan waktu lama dieksekusi secara independen dari satu sama lain. Sebuah tugas dapat dimulai, dan aplikasi dapat melanjutkan menjalankan tugas-tugas lainnya tanpa harus menunggu tugas tersebut selesai. Ini memungkinkan aplikasi untuk tetap responsif, bahkan saat melakukan operasi yang membutuhkan waktu lama.

### Contoh program yang menggunakan asynchronous
- #### Future
    `Future` adalah objek yang mewakili hasil atau kesalahan yang akan tersedia di masa depan, biasanya karena operasi asinkron. Dalam Dart, `Future` digunakan untuk menangani operasi asinkron dan mengembalikan nilai atau kesalahan setelah operasi selesai.
    #### Kapan Menggunakan Future?
    `Future` digunakan ketika Anda perlu menjalankan operasi yang membutuhkan waktu, seperti mengambil data dari jaringan atau sistem file, menjalankan perhitungan yang intensif, atau menunggu input pengguna.

    `Future` memiliki dua kemungkinan hasil: nilai atau kesalahan. Anda dapat menggunakan metode `then()` untuk menangani nilai yang dikembalikan oleh Future, dan metode `catchError()` untuk menangani kesalahan yang terjadi selama eksekusi Future.

    #### Contoh Penggunaan Future
    ```dart
    import 'dart:async';

    void main() {
    print('Memulai operasi asinkron');
    // Membuat Future yang mengembalikan nilai integer setelah 2 detik
    Future<int>.delayed(Duration(seconds: 2), () {
        return 42;
    }).then((value) {
        // Menangani nilai yang dikembalikan oleh Future
        print('Nilai yang diterima: $value');
    }).catchError((error) {
        // Menangani kesalahan yang terjadi selama eksekusi Future
        print('Kesalahan: $error');
    });
    print('Operasi asinkron sedang berjalan...');
    }
    ```
    Dalam contoh di atas, kita membuat `Future` yang mengembalikan nilai 42 setelah 2 detik menggunakan metode `delayed()`. Kemudian, kita menggunakan metode `then()` untuk menangani nilai yang dikembalikan oleh Future, dan metode `catchError()` untuk menangani kesalahan yang terjadi. Prosedur ini dilakukan secara asinkron, sehingga program dapat melanjutkan eksekusi sambil menunggu hasil dari Future.

- #### async dan await 
    Ketika Anda bekerja dengan operasi asinkron dalam Dart, Anda dapat menggunakan kata kunci `async` dan `await` untuk menangani eksekusi kode secara non-blok. Ini membuat kode Anda lebih mudah dibaca dan dipahami, terutama saat Anda memiliki serangkaian operasi asinkron yang harus dilakukan secara berurutan.
    #### Kapan Menggunakan async dan await?
    Anda harus menggunakan `async` dan `await` ketika Anda ingin menjalankan kode secara asinkron dan menunggu hasilnya sebelum melanjutkan eksekusi kode berikutnya. Ini sangat berguna saat Anda membutuhkan hasil dari operasi asinkron sebelum melanjutkan dengan operasi berikutnya.

    - Kata kunci `async` digunakan untuk menandai bahwa fungsi dapat berjalan secara asinkron.
    - Kata kunci `await` digunakan untuk menunggu hasil dari operasi  asinkron. Penggunaan `await` hanya diperbolehkan di dalam fungsi yang diberi label `async`.

    #### Contoh Penggunaan async dan await
    ```dart
    import 'dart:async';

    void main() async {
    print('Memulai operasi asinkron');
    
    try {
        // Memanggil fungsi yang mengembalikan Future dan menunggu hasilnya
        var result = await fetchData();
        print('Data yang diterima: $result');
    } catch (error) {
        // Menangani kesalahan yang terjadi selama eksekusi Future
        print('Kesalahan: $error');
    }
    
    print('Operasi asinkron selesai');
    }

    // Fungsi yang mengembalikan Future dengan delay 2 detik
    Future<String> fetchData() {
    return Future.delayed(Duration(seconds: 2), () {
        // Mengembalikan data setelah 2 detik
        return 'Data dari server';
    });
    
    }
    ```
    Dalam contoh di atas, kita menggunakan `async` pada fungsi `main()` untuk menandai bahwa kita akan menggunakan `await` di dalamnya. Kemudian, kita menggunakan `await` saat memanggil fungsi` fetchData()` untuk menunggu hasil operasi asinkron. Ini memungkinkan kita untuk menerima data dari `Future` dan mencetaknya setelahnya. Jika ada kesalahan selama eksekusi `Future`, kita menangani kesalahan tersebut dengan blok `catch`.

- #### Stream 
    `Stream` adalah aliran data yang berkelanjutan yang mengirimkan data secara berurutan. Dalam Dart, `stream` digunakan untuk menangani aliran data yang bersifat asinkron, seperti data yang diterima dari sumber eksternal seperti jaringan atau input pengguna.

    #### Kapan Menggunakan Stream?
    `Stream` digunakan ketika Anda perlu mengelola aliran data yang berkelanjutan, seperti data sensor real-time, tanggapan dari server, atau input pengguna yang kontinu.
    
    - `Stream` adalah objek yang menghasilkan data seiring waktu. Anda dapat mendaftarkan pendengar (listener) pada `stream` untuk menerima dan menangani data saat tersedia.
    - `Stream` dapat menghasilkan tipe data yang berbeda, seperti String, integer, atau objek kustom.

    #### Contoh Penggunaan Stream
    ```dart 
    import 'dart:async';

    void main() {
    // Membuat stream yang menghasilkan data setiap detik
    Stream<int> counterStream = Stream.periodic(Duration(seconds: 1), (int count) => count);

    // Mendaftarkan pendengar pada stream untuk menangani data yang diterima
    StreamSubscription<int> subscription = counterStream.listen((int count) {
        print('Counter: $count');
    });

    // Menunggu 5 detik
    Future.delayed(Duration(seconds: 5), () {
        // Membatalkan langganan (subscription) stream
        subscription.cancel();
        print('Pendengar stream dibatalkan');
    });
    }
    ```
    Dalam contoh di atas, kita membuat sebuah `stream` menggunakan `Stream.periodic()` yang akan menghasilkan data setiap detik. Kemudian, kita mendaftarkan pendengar pada `stream` menggunakan metode `listen()` untuk menangani data yang diterima. Setelah 5 detik, kita membatalkan langganan (subscription) `stream` menggunakan metode` cancel()`. Ini memungkinkan kita untuk menghentikan langganan pada `stream` dan menghentikan penanganan data.

# Author
author : [mawlibrahim](https://github.com/mawlibrahim)