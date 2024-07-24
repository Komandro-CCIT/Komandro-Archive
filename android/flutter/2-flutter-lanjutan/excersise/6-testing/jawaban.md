# Jawaban

### 1. Buat Aplikasi Flutter dengan Dua Halaman
- `main.dart`

    ```dart
    import 'package:flutter/material.dart';

    void main() {
    runApp(MyApp());
    }

    class MyApp extends StatelessWidget {
    @override
    Widget build(BuildContext context) {
        return MaterialApp(
        home: HomePage(),
        );
    }
    }

    class HomePage extends StatefulWidget {
    @override
    _HomePageState createState() => _HomePageState();
    }

    class _HomePageState extends State<HomePage> {
    final TextEditingController _controller = TextEditingController();

    @override
    Widget build(BuildContext context) {
        return Scaffold(
        appBar: AppBar(title: Text('Home Page')),
        body: Padding(
            padding: const EdgeInsets.all(16.0),
            child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: [
                TextField(
                controller: _controller,
                decoration: InputDecoration(labelText: 'Enter text'),
                ),
                SizedBox(height: 20),
                ElevatedButton(
                onPressed: () {
                    Navigator.push(
                    context,
                    MaterialPageRoute(
                        builder: (context) => SecondPage(text: _controller.text),
                    ),
                    );
                },
                child: Text('Go to Second Page'),
                ),
            ],
            ),
        ),
        );
    }
    }

    class SecondPage extends StatelessWidget {
    final String text;

    SecondPage({required this.text});

    @override
    Widget build(BuildContext context) {
        return Scaffold(
        appBar: AppBar(title: Text('Second Page')),
        body: Center(
            child: Text(text),
        ),
        );
    }
    }
    ```
### 2. Buat Pengujian Integrasi
- Buat file bernama `app_test.dart` di dalam direktori `integration_test`.

    ```dart
    import 'package:flutter/material.dart';
    import 'package:flutter_application_1/main.dart';
    import 'package:flutter_test/flutter_test.dart';
    import 'package:integration_test/integration_test.dart'; // Ganti dengan path yang sesuai

    void main() {
    IntegrationTestWidgetsFlutterBinding.ensureInitialized();

    testWidgets('Text is passed from HomePage to SecondPage', (WidgetTester tester) async {
        await tester.pumpWidget(MyApp());

        // Cari TextField dan ElevatedButton di HomePage
        final textField = find.byType(TextField);
        final button = find.byType(ElevatedButton);

        // Masukkan teks ke dalam TextField
        await tester.enterText(textField, 'Hello, Flutter!');
        await tester.tap(button);
        await tester.pumpAndSettle();

        // Cari teks di SecondPage
        expect(find.text('Hello, Flutter!'), findsOneWidget);
    });
    }
    ```
### 3. Menjalankan Pengujian Integrasi
Untuk menjalankan pengujian integrasi, gunakan perintah berikut di terminal:
```sh
flutter test integration_test/app_test.dart
```

### Penjelasan:

1. `main.dart`:

    - HomePage memiliki TextField dan ElevatedButton.

    - Ketika ElevatedButton ditekan, aplikasi akan menavigasi ke SecondPage dan mengirimkan teks dari TextField.

2. `app_test.dart`:

    - Pengujian ini memeriksa apakah teks yang dimasukkan di `TextField` di `HomePage` ditampilkan dengan benar di `SecondPage`.

    - `IntegrationTestWidgetsFlutterBinding.ensureInitialized()` menginisialisasi binding untuk pengujian integrasi.

    - `enterText` digunakan untuk memasukkan teks ke dalam `TextField`.

    - `tap` digunakan untuk menekan tombol `ElevatedButton`.

    - `pumpAndSettle()` menunggu hingga semua animasi dan transisi selesai.

    - `expect` digunakan untuk memverifikasi bahwa teks yang dimasukkan di `TextField` muncul di `SecondPage`.
        