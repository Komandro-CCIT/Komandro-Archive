# Jawaban
```dart
import 'package:flutter/material.dart';

void main() {
  runApp(MyApp());
}

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      initialRoute: '/',
      routes: {
        '/': (context) => HomeScreen(),
        '/about': (context) => AboutScreen(),
        '/contact': (context) => ContactScreen(),
      },
    );
  }
}

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Home Screen'),
      ),
      body: Center(
        child: Column(
          mainAxisAlignment: MainAxisAlignment.center,
          children: [
            ElevatedButton(
              onPressed: () {
                // Navigasi ke halaman About
                Navigator.pushNamed(context, '/about');
              },
              child: Text('Go to About Screen'),
            ),
            SizedBox(height: 20),
            ElevatedButton(
              onPressed: () {
                // Navigasi ke halaman Contact
                Navigator.pushNamed(context, '/contact');
              },
              child: Text('Go to Contact Screen'),
            ),
          ],
        ),
      ),
    );
  }
}

class AboutScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('About Screen'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Kembali ke halaman Home
            Navigator.pop(context);
          },
          child: Text('Go back to Home Screen'),
        ),
      ),
    );
  }
}

class ContactScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text('Contact Screen'),
      ),
      body: Center(
        child: ElevatedButton(
          onPressed: () {
            // Kembali ke halaman Home
            Navigator.pop(context);
          },
          child: Text('Go back to Home Screen'),
        ),
      ),
    );
  }
}
```

### Penjelasan

- `MyApp` adalah kelas utama aplikasi yang menggunakan `MaterialApp` dan mendefinisikan rute-rute aplikasi.

- `HomeScreen`, `AboutScreen`, dan `ContactScreen` adalah layar-layar aplikasi dengan masing-masing memiliki tombol untuk navigasi.

- Di `HomeScreen`, terdapat dua tombol yang menggunakan Navigator.pushNamed untuk berpindah ke `AboutScreen` dan `ContactScreen`.

- Di `AboutScreen` dan `ContactScreen`, terdapat tombol yang menggunakan `Navigator.pop` untuk kembali ke `HomeScreen`.