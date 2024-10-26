# 1. Introduction to Programming

Author: Bara Muthi

## Overview

Untuk memulai menjadi seorang QA, kamu memerlukan pengetahuan dalam basic Programming. Perlu diketahui bahwa basic programming meliputi berbagai hal, seperti:

1. Variabel dan tipe data
2. Kondisi
3. Perulangan
4. Fungsi dan Class

## Variabel dan Tipe data

apa sih variable itu? Nah, variable dalam Python itu bisa kita ibaratkan seperti "kotak" atau "wadah" untuk menyimpan suatu nilai data. 

Misalnya, kalau kita punya angka atau teks yang mau kita simpen biar bisa dipake lagi nanti, kita tinggal masukin ke dalam "kotak" ini. Di python, variable ini fleksibel banget tipenya, jadi engga perlu nentuin tipe datanya dari awal. Kamu bisa langsung masukin  data apa saja ke dalam variable tersebut

Untuk memulainya cobalah buat sebuah file, beri nama `main.py` lalu masukkan kode di bawah ini:

```python
nama = "muti"
umur = 19

print(nama)
print(umur)
```

Untuk menjalankannya kamu bisa menggunakan `Terminal > New Terminal`, lalu masukkan perintah berikut:

```bash
python main.py
```


Apabila kode dijalankan kamu akan melihat teks berikut:

```bash
muti
19
```

Berdasarkan kode diatas terdapat dua variabel, variabel `nama` berisi `'muti'` dan variabel `umur` yang isinya `19`. Jadi kalau kita mau mengakses atua menampilkan nilai `nama` atau `umur`, cukup panggil nama variabelnya saja.

Berikut adalah cara penulisan variable yang benar nih ges:

| Contoh     | Validitas | Keterangan                                    |
| ---------- | --------- | --------------------------------------------- |
| name       | ✅         | Variabel benar                                |
| namesecond | ✅         | Variabel benar                                |
| name2      | ✅         | Variabel benar                                |
| my_name    | ✅         | Variabel benar                                |
| myName     | ✅         | Variabel benar                                |
| my_name_is | ✅         | Variabel benar                                |
| myNameIs   | ✅         | Variabel benar                                |
| nilai y    | ❌         | Tidak boleh ada spasi                         |
| 2anak      | ❌         | Tidak boleh diawali dengan angka              |
| anak@1#$   | ❌         | Tidak boleh ada simbol kecuali underscore (_) |

## Tipe Data

Nah, sekarang kita bahas tipe data nih ges, jadi tipe data itu sepertijenis data yang bisa kamu simpen di dalam variabel. 

Pada Python, ada beberapa tipe data yang sering digunakan:

1. `Int`: Ini untuk angka bulat, contohnya 5 atau -10.
2. `Float`: Ini untuk angka desimal, kayak 3.14 atau 0.8
3.  `String (str)`: Ini untuk karakter (alphanumeric) ditulis di antara tanda kutip, misalnya `"hallo"` atau `'world'`.
4. `Boolean (bool)`: Ini unntuk nilai true atau false, yang bisa dipake buat nentuin kondisi.

## Kondisi

Kondisi digunakan untuk membuat keputusan. Menggunakan kondisi, kita bisa bilang ke program kita, `"kalau ini benar, maka lakukan ini; kalau tidak, maka lakukan itu"`. Python menggunakan perintah `if`, `elif` (else if), dan `else`. yang dimana jika suatu kondisi benar, kode di dalam blok tersebut akan dijalakan. Apabila kondisi `if` salah maka kode di dalam `elif` akan diperiksa, apabila kondisi elif juga masih belom tepat, maka akan beralih ke kondisi default yaitu `else`.

Pada kondisi, kamu dapat memiliki susunan sebagai berikut:

1. If
2. Elif (else if)
3. Else

Kamu dapat memilih apakah menggunakan ketiganya atau hanya if saja, secara *default* kamu memerlukan sebuah kondisi saja.

Contohnya nih ges:

```python
umur = 15
if umur >= 18:
    print("kamu sudah dewasa.")
else:
    print("kamu masih di bawah umur.")
```

saat kode di jalankan:

```
kamu masih di bawah umur.
```

Nah, berdasarkan kode di atas kita punya variabel `umur` yang nilainya 15. Kita mau ngecek umur 15 itu udah dianggap dewasa atau masih di bawah umur.

Kondisinya gini:

- Kalau umur 18 atau lebih, tampilkan "Kamu sudah dewasa."
- Kalau kurang dari 18, tampilkan "Kamu masih di bawah umur."

Dengan umur 15, jelas umurnya kurang dari 18 dan kondisi pertama tidak memenuhi karena kondisinya adalah `umur >= 18` sedangkan 15 itu lebih kecil dari 18. Jadi, output yang akan muncul adalah `"Kamu masih di bawah umur."` paham kan ges? Oke sekarang contoh yang kondisi `elif`.

```python
nilai = 85

if nilai >= 90:
    print("Grade A")
elif nilai >= 80:
    print("Grade B")
else nilai >= 70:
    print("Grade C")
else:
    print("Grade D")
```

Saat kode di jalankan:

```bash
Grade B
```

Kenapa ada else di sini?

Sintaks `else` akan menangani semua nilai yang tidak memenuhi kondisi di if dan elif, kita juga dapat menyebutnya kondisi `default`.

Nah, dari kode di atas sebenarnya sama aja dibandingkan dengan contoh pertama dimana kita memeriksa nilai untuk menentukan grade yang sesuai.

Perbedaannya disini kita memiliki lebih banyak kondisi yang diperiksa, jadi kita menggunakan beberapa `elif` untuk menangani berbagai rentang nilai.

- `if`  memeriksa kondisi pertama (apakah `nilai >= 90`).
- Jika tidak memenuhi kondisi `if`, kita lanjut ke `elif` pertama (apakah `nilai >= 80`).
- Jika kondisi itu juga tidak terpenuhi, kita cek `elif` berikutnya (apakah `nilai >= 70`).
- Terakhir, jika tidak ada kondisi `if` atau `else` yang terpenuhi, kita pakai `else` untuk menangani semua nilai yang kurang dari 70.

Dengan nilai `85` jelas sekali nilai tersebut lebih besar dari 80. Sehingga, output yang bakal muncul adalah `'Grade B'`.

Gitu gess, paham kan? :smile:

## Looping

Looping (perulangan) itu ibaratnya kamu nyuruh program buat ngelakuin sesuatu berulang-ulang. 

Misalnya kalau kamu mau nyetak angka 1 sampai 5, kamu bisa pake loop biar program ngulang cetak angka satu per satu tanpa kamu harus ngetik perintahnya berkali-kali. Nah, python sendiri punya dua jenis loop utama: `for loop` dan `while loop`.

Apa bedanya `for loop` dengan `while loop`? Intinya gini, gunakan `for loop` kalau kamu tahu pasti berapa kali pengulangan akan dilakukan. 

Gunakan `while loop` kalau kamu nggak tahu pasti jumlah pengulangannya dan hanya ingin mengulang sampai kondisi tertentu berhenti. 

Contoh dari while loop nih ges:

```python
angka = 1

while angka <= 5:
  print(angka)
  angka += 1
```

> [!NOTE]
> Angka perlu ditambahkan (increment) sebanyak 1 untuk membuat looping dapat berhenti, apabila kita tidak menggunakan `angka += 1` maka kamu akan menemukan endless loop (loop yang tidak akan berhenti)

Berikut saat kode dijalankan:

```
1
2
3
4
5
```

Disini, loop akan terus berjalan selama angka kurang dari atau sama  dengan 5. Apabila angka berubah jadi lebih dari 5, loop berhenti. Tapi kita nggak tahu dari awal berapa kali loop-nya jalan, kita cuma tau itu tergantung dari kondisi.

Sekarang kita liat contoh dari `for loop` ya ges:

```
for i int range(1, 8):
    print(i)
```

Berikut saat kode dijalankan:
```
1
2
3
4
5
6
7
```

Dari kode di atas, kita tahu persis berapa kali loop akan berjalan. Ini akan mencetak angka 1 sampai 7 karena kita tahu loop akan berjalan 7 kali.

## Function / Method

Fungsi dalam Python itu semacam kumpulan atau blok kode yang dibuat untuk mengerjakan tugas tertentu.

Coba deh kamu bayangin punya serangkaian instruksi yang sering kamu pake berkali-kali di berbagai bagian kode. 

Daripada nulis ulang terus, kamu hanya perlu membuat fungsi untuk membungkus instruksi-instruksi itu jadi menjadi satu paket. Jadi setiap kali membutuhkan fungsi itu, tinggal panggil fungsinya aja ngga perlu nulis ulang semua kodenya.
contoh:

```python
def cetak_halo():
    print("Hallo!)

cetak_halo()
cetak_halo()
```

Oke, jadi begini, pada kode tersebut kita membuat  fungsi yang namanya `cetak_halo`. Fungsi ini isinya hanya satu baris kode untuk mencetak `"Halo!"`. 

Setiap kali kita panggil `cetak_halo()`, dia bakal jalanin kode di dalamnya dan munculin tulisan `"Halo!"` di layar.

Jadi, daripada nulis `print("Halo!")` berulang-ulang, kita cukup panggil `cetak_halo()` aja tiap kali butuh. Simpel banget, kan?

Di fungsi juga ada yang namanya **parameter**, apa itu parameter? Parameter adalah seperti syarat atau nilai yang diperlukan. Nilai yang diberikan pada saat memanggil fungsi disebut `argumen`

## Class

Kelas (class) di Python adalah cara untuk mendefinisikan tipe data baru dengan struktur dan perilaku tertentu. 

Class memungkinkan kamu untuk mengelompokkan data dan fungsi dalam sebuah unit yang bisa dipakai ulang.

Class juga merupakan koleksi dari fungsi, artinya kita bisa memiliki banyak fungsi di dalam sebuah class.