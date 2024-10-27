# 5. Latihan

Author: Bara Muthi
Editor: Hudya

## Overview

Sebelum kamu melangkah lebih jauh dalam dunia pengujian perangkat lunak, penting untuk memahami dan menguasai manual testing.

Manual testing adalah fondasi dari quality assurance, di mana kamu sebagai tester secara langsung berinteraksi dengan aplikasi, menguji fungsionalitasnya, dan mengidentifikasi bug atau masalah potensial.

Proses ini memungkinkan kamu untuk mendapatkan pemahaman mendalam tentang perilaku aplikasi, pengalaman pengguna, dan berbagai skenario yang mungkin terjadi dalam penggunaan sehari-hari. Dengan melakukan manual testing, kamu akan mengembangkan intuisi yang kuat tentang bagaimana sebuah aplikasi seharusnya berfungsi dan bagaimana pengguna mungkin berinteraksi dengannya.

## Latihan Pengujian

Website yang digunakan adalah https://www.saucedemo.com/. Sekarang pindahkan semua data pada tabel di bawah ini ke excel/google sheets lalu mulai-lah berlatih untuk menguji kumpulan skenario di bawah ini.

Dikarenakan ini merupakan ujicoba secara manual, maka kamu harus mencobanya secara manual.

Tambahkan beberapa kolom pada bagian kanan dengan kolom sebagai berikut:

- Actual_Result: Hasil akhir, kamu bisa menjelaskan hasil akhir sebagai contoh: **"same as expected"**, atau kamu bisa menjelaskan beberapa perbedaan apabila terdapat perbedaan dengan ekspektasi.
- Evidance: Bukti pengujian, kamu dapat melakukan screenshot dan menaruhnya pada kolom ini.
- Notes: Tulis apabila ada catatan dari perilaku yang mempengaruhi, misalnya apabila diam di halaman selama 1 menit tanpa melakukan klik apapun maka akan muncul tampilan yang berbeda
- Tested by: Tulis nama penguji (nama kamu)
- Timestamp: Tulis tanggal lengkap hingga waktu kamu menguji, misalnya, 10-12-2024 10:23:45 WIB

## Test Plan

### Tujuan pengujian

Memastikan fitur pada website https://www.saucedemo.com/ berjalan dengan baik, Menemukan dan mengidentifikasi bug dan Memastikan kompatibilitas tampilan di perangkat mobile dan desktop.

### Fungsi

Fungsi yang akan di uji adalah:

- Halaman login
- inventory
- carts
- checkout
- logout
-

### Skenario Pengujian

Berikut merupakan skenario pengujian pada website saucedemo:

- Skenario login dengan kredensial yang valid dan tidak valid.
- Skenario navigasi di dalam daftar produk.
- Penambahan dan penghapusan produk ke keranjang.
- Melakukan checkout dengan produk yang dipilih.
- Logout.

### Strategi pengujian

strategi pengujian dilakukan secara manual dengan website https://www.saucedemo.com/

## Test Cases

| No  |   Fitur   | Test_case                          | Type     | Test_Scenario                                                                                                           | Test_Data                                                | Test_Step                                                                                                                                                                                                          | Expected_Result                                                                      |
| --- | :-------: | ---------------------------------- | -------- | ----------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------ |
| 1.  |   Login   | open website                       | positive | Before logging in, as a user, I should be able to access the website and view the login form and with the login button. |                                                          | 1.open website https://www.saucedemo.com/ 2.Validate there are a login form with username and password                                                                                                             | can see form and login page with your username and password and button login         |
| 2.  |   Login   | login with valid data              | positive | As a user, I should be able to login using valid data                                                                   | Username: `standard_user` <br>Password: `secret_sauce`   | 1. Open https://www.saucedemo.com/ <br>2. Enter valid username and password <br>3. Click Login button                                                                                                              | User successfully logged in and redirected to the product page                       |
| 3.  |   Login   | Login with Locked User             | Negative | As a user, I should not be able to login with a locked account                                                          | Username: `locked_out_user` <br>Password: `secret_sauce` | 1. Open `https://www.saucedemo.com/` <br>2. Enter locked user credentials <br>3. Click Login button 4.there is note "Epic sadface: Sorry, this user has been locked out."                                          | Error message: "Epic sadface: Sorry, this user has been locked out."                 |
| 4.  | inventory | inventory-page                     | positive | As a user, I should be able to view all products in inventory page                                                      | Username: `standard_user` <br>Password: `secret_sauce`   | 1. Open https://www.saucedemo.com/ <br>2. Enter username and password 3. click Login with valid data <br>4. Navigate to the inventory page and you can see 6 items                                                 | All available products are displayed with the price, name, and "Add to cart" button  |
| 5.  | inventory | inventory- add to carts            | positive | As a user, I should be able to add products to the cart                                                                 | Product: `Sauce Labs Backpack`                           | 1. Open https://www.saucedemo.com/ <br>2. Enter username and password 3. click Login with valid data <br>4. Navigate to the inventory page and you can see 6 items 5.Click "Add to cart" for `Sauce Labs Backpack` | Product successfully added to cart, cart icon shows incremented number               |
| 6.  | inventory | inventory-Remove Product from Cart | positive | As a user, I should be able to remove products from the cart                                                            | Product: `Sauce Labs Backpack`                           | 1. Open https://www.saucedemo.com/ <br>2. Enter username and password 3. click Login with valid data 4. Add a product to the cart <br>5. Go to the cart page <br>6. Click "Remove" next to the product             | Product is successfully removed from the cart, so cart icon shows decremented number |
| 7.  |   cart    | cart-page                          | positive | As a user, I should be able to view the items in cart page                                                              |                                                          | 1. Add products to the cart <br>2. Click on the cart icon (top right corner)                                                                                                                                       | Cart page shows list of added products with price and quantity                       |
| 8.  | checkout  | checkout product                   | positive | As a user, I should be able to complete the checkout process                                                            | First Name, Last Name, Postal Code                       | 1. Add products to the cart <br>2. Click on "Checkout" <br>3. Enter First Name, Last Name, Postal Code <br>4. Click "Continue" <br>5. Click "Finish"                                                               | Checkout is completed, user is redirected to "Thank you for your order!" page        |
| 9.  | checkout  | cancel checkout                    | negative | As a user, I should be able to cancel checkout process                                                                  |                                                          | 1. Add products to the cart <br>2. Click on "Checkout" <br>3. Click "Cancel" button                                                                                                                                | Checkout is canceled, user is redirected back to the cart page                       |
| 10. |  logout   | logout                             | positive | As a user, I should be able to logout                                                                                   |                                                          | 1. Open https://www.saucedemo.com/ <br>2. Enter username and password 3. click Login with valid data <br>4. Click on the menu icon (top right) <br>5. Click "Logout"                                               | User is successfully logged out                                                      |

## Penjelasan

- **No**

  Nah, kolom **No** ini simpel aja, isinya nomor urut dari test case-nya. Jadi gampang aja kalo mau nyari test case yang spesifik. Urutannya tinggal liat dari angka di kolom ini.

- **Fitur**

  Kolom **Fitur** ini ngasih tau kita, fitur apa yang lagi di-tes. Misalnya kayak "Login", "Inventory", atau "Checkout". Jadi kita bisa tau kita lagi ngetes bagian mana dari aplikasi/web.

- **Test Case**

  **Test Case** ini menjelaskan secara spesifik apa yang kita tes. Misalnya kayak “login dengan data valid” atau “cek halaman inventory”. Jadi dari sini kita tahu detail tes yang lagi dijalankan.

- **Type**

  Nah, ini ngasih tau tipe dari test case-nya. Biasanya ada dua tipe nih:

  - **Positive**: Artinya tes ini untuk ngecek apakah fitur jalan dengan benar dengan input yang bener.
  - **Negative**: Ini sebaliknya, buat ngetes apakah aplikasi bisa nangani error atau kondisi gagal dengan baik. Misalnya login dengan akun yang diblokir.

- **Test Scenario**

  Disini, kita nulis cerita lengkapnya, kayak “Sebagai user, pengen bisa login pake data valid” atau “Sebagai user, kalo pake akun yang diblokir, harusnya nggak bisa login”. Jadi ini kayak overview-nya aja buat jelasin tujuannya.

- **Test Data**

  Nah, kolom ini isinya data yang dipake buat tesnya. Misalnya buat login pake username dan password apa. Contohnya kayak gini nih:

  - Username: `standard_user`
  - Password: `secret_sauce`

- **Test Step**

  Ini penting banget, ges. Di sini kita tulis langkah-langkah detail yang harus dilakukan buat ngetes fiturnya. Misalnya:

  1. Buka website
  2. Masukin username dan password
  3. Klik tombol login Ini biar tesnya jelas dan bisa diikutin sama siapa aja.

- **Expected Result**

  Nah, ini bagian yang ngejelasin apa yang kita harapin kalo tesnya berhasil. Misalnya, setelah login pake data valid, kita harusnya dialihin ke halaman produk. Jadi ini kayak hasil idealnya.

- **Status**

  Kolom ini buat ngasih tau hasil tesnya sukses atau nggak. Biasanya ada dua status:

  - **Pass**: Tes sukses, hasilnya sesuai harapan.
  - **Fail**: Tes gagal, hasilnya nggak sesuai ekspektasi.

- **Actual Result**

  Ini ngejelasin hasil tes yang sebenernya. Apakah sesuai ekspektasi atau nggak. Biasanya kalo sesuai, tinggal ditulis “same as expected”. Tapi kalo nggak, jelasin detail errornya.

- **Evidance (Evidence)**

  Di kolom ini, kita bisa masukin bukti screenshot atau hasil tes yang udah dijalankan. Misalnya kayak screenshot pas login berhasil atau pas ada error muncul.

- **Noted**

  Ini buat catatan tambahan aja. Misalnya ada info yang perlu dicatat tapi nggak masuk di kolom lain.

- **Tested by**

  Nah, di sini diisi nama orang yang udah ngetes.

- **Timestamp**

  Ini buat catat tanggal dan waktu tes dijalankan. Biar kita bisa tracking kapan tesnya dilakukan.

## Example Action

Nah sekarang kita ambil satu contoh ya, jadi di sini kita mau ngecek fitur login nih dengan urut nomor satu.

Pertama, kita bakal buka websitenya di [https://www.saucedemo.com/](https://www.saucedemo.com/).

Pada tahap ini, kita pastiin dulu nih, tampilannya bener gak? Harusnya muncul form login, yang ada kolom buat username, password, sama tombol login.

Kalau semuanya muncul sesuai harapan, berarti berhasil nih, dan kita bisa lanjut ke langkah berikutnya.

Jadi kalau berhasil, tampilan form login-nya kelihatan lengkap dan siap diisi.

Hasilnya di sini "pass" karena tampilannya sesuai sama yang diharapkan, udah kelihatan form login-nya dengan username, password, sama tombol login.

## Summary

Tabel test cases di atas adalah contoh konkret dari bagaimana manual testing distrukturkan dan didokumentasikan.

Setiap baris dalam tabel mewakili sebuah test case yang mencakup berbagai aspek dari aplikasi, mulai dari login hingga checkout dan logout.

Dengan mengikuti langkah-langkah yang diuraikan dalam tabel ini, kamu akan belajar bagaimana merancang test case yang efektif, mengidentifikasi skenario pengujian yang kritis, dan memahami pentingnya dokumentasi yang rinci dalam proses QA.

Praktik ini tidak hanya akan meningkatkan keterampilanmu dalam menemukan bug, tetapi juga akan membantu kamu mengembangkan pemikiran kritis dan analitis yang esensial dalam karir QA.

Hasil akhir dari testing manual di atas dapat kamu temui pada URL [berikut](https://docs.google.com/spreadsheets/d/1z62TVKpQ4q4lp_bR5i_llnZF_bECdsUsCU9qLLDJ4UU/edit?usp=sharing).
