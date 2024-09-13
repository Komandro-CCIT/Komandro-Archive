# Modul CRUD dengan PHP dan MySQL
# Pendahuluan
Modul ini akan membahas bagaimana membuat aplikasi CRUD (Create, Read, Update, Delete) sederhana menggunakan PHP dan MySQL. Kita akan membuat aplikasi untuk mengelola data mahasiswa, termasuk menambahkan, menampilkan, mengedit, dan menghapus data.

# Membuat Database dan Tabel

1. Membuat Database
Pertama, kita perlu membuat database untuk menyimpan data mahasiswa, beri nama database, misalnya `universitas`, dan klik `Create`.

2. Membuat Tabel mahasiswa
Setelah database dibuat, kita perlu membuat tabel untuk menyimpan data mahasiswa.

```sql
CREATE TABLE mahasiswa (
    id INT AUTO_INCREMENT PRIMARY KEY,
    nim VARCHAR(20) NOT NULL,
    nama VARCHAR(100) NOT NULL,
    alamat VARCHAR(255),
    fakultas VARCHAR(50)
);
```

# Koneksi ke Database
Langkah pertama dalam file index.php adalah membuat koneksi ke database.

```php
<?php
// Koneksi ke Database
$host       = "localhost"; // Nama host
$user       = "root";      // Username database
$pass       = "";          // Password database (kosong jika default)
$db         = "universitas"; // Nama database

$koneksi    = mysqli_connect($host, $user, $pass, $db);
if (!$koneksi) { // Jika gagal koneksi
    die("Tidak bisa terkoneksi ke database: " . mysqli_connect_error());
}
?>
```

Menggunakan mysqli_connect() untuk menghubungkan PHP dengan MySQL.
Jika koneksi gagal, script akan berhenti dan menampilkan pesan error.

# Membuat Form Input Data
Form ini akan digunakan untuk menambahkan data baru atau mengedit data yang sudah ada.

1. Membuat Formulir
Tambahkan kode HTML berikut setelah kode koneksi:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <!-- Meta tags dan link CSS Bootstrap -->
</head>
<body>
    <div class="mx-auto">
        <!-- Form Input Data -->
        <div class="card">
            <div class="card-header">
                Create / Edit Data
            </div>
            <div class="card-body">
                <!-- Form untuk input data mahasiswa -->
                <form action="" method="POST">
                    <!-- NIM -->
                    <div class="mb-3 row">
                        <label for="nim" class="col-sm-2 col-form-label">NIM</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="nim" name="nim" value="<?php echo $nim ?>">
                        </div>
                    </div>
                    <!-- Nama -->
                    <div class="mb-3 row">
                        <label for="nama" class="col-sm-2 col-form-label">Nama</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="nama" name="nama" value="<?php echo $nama ?>">
                        </div>
                    </div>
                    <!-- Alamat -->
                    <div class="mb-3 row">
                        <label for="alamat" class="col-sm-2 col-form-label">Alamat</label>
                        <div class="col-sm-10">
                            <input type="text" class="form-control" id="alamat" name="alamat" value="<?php echo $alamat ?>">
                        </div>
                    </div>
                    <!-- Fakultas -->
                    <div class="mb-3 row">
                        <label for="fakultas" class="col-sm-2 col-form-label">Fakultas</label>
                        <div class="col-sm-10">
                            <select class="form-control" name="fakultas" id="fakultas">
                                <option value="">- Pilih Fakultas -</option>
                                <option value="saintek" <?php if ($fakultas == "saintek") echo "selected" ?>>Saintek</option>
                                <option value="soshum" <?php if ($fakultas == "soshum") echo "selected" ?>>Soshum</option>
                            </select>
                        </div>
                    </div>
                    <!-- Tombol Simpan -->
                    <div class="col-12">
                        <input type="submit" name="simpan" value="Simpan Data" class="btn btn-primary" />
                    </div>
                </form>
            </div>
        </div>
        <!-- Tabel Data Mahasiswa akan ditambahkan di sini -->
    </div>
</body>
</html>
```

Menggunakan Bootstrap untuk styling agar tampilan lebih menarik.
Form menggunakan metode POST untuk mengirim data ke server.
Value pada input diisi dengan variabel PHP untuk mendukung fitur edit data.
# Menambahkan Data (Create)
Sekarang kita akan menambahkan fungsionalitas untuk menyimpan data yang diinput ke database.

1. Menginisialisasi Variabel
Tambahkan kode berikut setelah kode koneksi:

```php
$nim        = "";
$nama       = "";
$alamat     = "";
$fakultas   = "";
$sukses     = "";
$error      = "";
```

Variabel ini akan digunakan untuk menyimpan data input dan pesan sukses/error.

2. Menangani Form Submission
Tambahkan kode berikut sebelum HTML form:

```php
if (isset($_POST['simpan'])) { // Jika tombol simpan ditekan
    $nim        = $_POST['nim'];
    $nama       = $_POST['nama'];
    $alamat     = $_POST['alamat'];
    $fakultas   = $_POST['fakultas'];

    if ($nim && $nama && $alamat && $fakultas) {
        $sql1 = "INSERT INTO mahasiswa (nim, nama, alamat, fakultas) VALUES ('$nim', '$nama', '$alamat', '$fakultas')";
        $q1   = mysqli_query($koneksi, $sql1);
        if ($q1) {
            $sukses = "Berhasil memasukkan data baru";
        } else {
            $error  = "Gagal memasukkan data";
        }
    } else {
        $error = "Silakan masukkan semua data";
    }
}
```

Memeriksa apakah semua field diisi.
Jika semua field terisi, data disimpan ke database.

3. Menampilkan Pesan Sukses atau Error
Tambahkan kode berikut sebelum form:

```html
<?php
if ($error) {
?>
    <div class="alert alert-danger" role="alert">
        <?php echo $error ?>
    </div>
<?php
}
if ($sukses) {
?>
    <div class="alert alert-success" role="alert">
        <?php echo $sukses ?>
    </div>
<?php
}
?>
```

Jika variabel `$error` atau `$sukses` terisi, maka akan ditampilkan pesan yang sesuai.

# Menampilkan Data (Read)
Selanjutnya, kita akan menampilkan data mahasiswa yang ada di database dalam bentuk tabel.

1. Membuat Tabel Data Mahasiswa

Tambahkan kode berikut setelah form input data:

```html
<!-- Tabel Data Mahasiswa -->
<div class="card">
    <div class="card-header text-white bg-secondary">
        Data Mahasiswa
    </div>
    <div class="card-body">
        <table class="table">
            <thead>
                <tr>
                    <th>#</th>
                    <th>NIM</th>
                    <th>Nama</th>
                    <th>Alamat</th>
                    <th>Fakultas</th>
                    <th>Aksi</th>
                </tr>
            </thead>
            <tbody>
                <?php
                $sql2 = "SELECT * FROM mahasiswa ORDER BY id DESC";
                $q2   = mysqli_query($koneksi, $sql2);
                $urut = 1;
                while ($r2 = mysqli_fetch_array($q2)) {
                    $id       = $r2['id'];
                    $nim      = $r2['nim'];
                    $nama     = $r2['nama'];
                    $alamat   = $r2['alamat'];
                    $fakultas = $r2['fakultas'];
                ?>
                    <tr>
                        <td><?php echo $urut++ ?></td>
                        <td><?php echo $nim ?></td>
                        <td><?php echo $nama ?></td>
                        <td><?php echo $alamat ?></td>
                        <td><?php echo $fakultas ?></td>
                        <td>
                            <!-- Tombol Edit dan Delete akan ditambahkan nanti -->
                        </td>
                    </tr>
                <?php
                }
                ?>
            </tbody>
        </table>
    </div>
</div>
```


Mengambil data dari database menggunakan `SELECT * FROM mahasiswa.`
Menampilkan data dalam tabel HTML.
Menggunakan loop while untuk menampilkan setiap baris data.

# Mengedit Data (Update)

Kita akan menambahkan fitur untuk mengedit data mahasiswa yang sudah ada.

1. Menangani Parameter op untuk Edit
Tambahkan kode berikut setelah inisialisasi variabel:

```php
if (isset($_GET['op'])) {
    $op = $_GET['op'];
} else {
    $op = "";
}

if ($op == 'edit') {
    $id    = $_GET['id'];
    $sql1  = "SELECT * FROM mahasiswa WHERE id = '$id'";
    $q1    = mysqli_query($koneksi, $sql1);
    $r1    = mysqli_fetch_array($q1);
    $nim   = $r1['nim'];
    $nama  = $r1['nama'];
    $alamat= $r1['alamat'];
    $fakultas = $r1['fakultas'];

    if ($nim == '') {
        $error = "Data tidak ditemukan";
    }
}
```

Memeriksa apakah parameter `op` adalah edit.
Jika ya, mengambil data mahasiswa berdasarkan id dan mengisi variabel input dengan data tersebut.
Hal ini memungkinkan form menampilkan data yang akan diedit.

2. Memodifikasi Proses Simpan Data
Ubah kode simpan data menjadi:

```php
if (isset($_POST['simpan'])) {
    // ... kode mengambil data input ...

    if ($nim && $nama && $alamat && $fakultas) {
        if ($op == 'edit') { // Mode edit
            $sql1 = "UPDATE mahasiswa SET nim = '$nim', nama = '$nama', alamat = '$alamat', fakultas = '$fakultas' WHERE id = '$id'";
            $q1   = mysqli_query($koneksi, $sql1);
            if ($q1) {
                $sukses = "Data berhasil diupdate";
            } else {
                $error  = "Data gagal diupdate";
            }
        } else { // Mode tambah data baru
            // ... kode insert data baru ...
        }
    } else {
        $error = "Silakan masukkan semua data";
    }
}
```

Jika `op` adalah edit, maka lakukan query UPDATE.
Jika tidak, lakukan query INSERT seperti sebelumnya.

3. Menambahkan Tombol Edit
Tambahkan tombol edit pada tabel data mahasiswa:

```html
<td>
    <a href="index.php?op=edit&id=<?php echo $id ?>"><button type="button" class="btn btn-warning">Edit</button></a>
    <!-- Tombol Delete akan ditambahkan nanti -->
</td>
```

Tombol edit akan mengarahkan ke halaman yang sama (index.php) dengan parameter op=edit dan id mahasiswa.
Saat diakses, form input data akan terisi dengan data mahasiswa yang dipilih.
 
# Menghapus Data (Delete)
Sekarang kita akan menambahkan fitur untuk menghapus data mahasiswa.

1. Menangani Parameter `op` untuk Delete

Tambahkan kode berikut setelah handling op:

```php
if ($op == 'delete') {
    $id   = $_GET['id'];
    $sql1 = "DELETE FROM mahasiswa WHERE id = '$id'";
    $q1   = mysqli_query($koneksi, $sql1);
    if ($q1) {
        $sukses = "Berhasil menghapus data";
    } else {
        $error  = "Gagal menghapus data";
    }
}
```


Memeriksa apakah parameter `op` adalah delete.
Jika ya, lakukan query DELETE berdasarkan `id`.

2. Menambahkan Tombol Delete
Tambahkan tombol delete pada tabel data mahasiswa:

```html
<td>
    <!-- Tombol Edit -->
    <a href="index.php?op=edit&id=<?php echo $id ?>"><button type="button" class="btn btn-warning">Edit</button></a>
    <!-- Tombol Delete -->
    <a href="index.php?op=delete&id=<?php echo $id ?>" onclick="return confirm('Yakin mau menghapus data?')"><button type="button" class="btn btn-danger">Delete</button></a>
</td>
```

Tombol delete akan mengarahkan ke halaman yang sama dengan parameter op=delete dan id mahasiswa.

Menambahkan konfirmasi JavaScript sebelum menghapus data.

# Menyempurnakan Aplikasi
1. Styling dengan Bootstrap
Pastikan Anda telah menambahkan link CSS Bootstrap pada bagian <head>:

```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta2/dist/css/bootstrap.min.css" rel="stylesheet">
```

Tambahkan juga styling tambahan:

```html
<style>
    .mx-auto {
        width: 800px;
    }
    .card {
        margin-top: 10px;
    }
</style>
```

2. Redirect Setelah Operasi
Untuk meningkatkan UX, kita bisa menambahkan redirect setelah operasi berhasil.

Tambahkan kode berikut setelah pesan sukses atau error:

```php
if ($error) {
    // ... pesan error ...
    header("refresh:5;url=index.php"); // Redirect setelah 5 detik
}

if ($sukses) {
    // ... pesan sukses ...
    header("refresh:5;url=index.php"); // Redirect setelah 5 detik
}
```

Penjelasan:
Setelah menampilkan pesan, halaman akan refresh kembali ke index.php setelah 5 detik.
3. Menjaga Keamanan Input
Untuk mencegah SQL Injection, sebaiknya gunakan prepared statements atau setidaknya escape input.

Contoh menggunakan mysqli_real_escape_string:

```php
$nim      = mysqli_real_escape_string($koneksi, $_POST['nim']);
$nama     = mysqli_real_escape_string($koneksi, $_POST['nama']);
$alamat   = mysqli_real_escape_string($koneksi, $_POST['alamat']);
$fakultas = mysqli_real_escape_string($koneksi, $_POST['fakultas']);
```

Anda telah berhasil membuat aplikasi CRUD sederhana menggunakan PHP dan MySQL. Aplikasi ini memungkinkan Anda untuk menambahkan, menampilkan, mengedit, dan menghapus data mahasiswa.
---
Author : Irza.
