# Pengenalan terhadap snippet bootstrap
![head](https://www.tutorialrepublic.com/lib/images/bootstrap-5.0-illustration.png)
### Apasih sebuah snippet dalam dunia programming?

Snippet code adalah sepotong kecil kode atau fragmen kode yang digunakan untuk melakukan tugas tertentu dalam pemrograman. Snippet code biasanya merupakan implementasi singkat dari suatu konsep atau fungsi yang dapat digunakan kembali dalam pengembangan perangkat lunak.

Penerapan snippet code sangat berguna karena dapat membantu programmer menghemat waktu dan usaha dalam menulis kode yang serupa berulang-ulang. Dengan menggunakan snippet code, programmer dapat dengan mudah mengimpor dan memodifikasi kode yang sudah ada untuk memenuhi kebutuhan spesifik mereka.

Snippet code biasanya dikembangkan dan dibagikan oleh komunitas pemrograman atau individu melalui platform seperti GitHub atau paket manajer dependensi. Mereka bisa berupa fungsi matematika sederhana, logika pengolahan data, atau bahkan struktur kontrol yang kompleks.

Penting untuk dicatat bahwa snippet code bukanlah solusi lengkap untuk masalah pemrograman. Mereka lebih berfungsi sebagai alat bantu yang dapat membantu programmer mempelajari dan menerapkan konsep-konsep pemrograman yang umum. Dalam penggunaannya, snippet code perlu dimodifikasi dan disesuaikan dengan kebutuhan proyek yang sedang dikerjakan.

Dengan menggunakan snippet code dengan bijak, programmer dapat mengoptimalkan produktivitas mereka dan membangun perangkat lunak dengan lebih efisien.

### Apakah mengunakan snippet termasuk curang?

Menggunakan snippet code dalam pemrograman tidak dapat dikategorikan sebagai curang. Snippet code adalah alat yang tersedia untuk membantu programmer meningkatkan efisiensi dan produktivitas mereka. Mengapa? Karena snippet code biasanya merupakan bagian kecil dari kode yang telah dikembangkan oleh komunitas pemrograman atau individu lainnya.

Penting untuk diingat bahwa snippet code tidak dimaksudkan sebagai solusi lengkap untuk setiap masalah pemrograman. Mereka hanya menyediakan contoh implementasi yang dapat digunakan sebagai awal atau referensi dalam membangun perangkat lunak. Ketika menggunakan snippet code, programmer masih perlu memahami dan memodifikasinya agar sesuai dengan kebutuhan spesifik proyek yang sedang dikerjakan.

Sebagai programmer, penting untuk memiliki pemahaman yang kuat tentang konsep-konsep pemrograman dan kemampuan untuk menulis kode dari awal. Menggunakan snippet code hanya sebagai sumber inspirasi atau bantuan untuk mempercepat pengembangan tidak dapat dianggap sebagai tindakan curang. Selama kode tersebut dimodifikasi dan disesuaikan dengan kebutuhan proyek, penggunaan snippet code adalah praktik yang umum dan diterima dalam komunitas pemrograman.

Namun, penting untuk mencantumkan sumber atau kredit kepada pencipta snippet code jika mereka mengharapkannya. Ini adalah etika yang baik dalam komunitas pemrograman dan mendorong kolaborasi dan berbagi pengetahuan di antara para pengembang.

## Implementasi snippet menggunakan bootstrap

Ada banyak web di internet yang mengumpulkan snippet bootstrap, salah satu web tersebut adalah `startbootstrap.com` di web tersebut tersedia banyak resources untuk membantu developer membangun UI yang bagus untuk project mereka.

Untuk tutorial kali ini, aku akan memberikan contoh implementasi kode snippet bootstrap menggunakan web `startbootstrap.com`.

## Langkah menggunakan kode snippet dari startbootstrap.com

1. Pertama Buka web [startbootstrap.com](https://startbootstrap.com)
   
2. Pilih resources di navbar, kemudian klik `snippet`
 
3. Pilih card yang berisi tampilan dari code snippet yang ingin kalian insert ke web kalian
   
    <img src="https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/13db00d2-fea4-4bd3-b4b3-fdf15bece07a" width="500"></img>

4. Di sini aku memilih Modern sign in page
   
   ![](https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/c96b580a-1a7e-4019-aed3-1b3cc2d4ec7a)

5. Saat kalian memilih snippet, kalian langsung dapat melihat demo dari snippet tersebut

    <img src="https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/28816a2f-5d33-49cd-b59d-f5ccb2bc3ff8" width="500"></img>

6. Kita akan copy semua yang kita butuhkan untuk snippet yang ingin kita gunakan, seperti html, css, js , dan resources lainnya

7. Berikut adalah kode dari html snippet yang aku copy

    ```html
    <div class="container-fluid ps-md-0">
      <div class="row g-0">
        <div class="d-none d-md-flex col-md-4 col-lg-6 bg-image"></div>
        <div class="col-md-8 col-lg-6">
          <div class="login d-flex align-items-center py-5">
            <div class="container">
              <div class="row">
                <div class="col-md-9 col-lg-8 mx-auto">
                  <h3 class="login-heading mb-4">Welcome back!</h3>
    
                  <!-- Sign In Form -->
                  <form>
                    <div class="form-floating mb-3">
                      <input type="email" class="form-control" id="floatingInput" placeholder="name@example.com">
                      <label for="floatingInput">Email address</label>
                    </div>
                    <div class="form-floating mb-3">
                      <input type="password" class="form-control" id="floatingPassword" placeholder="Password">
                      <label for="floatingPassword">Password</label>
                    </div>
    
                    <div class="form-check mb-3">
                      <input class="form-check-input" type="checkbox" value="" id="rememberPasswordCheck">
                      <label class="form-check-label" for="rememberPasswordCheck">
                        Remember password
                      </label>
                    </div>
    
                    <div class="d-grid">
                      <button class="btn btn-lg btn-primary btn-login text-uppercase fw-bold mb-2" type="submit">Sign in</button>
                      <div class="text-center">
                        <a class="small" href="#">Forgot password?</a>
                      </div>
                    </div>
    
                  </form>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    ```

8. Selanjutnya, copy css yang tersedia

    ```css
    .login {
      min-height: 100vh;
    }
    
    .bg-image {
      background-image: url('https://source.unsplash.com/WEQbe2jBg40/600x1200');
      background-size: cover;
      background-position: center;
    }
    
    .login-heading {
      font-weight: 300;
    }
    
    .btn-login {
      font-size: 0.9rem;
      letter-spacing: 0.05rem;
      padding: 0.75rem 1rem;
    }
    ```

9. Pastikan lagi apakah kalian sudah copy semua code dari section yang ada (html,css,js)
    
10. Jika sudah, kalian bisa langsung insert kode yang sudah kalian salin ke project kalian
  
11. Jangan lupa untuk include resources yang di perlukan seperti bundle bootstrap, dll

12. Berikut adalah hasil dari kode yang di ambil dari web startbootstrap.com

    ![image](https://github.com/Komandro-CCIT/Komandro-Archive/assets/125471579/4224f45f-4823-4ac6-9ace-0a246c0b9136)

## Keuntungan dari menggunakan snippet bootstarp di project yang kita kerjakan

* Efisiensi: Bootstrap adalah kerangka kerja CSS yang populer dan banyak digunakan yang menawarkan snippet code yang siap pakai untuk berbagai komponen dan tata letak. Dengan menggunakan snippet Bootstrap, kita dapat menghemat waktu dan usaha dalam menulis kode CSS dan HTML dari awal. Kita dapat dengan cepat mengimpor snippet yang sesuai dengan kebutuhan kita dan menggunakannya dalam proyek kita.

* Responsif dan Kompatibilitas Lintas Browser: Bootstrap dirancang dengan responsif dalam pikiran. Dengan menggunakan snippet Bootstrap, kita dapat dengan mudah membuat tampilan situs web atau aplikasi kita responsif dengan berbagai perangkat dan ukuran layar. Selain itu, Bootstrap secara umum telah diuji dan dioptimalkan untuk kompatibilitas lintas browser, sehingga kita dapat yakin bahwa komponen dan tata letak yang kita gunakan akan berfungsi dengan baik di berbagai peramban web yang umum digunakan.

* Desain yang Menarik: Bootstrap menyediakan gaya dan tema yang siap pakai yang dapat memberikan tampilan yang menarik dan profesional untuk proyek kita. Dengan menggunakan snippet Bootstrap, kita dapat dengan mudah menerapkan kelas dan gaya yang telah ditentukan untuk membuat elemen tampilan seperti tombol, navbars, jumbotron, kartu, dan lainnya terlihat menarik dengan sedikit usaha.

* Konsistensi: Bootstrap menyediakan aturan dan panduan yang konsisten dalam pengembangan tampilan. Dengan menggunakan snippet Bootstrap, kita dapat memastikan bahwa tampilan dan perilaku komponen kita konsisten di seluruh proyek kita. Ini dapat membantu menciptakan pengalaman pengguna yang lebih baik dan memudahkan pemeliharaan kode di masa depan.

* Komunitas dan Dukungan: Bootstrap adalah kerangka kerja yang populer dengan komunitas yang besar dan aktif. Ada banyak sumber daya, dokumentasi, dan forum di mana kita dapat menemukan snippet code, tutorial, dan bantuan yang relevan. Menggunakan snippet Bootstrap memungkinkan kita untuk memanfaatkan pengetahuan dan pengalaman kolektif dari komunitas ini.

## Kesimpulan

Menggunakan kode snippet yang tersedia di internet memudahkan kita untuk meningkatkan efisiensi pengerjaan project yang sedang kita kerjakan, selain implementasi yang mudah dan cepat, snippet yang bagus dapat membuat web kita berkali-kali lebih indah, kebanyakan snippet yang tesedia juga sudah mendukung responsive dari perangkat perangkat lainnya seperti mobile, dekstop, dan lainnya.

---
Author : [Ifarra](https://github.com/Ifarra)
