# 4. Exercise with OOP - Part 2 (Inheritance and Abstraction)

Author: Erisa Mayla

---

## Overview

Pada kesempatan kali ini kita akan membahas tentang Inheritance dan abstraction.

Inheritance atau pewarisan adalah konsep di mana sebuah kelas (kelas anak) dapat mewarisi atribut dan metode dari kelas lain (kelas induk). Ini memungkinkan kita untuk menggunakan kembali kode yang sudah ada.

## Code Time - Inheritance

Oke, kita langsung masuk ke dalam kode programnya aja ya:

### Mendefinisikan Kelas Induk

Pertama, mendefinisikan Kelas Induk. Kita akan menerapkan `inheritance` (pewarisan) dalam OOP (Object-Oriented Programming), dimana kelas turunan (`Anjing` dan `Kucing`) mewarisi atribut dan metode dari kelas induk (`Hewan`).

Buat sebuah file baru bernama `hewan.py` lalu masukkan kode di bawah ini:

```python
class Hewan:
    def __init__(self, nama, suara):
        self.nama = nama
        self.suara = suara
    
    def bersuara(self):
        return f'{self.nama} bersuara: {self.suara}'
```

Pada baris pertama kita mendefinisikan kelas induk yakni `Hewan`. Kita akan menggunakan konstruktor `__init__` yang digunakan untuk menginisialisasi objek dari kelas hewan. Dalam hal ini, setiap hewan akan memiliki **nama** dan **suara** yang disimpan dalam atribut `self.nama` dan `self.suara`.

### Mendefinisikan Kelas Anak

Berikutnya kita akan definisikan kelas anak yakni `Anjing` dan `Kucing`.

Buat file baru bernama `anjing.py` lalu masukkan kode di bawah ini:

```python
from hewan import Hewan

class Anjing(Hewan):
    def __init__(self, nama, suara, jenis):
        super().__init__(nama, suara)
        self.jenis = jenis

    def info(self):
        return f'Ini adalah {self.jenis} bernama {self.nama}'
```

Kelas `Anjing` adalah kelas turunan dari kelas `Hewan`, yang berarti kelas ini mewarisi atribut dan metode dari kelas `Hewan`. 

Kita kembali menggunakan konstruktor `__init__` untuk menginisialisasi atribut tambahan pada kelas `Anjing`, yaitu `jenis`. 

Untuk atribut `nama` dan `suara`, kelas `Anjing` menggunakan **konstruktor dari kelas induk** dengan memanggil `super().__init__(nama, suara)`. `super()` berfungsi untuk memanggil konstruktor dari kelas induk (`Hewan`), sehingga kita tidak perlu mendefinisikan ulang atribut `nama` dan `suara`.

Kita juga mendefinisikan `info()`, metode ini mengembalikan string yang menyebutkan jenis anjing beserta namanya.

Berikutnya kita kembali mendefinisikan kelas anak yang lain, yakni `Kucing`. Buat file baru bernama `kucing.py` lalu masukkan kode di bawah ini:

```python
from hewan import Hewan

class Kucing(Hewan):
    def __init__(self, nama, suara, warna):
        super().__init__(nama, suara)
        self.warna = warna

    def info(self):
        return f'Kucing {self.warna} ini bernama {self.nama}'
```

Sama seperti kelas `Anjing`, kelas `Kucing` juga turunan dari `Hewan` yang mewarisi atribut dan metode dari kelas induk.

Kita gunakan konstruktor `__init__` dan menambahkan atribut `warna` ke objek `Kucing`, selain atribut `nama` dan `suara` yang diwariskan dari kelas induk. 

Atribut `nama` dan `suara` diinisialisasi menggunakan `super().__init__(nama, suara)`, yang memanggil konstruktor kelas induk.

Selanjutnya kita definisikan `info()`. Metode ini mengembalikan string yang menyebutkan warna kucing beserta namanya.


### Mendefinisikan Objek dari Kelas Anak

Sekarang kita coba untuk implementasi, buat file baru bernama `main.py` lalu masukkan kode di bawah ini:

```python
anjing = Anjing('Buddy', 'Guk-guk', 'Bulldog')
kucing = Kucing('Luna', 'Meong', 'Putih')

```

```python
from anjing import Anjing
from kucing import Kucing

a = Anjing('Buddy', 'Guk-guk', 'Bulldog')
k = Kucing('Luna', 'Meong', 'Putih')


print(a.info())
print(a.bersuara())

print(k.info())
print(k.bersuara())
```

### Explanation


```python
a = Anjing('Buddy', 'Guk-guk', 'Bulldog')
k = Kucing('Luna', 'Meong', 'Putih')
```


Objek variabel bernama `obj_a` dibuat dari kelas `Anjing`, dengan nama `"Buddy"`, suara `"Guk-guk"`, dan jenis `"Bulldog"`. Atribut `nama` dan `suara` di-inisiasi melalui kelas induk `Hewan`, sedangkan atribut `jenis` di-inisiasi pada kelas `Anjing`.

Objek variabel bernama `obj_k` dibuat dari kelas `Kucing`, dengan nama `"Luna"`, suara `"Meong"`, dan warna `"Putih"`. Atribut `nama` dan `suara` di-inisiasi melalui kelas induk, sedangkan atribut `warna` di-inisiasi di kelas `Kucing`.

```python
print(anjing.info())
print(anjing.bersuara())

print(kucing.info())
print(kucing.bersuara())
```

Kode `print(anjing.info())` memanggil metode `info()` dari kelas `Anjing`, yang mengembalikan nilai string.

Sementara kode `anjing.bersuara()` memanggil metode `bersuara()` dari kelas `Hewan`, yang mengembalikan nilai string pula. 

Penjelasan ini juga berlaku pada kode `print(kucing.info())` dan `print(kucing.bersuara())`.

Karena terdapat syntax `print`, maka akan ada output dari kode tersebut apabila dijalankan. Berikut output yang akan muncul apabila kita run kode program tersebut:

```bash
PS C:\Users\Asus\vscode QA> python main.py

## Output

Ini adalah Bulldog bernama Buddy
Buddy bersuara: Guk-guk
Kucing Putih ini bernama Luna
Luna bersuara: Meong
```

> [!NOTE]
> Mungkin tadi temen-temen ada yang bingung ya, kira-kira kalo mau buat inheritance bisa ngga sih ngga make `__init__`?

Sebenernya **bisa** membuat inheritance di OOP tanpa harus menggunakan metode `__init__` dalam kelas turunan.

Namun, penggunaan `__init__` diperlukan ketika ingin menginisialisasi atribut khusus pada kelas turunan yang berbeda dari kelas induk. 

Jika kelas turunan tidak membutuhkan inisialisasi baru atau tambahan dari kelas induk, maka tidak perlu menulis metode `__init__` di dalam kelas turunan, dan kelas turunan akan secara otomatis mewarisi semua atribut dan metode dari kelas induk.

> Lalu kira-kira kapan menggunakan `__init__` dalam inheritance?

Penggunaan `__init__` digunakan jika ingin menambahkan atribut khusus di kelas turunan, kamu harus mendefinisikan `__init__` pada kelas turunan dan menggunakan `super()` untuk memanggil **`__init__`** dari kelas induk, agar semua atribut dari kelas induk tetap di-inisiasi.


## Code Time - Abstraction

Kita akan mempelajari mengenai prinsip Abstraction dalam OOP. 

Abstraction merupakan proses menyembunyikan detail implementasi dan hanya menampilkan fungsi penting.

Oke, langsung aja kita masuk ke implementasi abstraksi.

### Membuat Parent Class Abstraction

Menggunakan kode latihan sebelumnya, kamu bisa mengubah seluruh kode pada file `hewan.py`.

```python
from abc import ABC, abstractmethod

class Hewan(ABC):

    @abstractmethod
    def bergerak(self):
        pass

    @abstractmethod
    def makan(self):
        pass

    @abstractmethod
    def bersuara(self):
        pass
```

Kode dimulai dengan mengimpor dua modul dari modul `abc` yaitu `ABC` dan `abstractmethod`. 

`ABC` adalah singkatan dari Abstract Base Class, yaitu jenis kelas yang tidak dapat diinstansiasi sendiri dan dimaksudkan untuk diwariskan oleh kelas lain. 

`abstractmethod` adalah dekorator yang digunakan untuk mendefinisikan metode abstrak, yaitu metode yang harus diimplementasikan oleh setiap subclass dari kelas abstrak.

Baris berikutnya mendefinisikan kelas `Hewan` yang mewarisi dari `ABC`. Ini berarti bahwa `Hewan` adalah kelas abstrak.

Kelas `Hewan` mendefinisikan tiga metode abstrak: `bergerak`, `makan`, dan `bersuara`. Metode-metode ini ditandai sebagai abstrak menggunakan dekorator `@abstractmethod`, yang berarti bahwa setiap subclass dari `Hewan` harus mengimplementasikan metode-metode ini.

Syntax `pass` merupakan placeholder yang menandakan bahwa metode tersebut tidak memiliki implementasi di kelas ini.

Metode-metode abstrak ini (`bergerak`, `makan`, `bersuara`) harus diikuti oleh setiap subclass dari `Hewan`.

### Perubahan Kelas `Kucing` dan `Anjing`

Sekarang ubah masing-masing isi kode file kucing.py dan anjing.py dengan kode di bawah ini:


```python
from hewan import Hewan

class Kucing(Hewan):
    def bergerak(self):
        print("Kucing bergerak dengan lincah.")

    def makan(self):
        print("Kucing makan ikan dan daging.")

    def bersuara(self):
        print("Kucing mengeong.")
```

```python
from hewan import Hewan

class Anjing(Hewan):
    def bergerak(self):
        print("Anjing berlari dengan cepat.")

    def makan(self):
        print("Anjing makan daging dan makanan anjing.")

    def bersuara(self):
        print("Anjing menggonggong.")
```

`class Kucing(Hewan)` dan `class Anjing(Hewan)`, kedua kelas tersebut mewarisi dari `Hewan`, jadi harus mengimplementasikan semua metode abstrak dari `Hewan`. 


### Implementasi Kelas Abstrak

Sekarang ubah keseluruhan file `main.py` menjadi seperti ini:

```python
from kucing import Kucing
from anjing import Anjing

k = Kucing()
k.bergerak()
k.makan()
k.bersuara()

a = Anjing()
a.bergerak()
a.makan()
a.bersuara()
```

Kita membuat objek dari kelas `Kucing`, kemudian memanggil metode `bergerak`, `makan`, dan `bersuara` yang akan mencetak string.

Demikian pula, kita membuat objek dari kelas `Anjing` dan memanggil metode-metodenya.

### Bagaimana Abstraction Berfungsi?

Untuk memastikan bahwa abstraction berfungsi caranya sederhana:

Pergi ke file `anjing.py` lalu ubah keseluruhan kode menjadi seperti ini:

```python
from hewan import Hewan

class Anjing(Hewan):
    def bergerak(self):
        print("Anjing berlari dengan cepat.")

    def makan(self):
        print("Anjing makan daging dan makanan anjing.")
```

Pada kode di atas, kita menghilangkan method / fungsi bersuara.


Sekarang kembali ke main.py lalu ubah keseluruhan kode menjadi seperti ini:

```python
from kucing import Kucing
from anjing import Anjing

k = Kucing()
k.bergerak()
k.makan()
k.bersuara()

a = Anjing()
a.bergerak()
a.makan()
```

Sekarang kamu akan menemukan kode kamu error karena tidak mengimplementasikan fungsi bersuara.

> [!NOTE]
> Jadi fungsi utama dari abstraction adalah **memaksa** sebuah fungsi turunannya untuk menurunkan sifat dan mengimplementasikan fungsi yang berada pada *parent class*-nya.
