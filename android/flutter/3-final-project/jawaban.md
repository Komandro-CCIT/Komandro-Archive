# Jawaban

```dart
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:supabase_flutter/supabase_flutter.dart';
import 'dart:convert';
import 'package:crypto/crypto.dart';

void main() async {
  WidgetsFlutterBinding.ensureInitialized();
  await Supabase.initialize(
    url: 'url supabase-mu',
    anonKey:
        'anonKey supabase-mu',
    debug: true,
  );
  runApp(const MyApp());
}

class MyApp extends StatelessWidget {
  const MyApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      debugShowCheckedModeBanner: false,
      title: 'TodoList with Auth',
      theme: ThemeData(primarySwatch: Colors.blue),
      home: const LoginPage(),
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
  final _formKey = GlobalKey<FormState>();

  String _hashPassword(String password) {
    final bytes = utf8.encode(password);
    final digest = sha256.convert(bytes);
    return digest.toString();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(16.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                "Login",
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),
              const SizedBox(
                height: 50,
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                child: TextFormField(
                  controller: _usernameController,
                  decoration: const InputDecoration(
                      labelText: 'Username',
                      contentPadding:
                          EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(3)))),
                  validator: (value) =>
                      value!.isEmpty ? 'Username is required' : null,
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                child: TextFormField(
                  controller: _passwordController,
                  decoration: const InputDecoration(
                      labelText: 'Password',
                      contentPadding:
                          EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(3)))),
                  obscureText: true,
                  validator: (value) =>
                      value!.isEmpty ? 'Password is required' : null,
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                style: const ButtonStyle(
                  backgroundColor:
                      WidgetStatePropertyAll(Color.fromARGB(255, 82, 177, 255)),
                ),
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    final username = _usernameController.text;
                    final password = _hashPassword(_passwordController.text);
                    try {
                      final response = await Supabase.instance.client
                          .from('tbl_user')
                          .select()
                          .eq('username', username)
                          .eq('password', password);

                      if (response.isNotEmpty) {
                        Navigator.pushReplacement(
                          context,
                          MaterialPageRoute(
                            builder: (context) => ChangeNotifierProvider(
                              create: (_) =>
                                  TodoProvider(response[0]['id'].toString()),
                              child: const TodoListPage(),
                            ),
                          ),
                        );
                      } else {
                        ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                                content: Text('Invalid username or password')));
                      }
                    } catch (error) {
                      print(error);
                      ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('Login failed: $error')));
                    }
                  }
                },
                child: const Text(
                  'Login',
                  style: TextStyle(fontSize: 20, color: Colors.black),
                ),
              ),
              TextButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const SignupPage()),
                  );
                },
                child: const Text('Don\'t have an account? Signup'),
              ),
            ],
          ),
        ),
      ),
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
  final _formKey = GlobalKey<FormState>();

  String _hashPassword(String password) {
    final bytes = utf8.encode(password);
    final digest = sha256.convert(bytes);
    return digest.toString();
  }

  Future<bool> _checkUsernameAvailability(String username) async {
    try {
      final response = await Supabase.instance.client
          .from('tbl_user')
          .select('id')
          .eq('username', username);
      return response.isEmpty;
    } catch (error) {
      print('Error checking username availability: $error');
      return false;
    }
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      body: Padding(
        padding: const EdgeInsets.all(8.0),
        child: Form(
          key: _formKey,
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              const Text(
                "Sign Up",
                style: TextStyle(fontSize: 30, fontWeight: FontWeight.bold),
              ),
              const SizedBox(
                height: 50,
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                child: TextFormField(
                  controller: _emailController,
                  decoration: const InputDecoration(
                      labelText: 'Email',
                      contentPadding:
                          EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(3)))),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Email is required';
                    } else if (!value.contains('@gmail.com')) {
                      return 'Email must be a valid Gmail address';
                    }
                    return null;
                  },
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                child: TextFormField(
                  controller: _usernameController,
                  decoration: const InputDecoration(
                      labelText: 'Username',
                      contentPadding:
                          EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(3)))),
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Username is required';
                    } else if (value.length < 3 || value.length > 20) {
                      return 'Username must be between 3 and 20 characters';
                    }
                    return null;
                  },
                ),
              ),
              const SizedBox(
                height: 10,
              ),
              Padding(
                padding:
                    const EdgeInsets.symmetric(horizontal: 10, vertical: 4),
                child: TextFormField(
                  controller: _passwordController,
                  decoration: const InputDecoration(
                      labelText: 'Password',
                      contentPadding:
                          EdgeInsets.symmetric(horizontal: 6, vertical: 3),
                      border: OutlineInputBorder(
                          borderRadius: BorderRadius.all(Radius.circular(3)))),
                  obscureText: true,
                  validator: (value) {
                    if (value!.isEmpty) {
                      return 'Password is required';
                    } else if (value.length < 8) {
                      return 'Password must be at least 8 characters';
                    }
                    return null;
                  },
                ),
              ),
              const SizedBox(height: 20),
              ElevatedButton(
                style: const ButtonStyle(
                    backgroundColor: WidgetStatePropertyAll(
                        Color.fromARGB(255, 82, 177, 255))),
                onPressed: () async {
                  if (_formKey.currentState!.validate()) {
                    final email = _emailController.text;
                    final username = _usernameController.text;
                    final password = _hashPassword(_passwordController.text);
                    try {
                      final isUsernameAvailable =
                          await _checkUsernameAvailability(username);
                      if (!isUsernameAvailable) {
                        ScaffoldMessenger.of(context).showSnackBar(
                            const SnackBar(
                                content: Text('Username already exists')));
                        return;
                      }

                      await Supabase.instance.client.from('tbl_user').insert({
                        'email': email,
                        'username': username,
                        'password': password,
                      });

                      Navigator.pushReplacement(
                        context,
                        MaterialPageRoute(
                          builder: (context) => const LoginPage(),
                        ),
                      );
                    } catch (error) {
                      ScaffoldMessenger.of(context).showSnackBar(
                          SnackBar(content: Text('Signup failed: $error')));
                    }
                  }
                },
                child: const Text(
                  'Signup',
                  style: TextStyle(fontSize: 20, color: Colors.black),
                ),
              ),
              TextButton(
                onPressed: () {
                  Navigator.push(
                    context,
                    MaterialPageRoute(builder: (context) => const LoginPage()),
                  );
                },
                child: const Text('Already have an account? Login'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}

class TodoProvider with ChangeNotifier {
  final String userId;

  TodoProvider(this.userId);

  List<Map<String, dynamic>> _todos = [];
  List<Map<String, dynamic>> get todos => _todos;

  Future<void> fetchTodos() async {
    try {
      final response = await Supabase.instance.client
          .from('tbl_todo')
          .select()
          .eq('user_id', userId);

      _todos = List<Map<String, dynamic>>.from(response);
      notifyListeners();
    } catch (error) {
      throw Exception('Error fetching todos: $error');
    }
  }

  Future<void> addTodo(String body) async {
    try {
      await Supabase.instance.client.from('tbl_todo').insert({
        'user_id': userId,
        'body': body,
      });
      await fetchTodos();
    } catch (error) {
      throw Exception('Error adding todo: $error');
    }
  }

  Future<void> updateTodo(int todoId, String newBody) async {
    try {
      await Supabase.instance.client
          .from('tbl_todo')
          .update({'body': newBody}).eq('id', todoId);
      await fetchTodos();
    } catch (error) {
      throw Exception('Error updating todo: $error');
    }
  }

  Future<void> deleteTodo(int todoId) async {
    try {
      await Supabase.instance.client.from('tbl_todo').delete().eq('id', todoId);
      await fetchTodos();
    } catch (error) {
      throw Exception('Error deleting todo: $error');
    }
  }
}

class TodoListPage extends StatelessWidget {
  const TodoListPage({super.key});

  @override
  Widget build(BuildContext context) {
    final provider = Provider.of<TodoProvider>(context);

    return Scaffold(
      appBar: AppBar(
        automaticallyImplyLeading: false,
        title: const Text('Todo List'),
        centerTitle: true,
        actions: [
          IconButton(
            icon: const Icon(Icons.logout),
            onPressed: () async {
              try {
                await Supabase.instance.client.auth.signOut();
                Navigator.of(context).push(
                  MaterialPageRoute(builder: (context) => const LoginPage()),
                );
              } catch (error) {
                ScaffoldMessenger.of(context).showSnackBar(
                    SnackBar(content: Text('Logout failed: $error')));
              }
            },
          ),
        ],
      ),
      body: RefreshIndicator(
        onRefresh: () => provider.fetchTodos(),
        child: FutureBuilder<void>(
            key: UniqueKey(),
            future: provider.fetchTodos(),
            builder: (context, snapshot) {
              if (provider.todos.isEmpty) {
                return const Center(child: Text("No todo added yet"));
              } else {
                return ListView.builder(
                  itemCount: provider.todos.length,
                  itemBuilder: (context, index) {
                    final todo = provider.todos[index];
                    return Padding(
                      padding: const EdgeInsets.all(7),
                      child: ListTile(
                        tileColor: const Color.fromARGB(255, 232, 224, 224),
                        title: Text(todo['body']),
                        trailing: GestureDetector(
                          onTap: () async {
                            await provider.deleteTodo(todo['id']);
                            await provider.fetchTodos();
                          },
                          child: const Icon(
                            Icons.delete,
                            color: Colors.red,
                            size: 30,
                          ),
                        ),
                        onTap: () async {
                          final newBody = await showDialog<String>(
                            context: context,
                            builder: (context) {
                              final controller =
                                  TextEditingController(text: todo['body']);
                              return AlertDialog(
                                title: const Text('Edit Todo'),
                                content: TextField(
                                  controller: controller,
                                  decoration:
                                      const InputDecoration(labelText: 'Todo'),
                                ),
                                actions: [
                                  TextButton(
                                    onPressed: () => Navigator.pop(context),
                                    child: const Text('Cancel'),
                                  ),
                                  TextButton(
                                    onPressed: () =>
                                        Navigator.pop(context, controller.text),
                                    child: const Text('Save'),
                                  ),
                                ],
                              );
                            },
                          );

                          if (newBody != null) {
                            await provider.updateTodo(todo['id'], newBody);
                            await provider.fetchTodos();
                          }
                        },
                      ),
                    );
                  },
                );
              }
            }),
      ),
      floatingActionButton: FloatingActionButton(
        backgroundColor: const Color.fromARGB(255, 98, 184, 255),
        onPressed: () async {
          final body = await showDialog<String>(
            context: context,
            builder: (context) {
              final controller = TextEditingController();
              return AlertDialog(
                title: const Text('New Todo'),
                content: TextField(
                  controller: controller,
                  decoration: const InputDecoration(labelText: 'Todo'),
                ),
                actions: [
                  TextButton(
                    onPressed: () => Navigator.pop(context),
                    child: const Text('Cancel'),
                  ),
                  TextButton(
                    onPressed: () => Navigator.pop(context, controller.text),
                    child: const Text('Save'),
                  ),
                ],
              );
            },
          );

          if (body != null) {
            await provider.addTodo(body);
            await provider.fetchTodos();
          }
        },
        child: const Icon(Icons.add),
      ),
    );
  }
}
```

## Penjelasan Kode

Kode ini adalah aplikasi Flutter dengan integrasi Supabase untuk autentikasi dan pengelolaan daftar tugas (to-do list). Aplikasi ini memiliki dua halaman utama: halaman login dan halaman pendaftaran. Berikut adalah penjelasan bagian-bagian utama kode:

### Struktur Utama

- `main()`: Fungsi utama yang menginisialisasi Supabase dan menjalankan aplikasi.

- `MyApp`: Widget utama yang mengatur tema dan halaman awal aplikasi.

### Skema Database

- Tabel `tbl_user`
  Tabel ini menyimpan informasi user yang melakukan registrasi pada aplikasi. Berikut adalah skema untuk tabel `tbl_user`:

  ```sql
  CREATE TABLE tbl_user (
  id serial PRIMARY KEY,
  username text NOT NULL UNIQUE,
  email text NOT NULL UNIQUE,
  password text NOT NULL
  );
  ```

  - `id`: Kolom ini merupakan primary key dengan tipe data `serial`, yang berarti nilainya akan secara otomatis bertambah untuk setiap entri baru.

  - `username`: Kolom ini menyimpan username user. Tipe datanya adalah `text` dan harus unik serta tidak boleh kosong (`NOT NULL`).

  - `email`: Kolom ini menyimpan alamat email user. Tipe datanya adalah `text` dan harus unik serta tidak boleh kosong (`NOT NULL`).

  - `password`: Kolom ini menyimpan password user yang sudah di-hash. Tipe datanya adalah `text` dan tidak boleh kosong (`NOT NULL`).

- Tabel `tbl_todo`
  Tabel ini menyimpan todo list yang dibuat oleh user. Berikut adalah skema untuk tabel tbl_todo:

  ```sql
  CREATE TABLE public.tbl_todo (
  id serial PRIMARY KEY,
  user_id integer REFERENCES public.tbl_user(id) ON DELETE CASCADE,
  body text NOT NULL
  );
  ```

  - `id`: Kolom ini merupakan primary key dengan tipe data `serial`, yang berarti nilainya akan secara otomatis bertambah untuk setiap entri baru.

  - `user_id`: Kolom ini merupakan foreign key yang merujuk ke kolom `id` di tabel `tbl_user`. Tipe datanya adalah `integer`. Jika pengguna dihapus, semua to-do yang terkait dengan pengguna tersebut juga akan dihapus (`ON DELETE CASCADE`).

  - `body`: Kolom ini menyimpan isi atau deskripsi dari to-do. Tipe datanya adalah `text` dan tidak boleh kosong (`NOT NULL`).

### Halaman Login

- `LoginPage`: StatefulWidget yang mengatur tampilan dan logika halaman login.

- `_LoginPageState`: State untuk `LoginPage` yang mengelola input user dan proses login.

- `_hashPassword`: Fungsi untuk mengenkripsi password menggunakan SHA-256.

- `onPressed`: Metode yang dipanggil saat tombol login ditekan, memeriksa kredensial user terhadap database Supabase dan navigasi ke halaman daftar tugas jika berhasil.

### Halaman Pendaftaran

- `SignupPage`: StatefulWidget yang mengatur tampilan dan logika halaman pendaftaran.

- `_SignupPageState`: State untuk SignupPage yang mengelola input user dan proses pendaftaran.

- `_hashPassword`: Fungsi untuk mengenkripsi password menggunakan SHA-256.
  \_checkUsernameAvailability: Fungsi untuk memeriksa ketersediaan username di database Supabase.

- `onPressed`: Metode yang dipanggil saat tombol signup ditekan, memeriksa validitas input user, memeriksa ketersediaan username, dan menambahkan user baru ke database Supabase jika valid.

### Todo List Provider

- `TodoProvider`: Penyedia yang mengelola daftar tugas untuk user tertentu.

- `fetchTodos`: Mengambil daftar tugas dari database.

- `addTodo`: Menambahkan tugas baru ke database.

- `updateTodo`: Memperbarui tugas di database.

- `deleteTodo`: Menghapus tugas dari database.

### Halaman Todo List

`TodoListPage`: StatelessWidget yang menampilkan daftar tugas user.

Tidak masalah jika aplikasi yang Anda buat tidak mirip persis seperti ini. Yang terpenting adalah aplikasi yang Anda buat memenuhi kriteria yang telah ditentukan, seperti memiliki fungsi login, pendaftaran, dan pengelolaan daftar tugas dengan integrasi ke Supabase.
