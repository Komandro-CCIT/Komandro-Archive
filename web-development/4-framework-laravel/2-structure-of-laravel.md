# 2 - Konsep Dasar Laravel

- [2 - Konsep Dasar Laravel](#2---konsep-dasar-laravel)
  - [Struktur Folder di Laravel](#struktur-folder-di-laravel)
  - [Routing](#routing)
  - [Controller](#controller)
  - [Views dan Blade Template](#views-dan-blade-template)

Author: Muhammad Irza Arifin (@rifinsra_05)

---

Pada bagian ini, kita akan menjelajahi konsep-konsep dasar yang penting dalam framework Laravel. Memahami konsep-konsep ini akan menjadi fondasi yang kuat untuk membangun aplikasi web yang kompleks dan terstruktur dengan Laravel.

## Struktur Folder di Laravel

Laravel memiliki struktur folder yang terorganisir dengan baik, yang membantu dalam menjaga kode tetap bersih dan mudah dikelola. Memahami struktur ini penting untuk navigasi dan pengembangan aplikasi.

Berikut adalah penjelasan detail untuk setiap direktori dan file kunci dalam struktur Laravel:

- **`app`:** Direktori ini berisi inti dari aplikasi Laravel, termasuk model, controller, middleware, dan service provider.
    - **`Console`:** Berisi Artisan command untuk otomatisasi tugas.
    - **`Exceptions`:** Berisi handler untuk exception.
    - **`Http`:** Berisi controller, middleware, dan request.
    - **`Models`:** Berisi model Eloquent untuk interaksi database.
    - **`Providers`:** Berisi service provider untuk konfigurasi dan booting aplikasi.
- **`bootstrap`:** Berisi file untuk booting framework dan autoloading.
- **`config`:** Berisi file konfigurasi untuk aplikasi, seperti database, mail, dan session.
- **`database`:** Berisi file migrasi, seeder, dan factory untuk database.
- **`public`:** Direktori root untuk aplikasi, berisi file `index.php` yang menjadi entry point aplikasi.
- **`resources`:** Berisi view, aset (CSS, JavaScript, gambar), dan file bahasa.
    - **`views`:** Berisi template Blade untuk tampilan aplikasi.
- **`routes`:** Berisi definisi route untuk aplikasi.
- **`storage`:** Berisi file yang di-generate oleh aplikasi, seperti log, cache, dan session.
- **`tests`:** Berisi test unit dan feature untuk aplikasi.
- **`vendor`:** Berisi package yang diinstall melalui Composer.

**Visualisasi Struktur Folder:**

```
laravel-project/
├── app/
│   ├── Console/
│   ├── Exceptions/
│   ├── Http/
│   │   ├── Controllers/
│   │   ├── Middleware/
│   │   └── Requests/
│   ├── Models/
│   └── Providers/
├── bootstrap/
├── config/
├── database/
│   ├── migrations/
│   ├── seeders/
│   └── factories/
├── public/
├── resources/
│   ├── views/
│   └── assets/
├── routes/
├── storage/
├── tests/
└── vendor/
```

## Routing

Routing adalah proses mendefinisikan URL aplikasi dan menghubungkannya dengan controller atau closure yang akan menangani request. Laravel menyediakan sistem routing yang fleksibel dan mudah digunakan.

**Jenis-jenis Route:**

- **Route GET:** Menangani request HTTP GET, digunakan untuk menampilkan data.
- **Route POST:** Menangani request HTTP POST, digunakan untuk mengirim data ke server (misalnya, form submission).
- **Route PUT:** Menangani request HTTP PUT, digunakan untuk memperbarui data.
- **Route DELETE:** Menangani request HTTP DELETE, digunakan untuk menghapus data.
- **Route PATCH:** Menangani request HTTP PATCH, digunakan untuk memperbarui sebagian data.

**Contoh Kode Routing:**

```php
// routes/web.php

// Route GET untuk menampilkan halaman beranda
Route::get('/', function () {
    return view('welcome'); 
});

// Route POST untuk memproses form login
Route::post('/login', 'LoginController@login');

// Route GET untuk menampilkan profil user dengan ID tertentu
Route::get('/users/{id}', 'UserController@show'); 
```

**Penjelasan Kode:**

- `Route::get('/', ...)`: Mendefinisikan route GET untuk URL `/`.
- `return view('welcome');`: Mengembalikan view `welcome.blade.php` yang akan ditampilkan di browser.
- `Route::post('/login', 'LoginController@login');`: Mendefinisikan route POST untuk URL `/login` dan menghubungkannya dengan method `login` di controller `LoginController`.
- `Route::get('/users/{id}', 'UserController@show');`: Mendefinisikan route GET untuk URL `/users/{id}` dimana `{id}` adalah parameter dinamis yang akan dilewatkan ke method `show` di controller `UserController`.

**Route Parameter:**

Route parameter memungkinkan Kamu untuk menangkap segmen URL dan menggunakannya dalam controller atau closure. 

```php
Route::get('/users/{id}', function ($id) {
    return 'User ID: ' . $id;
});
```

**Route Naming:**

Kamu dapat memberi nama pada route untuk memudahkan penggunaan di tempat lain dalam aplikasi.

```php
Route::get('/users/{id}', 'UserController@show')->name('users.show'); 
```

**Route Groups:**

Route group memungkinkan Kamu untuk mengelompokkan route yang memiliki prefix atau middleware yang sama.

```php
Route::prefix('admin')->group(function () {
    Route::get('/dashboard', 'AdminController@dashboard');
    Route::get('/users', 'AdminController@users');
});
```

## Controller

Controller adalah kelas PHP yang bertanggung jawab untuk menangani request HTTP, memproses data, dan mengembalikan response. Controller bertindak sebagai "otak" dari aplikasi, mengatur logika bisnis dan interaksi dengan model dan view.

**Membuat Controller:**

Kamu dapat membuat controller baru dengan menggunakan Artisan command:

```bash
php artisan make:controller UserController
```

**Contoh Controller:**

```php
// app/Http/Controllers/UserController.php

namespace App\Http\Controllers;

use Illuminate\Http\Request;
use App\Models\User;

class UserController extends Controller
{
    public function show($id)
    {
        $user = User::find($id);
        return view('users.show', ['user' => $user]); 
    }
}
```

**Penjelasan Kode:**

- `namespace App\Http\Controllers;`: Mendefinisikan namespace untuk controller.
- `use App\Models\User;`: Mengimport model `User` agar dapat digunakan di controller.
- `public function show($id)`: Mendefinisikan method `show` yang menerima parameter `$id`.
- `$user = User::find($id);`: Mencari user di database berdasarkan ID.
- `return view('users.show', ['user' => $user]);`: Mengembalikan view `users.show.blade.php` dan mengirimkan data user ke view.

**Best Practices Controller:**

- Gunakan nama controller yang deskriptif dan konsisten (misalnya, `UserController`, `ProductController`).
- Pisahkan logika bisnis dari controller ke model atau service class.
- Gunakan dependency injection untuk menginject dependensi ke controller.

## Views dan Blade Template

View adalah bagian dari aplikasi yang bertanggung jawab untuk menampilkan data ke user. Laravel menggunakan Blade template engine, yang memungkinkan Kamu untuk menulis template HTML dengan sintaks yang elegan dan mudah dipahami.

**Blade Template:**

Blade template adalah file HTML dengan ekstensi `.blade.php` yang disimpan di direktori `resources/views`. Blade menyediakan berbagai fitur seperti:

- **Template Inheritance:**  Memungkinkan Kamu untuk membuat layout dasar dan mewarisinya di view lain.
- **Data Display:** Menampilkan data yang dikirim dari controller.
- **Control Structures:** Menggunakan conditional statement (if, else) dan loop (foreach).
- **Components and Slots:** Membuat komponen reusable dan slot untuk konten dinamis.

**Contoh Blade Template:**

```blade
<!-- resources/views/users/show.blade.php -->

<h1>{{ $user->name }}</h1>
<p>Email: {{ $user->email }}</p>
```

**Penjelasan Kode:**

- `{{ $user->name }}`: Menampilkan nilai properti `name` dari objek `$user`.
- `{{ $user->email }}`: Menampilkan nilai properti `email` dari objek `$user`.

**Layouts:**

Layout adalah template dasar yang digunakan untuk membungkus view lain. Kamu dapat mendefinisikan layout di direktori `resources/views/layouts`.

```blade
<!-- resources/views/layouts/app.blade.php -->

<!DOCTYPE html>
<html>
<head>
    <title>My App</title>
</head>
<body>
    @yield('content') 
</body>
</html>
```

**Penjelasan Kode:**

- `@yield('content')`: Mendefinisikan section `content` yang akan diisi oleh view lain.

**Memakai Layout di View:**

```blade
<!-- resources/views/users/show.blade.php -->

@extends('layouts.app')

@section('content')
    <h1>{{ $user->name }}</h1>
    <p>Email: {{ $user->email }}</p>
@endsection
```

**Penjelasan Kode:**

- `@extends('layouts.app')`: Mewarisi layout `app.blade.php`.
- `@section('content') ... @endsection`: Mengisi section `content` yang didefinisikan di layout.

**Components:**

Blade components memungkinkan Kamu untuk membuat komponen UI yang reusable. 

**Directives:**

Blade directives adalah tag khusus yang digunakan untuk melakukan tindakan tertentu, seperti conditional rendering dan loop.

**Kesimpulan:**

Pada bagian ini, kita telah mempelajari konsep dasar Laravel yang penting, termasuk struktur folder, routing, controller, dan views dengan Blade template. Memahami konsep-konsep ini merupakan langkah awal yang krusial dalam membangun aplikasi web dengan Laravel.

**Langkah Selanjutnya:**

Pada bagian selanjutnya, kita akan membahas interaksi dengan database menggunakan Eloquent ORM, termasuk konfigurasi database, migrasi, seeder, dan query database.