# Jawaban

```dart
import 'package:flutter/material.dart';
import 'package:supabase_flutter/supabase_flutter.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
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
      home: SignupPage(),
    );
  }
}

class SignupPage extends StatefulWidget {
  const SignupPage({super.key});

  @override
  _SignupPageState createState() => _SignupPageState();
}

class _SignupPageState extends State<SignupPage> {
  final TextEditingController _emailController = TextEditingController();
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final SupabaseClient _supabase = Supabase.instance.client;

  Future<void> _signUp() async {
    final email = _emailController.text;
    final username = _usernameController.text;
    final password = _passwordController.text;

    if (!_isValidEmail(email)) {
      _showErrorDialog('Invalid Email Format');
      return;
    }

    if (!_isValidUsername(username)) {
      _showErrorDialog('Username must be between 4 to 20 characters');
      return;
    }

    if (await _isUsernameTaken(username)) {
      _showErrorDialog('Username is already taken');
      return;
    }

    if (!_isValidPassword(password)) {
      _showErrorDialog('Password must be at least 6 characters long');
      return;
    }

    final response = await _supabase.auth.signUp(
      email,
      password,
    );

    if (response.error == null) {
      await _addUserToDatabase(
          response.data!.user!.id, email, username, password);
      print('Sign up successful');

      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => LoginPage(),
        ),
      );
    } else {
      print('Sign up error: ${response.error!.message}');
      _showErrorDialog('Sign up error: ${response.error!.message}');
    }
  }

  Future<void> _addUserToDatabase(
      String userId, String email, String username, String password) async {
    final response = await _supabase.from('users').insert({
      'id': userId,
      'username': username,
      'email': email,
      'password': password,
    }).execute();

    if (response.error != null) {
      print('Error adding user to database: ${response.error!.message}');
    }
  }

  Future<bool> _isUsernameTaken(String username) async {
    final response = await _supabase
        .from('users')
        .select()
        .eq('username', username)
        .execute();
    if (response.error != null) {
      print('Error checking username availability: ${response.error!.message}');
      return true;
    }
    return response.data!.length > 0;
  }

  bool _isValidEmail(String email) {
    return RegExp(r'^[\w-\.]+@([\w-]+\.)+[\w-]{2,4}$').hasMatch(email);
  }

  bool _isValidUsername(String username) {
    return username.length >= 4 && username.length <= 20;
  }

  bool _isValidPassword(String password) {
    return password.length >= 6;
  }

  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (BuildContext context) => AlertDialog(
        title: Text('Error'),
        content: Text(message),
        actions: <Widget>[
          TextButton(
            onPressed: () {
              Navigator.pop(context);
            },
            child: Text('OK'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Signup')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _emailController,
              decoration: const InputDecoration(labelText: 'Email'),
            ),
            TextField(
              controller: _usernameController,
              decoration: const InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: _passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _signUp,
              child: const Text('Sign Up'),
            ),
          ],
        ),
      ),
    );
  }
}

class LoginPage extends StatefulWidget {
  const LoginPage({super.key});

  @override
  _LoginPageState createState() => _LoginPageState();
}

class _LoginPageState extends State<LoginPage> {
  final TextEditingController _usernameController = TextEditingController();
  final TextEditingController _passwordController = TextEditingController();
  final SupabaseClient _supabase = Supabase.instance.client;

  Future<void> _signIn() async {
    final username = _usernameController.text;
    final password = _passwordController.text;

    final response = await _supabase.auth.signIn(
      email: username,
      password: password,
    );

    if (response.error == null) {
      Navigator.pushReplacement(
        context,
        MaterialPageRoute(
          builder: (context) => HomePage(username: username),
        ),
      );
    } else {
      print('Sign in error: ${response.error!.message}');
      _showErrorDialog('Sign in error: ${response.error!.message}');
    }
  }

  void _showErrorDialog(String message) {
    showDialog(
      context: context,
      builder: (BuildContext context) => AlertDialog(
        title: Text('Error'),
        content: Text(message),
        actions: <Widget>[
          TextButton(
            onPressed: () {
              Navigator.pop(context);
            },
            child: Text('OK'),
          ),
        ],
      ),
    );
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Login')),
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Column(
          children: [
            TextField(
              controller: _usernameController,
              decoration: const InputDecoration(labelText: 'Username'),
            ),
            TextField(
              controller: _passwordController,
              decoration: const InputDecoration(labelText: 'Password'),
              obscureText: true,
            ),
            const SizedBox(height: 20),
            ElevatedButton(
              onPressed: _signIn,
              child: const Text('Sign In'),
            ),
          ],
        ),
      ),
    );
  }
}

class HomePage extends StatelessWidget {
  final String username;

  const HomePage({super.key, required this.username});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text('Home')),
      body: Center(
        child: Text('Hello $username'),
      ),
    );
  }
}
```

# Penjelasan Kode

### Inisialisasi Supabase

- Pada fungsi `main()`, kita memastikan bahwa Flutter sudah diinisialisasi dengan memanggil `WidgetsFlutterBinding.ensureInitialized()`.

- `Supabase.initialize()` digunakan untuk menginisialisasi Supabase dengan URL dan AnonKey Supabase Anda.

### MyApp

- Kelas `MyApp` adalah kelas utama yang mewarisi `StatelessWidget`. Ini adalah entri utama aplikasi Flutter dan menentukan halaman awal sebagai `SignupPage`.

### SignupPage

- `SignupPage` adalah kelas `StatefulWidget` yang berisi form pendaftaran.

- State dari form diatur dengan menggunakan `TextEditingController` untuk mengontrol input dari `TextField`.

- Pada fungsi `_signUp()`, terjadi validasi input email, username, dan password sebelum melakukan pendaftaran dengan `Supabase`.

- Setelah pendaftaran sukses, user akan ditambahkan ke database Supabase dengan menggunakan `insert` dari `SupabaseClient`.

- Jika ada kesalahan selama pendaftaran, dialog error ditampilkan menggunakan `_showErrorDialog()`.

### LoginPage

- `LoginPage` juga merupakan `StatefulWidget` yang berisi form untuk masuk.

- Fungsi `signIn()` melakukan autentikasi dengan memanggil `auth.signIn` dari `SupabaseClient`.

- Jika masuk sukses, user diarahkan ke halaman `HomePage`.

- Jika gagal, dialog error ditampilkan menggunakan `_showErrorDialog()`.

### HomePage

- `HomePage` adalah `StatelessWidget` sederhana yang menampilkan pesan sambutan kepada user setelah berhasil masuk.

Implementasi ini memanfaatkan `supabase_flutter` package untuk mengintegrasikan autentikasi dengan Supabase ke dalam aplikasi Flutter. Dengan menggunakan method `auth.signUp` dan `auth.signIn`, user dapat mendaftar dan masuk ke aplikasi, serta data user disimpan dan diverifikasi dengan database Supabase.
