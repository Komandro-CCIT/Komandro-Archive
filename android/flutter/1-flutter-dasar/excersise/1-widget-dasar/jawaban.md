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
      title: 'Flutter Widget Demo',
      theme: ThemeData(
        primarySwatch: Colors.blue,
      ),
      home: Scaffold(
        appBar: AppBar(
          title: Text('Flutter Widget Demo'),
        ),
        body: Center(
          child: Column(
            mainAxisAlignment: MainAxisAlignment.center,
            children: <Widget>[
              Text(
                'Welcome to Flutter',
                style: TextStyle(fontSize: 24),
              ),
              Icon(
                Icons.star,
                color: Colors.yellow,
                size: 48.0,
              ),
              ElevatedButton(
                onPressed: () {
                  print('Button Pressed');
                },
                child: Text('Press Me'),
              ),
            ],
          ),
        ),
      ),
    );
  }
}
```

Penjelasan:

**AppBar**: Menambahkan AppBar dengan judul "Flutter Widget Demo".

**Column**: Mengatur widget anak dalam susunan vertikal.

**Text**: Menampilkan teks "Welcome to Flutter" dengan ukuran font 24.

**Icon**: Menampilkan ikon bintang berwarna kuning dengan ukuran 48 piksel.

**ElevatedButton**: Menampilkan tombol dengan teks "Press Me". Ketika tombol ditekan, pesan "Button Pressed" akan dicetak di console.