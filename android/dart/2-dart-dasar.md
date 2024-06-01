# Dasar - Dasar Dart

<br />

# Membuat kalimat hello world
Agar kode dalam file dart bisa dijalankan, maka kode tersebut harus memiliki fungsi `main`. Di bawah ini kami berikan contoh program untuk menampilkan kalimat “Hello world”.
```
void main() {
print("Hello world");
}
```
Terlihat ada tanda baca `;` di akhir fungsi `print`. Tanda baca tersebut berguna untuk mengakhiri barisan.

# Penggunaan variabel
Seperti halnya di matematika, pemrograman juga memiliki konsep variabel. Variabel, sederhananya, merupakan sebuah wadah yang di dalamnya berisi nilai (value). 

```dart
void main() {
String name = "Baim";
int age = 19;
  var city = "Bogor";
  
  print("Hello my name is $name.");
  print("I'm $age years old, from $city.");
}
```
Di atas, terlihat ada tiga buah variabel, yakni variabel `name`, `age`, dan `city`. Masing-masing dari mereka memiliki value “Baim”, 19, dan “Bogor”. 

Lalu, apa makna kata `String`, `int`, dan `var` sebelum nama variabel? Ternyata, istilah-istilah tersebut digunakan untuk mendeklarasikan tipe data dalam variabel. Keyword `String` berarti value dari variabel `name` merupakan rangkaian karakter atau teks. Keyword `int` berarti integer atau yang dalam Bahasa Indonesia berarti bilangan bulat. Dan keyword `var` berarti variabel tersebut bisa diisi oleh tipe data apa pun.

# Operators
Seperti halnya dalam matematika, pemrograman juga memiliki konsep operator. Operator adalah simbol yang memberitahu kompiler untuk melakukan operasi tertentu. Di Dart, terdapat beberapa jenis operator yang sering digunakan, antara lain operator aritmatika, operator perbandingan, dan operator logika.

- **Operator Aritmatika**
    <br/>
     digunakan untuk melakukan operasi matematika dasar seperti penjumlahan, pengurangan, perkalian, pembagian, dan sisa bagi (modulus).

     ```dart
    void main() {
    int a = 10;
    int b = 5;

    print('Addition: ${a + b}'); // Penjumlahan
    print('Subtraction: ${a - b}'); // Pengurangan
    print('Multiplication: ${a * b}'); // Perkalian
    print('Division: ${a / b}'); // Pembagian
    print('Modulus: ${a % b}'); // Sisa bagi
    }
    ```
    Di atas, terdapat dua variabel `a` dan `b` dengan nilai masing-masing 10 dan 5. Kemudian, dilakukan operasi aritmatika menggunakan operator `+`, `-`, `*`, `/`, dan `%`.

- **Operator Perbandingan**
    <br/>
    Operator perbandingan digunakan untuk membandingkan dua nilai dan menghasilkan nilai boolean (`true` atau `false`).
    ```dart
    void main() {
    int a = 10;
    int b = 5;

    print('Equal: ${a == b}'); // Apakah a sama dengan b?
    print('Not equal: ${a != b}'); // Apakah a tidak sama dengan b?
    print('Greater than: ${a > b}'); // Apakah a lebih besar dari b?
    print('Less than: ${a < b}'); // Apakah a lebih kecil dari b?
    print('Greater than or equal to: ${a >= b}'); // Apakah a lebih besar atau sama dengan b?
    print('Less than or equal to: ${a <= b}'); // Apakah a lebih kecil atau sama dengan b?
    }
    ```
- **Operator Logika**
    <br/>
    Operator logika digunakan untuk mengkombinasikan dua nilai boolean. Terdapat tiga operator logika utama di Dart, yaitu `&&` (AND), `||` (OR), dan `!` (NOT).
    ```dart
    void main() {
    bool isTrue = true;
    bool isFalse = false;

    print('AND: ${isTrue && isFalse}'); // AND
    print('OR: ${isTrue || isFalse}'); // OR
    print('NOT: ${!isTrue}'); // NOT
    }
    ```
    Di atas, terdapat dua variabel boolean `isTrue` dan `isFalse` dengan nilai `true` dan `false`. Kemudian, dilakukan operasi logika menggunakan operator `&&,` `||`, dan `!`.

    Dengan memahami penggunaan operator di Dart, Anda dapat melakukan berbagai operasi pada data dengan lebih efisien dan efektif. Selamat belajar!

# Control Flow
Control flow atau kontrol aliran digunakan untuk mengarahkan jalannya eksekusi program berdasarkan kondisi tertentu. Dart mendukung pernyataan kondisional dan perulangan.

- **If-Else Statement**
    <br/>
    If-Else statement digunakan untuk melakukan pengujian kondisi dan menjalankan blok kode tertentu jika kondisi terpenuhi.
    ```dart
    void main() {
    int number = 10;

    if (number > 0) {
        print('Positive');
    } else if (number < 0) {
        print('Negative');
    } else {
        print('Zero');
    }

    }
    ```
    Di atas, terdapat variabel `number` yang diuji dengan `If-Else` statement. Jika nilai `number` lebih besar dari 0, maka akan dicetak "Positive". Jika tidak, akan dilanjutkan ke kondisi berikutnya.

- **For Loop**
    <br/>
    For loop digunakan untuk melakukan iterasi atau perulangan sejumlah kali tertentu.
    ```dart
    void main() {
    for (int i = 0; i < 5; i++) {
        print('For loop: $i');
    }

    }
    ```
    Di atas, terdapat perulangan menggunakan `For` loop yang akan mencetak nilai `i` dari 0 hingga 4.

- **While Loop**
    <br/>
    `While` loop digunakan untuk melakukan iterasi atau perulangan selama kondisi tertentu terpenuhi.
    ```dart
    void main() {
    int j = 0;
    while (j < 5) {
        print('While loop: $j');
        j++;
    }

    }
    ```
    Di atas, terdapat perulangan menggunakan `While` loop yang akan mencetak nilai `j` dari 0 hingga 4.

- **Do-While Loop**
    <br/>
    `Do-While` loop mirip dengan `While` loop, namun pernyataan di dalam blok kode akan dieksekusi setidaknya satu kali sebelum kondisi dicek.

    ```dart
    void main() {
    int k = 0;
    do {
        print('Do-While loop: $k');
        k++;
    } while (k < 5);

    }
    ```
    Di atas, terdapat perulangan menggunakan `Do-While` loop yang akan mencetak nilai `k` dari 0 hingga 4.

    Dengan memahami konsep control flow atau kontrol aliran di Dart, Anda dapat mengatur jalannya eksekusi program dengan lebih fleksibel sesuai dengan kondisi yang diberikan. Selamat belajar!

# Functions
Function adalah blok kode yang dapat digunakan untuk melakukan tugas tertentu. Dart mendukung pembuatan dan pemanggilan function.

- **Deklarasi Function**
    <br/>
    Function dideklarasikan menggunakan kata kunci `void` (jika tidak mengembalikan nilai) atau tipe data yang dikembalikan, diikuti oleh nama function dan parameter (jika ada).

    ```dart
    // Function tanpa parameter dan tanpa nilai kembali
    void greet() {
    print('Hello!');
    }

    // Function dengan parameter dan tanpa nilai kembali
    void greetWithName(String name) {
    print('Hello, $name!');
    }

    // Function dengan parameter dan nilai kembali
    int add(int a, int b) {
    return a + b;
    }
    ```
    Di atas, terdapat contoh deklarasi function tanpa parameter, dengan parameter, dan dengan nilai kembali.

- **Pemanggilan Function**
    <br/>
    Function dipanggil dengan menggunakan nama function diikuti oleh argumen (jika ada).

    ```dart
    void main() {
    greet(); // Memanggil function tanpa parameter
    greetWithName('Sulaiman'); // Memanggil function dengan parameter
    int result = add(3, 5); // Memanggil function dengan nilai kembali
    print('Result: $result');
    }
    ```
    Di atas, terdapat contoh pemanggilan function yang telah dideklarasikan sebelumnya.

    Dengan menggunakan function, Anda dapat memecah kode menjadi bagian-bagian yang lebih kecil dan mudah dikelola, serta dapat digunakan kembali di berbagai bagian program. Selamat belajar!

    
# Author
author : [mawlibrahim](https://github.com/mawlibrahim)
