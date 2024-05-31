# Object-Oriented Programming

OOP atau Pemrograman Berorientasi Objek adalah paradigma pemrograman yang menggunakan objek sebagai unit dasar untuk membangun program. Setiap objek memiliki atribut (data) dan metode (fungsi) yang berinteraksi satu sama lain. 

Berikut adalah konsep-konsep penting yang ada dalam OOP : 
# Kelas dan Objek

Kelas adalah blueprint atau cetak biru untuk objek. Kelas mendefinisikan atribut (properties) dan metode (methods) yang dimiliki oleh objek. Objek adalah instance dari kelas, artinya objek dibuat berdasarkan blueprint dari kelas.

```dart
class Animal {
  String name;
  int age;

  Animal(this.name, this.age);

  void makeSound() {
    print('$name makes a sound.');
  }
}

void main() {
  Animal cat = Animal('Cat', 3);
  print('${cat.name} is ${cat.age} years old.');
  cat.makeSound();
}
```
Di atas, kita mendefinisikan kelas `Animal` dengan dua atribut `name` dan `age`, serta satu metode `makeSound`. Kemudian, kita membuat objek `cat` dari kelas `Animal` dan menggunakan atribut dan metodenya.

### Named Parameters
Named parameters adalah cara untuk memberikan nilai pada parameter dengan menyebutkan nama parameternya. Ini membuat kode lebih mudah dibaca dan mengurangi kemungkinan kesalahan saat mengatur nilai pada parameter. Named parameters didefinisikan dengan menggunakan `{}` dalam deklarasi konstruktor atau metode

### Contoh penggunaan named parameters dalam kelas
```dart 
class Animal {
  String name;
  int age;

  Animal({required this.name, required this.age});

  void makeSound() {
    print('$name makes a sound.');
  }
}

void main() {
  Animal cat = Animal(name: 'Cat', age: 3);
  print('${cat.name} is ${cat.age} years old.');
  cat.makeSound();
}
```

Dalam contoh di atas, konstruktor `Animal` menggunakan named parameters untuk `name` dan `age`. Ketika membuat objek `cat`, kita menyebutkan nama parameternya (`name: 'Cat'` dan `age: 3`). Hal ini meningkatkan kejelasan dan keterbacaan kode, terutama ketika kelas memiliki banyak parameter.

### Mengapa mengunakan Named Parameter?
- **Keterbacaan**: 
<br/>
  Named parameters membuat kode lebih mudah dibaca karena jelas parameter mana yang diberikan nilai.

- **Urutan Tidak Penting**:
<br/>
  Urutan pemberian nilai tidak penting, sehingga lebih fleksibel dalam penggunaan.

- **Parameter Opsional**:
<br/>
  Named parameters dapat diberi nilai default atau ditandai sebagai opsional, sehingga tidak semua parameter harus diberikan nilai setiap kali objek dibuat.

### Contoh penggunaan named parameters dengan nilai default dan parameter opsional
```dart
class Animal {
  String name;
  int age;
  String sound;

  Animal({required this.name, required this.age, this.sound = 'makes a sound'});

  void makeSound() {
    print('$name $sound.');
  }
}

void main() {
  Animal cat = Animal(name: 'Cat', age: 3);
  Animal dog = Animal(name: 'Dog', age: 5, sound: 'barks');
  
  print('${cat.name} is ${cat.age} years old.');
  cat.makeSound();

  print('${dog.name} is ${dog.age} years old.');
  dog.makeSound();
}
```
Dalam contoh ini, `sound` adalah parameter opsional dengan nilai default `makes a sound`. Saat membuat objek `cat`, kita tidak memberikan nilai untuk `sound`, sehingga nilai default digunakan. Untuk objek `dog`, kita memberikan nilai `barks` untuk `sound`.

### Penggunaan Named Parameters dalam Flutter
Saat Anda mulai membuat aplikasi dengan Flutter, Anda akan sering menemukan penggunaan named parameters. Flutter memanfaatkan named parameters secara ekstensif untuk meningkatkan keterbacaan dan kemudahan dalam menulis kode UI. Sebagai contoh, banyak widget di Flutter menggunakan named parameters untuk menerima berbagai konfigurasi dan properti, seperti `padding`, `margin`, `child`, `color`, dan sebagainya. Anda akan melihatnya nanti di materi Flutter.

# Inheritance (Pewarisan)
Inheritance adalah mekanisme di mana sebuah kelas dapat mewarisi properti dan metode dari kelas lain. Kelas yang mewarisi disebut subclass, dan kelas yang diwarisi disebut superclass.

```dart
class Animal {
  String name;

  Animal(this.name);

  void makeSound() {
    print('$name makes a sound.');
  }
}

class Dog extends Animal {
  Dog(String name) : super(name);

  void bark() {
    print('$name barks.');
  }
}

void main() {
  Dog dog = Dog('Buddy');
  dog.makeSound(); // Memanggil metode dari superclass
  dog.bark(); // Memanggil metode dari subclass
}
```
Di atas, kelas `Dog` mewarisi dari kelas `Animal` dan menambahkan metode `bark`. Kita dapat menggunakan atribut dan metode dari superclass dan subclass.

# Abstraction (abstraksi)

Abstraksi adalah konsep dalam pemrograman berorientasi objek (OOP) yang digunakan untuk menyembunyikan detail implementasi internal dari sebuah objek dan hanya menampilkan fungsionalitas yang relevan kepada pengguna. Tujuan utama dari abstraksi adalah untuk mengurangi kompleksitas dan meningkatkan efisiensi dalam pengembangan perangkat lunak.

- ### Kelas Abstrak (`abstract class`)

  Dalam Dart, kelas abstrak (`abstract class`) digunakan untuk mendefinisikan kelas yang tidak dapat diinstansiasi langsung. Kelas abstrak dapat memiliki metode dengan atau tanpa implementasi. Kelas ini biasanya digunakan sebagai dasar untuk kelas-kelas lain yang mewarisinya dan menyediakan implementasi untuk metode-metode abstrak tersebut.


  ```dart
  // Definisikan kelas abstrak
  abstract class Animal {
    void makeSound(); // Metode abstrak
    void eat() {
      // Metode dengan implementasi
      print('Animal eats.');
    }
  }

  // Kelas Cat mengextends kelas abstrak Animal
  class Cat extends Animal {
    @override
    void makeSound() {
      print('Cat meows.');
    }
  }

  // Kelas Dog mengextends kelas abstrak Animal
  class Dog extends Animal {
    @override
    void makeSound() {
      print('Dog barks.');
    }
  }

  void main() {
    Cat cat = Cat();
    Dog dog = Dog();

    cat.makeSound();
    cat.eat();

    dog.makeSound();
    dog.eat();
  }
  ```
  Di atas, kita mendefinisikan sebuah kelas abstrak `Animal` dengan metode abstrak `makeSound` dan metode dengan implementasi `eat`. Kelas `Cat` dan `Dog` mengextends kelas abstrak `Animal` dan menyediakan implementasi untuk metode `makeSound`. Dalam fungsi main, kita membuat objek `Cat` dan `Dog`, lalu memanggil metode `makeSound` dan `eat` pada masing-masing objek.

  #### Keuntungan Menggunakan Kelas Abstrak
  Dengan menggunakan kelas abstrak, kita dapat membuat struktur dasar untuk kelas-kelas lain tanpa harus menyediakan implementasi lengkap. Ini memaksa kelas turunan untuk menyediakan implementasi mereka sendiri untuk metode-metode abstrak, memastikan bahwa setiap kelas turunan memenuhi kontrak yang ditentukan oleh kelas abstrak.

  Kelas abstrak membantu dalam desain dan pengorganisasian kode, memungkinkan pemisahan tanggung jawab dengan jelas. Mereka juga menyediakan cara untuk mendefinisikan perilaku yang harus diikuti oleh kelas-kelas turunan, memudahkan pemeliharaan dan pengembangan aplikasi yang lebih besar.

- ### `dart implements`

  Dalam Dart, keyword `implements` digunakan untuk menunjukkan bahwa sebuah kelas harus memenuhi kontrak yang ditentukan oleh satu atau lebih antarmuka (interfaces). Antarmuka adalah kelas abstrak yang mendefinisikan metode tanpa implementasi. Kelas yang mengimplementasikan antarmuka harus menyediakan implementasi dari semua metode yang didefinisikan dalam antarmuka tersebut.

  ```dart
  // Definisikan antarmuka
  abstract class Animal {
    void makeSound();
    void eat();
  }

  // Kelas Cat mengimplementasikan antarmuka Animal
  class Cat implements Animal {
    @override
    void makeSound() {
      print('Cat meows.');
    }

    @override
    void eat() {
      print('Cat eats.');
    }
  }

  // Kelas Dog mengimplementasikan antarmuka Animal
  class Dog implements Animal {
    @override
    void makeSound() {
      print('Dog barks.');
    }

    @override
    void eat() {
      print('Dog eats.');
    }
  }

  void main() {
    Cat cat = Cat();
    Dog dog = Dog();

    cat.makeSound();
    cat.eat();

    dog.makeSound();
    dog.eat();
  }
  ```
  Di atas, kita mendefinisikan sebuah antarmuka `Animal` dengan dua metode `makeSound` dan `eat`. Kelas `Cat` dan `Dog` mengimplementasikan antarmuka `Animal` dan menyediakan implementasi untuk kedua metode tersebut. Dalam fungsi `main`, kita membuat objek `Cat` dan `Dog`, lalu memanggil metode `makeSound` dan `eat` pada masing-masing objek.

  #### Keuntungan Menggunakan implements
  Dengan menggunakan keyword `implements`, kita dapat memastikan bahwa kelas-kelas yang berbeda memenuhi kontrak yang sama, yang membuat kode lebih konsisten dan dapat diandalkan. Ini juga memudahkan pengembang untuk memahami dan menggunakan kelas-kelas tersebut karena mereka tahu bahwa semua kelas yang mengimplementasikan antarmuka tertentu akan memiliki metode yang sama.

#### Perbedaan Antara `abstract class` dan `interface`
Meskipun keduanya dapat digunakan untuk mendefinisikan kontrak yang harus diikuti oleh kelas-kelas lain, ada beberapa perbedaan penting antara `abstract class` dan `interface`:

- **Kelas abstrak** : Dapat memiliki metode dengan implementasi dan variabel instance. Kelas hanya dapat mengextends satu kelas abstrak.

- **Interface**: Hanya dapat mendefinisikan metode tanpa implementasi. Kelas dapat mengimplementasikan beberapa antarmuka.
Kita menggunakan kelas abstrak ketika kita ingin menyediakan beberapa implementasi dasar dan memaksa kelas turunan untuk mengimplementasikan metode tertentu. Di sisi lain, kita menggunakan antarmuka ketika kita ingin mendefinisikan kontrak tanpa menyediakan implementasi apa pun, memungkinkan fleksibilitas yang lebih besar dengan mengimplementasikan beberapa antarmuka.

Penggunaan antarmuka dan keyword `implements` juga memungkinkan pemisahan antara deklarasi dan implementasi, yang membantu dalam pemeliharaan kode dan memungkinkan penggantian atau perubahan implementasi tanpa mengubah antarmuka publik.


# Polimorphism (Polimorfisme) 

Polimorfisme adalah konsep dalam pemrograman berorientasi objek (OOP) yang memungkinkan objek dari kelas yang berbeda untuk diperlakukan sebagai objek dari kelas yang sama melalui antarmuka atau kelas dasar yang sama. Polimorfisme memungkinkan metode yang sama untuk digunakan pada objek yang berbeda, yang dapat memiliki perilaku yang berbeda berdasarkan implementasi spesifik mereka.

```dart
// Definisikan kelas abstrak
abstract class Animal {
  void makeSound();
}

// Kelas Dog mengextends kelas abstrak Animal
class Dog extends Animal {
  @override
  void makeSound() {
    print('Bark');
  }
}

// Kelas Cat mengextends kelas abstrak Animal
class Cat extends Animal {
  @override
  void makeSound() {
    print('Meow');
  }
}

// Kelas Cow mengextends kelas abstrak Animal
class Cow extends Animal {
  @override
  void makeSound() {
    print('Moo');
  }
}

void main() {
  // Membuat objek dari kelas Dog, Cat, dan Cow
  Animal dog = Dog();
  Animal cat = Cat();
  Animal cow = Cow();

  // Menggunakan polimorfisme untuk memanggil metode makeSound pada setiap objek
  dog.makeSound();
  cat.makeSound();
  cow.makeSound();
}
```
Di atas, kita mendefinisikan sebuah kelas abstrak `Animal` dengan metode abstrak `makeSound`. Kelas `Dog`, `Cat`, dan `Cow` mengextends kelas `Animal` dan menyediakan implementasi untuk metode `makeSound`. Dalam fungsi `main`, kita membuat objek `Dog`, `Cat`, dan `Cow`, lalu menggunakan polimorfisme untuk memanggil metode `makeSound` pada setiap objek.

Polimorfisme memungkinkan objek dari kelas yang berbeda untuk diperlakukan sebagai objek dari kelas yang sama.

# Enscapculation (Enkapkulasi)
Enkapsulasi adalah konsep dalam pemrograman berorientasi objek (OOP) yang menyembunyikan detail implementasi internal dari suatu objek dan hanya menyediakan antarmuka yang terbatas untuk berinteraksi dengan objek tersebut. Enkapsulasi memastikan bahwa data dalam suatu objek hanya dapat diubah melalui metode yang ditentukan, sehingga menjaga integritas dan konsistensi data.

```dart
class Person {
  // Properti privat
  String _name;
  int _age;

  // Konstruktor
  Person(this._name, this._age);

  // Metode getter untuk properti name
  String get name => _name;

  // Metode setter untuk properti name
  set name(String name) {
    if (name.isNotEmpty) {
      _name = name;
    } else {
      print('Name cannot be empty');
    }
  }

  // Metode getter untuk properti age
  int get age => _age;

  // Metode setter untuk properti age
  set age(int age) {
    if (age > 0) {
      _age = age;
    } else {
      print('Age must be positive');
    }
  }

  // Metode untuk menampilkan informasi person
  void displayInfo() {
    print('Name: $_name, Age: $_age');
  }
}

void main() {
  // Membuat objek dari kelas Person
  Person person = Person('Leman', 19);

  // Menampilkan informasi person
  person.displayInfo();

  // Mengubah properti name menggunakan metode setter
  person.name = 'Sulaiman';

  // Mengubah properti age menggunakan metode setter
  person.age = 25;

  // Menampilkan informasi person setelah perubahan
  person.displayInfo();
}
```
Di atas, kita mendefinisikan kelas `Person` dengan dua properti privat (`_name` dan `_age`). Properti ini hanya dapat diakses dan diubah melalui metode getter dan setter yang telah ditentukan. Metode getter mengembalikan nilai properti, sedangkan metode setter memvalidasi dan mengubah nilai properti.

Enkapsulasi memastikan bahwa data dalam suatu objek hanya dapat diubah melalui metode yang ditentukan.

