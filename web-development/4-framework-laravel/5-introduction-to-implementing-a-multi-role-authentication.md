# 5 - Pengantar Multi-Auth di Laravel 11 dengan Breeze

## Daftar Isi
- [Konsep Dasar Autentikasi di Laravel](#51-konsep-dasar-autentikasi-di-laravel)
- [ Mengenal Laravel Breeze](#52-mengenal-laravel-breeze)
- [Perbedaan Autentikasi dan Otorisasi](#53-perbedaan-autentikasi-dan-otorisasi)
- [Peran Middleware dalam Autentikasi](#54-peran-middleware-dalam-autentikasi)
- [Konsep Multi-Auth](#55-konsep-multi-auth)
- [Penerapan Multi-Auth dalam Aplikasi](#56-penerapan-multi-auth-dalam-aplikasi)
- [Kesimpulan](#kesimpulan)

---

### 5.1 Konsep Dasar Autentikasi di Laravel

Autentikasi adalah proses verifikasi identitas pengguna dalam sebuah aplikasi. Dalam Laravel, autentikasi memiliki beberapa komponen penting:

1. **User Model**: Representasi data pengguna dalam database.
2. **Guards**: Menentukan bagaimana pengguna diautentikasi untuk setiap permintaan.
3. **Providers**: Menentukan cara mengambil data pengguna dari penyimpanan (biasanya database).

Laravel 11 menawarkan fleksibilitas dalam pemilihan sistem autentikasi. Kamu bisa memilih antara menggunakan package seperti Breeze, atau membangun sistem autentikasi sendiri.

### 5.2 Mengenal Laravel Breeze

Laravel Breeze adalah package yang menyediakan implementasi autentikasi sederhana untuk Laravel. Fitur-fitur Breeze meliputi:

- Registrasi pengguna
- Login
- Reset password
- Verifikasi email
- Template dasar menggunakan Blade dan Tailwind CSS

Breeze cocok untuk proyek yang membutuhkan sistem autentikasi dasar tanpa fitur kompleks tambahan.

### 5.3 Perbedaan Autentikasi dan Otorisasi

Penting untuk memahami perbedaan antara autentikasi dan otorisasi:

- **Autentikasi**: Memverifikasi identitas pengguna ("Siapa Kamu?")
- **Otorisasi**: Menentukan hak akses pengguna ("Apa yang boleh Kamu lakukan?")

Dalam Laravel, autentikasi biasanya ditangani oleh sistem login, sedangkan otorisasi menggunakan sistem Gates dan Policies.

### 5.4 Peran Middleware dalam Autentikasi

Middleware dalam Laravel berfungsi sebagai filter untuk HTTP request. Dalam konteks autentikasi, middleware berperan penting:

- `auth` middleware: Memastikan pengguna sudah login sebelum mengakses rute tertentu.
- `guest` middleware: Memastikan pengguna belum login (berguna untuk halaman login/register).
- `verified` middleware: Memeriksa apakah email pengguna sudah diverifikasi.

Middleware membantu mengontrol akses ke berbagai bagian aplikasi berdasarkan status autentikasi pengguna.

### 5.5 Konsep Multi-Auth

Multi-auth atau multiple authentication memungkinkan aplikasi memiliki beberapa jenis pengguna dengan proses autentikasi yang berbeda. Konsep ini melibatkan:

1. **Multiple Guards**: Menggunakan beberapa guard untuk menangani berbagai jenis pengguna.
2. **Separate User Models**: Menggunakan model terpisah untuk setiap jenis pengguna.
3. **Custom Authentication Logic**: Menyesuaikan logika autentikasi untuk setiap jenis pengguna.

Multi-auth berguna ketika aplikasi Kamu memiliki berbagai jenis pengguna dengan hak akses yang berbeda-beda.

### 5.6 Penerapan Multi-Auth dalam Aplikasi

Berikut beberapa skenario di mana multi-auth bisa diterapkan:

1. **E-commerce Platform**:
   - Pembeli: Melihat produk, melakukan pembelian
   - Penjual: Mengelola produk, melihat pesanan
   - Admin: Mengelola seluruh platform

2. **Sistem Manajemen Sekolah**:
   - Siswa: Melihat nilai, mengakses materi
   - Guru: Menginput nilai, mengelola kelas
   - Administrator: Mengelola akun, mengatur kebijakan sekolah

Dalam implementasinya, setiap jenis pengguna akan memiliki proses login terpisah dan akses ke fitur yang berbeda sesuai peran mereka.

## Kesimpulan

Memahami konsep autentikasi, otorisasi, dan multi-auth adalah langkah penting dalam membangun aplikasi web yang aman dan terorganisir dengan Laravel 11. Laravel Breeze menyediakan dasar yang solid untuk memulai, sementara pemahaman tentang middleware dan multi-auth membuka kemungkinan untuk pengembangan aplikasi yang lebih kompleks.

Dengan pengetahuan ini, Kamu siap untuk mulai mengimplementasikan sistem autentikasi yang sesuai dengan kebutuhan proyek Kamu. Pada modul praktik selanjutnya, kita akan melihat bagaimana konsep-konsep ini diterapkan dalam kode.
