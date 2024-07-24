# Jawaban 

<br/>

# Soal 1: Supabase
```dart
import 'package:supabase_flutter/supabase_flutter.dart';

final supabaseUrl = '(URL supabase-mu)';


final publicAnonKey = '(AnonKey-mu)';

final client = SupabaseClient(supabaseUrl, publicAnonKey);

Future<void> readElectronicsData() async {
  try {

    final response = await client
        .from('products')
        .select().eq('category', 'electronics');
        

    print('Data: ${response}');
  } catch (error) {
    print('Error fetching data: ${error}');
  } 
}



void main() async {
  await readElectronicsData();
}
```
### Penjelasan:

- `SupabaseClient` diinisialisasi dengan URL proyek dan kunci publik anonim.

- Fungsi `readElectronicsData` digunakan untuk mengambil data dari tabel `products` dengan kondisi di mana kolom `category` bernilai 'electronics'.

- Fungsi `eq` digunakan untuk menyaring data berdasarkan kolom `category`.

- Jika tidak ada kesalahan (`catch (error)`), data elektronik yang diambil akan dicetak. Jika ada kesalahan, pesan kesalahan akan dicetak.

# Soal 2: Hive
```dart
import 'package:flutter/material.dart';
import 'package:hive/hive.dart';
import 'package:hive_flutter/hive_flutter.dart';

void main() async {
  await Hive.initFlutter();
  var box = await Hive.openBox('userBox');

  // Create
 await createUser(box, 'user1', {'name': 'John Doe', 'email': 'john@example.com'});
  
  // Read
 await readUser(box, 'user1');
  
  // Update
 await updateUser(box, 'user1', {'name': 'John Smith', 'email': 'johnsmith@example.com'});
  
  // Delete
 await deleteUser(box, 'user1');
}

Future<void> createUser(Box box, String userId, Map<String, String> user) async {
  await box.put(userId, user);
  print('User created: ${box.get(userId)}');
}

Future<void> readUser(Box box, String userId) async {
  var user = box.get(userId);
  print('User read: $user');
}

Future<void> updateUser(Box box, String userId, Map<String, String> updatedUser) async {
  await box.put(userId, updatedUser);
  print('User updated: ${box.get(userId)}');
}

Future<void> deleteUser(Box box, String userId) async {
  await box.delete(userId);
  print('User deleted: ${box.get(userId)}'); // should print null
}
```

### Penjelasan:

- Hive diinisialisasi menggunakan `Hive.initFlutter()` dan membuka box dengan nama `"userBox"`.

- Fungsi `createUser` menyimpan data pengguna dengan `userId` sebagai kunci utama. Data pengguna disimpan dalam bentuk Map.

- Fungsi `readUser` mengambil data pengguna berdasarkan `userId` dan mencetaknya.

- Fungsi `updateUser` memperbarui data pengguna dengan `userId` tertentu.

- Fungsi `deleteUser` menghapus data pengguna berdasarkan `userId` dan memastikan data tersebut telah dihapus dengan mencetak hasilnya.