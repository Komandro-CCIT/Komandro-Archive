# Soal

Pada Latihan kali ini, kita akan membuat aplikasi Flutter yang mengimplementasikan sistem autentikasi menggunakan Supabase sebagai database. Aplikasi akan memiliki halaman signup dan login yang memungkinkan user untuk mendaftar dan masuk ke dalam aplikasi dengan validasi email, username, dan password. Setelah berhasil login, user akan diarahkan ke halaman Home Page yang menampilkan pesan "Hello [username]".

### Persyaratan

### 1. Skema Database

- Buat tabel `users` dengan kolom-kolom berikut:

  - `id` (serial, primary key)

  - `username` (varchar(50), unique, not null)

  - `email` (varchar(100), unique, not null)

  - `password` (varchar(255), not null)

### 2. Signup Page

- Form signup harus memvalidasi email, username, dan password.

- Email harus valid.

- Username tidak boleh kosong dan harus unik di dalam database.

- Password harus memiliki minimal 6 karakter.

### 3. Login Page

- Form login harus memvalidasi email atau username serta password.

- user dapat login dengan menggunakan email atau username.

- user harus terdaftar di database Supabase.

- Password yang dimasukkan harus sesuai dengan yang tersimpan di database.

### 4. Home Page

- Setelah login berhasil, arahkan user ke Home Page yang menampilkan pesan "Hello [username]".
