# Authentication in PHP

## **Chapter 1 : Pengertian Authentication**

Authentication adalah proses memverifikasi identitas seseorang atau sistem yang mencoba mengakses layanan atau sumber daya.
Tujuan utama dari proses ini adalah untuk memverifikasi bahwa entitas yang mencoba mengakses  benar-benar memiliki izin yang sesuai.

Dan banyak dari website atau layanan sejenisnya memerlukan sebuah verifikasi berupa `login`, agar tidak sembarang orang bisa masuk atau mengakses sebuah website atau layanan tertentu.

Dan pada materi `authentication` ini ada 4 sub materi yang akan kita pelajari.
1. Registrasi
2. Login
3. Session
4. Cookie

## **Chapter 2 : Registrasi**

Untuk mengakses suatu website atau layanan tertentu, kita harus mendaftarkan diri terlebih dahulu dengan mengirimkan sebuah data, biasanya berupa username, email, nomer hp dan sebagainya. Dan pada bagian ini dinamakan sesi `registrasi`.

Mari kita coba membuat sebuah halaman registrasi sederhana agar bisa lebih mudah dipahami.

### **1. Persiapan Tabel Database** 

Untuk menyimpan data pengguna yang masuk, kita membutuhkan tabel pada sebuah database.

<img src="asset/database.png">

Sebagai contoh kita akan membuat table `user` dalam database `phpdasar`. Data yang ada pada table bisa disesuaikan sesuai kebutuhan.

### **2. Menyiapkan Halaman Registrasi** 

1. Ketikan `!` kemudian `tab` maka akan otomatis dibuatkan sintak seperti dibawah

```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Document</title>
    </head>
    <body>
        
    </body>
    </html>
```


2. Kemudian pada bagian Body kita tambahkan sebuah form sederhana untuk mendaftarkan user
```html
    <body>
    
    <h1>HALAMAN REGISTRASI</h1>
    <form action="" method="post">

        <ul>
            <li>
                <label for="username">Username :</label>
                <input type="text" name="username" id="username">
            </li>
            <li>
                <label for="password">Password :</label>
                <input type="password" name="password" id="password">
            </li>
            <li>
                <label for="password2">Konfirmasi Password :</label>
                <input type="password" name="password2" id="password2">
            </li>
            <li>
                <button type="submit" name="register">Registrasi!</button>
            </li>
        </ul>

    </form>

</body>
```
Ada beberapa hal yang harus diperhatikan ketika membuat form
1. `Atribut pada form` : Pada bagian form harus memiliki atribut action dan method. Atribut action dikosongkan agar data yang diperoleh dari form kita proses didalam halaman registrasi ini, dan atribut method kita menggunakan post agar tidak ada data yang tampil di url.

2. `Atribut Type` : Pastikan atribut type pada bagian password menggunakan type 'password' agar typing dari user tidak bisa dilihat

3. `Atribut pada button` : Tipe submit digunakan untuk membuat tombol submit dalam formulir. Fungsi utama dari atribut submit ini adalah untuk mengirim data.

4. Pastikan atribut `for`, `name`, dan `id` memiliki nilai yang sama 



### **3. Mengolah Data Menggunakan Tag PHP** 

- Pertama kita hubungkan terlebih dahulu halaman registrasi dengan database
```php
     $conn = mysqli_connect("localhost", "root", "", "phpdasar" );
```
Baris ini digunakan untuk membuat koneksi ke database MySQL. Parameter yang diberikan adalah:

1. "localhost": Nama host dimana MySQL berjalan.
2. "root": Nama pengguna MySQL.
3. "": Kata sandi pengguna MySQL (dalam contoh ini kosong).
4.  "phpdasar": Nama database yang digunakan.

---

- Kedua kita akan membuat kondisi ketika tombol register sudah ditekan
```php
<?php
    if( isset($_POST["register"]))
    {
        if(registrasi($_POST) > 0)
        {
            echo    "<script>
                        alert('User Berhasil Ditambahkan');
                    </script>";
            
                    header("location:login.php");
                    exit;
        }
        else
        {
            echo mysqli_error($conn);
        }
    }
?>
```
Mari kita bedah kode diatas
1. Memeriksa Pengiriman Form:
```php
if (isset($_POST["register"])) {
```
Memeriksa apakah form registrasi telah dikirim.

---

2. Memanggil Fungsi Registrasi:
```php
if (registrasi($_POST) > 0) {
```
Memanggil fungsi registrasi dengan data dari form. Jika fungsi mengembalikan nilai lebih dari 0, berarti registrasi berhasil.

---

3. Pesan Berhasil dan Redirect:
```php
echo "<script>alert('User Berhasil Ditambahkan');</script>";
header("location:login.php");
exit;
```
Menampilkan pesan berhasil dan mengarahkan pengguna ke halaman login.

---

4. Pesan Kesalahan: 
```php
echo mysqli_error($conn);
```
Menampilkan pesan kesalahan jika registrasi gagal.

---
- Yang ketiga kita membuat sebuah `function` untuk menerima inputan data dari `$_post`, dan didalam `function` "registrasi" ini kita akan memastikan agar "password" yang di input harus sama persis dengan "konfirmasi password".
```php
    function registrasi($data)
        {
            global $conn;

            $username = strtolower(stripslashes($data["username"]));
            $password = mysqli_real_escape_string($conn, $data["password"]);
            $password2 = mysqli_real_escape_string($conn, $data["password2"]);

            if( $password !== $password2)
            {
                echo    "<script>
                            alert('Konfirmasi Tidak Sesuai');
                        </script>";
                return false;
            }

            $result = mysqli_query($conn, "SELECT username FROM user WHERE username = '$username'");
            if( mysqli_fetch_assoc($result))
            {
                echo    "<script>
                            alert('Username sudah terdaftar');
                        </script>";
                return false;
            }

            $password =password_hash($password, PASSWORD_DEFAULT);

            mysqli_query($conn, "INSERT INTO user VALUE('', '$username', '$password')");

            return mysqli_affected_rows($conn);

        }
```
1. Global Connection:
```php
    global $conn;
```
Menggunakan variabel global `$conn` yang telah didefinisikan di luar fungsi.

---
2. Mengamankan dan Memproses Input:
```php
    $username = strtolower(stripslashes($data["username"]));
    $password = mysqli_real_escape_string($conn, $data["password"]);
    $password2 = mysqli_real_escape_string($conn, $data["password2"]);
```
- strtolower: Mengubah username menjadi huruf kecil.
- stripslashes: Menghilangkan karakter backslash.
- mysqli_real_escape_string: Mengamankan input terhadap serangan SQL injection.

---
3. Memeriksa Kesamaan Password:
```php
    if ($password !== $password2) {
        echo "<script>alert('Konfirmasi Tidak Sesuai');</script>";
        return false;
    }
```
Memastikan password dan konfirmasi password sesuai.

---
4. Memeriksa Ketersediaan Username:
```php
    $result = mysqli_query($conn, "SELECT username FROM user WHERE username = '$username'");
    if (mysqli_fetch_assoc($result)) {
        echo "<script>alert('Username sudah terdaftar');</script>";
        return false;
    }
```
Mengecek apakah username sudah ada di database.

---
5. Meng-hash Password:
```php
    $password = password_hash($password, PASSWORD_DEFAULT);
```
Menggunakan `password_hash` untuk mengamankan password.

---
6. Menyimpan Pengguna Baru:
```php
    mysqli_query($conn, "INSERT INTO user VALUE('', '$username', '$password')");
```
Menyimpan data pengguna baru ke database.

---
7. Mengembalikan Hasil:
```php
    return mysqli_affected_rows($conn);
```
Mengembalikan jumlah baris yang terpengaruh oleh query (lebih besar dari 0 jika berhasil).

---
- Didalam function Registrasi kita juga harus memastikan agar `username` yang sudah terdaftar tidak boleh di input kembali.
```php
    $result = mysqli_query($conn, "SELECT username FROM user WHERE username = '$username'");

        if( mysqli_fetch_assoc($result))
        {
            echo    "<script>
                        alert('Username sudah terdaftar');
                    </script>";
            return false;
        }
```

---
- Sebelum kita kirim datanya ke database, kita perlu enkripsi terlebih dahulu passwordnya agar keamanan akun user terjaga.
```php
    $password = password_hash($password, PASSWORD_DEFAULT);
```

---
- Setelah password kita enkripsi, selanjutnya kita masukan data yang sudah kita tangkap kedalam tabel `user` didalam database.
```php
    mysqli_query($conn, "INSERT INTO user VALUE('', '$username','$password')");

    return mysqli_affected_rows($conn);
```

---

## **Chapter 3 : Login**
Akun yang sudah didaftarkan pada halaman registrasi akan tersimpan di dalam database, dan pada halaman login akun yang sudah tersimpan akan dicek dan diverifikasi kecocokanya dengan username dan password ketika ada pengguna yang berusaha memasukan data, sebelum masuk ke halaman utama

Mari kita coba membuat sebuah halaman login sederhana agar bisa lebih mudah dipahami.

### **1. Menyiapkan Halaman Login** 
Sama seperti sebelumnya kita mulai dengan ketikan `!` kemudian tab. Dan tambahkan form yang beris beberapa input sesuai kebutuhan kalian
```php
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>login</title>
    </head>
    <body>
        <h1>HALAMAN LOGIN</h1>
            <?php if( isset($error)): ?>
                <p>username /password error</p>
            <?php endif; ?>

        <form action="" method="post">
            <ul>
                <li>
                    <label for="username">Username :</label>
                    <input type="text" name="username" id="username">
                </li>
                <li>
                    <label for="password">Password :</label>
                    <input type="password" name="password" id="password">
                </li>
                <li>
                    <button type="submit" name="login">Registrasi!</button>
                </li>
            </ul>
        </form>
    </body>
    </html>
```

### **2. Mengolah Data Menggunakan Tag PHP**

```php
<?php

$conn = mysqli_connect("localhost", "root", "", "phpdasar" );

    if( isset($_POST["login"]))
    {
       $username = $_POST["username"];
       $password = $_POST["password"];

       $result = mysqli_query($conn, "SELECT * FROM user WHERE username = '$username'");

       if( mysqli_num_rows($result) === 1){

           $row = mysqli_fetch_assoc($result);
           if(password_verify($password, $row["password"])){
               header("location:index.php");
               exit;
           }
       }
       $error = true;
       
    }
?>
```
Mari kita bedah satu persatu

---

**1. Koneksi ke Database:**
```php
    $conn = mysqli_connect("localhost", "root", "", "phpdasar");
```
Baris ini digunakan untuk membuat koneksi ke database MySQL. Parameter yang diberikan adalah:

- "localhost": Nama host dimana MySQL berjalan.
- "root": Nama pengguna MySQL.
- "": Kata sandi pengguna MySQL (dalam contoh ini kosong).
- "phpdasar": Nama database yang digunakan.

---
**2. Memeriksa apakah Form Login Dikirim:**
```php
    if( isset($_POST["login"]))
```
Kondisi ini memeriksa apakah tombol login telah ditekan dan data telah dikirim melalui metode POST.

---
**3. Mengambil Data dari Form:**
```php
    $username = $_POST["username"];
    $password = $_POST["password"];
```
Baris ini mengambil data yang dimasukkan oleh pengguna dalam form login.

---
**4. Menjalankan Query untuk Memeriksa Pengguna:**
```php
    $result = mysqli_query($conn, "SELECT * FROM user WHERE username = '$username'");
```
Query ini mencari pengguna dengan username yang sesuai dalam tabel user.

---
**5. Memeriksa Apakah Pengguna Ditemukan:**
```php
    if( mysqli_num_rows($result) === 1){
```
Kondisi ini memeriksa apakah ada tepat satu baris hasil dari query (berarti pengguna dengan username tersebut ditemukan).

---
**6. Memverifikasi Password:**
```php
    $row = mysqli_fetch_assoc($result);
    if(password_verify($password, $row["password"])){
```
Baris pertama mengambil data pengguna dalam bentuk array asosiatif. Fungsi `password_verify` kemudian digunakan untuk memeriksa apakah password yang dimasukkan sesuai dengan hash password yang tersimpan di database.

---
**7. Redirect ke Halaman Index:**
```php
    header("location:index.php");
    exit;  
```
Pengguna dialihkan ke halaman index.php setelah login berhasil.

---
**8. Menangani Kesalahan Login:**
```php
    $error = true;
```
Jika username tidak ditemukan atau password tidak cocok, variabel `$error` diset menjadi `true`, yang biasanya digunakan untuk menampilkan pesan kesalahan kepada pengguna.

---
**9. Menampilkan pesan kesalahan:**
```php
    <?php if( isset($error)): ?>
        <p>username /password error</p>
    <?php endif; ?>
```

---
## **Chapter 4 : Session**
Session adalah mekanisme yang digunakan untuk menyimpan informasi tentang pengguna di server selama pengguna berinteraksi dengan aplikasi web. Session memungkinkan aplikasi untuk melacak data pengguna antara berbagai halaman web.

### **Cara Kerja Session**
- Memulai Session: Ketika session dimulai, PHP membuat sebuah file unik di server untuk menyimpan variabel session.
- ID Session: Setiap session memiliki ID unik yang disimpan di cookie pada browser pengguna.
- Mengakses Data Session: Data yang disimpan dalam session dapat diakses dari setiap halaman selama session tersebut aktif.

Agar lebih memahami materi session ini, mari kita gunakan kembali halaman registrasi, halaman login, dan halaman index yamg sebelumnya telah kita buat

---
### **Memulai Session**
Sebelum menggunakan session, kita harus memulai session tersebut menggunakan fungsi `session_start()`. pastikan setiap halaman menggunakan fungsi ini

```php
    session_start();
```

---
### **Memeriksa Pengguna**
- Ketika pengguna belum login
```php
    if( !isset($_SESSION["login"]) == true){
        header("location: login.php");
        exit;
    }
```
Kode ini digunakan untuk memeriksa apakah pengguna belum login dan kemudian mengarahkan mereka ke halaman login jika mereka belum login. kita tambahkan kode berikut didalam halaman `index.php`.

```php
    if (isset($_SESSION["login"]) == true) {
        header("location: index.php");
        exit;
    }
```
Kode ini digunakan untuk memeriksa apakah pengguna sudah login dan kemudian mengarahkan mereka ke halaman utama jika mereka sudah login. kita tambahkan kode berikut didalam halaman `login.php` dan `registrasi.php`.

---
### **Membuat Tombol Logout**
Pada halaman `index.php` kita tambahkan sebuah tombol logout. Tapi sebelum itu kita siapkan halaman untuk logout, sebagai contoh kita namakan `logout.php`
```php
    <button>
        <a href="logout.php">Logout</a>
    </button>
```
dan kita sambungkan ke halaman `logout.php`. Dan didalam halaman logout kita tambahkan kode
```php
    <?php 
        session_start();    
        $_SESSION = [];     //Mengosongkan Variabel Sesi
        session_unset();    //Menghapus Variabel Sesi
        session_destroy();  //Menghancurkan Sesi

        header("location: login.php");
        exit;
        //Mengalihkan ke Halaman Login
    ?>  
```

## **Chapter 5 : Cookie**
Cookie adalah potongan data kecil yang dikirim dari server dan disimpan di komputer pengguna oleh browser. Cookie digunakan untuk menyimpan informasi yang dapat digunakan kembali oleh server pada kunjungan berikutnya.

### **Cara Kerja Cookie**
- Membuat Cookie: Server mengirimkan cookie ke browser menggunakan header HTTP.
- Menyimpan Cookie: Browser menyimpan cookie di komputer pengguna.
- Mengirim Cookie: Pada setiap permintaan berikutnya ke server, browser mengirimkan cookie yang relevan.

### **Membuat Cookie**
Cookie dibuat menggunakan fungsi `setcookie()` di PHP. Berikut adalah sintaks dasar untuk membuat cookie:
```php
    setcookie()
```

---
Mari kita tambahkan beberapa kode php kedalam halaman login

**1. YANG PERTAMA**
```php
    if( isset($_POST['remember'])){
        setcookie('id', $row['id'], time() + 60);
        setcookie('key',hash('sha256',$row['username']), time() + 60);
    }
```
Mari kita bedah satu persatu:

```php
if (isset($_POST['remember'])) {

}
```
- `isset()` adalah fungsi PHP yang memeriksa apakah sebuah variabel sudah diset dan tidak bernilai null.
- `$_POST['remember']` adalah data yang dikirimkan melalui form login ketika pengguna mencentang kotak "Remember Me".
- Kondisi ini memastikan bahwa kode di dalam blok if hanya akan dijalankan jika pengguna mencentang kotak "Remember Me".

---
```php
setcookie('id', $row['id'], time() + 60);
```
- `setcookie()` adalah fungsi PHP yang digunakan untuk mengirim cookie ke browser.
- `'id'` adalah nama cookie yang akan disimpan.
- `$row['id']` adalah nilai cookie, yang diambil dari kolom id dari hasil query database. Ini adalah ID pengguna dari database.
- `time() + 60` adalah waktu kedaluwarsa cookie. time() mengembalikan waktu saat ini dalam detik sejak Unix Epoch, dan menambahkan 60 detik (1 menit) untuk menentukan kapan cookie akan kedaluwarsa.

---
```php
setcookie('key', hash('sha256', $row['username']), time() + 60);
```
- `'key'` adalah nama cookie yang akan disimpan.
- `hash('sha256', $row['username'])` adalah nilai cookie, yang merupakan hash SHA-256 dari username pengguna. Menggunakan hash untuk menyimpan informasi sensitif seperti username meningkatkan keamanan.
- `time() + 60` menentukan waktu kedaluwarsa cookie, yang juga ditetapkan ke 60 detik (1 menit).

---
**2. YANG KEDUA**
```php
if( isset($_COOKIE['id']) && isset($_COOKIE['key']) ) {
    $id = $_COOKIE['id'];
    $key = $_COOKIE['key'];

    $result2 = mysqli_query($conn, "SELECT username FROM user WHERE id = $id");
    $row2 =  mysqli_fetch_assoc($result2);

    if(key === hash('sha256',$row['username'])) {
        $_SESSION['login'] = true;
    }
}
```
Kita bedah satu persatu

```php
if (isset($_COOKIE['id']) && isset($_COOKIE['key'])) {

}
```
Memeriksa Apakah Cookie id dan key Ada

---

```php
$id = $_COOKIE['id'];
$key = $_COOKIE['key'];
```
Mengambil Nilai Cookie

---

```php
$result2 = mysqli_query($conn, "SELECT username FROM user WHERE id = $id");
$row2 = mysqli_fetch_assoc($result2);
```
Mengambil Username dari Database Berdasarkan ID

---

```php
if ($key === hash('sha256', $row2['username'])) {
    $_SESSION['login'] = true;
}
```
Memverifikasi Key dengan Hash Username

---
**3. YANG KETIGA**

Yang terakhir kita tambahkan kode pada halaman logout, untuk menghentikan `cookie`
```php
    setcookie('id', '', time() - 3600);
    setcookie('key', '', time() - 3600);
```