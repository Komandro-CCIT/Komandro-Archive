# 3. Functional Programming

Author: Hudya Ramadhana

---

## Overview

Functional Programming (FP) adalah salah satu paradigma pemrograman dimana cara penulisan program berfokus pada penggunaan fungsi untuk menyelesaikan masalah, tanpa mengubah data secara langsung.

Bayangkan FP seperti resep masakan. Kamu memiliki bahan-bahan (data) dan mengikuti langkah-langkah (fungsi) untuk mengolah bahan tersebut menjadi masakan. Setiap langkah tidak mengubah bahan asli, tapi menghasilkan sesuatu yang baru.

## Prinsip utama FP

- Immutability (Tidak Berubah): Data tidak diubah setelah dibuat. Contoh: Alih-alih mengubah list, buat list baru dengan perubahan yang diinginkan.

- Pure Functions (Fungsi Murni): Fungsi yang selalu menghasilkan output yang sama untuk input yang sama. Tidak memiliki efek samping (seperti mengubah variabel global).

- First-Class Functions: Fungsi diperlakukan seperti tipe data lainnya. Bisa disimpan dalam variabel, dipass sebagai argumen, atau dikembalikan dari fungsi lain.

- Higher-Order Functions: Fungsi yang bisa menerima fungsi lain sebagai argumen atau mengembalikan fungsi.

## Contoh

```python
# Pure function
def sapa(nama):
    return f"Halo, {nama}!"

# Higher-order function
def ucapkan(fungsi_ucapan, nama):
    return fungsi_ucapan(nama)

print(ucapkan(sapa, "Budi"))  # Output: Halo, Budi!
```    

Berdasarkan contoh di atas kamu dapat melihat bahwa fungsi ucapkan dijalankan dengan mengirimkan dua argumen, yaitu `sapa dimana `sapa` adalah fungsi dan `Budi` dimana nilai ini adalah string.

Output yang akan terjadi adalah `Halo, Budi!` karena fungsi ucapkan menerima parameter `fungsi_ucapan` yang telah diisi oleh fungsi `sapa`, dan parameter nama menerima nilai nama yang diisi oleh `"Budi"`.

## Code Time

Untuk memahaminya lebih lanjut, mari kita coba buat proyek baru (folder baru) atau kalian dapat menggunakan proyek sebelumnya.

Pertama, kita perlu membuat sebuah file bernama main.py, lalu masukkan kode di bawah ini:

```python
def sum(a, b):
    return a + b

def result(func, a, b):
    x = func(a, b)
    return f"Hasilnya adalah: {x}"

def main():
    
    x = 10
    y = 20
    
    hasil = result(sum, x, y)
    print(hasil)

if __name__ == "__main__":
    main()
```

Sekarang coba jalankan, kamu akan melihat hasilnya sebagai berikut:

```bash
hudya@perogeremmer-pc:~/code/python/testing$ python main.py 
Hasilnya adalah: 30
```

Sekarang kita bedah kodenya. Pada bagian awal kamu melihat fungsi bernama `sum` dan `result`, fungsi `sum` menerima dua parameter, dan `result` menerima tiga parameter. Pada fungsi `result`, kamu melihat `x = func(a, b)`. Sintaks `func` artinya kita mencoba menjalankan fungsi yang berada parameter.

Pada fungsi main kita coba menjalankan fungsi `result` dengan mengirimkan fungsi `sum` pada argumen nilai pertama, dan nilai x, y sebagai argumen kedua dan ketiga. Hasil yang keluar adalah teks `Hasilnya adalah: ...`.

Menggunakan functional programming, kamu dapat menggunakan fungsi yang dilemparkan pada fungsi lain, fungsi lain yang menerima nilai fungsi (method) dapat digunakan kembali pada fungsi tersebut. Ini dia mengapa fungsi `sum` dapat berjalan pada fungsi `result` meskipun kita tidak melihat sintaks `sum` berada di dalamnya. Hal ini disebabkan fungsi sum sudah dilemparkan sebagai objek ketika fungsi result dijalankan, yaitu pada bagian `hasil = result(sum, x, y)`.

## Challenge Time

Menggunakan contoh di atas, dapatkah kamu membuat sebuah fungsi perhitungan luas lingkaran dengan menerapkan higher-order function di atas?