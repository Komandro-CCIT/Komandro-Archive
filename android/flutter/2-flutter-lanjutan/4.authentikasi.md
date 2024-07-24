| Author                                        | Editor |
| --------------------------------------------- | ------ |
| [SulaimanLmn](https://github.com/SulaimanLmn) | Ifarra |

# Autentikasi

- [Autentikasi](#autentikasi)
  - [Cara Kerja Autentikasi](#cara-kerja-autentikasi)
  - [Manfaat Autentikasi](#manfaat-autentikasi)
  - [Membuat Autentikasi Sederhana dengan Flutter dan Supabase](#membuat-autentikasi-sederhana-dengan-flutter-dan-supabase)
    - [Buat Skema Tabel](#buat-skema-tabel)
    - [Inisiasi Supabase dengan URL dan AnonKey](#inisiasi-supabase-dengan-url-dan-anonkey)
    - [Buat Project Flutter Baru](#buat-project-flutter-baru)
    - [Tambahkan Dependency Supabase](#tambahkan-dependency-supabase)
    - [Inisiasi Supabase dan Tambahkan User](#inisiasi-supabase-dan-tambahkan-user)

Autentikasi adalah proses verifikasi identitas pengguna untuk memastikan bahwa mereka adalah siapa yang mereka klaim. Ini adalah langkah pertama dalam memastikan keamanan akses ke data dan sistem.

## Cara Kerja Autentikasi

- Pengguna Memasukkan Kredensial: Seperti username dan password.

- Sistem Memverifikasi Kredensial: Membandingkan dengan data yang tersimpan.

- Akses Diberikan atau Ditolak: Berdasarkan validitas kredensial.

## Manfaat Autentikasi

- Keamanan Data: Melindungi informasi sensitif.

- Pencegahan Akses Ilegal: Menghalangi pengguna yang tidak sah.

## Membuat Autentikasi Sederhana dengan Flutter dan Supabase

### Buat Skema Tabel

Buat skema tabel users menggunakan SQL query sebagai berikut:

```sql
CREATE TABLE users (
    id SERIAL PRIMARY KEY,
    email VARCHAR(255) NOT NULL,
    password VARCHAR(255) NOT NULL
);
```

### Inisiasi Supabase dengan URL dan AnonKey

Pastikan Anda memiliki URL project Supabase dan AnonKey untuk mengakses database. Biasanya, URL project dan AnonKey ini dapat ditemukan di dashboard Supabase Anda.

### Buat Project Flutter Baru

Buka terminal dan buat proyek Flutter baru:

```sh
flutter create my_auth_app
cd my_auth_app
```

### Tambahkan Dependency Supabase

Buka `pubspec.yaml` dan tambahkan dependency Supabase:

```yaml
dependencies:
  flutter:
    sdk: flutter
  supabase_flutter: ^0.2.8
```

Jalankan perintah berikut untuk menginstall dependency:

```yaml
flutter pub get
```

### Inisiasi Supabase dan Tambahkan User

Buka file`main.dart` dan INisiasi Supabase. Selanjutnya, tambahkan fungsi untuk menambahkan user ke database Supabase:

```dart
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

void main() async {
  await Supabase.initialize(
    url: 'URL supabase-mu',
    anonKey: 'AnonKey supabase-mu',
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      title: 'Flutter Supabase Auth',
      home: AuthPage(),
    );
  }
}

class AuthPage extends StatefulWidget {
  const AuthPage({super.key});

  @override
  _AuthPageState createState() => _AuthPageState();
}

class _AuthPageState extends State<AuthPage> {
  final _emailController = TextEditingController();
  final _passwordController = TextEditingController();
  final _supabase = Supabase.instance.client;

  Future<void> _signUp() async {
    final response = await _supabase.auth.signUp(
      _emailController.text,
      _passwordController.text,
    );
    if (response.error == null) {
      // Jika berhasil, tambahkan ke database kita sendiri
      await _addUserToDatabase(response.data!.user!.id, _emailController.text);
      print('Sign up successful');
    } else {
      print('Sign up error: ${response.error!.message}');
    }
  }

  Future<void> _signIn() async {
    final response = await _supabase.auth.signIn(
      email: _emailController.text,
      password: _passwordController.text,
    );
    if (response.error == null) {
      print('Sign in successful');
    } else {
      print('Sign in error: ${response.error!.message}');
    }
  }

  Future<void> _addUserToDatabase(String userId, String email) async {
    final response = await _supabase.from('users').insert({
      'id': userId,
      'email': email,
      'password': _passwordController.text
    }).execute();
    if (response.error != null) {
      print('Error adding user to database: ${response.error!.message}');
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Auth with Supabase')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _emailController,
              decoration: const InputDecoration(labelText: 'Email'),
            ),
            TextField(
              controller: _passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(onPressed: _signUp, child: const Text('Sign Up')),
            ElevatedButton(onPressed: _signIn, child: const Text('Sign In')),
          ],
        ),
      ),
    );
  }
}
```

Dengan mengikuti langkah-langkah ini, Anda dapat membuat aplikasi Flutter sederhana yang menggunakan autentikasi dengan Supabase yang dapat disesuaikan dengan kebutuhan aplikasi Anda.