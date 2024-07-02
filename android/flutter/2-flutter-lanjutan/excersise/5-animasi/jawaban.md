# Jawaban

```dart
import 'package:flutter/material.dart';

void main() => runApp(MyApp());

class MyApp extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(title: Text('Multiple Animations Example')),
        body: AnimationExample(),
      ),
    );
  }
}

class AnimationExample extends StatefulWidget {
  @override
  _AnimationExampleState createState() => _AnimationExampleState();
}

class _AnimationExampleState extends State<AnimationExample> {
  bool _isExpanded = false;
  bool _isVisible = true;

  void _toggleContainerAnimation() {
    setState(() {
      _isExpanded = !_isExpanded;
    });
  }

  void _toggleOpacityAnimation() {
    setState(() {
      _isVisible = !_isVisible;
    });
  }

  @override
  Widget build(BuildContext context) {
    return Column(
      mainAxisAlignment: MainAxisAlignment.center,
      children: [
        AnimatedContainer(
          duration: Duration(seconds: 1),
          width: _isExpanded ? 200 : 100,
          height: _isExpanded ? 200 : 100,
          color: _isExpanded ? Colors.blue : Colors.red,
          alignment: Alignment.center,
          child: Text('Animated Container', style: TextStyle(color: Colors.white)),
        ),
        SizedBox(height: 20),
        ElevatedButton(
          onPressed: _toggleContainerAnimation,
          child: Text('Toggle Container Animation'),
        ),
        SizedBox(height: 40),
        AnimatedOpacity(
          opacity: _isVisible ? 1.0 : 0.0,
          duration: Duration(seconds: 1),
          child: Container(
            width: 200,
            height: 200,
            color: Colors.green,
            alignment: Alignment.center,
            child: Text('Animated Opacity', style: TextStyle(color: Colors.white)),
          ),
        ),
        SizedBox(height: 20),
        ElevatedButton(
          onPressed: _toggleOpacityAnimation,
          child: Text('Toggle Opacity Animation'),
        ),
      ],
    );
  }
}
```
### Penjelasan:

1. Main Widget:

    - `MyApp` adalah widget utama yang menjalankan aplikasi dan menampilkan `AnimationExample` di dalam Scaffold dengan AppBar.

2. Stateful Widget:

    - `AnimationExample` adalah Stateful widget yang mengelola dua animasi terpisah: satu untuk `AnimatedContainer` dan satu lagi untuk `AnimatedOpacity`.

3. State Management:

    - Dua boolean `_isExpanded` dan `_isVisible` digunakan untuk mengontrol status animasi.

    - Metode `_toggleContainerAnimation` dan `_toggleOpacityAnimation` masing-masing mengubah nilai `_isExpanded` dan `_isVisible` untuk memicu animasi.

4. UI Layout:
    - `AnimatedContainer` dan `AnimatedOpacity` digunakan untuk menampilkan animasi.

    - Dua tombol `ElevatedButton` digunakan untuk mengaktifkan animasi pada masing-masing widget.