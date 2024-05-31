# Soal 1: Variabel, Tipe Data, dan Operator Aritmatika

```dart
void main() {
  // Deklarasi variabel
  String name = "Baim"; // Nama disimpan dalam variabel bertipe String
  int age = 19; // Umur disimpan dalam variabel bertipe int
  String city = "Bogor"; // Kota disimpan dalam variabel bertipe String
  
  // Hitung umur dalam bulan
  int ageInMonths = age * 12; // Menghitung umur dalam bulan dengan mengalikan umur dalam tahun dengan 12
  
  // Deklarasi variabel untuk operasi aritmatika
  int a = 10; // Menyimpan angka pertama dalam variabel a
  int b = 5; // Menyimpan angka kedua dalam variabel b
  
  // Tampilkan informasi
  print("Nama saya $name."); // Menampilkan nama
  print("Saya berumur $age tahun, dan berasal dari $city."); // Menampilkan umur dan kota asal
  print("Umur saya dalam bulan adalah $ageInMonths."); // Menampilkan umur dalam bulan
  
  // Operasi aritmatika
  print('Hasil penjumlahan $a + $b = ${a + b}'); // Menampilkan hasil penjumlahan
  print('Hasil pengurangan $a - $b = ${a - b}'); // Menampilkan hasil pengurangan
  print('Hasil perkalian $a * $b = ${a * b}'); // Menampilkan hasil perkalian
  print('Hasil pembagian $a / $b = ${a / b}'); // Menampilkan hasil pembagian
  print('Hasil modulus $a % $b = ${a % b}'); // Menampilkan hasil modulus (sisa bagi)
}
```
### Penjelasan:

- Variabel `name`, `age`, dan `city` digunakan untuk menyimpan informasi tentang nama, umur, dan kota.
- `ageInMonths` dihitung dengan mengalikan umur (`age`) dengan 12.
Variabel `a` dan `b` menyimpan angka yang akan digunakan untuk operasi aritmatika.

- `print` digunakan untuk menampilkan informasi dan hasil operasi aritmatika.

# Soal 2: If-Else Statement dan Function
``` dart
void checkNumber(int number) {
  // Mengecek apakah angka positif, negatif, atau nol
  if (number > 0) {
    print('Number: $number');
    print('Positive'); // Menampilkan "Positive" jika number lebih besar dari 0
  } else if (number < 0) {
    print('Number: $number');
    print('Negative'); // Menampilkan "Negative" jika number kurang dari 0
  } else {
    print('Number: $number');
    print('Zero'); // Menampilkan "Zero" jika number sama dengan 0
  }
}

void main() {
  checkNumber(10); // Memanggil function checkNumber dengan argumen 10
  checkNumber(-5); // Memanggil function checkNumber dengan argumen -5
  checkNumber(0); // Memanggil function checkNumber dengan argumen 0
}
```

### Penjelasan:

- `checkNumber` adalah function yang menerima satu parameter `number`.

- Dalam function `checkNumber`, `if-else` digunakan untuk mengecek nilai `number`:
    - Jika `number` lebih besar dari 0, cetak "Positive".

    - Jika `number` kurang dari 0, cetak "Negative".

    - Jika `number` sama dengan 0, cetak "Zero".

- `main()` memanggil `checkNumber` dengan beberapa contoh angka (10, -5, 0) untuk menunjukkan bagaimana function bekerja dengan berbagai input.