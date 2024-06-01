# Jawaban
```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('To-Do List')),
        body: ToDoList(),
      ),
    );
  }
}

class ToDoList extends StatelessWidget {
  final List<String> tasks = [
    'Belajar Flutter',
    'Membaca dokumentasi Flutter',
    'Mengerjakan proyek Flutter',
    'Mengikuti kursus online Flutter',
  ];

  @override
  Widget build(BuildContext context) {
    return ListView.builder(
      itemCount: tasks.length,
      itemBuilder: (context, index) {
        return Padding(
          padding: const EdgeInsets.all(8.0),
          child: ListTile(
            leading: Icon(Icons.check_circle_outline),
            title: Text(tasks[index]),
          ),
        );
      },
    );
  }
}
```
### Penjelasan:

- `MyApp` adalah kelas utama aplikasi yang menggunakan `MaterialApp` dan menampilkan `ToDoList` di dalam `Scaffold`.

- `ToDoList` adalah kelas yang menampilkan daftar tugas menggunakan `ListView.builder`.

- `ListView.builder` digunakan untuk membuat daftar tugas dengan jumlah item yang dinamis sesuai dengan panjang daftar `tasks`.

- `Padding` digunakan di sekitar setiap `ListTile` untuk memberikan jarak 8 piksel di semua sisi, sehingga item tidak saling berhimpitan.

- Setiap `ListTile` menampilkan ikon centang di sebelah kiri (`leading: Icon(Icons.check_circle_outline)`) dan teks deskripsi tugas di sebelah kanan (`title: Text(tasks[index])`).