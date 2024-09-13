# Authentication PHP
# Pengertian Authentication
Authentication adalah proses verifikasi identitas pengguna yang ingin mengakses sebuah layanan. Proses ini memastikan bahwa hanya pengguna yang memiliki hak akses yang dapat masuk ke sistem.

# Registrasi
1. Membuat Tabel Database

Siapkan tabel user untuk menyimpan data pengguna, misalnya:

```sql
CREATE TABLE user (
    id INT PRIMARY KEY AUTO_INCREMENT,
    username VARCHAR(50) UNIQUE,
    password VARCHAR(255)
);
```

2. Membuat Halaman Registrasi

Form registrasi:
```html
<form action="" method="post">
    <ul>
        <li><label for="username">Username :</label><input type="text" name="username" id="username"></li>
        <li><label for="password">Password :</label><input type="password" name="password" id="password"></li>
        <li><label for="password2">Konfirmasi Password :</label><input type="password" name="password2" id="password2"></li>
        <li><button type="submit" name="register">Registrasi!</button></li>
    </ul>
</form>
```

3. PHP Script Registrasi

Koneksi ke Database

```php
$conn = mysqli_connect("localhost", "root", "", "phpdasar");

```
Proses Registrasi
```php
if (isset($_POST["register"])) {
    if (registrasi($_POST) > 0) {
        echo "<script>alert('User Berhasil Ditambahkan');</script>";
        header("Location: login.php");
        exit;
    } else {
        echo mysqli_error($conn);
    }
}

function registrasi($data) {
    global $conn;

    $username = strtolower(stripslashes($data["username"]));
    $password = mysqli_real_escape_string($conn, $data["password"]);
    $password2 = mysqli_real_escape_string($conn, $data["password2"]);

    if ($password !== $password2) {
        echo "<script>alert('Konfirmasi Tidak Sesuai');</script>";
        return false;
    }

    $result = mysqli_query($conn, "SELECT username FROM user WHERE username = '$username'");
    if (mysqli_fetch_assoc($result)) {
        echo "<script>alert('Username sudah terdaftar');</script>";
        return false;
    }

    $password = password_hash($password, PASSWORD_DEFAULT);
    mysqli_query($conn, "INSERT INTO user VALUES('', '$username', '$password')");

    return mysqli_affected_rows($conn);
}
```

# Login
1. Membuat Halaman Login
Form login sederhana:

```html
<form action="" method="post">
    <ul>
        <li><label for="username">Username :</label><input type="text" name="username" id="username"></li>
        <li><label for="password">Password :</label><input type="password" name="password" id="password"></li>
        <li><button type="submit" name="login">Login!</button></li>
    </ul>
</form>
```

2. PHP Script Login

```PHP
$conn = mysqli_connect("localhost", "root", "", "phpdasar");

if (isset($_POST["login"])) {
    $username = $_POST["username"];
    $password = $_POST["password"];

    $result = mysqli_query($conn, "SELECT * FROM user WHERE username = '$username'");

    if (mysqli_num_rows($result) === 1) {
        $row = mysqli_fetch_assoc($result);
        if (password_verify($password, $row["password"])) {
            session_start();
            $_SESSION["login"] = true;
            header("Location: index.php");
            exit;
        }
    }

    $error = true;
}
```

# Session
Session digunakan untuk menyimpan data pengguna selama interaksi dengan aplikasi.

1. Memulai Session
Tambahkan `session_start()` di awal file PHP yang membutuhkan session.

2. Memeriksa Pengguna yang Belum Login
Tambahkan kode ini di halaman utama (index.php) untuk memeriksa apakah pengguna sudah login:

```php
session_start();
if (!isset($_SESSION["login"])) {
    header("Location: login.php");
    exit;
}
```

3. Membuat Logout

```php
session_start();
$_SESSION = [];
session_unset();
session_destroy();
header("Location: login.php");
exit;
```

# Cookie
Cookie digunakan untuk menyimpan data pengguna di browser.

1. Membuat Cookie
Tambahkan kode ini di halaman login jika ingin menerapkan "Remember Me":

```php
if (isset($_POST["remember"])) {
    setcookie('id', $row['id'], time() + 3600);
    setcookie('key', hash('sha256', $row['username']), time() + 3600);
}
```

2. Memeriksa Cookie
Di halaman login, tambahkan pengecekan cookie:

```php
if (isset($_COOKIE['id']) && isset($_COOKIE['key'])) {
    $id = $_COOKIE['id'];
    $key = $_COOKIE['key'];

    $result = mysqli_query($conn, "SELECT username FROM user WHERE id = $id");
    $row = mysqli_fetch_assoc($result);

    if ($key === hash('sha256', $row['username'])) {
        $_SESSION['login'] = true;
    }
}
```

3. Menghapus Cookie Saat Logout
Tambahkan di halaman logout:

```php
setcookie('id', '', time() - 3600);
setcookie('key', '', time() - 3600);
```

Modul ini memberikan panduan dasar untuk membuat autentikasi di PHP menggunakan registrasi, login, session, dan cookie.
---
Author : Hanif.