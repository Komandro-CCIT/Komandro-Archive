# 4. Exercise with OOP - Part 1 (Encapsulation and Polymorphism)

Author: Bara Muthi

---

## Overview


Okay hari ini kita akan bahas terkait pemrograman berorientasi objek. Kira-kira OOP tuh apa sih? 

OOP atau Pemrograman Berorientasi Objek adalah paradigma pemrograman yang berfokus pada konsep "objek". Dalam OOP, program disusun sebagai kumpulan objek yang saling berinteraksi, dimana setiap objek dapat menyimpan data dan kode yang memanipulasi data tersebut. OOP bertujuan untuk meningkatkan fleksibilitas dan kemudahan dalam pengembangan serta pemeliharaan perangkat lunak.

Dalam OOP, kelas dan objek berinteraksi satu dengan lainnya sehingga tercipta suatu program.

## Kenapa OOP?

### Kode lebih teratur dan mudah dipahami

OOP membantu kamu menyusun kode seperti menyusun barang di lemari. Setiap 'barang' (objek) punya tempat sendiri, jadi lebih mudah dicari dan dimengerti. Misalnya, semua hal tentang 'Mahasiswa' ada di satu tempat, semua tentang 'Mata Kuliah' di tempat lain. Ini membuat kode kamu lebih rapi dan gampang dibaca.

### Bisa pakai ulang kode dengan mudah

Dengan OOP, kamu bisa membuat 'cetakan' (kelas) yang bisa dipakai berulang kali. Ini seperti cetakan kue - sekali buat cetakan, kamu bisa bikin banyak kue dengan bentuk yang sama. Jadi, kamu tidak perlu menulis ulang kode yang sama berkali-kali, cukup 'cetak' objek baru saja.

### Lebih mudah dikembangkan

Saat programmu bertambah besar, OOP membuatnya lebih mudah untuk ditambah atau diubah. Ini seperti main Lego - kamu bisa menambah atau mengubah bagian tertentu tanpa merusak keseluruhan. Jadi, kalau nanti kamu ingin menambah fitur baru, biasanya lebih gampang dilakukan di program yang pakai OOP.


## Empat Pilar OOP

Uniknya ngga cuman hidup kita aja yang punya prinsip, OOP juga punya loh yang disebut empat pilar OOP.

### Encapsulation (Enkapsulasi)

Bayangkan ini seperti kapsul obat. Dari luar, kamu hanya perlu tahu cara meminumnya, tidak perlu tahu isi detailnya. Dalam OOP, ini berarti menyembunyikan detail rumit di dalam objek dan hanya menunjukkan apa yang perlu diketahui dari luar. Contohnya, kamu bisa menggunakan HP tanpa perlu tahu cara kerja detil di dalamnya.

### Inheritance (Pewarisan)

Ini seperti anak mewarisi sifat dari orang tua. Dalam OOP, sebuah kelas bisa 'mewarisi' sifat dan kemampuan dari kelas lain. Misalnya, jika kamu punya kelas 'Kendaraan', kelas 'Mobil' bisa mewarisi sifat-sifat umum dari 'Kendaraan' dan menambah sifat khususnya sendiri.

### Polymorphism (Polimorfisme)

Kata ini berarti 'banyak bentuk'. Dalam OOP, ini berarti objek-objek berbeda bisa merespon perintah yang sama dengan cara yang berbeda. Bayangkan tombol 'start' pada berbagai alat elektronik - semua memulai alat tersebut, tapi dengan cara yang berbeda-beda sesuai alatnya.

### Abstraction (Abstraksi)

Ini seperti membuat sketsa sederhana dari benda yang rumit. Dalam OOP, kita menyederhanakan objek kompleks dengan hanya fokus pada informasi penting dan mengabaikan detail yang tidak perlu. Misalnya, saat menggambar mobil, kita tidak perlu menggambar setiap sekrup dan baut.


## Latihan

Oke, jadi kita punya aplikasi sederhana yang bikin daftar karyawan dengan dua jenis pekerjaan: **Programmer** dan **Manager**. Kita bakal lihat gimana semua ini bekerja dengan konsep **Object-Oriented Programming** (OOP) seperti **encapsulation** dan **polymorphism**.

Pertama, kamu bisa menggunakan projek yang sudah ada atau kamu membuat folder baru.

Kedua, jangan lupa membukanya melalui visual studio code.

Ketiga, kita buat class `Karyawan` terlebih dahulu, karna ini menjadi dasar dari seluruh proyek yang kita bangun. Buat file baru bernama `karyawan.py` lalu masukkan kode di bawah ini:

```python
class Karyawan():
    def __init__(self, nama, gaji):
        self.__nama = nama  # Variabel ini bertipe private, sehingga hanya dapat diakses di dalam kelas yang sama
        self.__gaji = gaji  # Ini juga variabel private

    def get_nama(self):
        return self.__nama  # Fungsi untuk mengambil nilai nama

    def set_gaji(self, gaji_baru):
        if gaji_baru > 0:
            self.__gaji = gaji_baru  # Fungsi untuk memperbarui nilai gaji apabila lebih dari 0
        else:
            raise ValueError("Gaji harus lebih dari 0")  # Terjadi Error apabila gaji kurang dari 0

    def get_gaji(self):
        return self.__gaji  # Fungsi untuk mengembalikan nilai gaji

    def pekerjaan(self):
        print("Setiap karyawan punya pekerjaan")
```

Melihat kode di atas apa yang akan terjadi? Singkatnya kita membuat class `Karyawan` lalu nama dan gaji adalah `private attributes`, artinya kamu nggak bisa akses langsung dari luar kelas. Kalau mau dapet atau ubah, harus pakai metode yang disediakan yaitu metode `get_nama()` dan `get_gaji()` buat ngambil nilai dari atribut tersebut dan method `set_gaji()` buat ngubah gaji, tapi cuma kalau gajinya lebih dari 0. Kalau nggak, dia bakal lempar error. Method `pekerjaan()` itu metode yang bisa diubah oleh class turunannya, hal ini karena kita mengimplementasikan fungsi polymorphism.

---

Selanjutnya kita perlu membuat kelas `Programmer`, nah kelas `Programmer` ini subclass atau turunan dari `class Karyawan`.

Buat file baru bernama `programmer.py` lalu masukkan kode di bawah ini:

```python
from karyawan import Karyawan

class Programmer(Karyawan):
    def _init_(self, nama, gaji, bahasa_pemrograman):
        super()._init_(nama, gaji)  # Memberikan argumen ke konstruktor dari Karyawan

        self.__bahasa_pemrograman = bahasa_pemrograman  # Private attribute

    def get_bahasa_pemrograman(self):
        return self.__bahasa_pemrograman  # Fungsi untuk mengembalikan nilai bahasa pemrograman

    def pekerjaan(self):
        return f"{ self.get_nama() } adalah seorang Programmer yang bekerja dengan { self.__bahasa_pemrograman }."
```

Sekarang kita perlu membuat file baru bernama `manager.py`. Masukkan kode ini untuk class `Manager`.

```python
from karyawan import Karyawan

class Manager(Karyawan):
    def _init_(self, nama, gaji, departemen):
        super()._init_(nama, gaji)  # Panggil konstruktor dari Karyawan
        self.__departemen = departemen  # Private attribute

    def get_departemen(self):
        return self.__departemen  # Fungsi buat ambil departemen

    def pekerjaan(self):
        return f"{self.get_nama()} adalah seorang Manager dari departemen {self.__departemen}."
```

Nah class ini juga mewarisi atribut dan method dari class `Karyawan` dan menambahkan atribut `departemen` dan metode `get_departemen()` buat dapetin nama departemen. Lalu `pekerjaan()` akan mengimplementasikan method dari `Karyawan` dan membuat deskripsi khusus untuk seorang manager juga.

Pada class `Manager`, class `Manager` dan `Programmer` mewarisi semua fungsi dan atribut dari class `Karyawan`, tapi juga menambahkan atribut `bahasa_pemrograman` yang bersifat `private`. Method `get_bahasa_pemrograman()` untuk dapetin nilai dari variabel `bahasa_pemrograman`, lalu method `pekerjaan()` mengimplementasikan metode dari Karyawan dan bikin deskripsi khusus untuk seorang programmer.


Terakhir, buat sebuah file baru bernama `main.py`, pada class `Main` ini kita buat dua objek, yaitu satu dari class `Programmer` dan satu lagi dari class `Manager`.

```python
from programmer import Programmer
from manager import Manager

def main():
    programmer1 = Programmer("Budi", 8000000, "Python")
    manager1 = Manager("Siti", 15000000, "Pemasaran")

    print(programmer1.get_nama())  # Output: Budi
    print(programmer1.get_gaji())  # Output: 8000000

    print(programmer1.pekerjaan())  # Output: Budi adalah seorang Programmer yang bekerja dengan Python.
    print(manager1.get_nama())  # Output: Siti
    print(manager1.get_gaji())  # Output: 15000000
    print(manager1.pekerjaan())  # Output: Siti adalah seorang Manager dari departemen Pemasaran.

    # Mengubah gaji
    programmer1.set_gaji(9000000)
    print(programmer1.get_gaji())  # Output: 9000000

if __name__ == "__main__":
    main()
```

Oke kita akan bahas...

Pertama, kita impor dua kelas yaitu `Programmer` dan `Manager` dari file terpisah. Ini kayak kita manggil blueprint untuk bikin objek. Hal ini disebut **inisiasi objek**.

Terus ada fungsi atau method yang diberi nama `main` yang isinya begini:

1. Kita bikin variabel objek `programmer1` dari kelas `Programmer`, lalu kita beri dua buah argumen, argumen pertama adalah nama, kita kasih nilai `"Budi"`, kemudian argumen kedua adalah gaji, kita beri nilai `8 juta`, dan argumen ketiga adalah bahasa pemrograman, maka kita beri nilai `"Python"`.
2. Kita buat variabel objek `manager1` dari kelas `Manager`, argumen pertama menerima nama, kita beri nilai `"Siti"`, argumen kedua yaitu gaji kita beri nilai `15 juta`, kemudian argumen ketiga adalah departemen, kita beri nilai `Pemasaran` karena bekerja di bawah departemen pemasaran.

Nah, kemudian ketika dijalankan kamu akan melihat hal berikut:

- Ketika objek variabel programmer1 diberi nilai nama Budi, nilai gaji 8 juta, dan diberi nilai bahasa Python, maka akan tercetak: `"Budi adalah seorang Programmer yang bekerja dengan Python."`
- Sama halnya dengan manager, ketika kita beri nilai argumen pada variabel objek `manager1` dengan argumen nama Siti, argumen gaji 15 juta, dan pekerjaannya pada departemen pemasaran, maka yang akan tercetak adalah: `"Siti adalah seorang Manager dari departemen Pemasaran."`

Padabagian bawah kamu akan menemukan baris kode dimana nilai gaji si `programmer1` diubah menjadi jadi 9 juta menggunakan fungsi `set_gaji(9000000)`, pada baris selanjutnya program mencetak nilai dari fungsi `get_gaji()` dan akan menampilkan nilai yang kita ubah.

Terakhir, ada pengecekan kalau kode ini hanya dapat  berjalan kalau kita langsung jalankan file main.py (bukan diimpor ke file lain), oleh karena kita gunakan `if __name__ == "__main__"` untuk memeriksa.

<br/>

> [!NOTE]
> Jadi singkatnya, kita bikin programmer dan manager, cek data mereka, terus naikin gaji si programmer.

Catatan tambahan:
- `Encapsulation`: Data seperti nama, gaji, bahasa pemrograman, dan departemen disembunyiin di dalam kelas, jadi cuma bisa diakses pake metode khusus (kayak `get_nama()` atau `get_gaji()`).
- `Polymorphism`: Metode `pekerjaan()` beda implementasinya di kelas `Programmer` dan `Manager`, tapi cara manggilnya sama aja. Jadi kamu bisa akses info pekerjaan mereka dengan gampang tanpa peduli dia programmer atau manager.