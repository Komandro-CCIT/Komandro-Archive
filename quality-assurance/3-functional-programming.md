Functional Programming (FP) adalah gaya atau cara menulis program yang metode utamanya adalah evaluasi fungsi-fungsi matematis dan menghindari perubahan data. 

# # Konsep Utama dalam Functional Programming

1. **Pure Function**
Fungsi murni adalah fungsi yang menghasilkan output yang sama untuk input yang sama dan tidak memiliki efek samping. Misalkan kamu punya kalkulator. Setiap kali kamu menekan tombol `'2 + 3'`, kalkulator itu selalu menampilkan `'5'`. Tidak peduli di mana kamu menggunakan kalkulator itu atau berapa kali kamu mencoba, hasilnya selalu `'5'`. Berikut contoh penerapannya.

```
def add(a, b):
	return a + b
	
result = add(2, 3) 
print(result)
```

Fungsi `'add(x, y)'` adalah fungsi murni karena hanya mengembalikan hasil penjumlahan x dan y tanpa mengubah apa pun di luar fungsi ini. Output dari kode diatas adalah `'5'`.

2. **Immutability**
Artinya data yang sudah dibuat tidak dapat dirubah. Apabila terdapat perubahan pada data akan menghasilkan data baru.

```
my_list = [1, 2, 3]
new_list = my_list.copy()
new_list.append(4)
print(my_list)
print(new_list)
```

Dalam contoh ini, kita akan membuat daftar baru `'new_list'` dengan menyalin daftar asli `'my_list'`. Kami kemudian menambahkan elemen baru ke `'new_list'`, tapi `'my_list'` tetap tidak berubah. Maka, output yang dihasilkan adalah 

```
[1, 2, 3]
[1, 2, 3, 4]
```

3. **First-Class Functions**
Fungsi dianggap sebagai objek kelas satu yang berarti fungsi dapat diperlakukan seperti nilai lain (misalnya disimpan dalam variabel, diteruskan sebagai argumen, atau dikembalikan dari fungsi lain). Berikut kodenya.

```
def greet(name):
	return f"Hello, {name}!"
```

Baris pertama kita mendefinisikan fungsi `greet(name)` yang menerima satu argumen `name`. Pada baris kedua akan mengembalikan string yang berisi sapaan "Hello," diikuti nama yang diberikan sebagai argumen, ini memungkinkan untuk menyisipkan nilai variabel `'name'` ke dalam string.

```
def say_twice(func, name):
	print(func(name))
	print(func(name))

say_twice(greet, "John")
```

Selanjutnya adalah mendefinisikan fungsi `'say twice` yang menerima dua argumen:
- `'func'`: Sebuah fungsi yang akan diterapkan.
- `'name`' :  Nama yang akan diberikan sebagai input atau argumen kepada fungsi `'func'` untuk diproses.

Misalnya, jika kita memanggil `'say_twice(greet, "John")'`, maka '`func(name)`' akan menjadi '`greet("John")`', yang akan mengembalikan '`"Hello, John!"`'. Hasil ini kemudian dicetak dua kali. Maka, output yang dihasilkan adalah sebagai berikut.

```
Hello, John!
Hello, John!
```

4. **Higher-Order Functions**
Fungsi tingkat tinggi merupakan fungsi yang menerima fungsi lain sebagai argumen atau mengembalikan fungsi lain sebagai hasil.

```
def double(x):
    return x * 2

def triple(x):
    return x * 3

def apply_function(func, x):
    return func(x)

result1 = apply_function(double, 5)
print(result1)

result2 = apply_function(triple, 5)
print(result2)
```

Dalam contoh ini, fungsi `'apply_function'` adalah fungsi tingkat tinggi karena memerlukan fungsi lain (`'double'` atau `'triple'`) sebagai argumen.

5. **Recursion**
Rekursi adalah proses di mana fungsi memanggil dirinya sendiri. 

```
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

result = factorial(5)
print(result) 
```

Di sini kita mendefinisikan fungsi '`factorial(n)`' yang dimana fungsi tersebut adalah fungsi rekursif yang menghitung faktorial dari `'n'` dengan memanggil dirinya sendiri sampai mencapai kondisi dasar `'n == 0'`.


# # Pros and Cons Functional Programming

## ## **Pros FP**

1. **Predictability**
Karena functional programming menghindari perubahan data yang tidak perlu dan efek samping, hasil dari suatu fungsi akan selalu sama jika diberikan input yang sama. Ini membuat kode lebih mudah diprediksi dan dipahami.

2. **Testability**
Fungsi-fungsi murni yang independen memudahkan proses pengujian karena kita dapat menguji setiap fungsi secara terpisah tanpa khawatir tentang kondisi atau status eksternal.

3. **Parallelism**
Karena data tidak berubah dan fungsi tidak memiliki efek samping, menjalankan beberapa proses secara bersamaan (paralel) menjadi lebih aman dan efisien

4. **Modularity and Reusability**
Fungsi murni dan high-orde function meningkatkan modularitas dan reusabilitas kode. Fungsi dapat dengan mudah digabungkan, dipanggil ulang, dan digunakan dalam berbagai konteks.

5. **Maintainability**
Struktur kode yang modular dan terorganisir memudahkan pengembang dalam memelihara dan menambahkan fitur baru tanpa mengganggu bagian kode lainnya.

## ## **Cons FP**

1. **Learning Curve**
Bagi pemula atau orang yang terbiasa dengan paradigma pemrograman lain (seperti OOP), FP mungkin lebih sulit dipahami karena konsep seperti "pure functions" dan "immutable data".

2. **Performance Overhead**
Karena data di FP biasanya tidak berubah (immutable), ini bisa menyebabkan lebih banyak alokasi memori dan mengurangi performa, terutama untuk aplikasi yang membutuhkan kecepatan tinggi.

3. **Verbosity**
Functional programming membuat kode lebih deklaratik, namun terkadang gaya fungsional dapat menyebabkan kode menjadi sulit dibaca, terutama jika digunakan secara berlebihan atau tidak tepat.

4. **Tidak selalu cocok untuk semua masalah**
Ada jenis masalah tertentu yang lebih mudah diselesaikan dengan pendekatan pemrograman lain. Memaksakan penggunaan functional programming pada semua masalah bisa menyebabkan kode menjadi kompleks dan sulit dipahami.

# # Penggunaan FP

Kira-kira kapan sih kita dapat menggunakan functional programming ini? 

Simak penjelasan berikut ini yaa.

1. **Data Transformation**
Functional programming (FP) sangat berguna ketika kita perlu melakukan banyak operasi pada data, seperti mengubah, menyaring, atau menyusun ulang data. Contoh yang umum adalah saat kita menggunakan fungsi seperti '`map`, `filter`, atau `reduce`' untuk memanipulasi data dalam sebuah daftar atau koleksi. FP membantu membuat kode yang lebih ringkas dan mudah dibaca untuk tugas-tugas semacam ini.

2. **Concurrent and Parallel Processing**
FP juga sangat bermanfaat dalam situasi di mana kita menjalankan banyak tugas secara bersamaan (paralel) atau secara konkuren (bergiliran). Karena FP tidak bergantung pada state atau data yang berubah-ubah, risiko terjadinya "race condition" (situasi di mana dua proses mencoba mengubah data yang sama secara bersamaan) bisa dihindari. Ini membuat FP lebih aman dan efektif untuk pemrosesan yang melibatkan banyak tugas secara bersamaan.

3. **Domain-Spesific Languages (DSLs)**
FP sering digunakan untuk membuat DSLs, yaitu bahasa pemrograman yang dirancang khusus untuk tugas tertentu. Misalnya, jika kita membuat sebuah alat atau framework untuk memproses data dengan aturan tertentu, FP dapat membantu karena pendekatannya yang lebih terstruktur dan deklaratif (menyatakan apa yang harus dilakukan, bukan bagaimana melakukannya).

4. **Mathematical and Scientific Computing**
FP sangat cocok digunakan dalam bidang matematika dan ilmu pengetahuan karena sifatnya yang mendukung penggunaan fungsi-fungsi murni (pure functions). Fungsi murni selalu memberikan hasil yang sama untuk input yang sama dan tidak mengubah state atau data lain. Ini membuat FP ideal untuk menangani perhitungan kompleks, seperti komposisi fungsi dan operasi matematis lainnya, dengan lebih mudah dan aman