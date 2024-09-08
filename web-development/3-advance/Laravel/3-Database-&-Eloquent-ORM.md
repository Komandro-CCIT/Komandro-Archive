# 3 - Database & Eloquent ORM

- [3 - Database & Eloquent ORM](#3---database--eloquent-orm)
  - [3.1 Konfigurasi Database](#31-konfigurasi-database)
  - [3.2 Migrasi](#32-migrasi)
  - [3.3 Seeder dan Factory](#33-seeder-dan-factory)
  - [3.4 Eloquent ORM](#34-eloquent-orm)

Author: Muhammad Irza Arifin (@rifinsra_05)

---

Pada bagian ini, kita akan membahas interaksi dengan database di Laravel, khususnya menggunakan Eloquent ORM (Object-Relational Mapping). Eloquent ORM adalah fitur powerful di Laravel yang memungkinkan Kamu untuk berinteraksi dengan database menggunakan sintaks PHP yang elegan dan intuitif, tanpa perlu menulis query SQL secara manual.

### 3.1 Konfigurasi Database

Langkah pertama dalam menggunakan database di Laravel adalah mengkonfigurasi koneksi database. Konfigurasi database disimpan di file `.env` yang berada di root project Laravel.

**Contoh Konfigurasi Database (MySQL):**

```
DB_CONNECTION=mysql
DB_HOST=127.0.0.1
DB_PORT=3306
DB_DATABASE=nama_database
DB_USERNAME=username_database
DB_PASSWORD=password_database
```

**Penjelasan:**

- `DB_CONNECTION`: Tipe database (mysql, pgsql, sqlite, sqlsrv).
- `DB_HOST`: Alamat host database.
- `DB_PORT`: Port database.
- `DB_DATABASE`: Nama database.
- `DB_USERNAME`: Username untuk koneksi database.
- `DB_PASSWORD`: Password untuk koneksi database.

**Konfigurasi Lanjutan:**

Kamu juga dapat mengkonfigurasi opsi lanjutan seperti charset, collation, dan prefix tabel di file `config/database.php`.

### 3.2 Migrasi

Migrasi adalah cara untuk mengelola struktur database Kamu menggunakan kode PHP. Migrasi memungkinkan Kamu untuk membuat, memodifikasi, dan menghapus tabel database dengan mudah dan terstruktur, tanpa perlu menulis query SQL secara manual.

**Membuat Migrasi:**

Kamu dapat membuat migrasi baru menggunakan Artisan command:

```bash
php artisan make:migration create_users_table 
```

**Contoh Migrasi:**

```php
// database/migrations/timestamp_create_users_table.php

use Illuminate\Database\Migrations\Migration;
use Illuminate\Database\Schema\Blueprint;
use Illuminate\Support\Facades\Schema;

return new class extends Migration
{
    /**
     * Run the migrations.
     */
    public function up(): void
    {
        Schema::create('users', function (Blueprint $table) {
            ```php
            $table->id();
            $table->string('name');
            $table->string('email')->unique();
            $table->timestamp('email_verified_at')->nullable();
            $table->string('password');
            $table->rememberToken();
            $table->timestamps();
        });
    }

    /**
     * Reverse the migrations.
     */
    public function down(): void
    {
        Schema::dropIfExists('users');
    }
};
```

**Penjelasan Kode:**

- `Schema::create('users', ...)`: Membuat tabel baru bernama `users`.
- `$table->id();`: Menambahkan kolom `id` sebagai primary key auto-increment.
- `$table->string('name');`: Menambahkan kolom `name` bertipe string.
- `$table->string('email')->unique();`: Menambahkan kolom `email` bertipe string dan unique.
- `$table->timestamp('email_verified_at')->nullable();`: Menambahkan kolom `email_verified_at` bertipe timestamp dan nullable.
- `$table->string('password');`: Menambahkan kolom `password` bertipe string.
- `$table->rememberToken();`: Menambahkan kolom `remember_token` untuk fitur "remember me".
- `$table->timestamps();`: Menambahkan kolom `created_at` dan `updated_at` untuk menyimpan timestamp.
- `Schema::dropIfExists('users');`: Menghapus tabel `users` (digunakan saat rollback migrasi).

**Menjalankan Migrasi:**

Untuk menjalankan migrasi, gunakan perintah berikut:

```bash
php artisan migrate
```

**Rollback Migrasi:**

Untuk membatalkan migrasi terakhir, gunakan perintah:

```bash
php artisan migrate:rollback
```

**Best Practices Migrasi:**

- Gunakan nama migrasi yang deskriptif.
- Pisahkan migrasi menjadi file-file kecil untuk memudahkan pengelolaan.
- Gunakan `php artisan migrate:fresh` untuk menghapus semua tabel dan menjalankan migrasi dari awal (hati-hati!).

### 3.3 Seeder dan Factory

Seeder digunakan untuk mengisi database dengan data awal. Seeder berguna untuk mengisi database dengan data dummy untuk keperluan development atau testing.

**Membuat Seeder:**

```bash
php artisan make:seeder UserSeeder
```

**Contoh Seeder:**

```php
// database/seeders/UserSeeder.php

use Illuminate\Database\Seeder;
use App\Models\User;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        User::create([
            'name' => 'John Doe',
            'email' => 'john.doe@example.com',
            'password' => bcrypt('password'),
        ]);

        // Tambahkan data user lainnya...
    }
}
```

**Menjalankan Seeder:**

```bash
php artisan db:seed --class=UserSeeder 
```

**Factory:**

Factory digunakan untuk membuat data dummy secara mudah dan cepat. Factory memungkinkan Kamu untuk mendefinisikan blueprint untuk model dan meng-generate data dummy berdasarkan blueprint tersebut.

**Membuat Factory:**

```bash
php artisan make:factory UserFactory --model=User
```

**Contoh Factory:**

```php
// database/factories/UserFactory.php

use Illuminate\Database\Eloquent\Factories\Factory;
use Illuminate\Support\Str;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\User>
 */
class UserFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    public function definition(): array
    {
        return [
            'name' => fake()->name(),
            'email' => fake()->unique()->safeEmail(),
            'email_verified_at' => now(),
            'password' => '$2y$10$92IXUNpkjO0rOQ5by9cq/uSwcorpwZjroozlClIt/Io6efp4xqCxK', // password
            'remember_token' => Str::random(10),
        ];
    }

    /**
     * Indicate that the model's email address should be unverified.
     */
    public function unverified(): static
    {
        return $this->state(fn (array $attributes) => [
            'email_verified_at' => null,
        ]);
    }
}
```

**Menggunakan Factory di Seeder:**

```php
// database/seeders/UserSeeder.php

use Illuminate\Database\Seeder;
use App\Models\User;

class UserSeeder extends Seeder
{
    /**
     * Run the database seeds.
     */
    public function run(): void
    {
        User::factory()->count(10)->create(); 
    }
}
```

**Penjelasan Kode:**

- `User::factory()->count(10)->create();`: Membuat 10 data user dummy menggunakan factory.

### 3.4 Eloquent ORM

Eloquent ORM adalah fitur powerful di Laravel yang memungkinkan Kamu untuk berinteraksi dengan database menggunakan objek PHP. Setiap tabel database direpresentasikan oleh sebuah model Eloquent.

**Membuat Model:**

```bash
php artisan make:model User 
```

**Contoh Model:**

```php
// app/Models/User.php

namespace App\Models;

use Illuminate\Database\Eloquent\Factories\HasFactory;
use Illuminate\Database\Eloquent\Model;

class User extends Model
{
    use HasFactory;

    protected $fillable = [
        'name',
        'email',
        'password',
    ];
}
```

**Penjelasan Kode:**

- `protected $fillable = [...]`: Mendefinisikan kolom-kolom yang boleh diisi secara massal.

**Query Database dengan Eloquent:**

Eloquent menyediakan berbagai method untuk melakukan query database, seperti:

- **`all()`:** Mengambil semua data dari tabel.
- **`find($id)`:** Mencari data berdasarkan ID.
- **`where('kolom', 'operator', 'nilai')`:** Mencari data berdasarkan kondisi tertentu.
- **`orderBy('kolom', 'asc/desc')`:** Mengurutkan data.
- **`first()`:** Mengambil data pertama yang cocok dengan kondisi.
- **`get()`:** Mengambil collection data yang cocok dengan kondisi.

**Contoh Query:**

```php
// Mengambil semua user
$users = User::all();

// Mencari user dengan ID 1
$user = User::find(1);

// Mencari user dengan email 'john.doe@example.com'
$user = User::where('email', 'john.doe@example.com')->first();

// Mengambil user yang namanya diawali dengan 'John' dan diurutkan berdasarkan nama secara ascending
$users = User::where('name', 'like', 'John%')->orderBy('name', 'asc')->get();
```

**Relasi:**

Eloquent juga mendukung relasi antar tabel database, seperti one-to-one, one-to-many, dan many-to-many. 

**Kesimpulan:**

Pada bagian ini, kita telah membahas interaksi dengan database di Laravel menggunakan Eloquent ORM, termasuk konfigurasi database, migrasi, seeder, factory, dan query database. Eloquent ORM memudahkan Kamu dalam mengelola dan berinteraksi dengan database, sehingga Kamu dapat fokus pada logika bisnis aplikasi.

**Langkah Selanjutnya:**

Pada bagian selanjutnya, kita akan membangun aplikasi web sederhana dengan operasi CRUD (Create, Read, Update, Delete) untuk mempraktekkan konsep-konsep yang telah dipelajari sejauh ini🎉🎉

---

_(Bersambung ke Bagian 4: Praktek Membuat Web dengan Operasi CRUD Sederhana)_
    