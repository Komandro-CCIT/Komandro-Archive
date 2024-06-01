# Soal 1: Penerapan Generic dan Koleksi dalam Dart

```dart
class Stack<T> {
  List<T> _elements = [];

  void push(T element) {
    _elements.add(element);
  }

  T pop() {
    if (_elements.isNotEmpty) {
      return _elements.removeLast();
    } else {
      throw Exception('Stack is empty');
    }
  }

  T peek() {
    if (_elements.isNotEmpty) {
      return _elements.last;
    } else {
      throw Exception('Stack is empty');
    }
  }

  bool get isEmpty => _elements.isEmpty;

  int get size => _elements.length;
}

void main() {
  // Stack dengan tipe data int
  Stack<int> intStack = Stack<int>();
  intStack.push(1);
  intStack.push(2);
  intStack.push(3);
  print('Top element of intStack: ${intStack.peek()}'); // Output: 3
  print('Popped element from intStack: ${intStack.pop()}'); // Output: 3
  print('Top element of intStack after pop: ${intStack.peek()}'); // Output: 2

  // Stack dengan tipe data String
  Stack<String> stringStack = Stack<String>();
  stringStack.push('Hello');
  stringStack.push('World');
  print('Top element of stringStack: ${stringStack.peek()}'); // Output: World
  print('Popped element from stringStack: ${stringStack.pop()}'); // Output: World
  print('Top element of stringStack after pop: ${stringStack.peek()}'); // Output: Hello

  // Stack dengan tipe data double
  Stack<double> doubleStack = Stack<double>();
  doubleStack.push(1.1);
  doubleStack.push(2.2);
  doubleStack.push(3.3);
  print('Top element of doubleStack: ${doubleStack.peek()}'); // Output: 3.3
  print('Popped element from doubleStack: ${doubleStack.pop()}'); // Output: 3.3
  print('Top element of doubleStack after pop: ${doubleStack.peek()}'); // Output: 2.2
}
```

### Penjelasan:

- Kelas `Stack<T>` menggunakan generic untuk dapat menyimpan elemen dengan tipe data apa pun.

- Menggunakan `List<T>` untuk menyimpan elemen stack.

- Metode `push()` menambahkan elemen ke stack.

- Metode `pop()` menghapus elemen teratas dari stack dan mengembalikannya. Jika stack kosong, akan melempar exception.

- Metode `peek()` melihat elemen teratas dari stack tanpa menghapusnya. Jika stack kosong, akan melempar exception.

- Dalam fungsi `main()`, instance dari `Stack` dibuat dengan berbagai tipe data (`int`, `String`, `double`), dan operasi dasar pada stack dilakukan.

# Soal 2: Penerapan Asynchronous Programming dalam Dart
```dart
import 'dart:async';

Future<String> fetchDataFromServer() async {
  print('Mengambil data dari server...');
  return Future.delayed(Duration(seconds: 2), () {
    return 'Data dari server';
  });
}

Future<String> processData(String data) async {
  print('Memproses data...');
  return Future.delayed(Duration(seconds: 1), () {
    return 'Data yang telah diproses: $data';
  });
}

void main() async {
  try {
    String data = await fetchDataFromServer();
    print('Data diterima: $data');
    
    String processedData = await processData(data);
    print(processedData);
  } catch (e) {
    print('Terjadi kesalahan: $e');
  } finally {
    print('Operasi asinkron selesai');
  }
}
```
### Penjelasan:

- Fungsi `fetchDataFromServer()` menggunakan `Future.delayed()` untuk mensimulasikan pengambilan data dari server dengan delay 2 detik.

- Fungsi `processData()` menggunakan `Future.delayed()` untuk mensimulasikan pemrosesan data dengan delay 1 detik, dan mengembalikan hasil pemrosesan sebagai `String`.

- Dalam fungsi `main()`, `fetchDataFromServer()` dipanggil dengan `await` untuk menunggu hasilnya sebelum melanjutkan eksekusi. Hasilnya disimpan dalam variabel `data`.

- `processData(data)` dipanggil dengan `await` untuk memproses data yang diterima dari server. Hasil pemrosesan disimpan dalam variabel `processedData`.

- Blok `try-catch` digunakan untuk menangani kemungkinan kesalahan selama operasi asinkron.

- Blok `finally` dieksekusi setelah operasi selesai, terlepas dari apakah ada kesalahan atau tidak.