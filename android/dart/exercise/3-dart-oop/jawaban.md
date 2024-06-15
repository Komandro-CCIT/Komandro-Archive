# Soal 1: Penerapan Inheritance dan Polimorfisme
```dart
abstract class Shape {
  double area();
}

class Circle extends Shape {
  double radius;

  Circle(this.radius);

  @override
  double area() {
    return 3.14 * radius * radius;
  }
}

class Rectangle extends Shape {
  double width;
  double height;

  Rectangle(this.width, this.height);

  @override
  double area() {
    return width * height;
  }
}

void main() {
  Shape circle = Circle(5);
  Shape rectangle = Rectangle(4, 6);

  print('Luas lingkaran: ${circle.area()}');
  print('Luas persegi panjang: ${rectangle.area()}');
}
```

### Penjelasan:

- `Shape` adalah kelas abstrak dengan metode abstrak `area()`.

- `Circle` dan `Rectangle` adalah kelas yang mengimplementasikan `Shape` dan menyediakan implementasi untuk metode area().

- Dalam fungsi `main()`, objek `circle` dan `rectangle` dibuat, dan luasnya dihitung menggunakan polimorfisme.

# Soal 2: Penerapan Encapsulation dan Named Parameters
```dart
class Employee {
  String _name;
  int _age;
  String _position;

  Employee({required String name, required int age, required String position})
      : _name = name,
        _age = age,
        _position = position;

  String get name => _name;

  set name(String name) {
    if (name.isNotEmpty) {
      _name = name;
    } else {
      print('Name cannot be empty');
    }
  }

  int get age => _age;

  set age(int age) {
    if (age > 0) {
      _age = age;
    } else {
      print('Age must be positive');
    }
  }

  String get position => _position;

  set position(String position) {
    if (position.isNotEmpty) {
      _position = position;
    } else {
      print('Position cannot be empty');
    }
  }

  void displayInfo() {
    print('Name: $_name, Age: $_age, Position: $_position');
  }
}

void main() {
  Employee employee = Employee(name: 'John Doe', age: 30, position: 'Manager');

  employee.displayInfo();

  employee.name = 'Jane Doe';
  employee.age = 28;
  employee.position = 'Senior Manager';

  employee.displayInfo();
}
```

### Penjelasan:

- `Employee` adalah kelas dengan properti privat `_name`, `_age`, dan `_position`.

- Konstruktor `Employee` menggunakan named parameters untuk menginisialisasi properti.

- Getter dan setter disediakan untuk setiap properti, dengan validasi untuk `age` dan `position`.

- Metode `displayInfo()` digunakan untuk menampilkan informasi karyawan.

- Dalam fungsi `main()`, objek `Employee` dibuat, dan getter serta setter digunakan untuk mengakses dan mengubah properti, lalu `displayInfo()` dipanggil untuk menampilkan informasi yang diperbarui.

