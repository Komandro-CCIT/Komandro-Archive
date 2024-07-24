
# Dark Mode Design Principles

<p align="center">
  <img src="https://cdn.sanity.io/images/ldtsy7j0/production/e55fcda32b88782ddf546602b72e9c80bfc7429b-1600x1200.png" width="50%">
</p>

Dark mode adalah tema interface yang di sukai banyak orang, selain tampilannya yang elegan kabarnya dark mode juga dapat meningkatkan lifespan battery user, lebih dari 80% user memilih untuk menggunakan dark mode sebagai tema UI mereka, oleh karena itu banyak developer web dan perangkat lunak lain yang memilih untuk menjadikan dark mode sebagai tema utama untuk aplikasi mereka.

Dengan banyaknya pengguna yang lebih menyukai dark mode ketimbang light mode, apa saja sih yang harus di pikirkan dan yang menjadi point penting dalam pengmbangan mode gelap ini, berikut adalah best practices dari penerapan dark mode.

## Dark mode meningkatkan aksesibilitas

<p align="center">
  <img src="https://www.shutterstock.com/blog/wp-content/uploads/sites/5/2019/06/Visual-Hierarchy-Featured-Image.jpg" width="50%">
</p>

Berdasarkan reserch dari sebuah institut di Düsseldorf yang meneliti efek dark mode pada membaca, Peserta perlu mendeteksi celah dalam bagan visual Landolt C dan mengidentifikasi kesalahan dalam bagian kecil. Hasil penelitian menunjukkan bahwa light mode berkinerja sedikit lebih baik, tetapi perbedaannya dapat diabaikan. 

Tim peneliti lain di MIT mempelajari efek dark mode pada polaritas kontras Peserta harus membedakan karakter dalam light mode vs dark mode, siang vs malam, dan pada ukuran font yang berbeda Hasilnya adalah pengaruh pencahayaan sekitar pada polaritas kontras Pada siang hari, kedua mode berperforma serupa, tetapi pada simulasi malam hari, mode terang lebih baik.

Sebuah tim di University of Minnesota menemukan bahwa dark mode mungkin lebih baik untuk orang-orang dengan cloudy ocular media. Hipotesisnya adalah bahwa layar memancarkan lebih sedikit cahaya dan cahaya itu kurang tersebar.

Temuan ini tampaknya tidak konklusif. Opsi terbaik adalah mengizinkan pengguna beralih ke dark mode jika mereka mau. Beberapa orang lebih suka tampilan modern yang ramping, sementara ada manfaat nyata bagi orang-orang dengan cacat visual tertentu. 

## Dark mode menghemat battery

Selain looks yang elegant, dark mode ternyata juga dapat meghemat battery di device tertentu dengan OLED screen, alasannya karena setiap pixel di generate secara indivisual dan black pixels tidak menggunakan power dari battery yang banyak.

Berbeda dengan LCD, Layar LCD menggunakan backlight. Ini berarti bahwa panel di belakang layar menghasilkan cahaya putih konstan setiap kali layar menyala. Jadi, meskipun layarnya hitam, jumlah cahaya yang dipancarkannya sama, dan mode gelap tidak ada bedanya. Hampir semua laptop memiliki layar LCD, serta sebagian besar monitor desktop.

Layar OLED, sebagian besar digunakan di smartphone, Perangkat semacam itu terbukti hemat daya dan memiliki kapasitas baterai yang lebih besar. Di masa depan, kita mungkin akan melihat lebih banyak layar OLED, yang berarti mode gelap akan terus populer di masa depan.

## Dark mode membuat tampilan aesthetic

<p align="center">
  <img src="https://www.easeout.co/images/uploads/unix-dark-mode.png" width="50%">
</p>

Meskipun beberapa orang menganggap mode gelap sebagai tren desain baru-baru ini, sebenarnya dark mode lebih tua dari yang kamu pikirkan. Penggunaannya yang paling awal kembali ke zaman monitor CRT lama yang menampilkan teks hijau dengan latar belakang hitam.

Di zaman sekarang, dark mode di lihat sebagai pilihan design, dan tidak bisa dipungkiri bahwa dark mode memang mempunyai tampilan yang aesthetic, Orang lebih suka dark mode saat bekerja di malam hari atau di lingkungan yang remang-remang. Tampaknya juga sempurna untuk hiburan larut malam. Saat menonton Netflix di malam hari, mode gelap menciptakan suasana berada di bioskop.

## Hindari transisi langsung dari putih ke hitam

<p align="center">
  <img src="https://atmos.style/images/blog/dark-mode-ui-best-practices/shadows.png" width="50%">
</p>

Mendapatkan dark mode yang tepat membutuhkan beberapa upaya dari desainer. Percaya atau tidak, orang tidak hanya membalik warna untuk membuat pallete dark mode. Melakukan hal itu akan merusak konsistensi tata letak, mengurangi hirarki keseluruhan, dan sangat menurunkan keterbacaan.

Triknya adalah menggunakan kontras yang dimodifikasi berdasarkan branding yang ada. Mulai dari warna dasar - tentukan warna primer dan sekunder serta warna untuk permukaan, termasuk latar belakang halaman dan komponen. Jangan lupa untuk memastikan mereka memenuhi rasio kontras 4.5:1 untuk teks normal.

## Gunakan desaturated colors

<p align="center">
  <img src="https://www.color-hex.com/palettes/101587.png" width="50%">
</p>

Saturasi menggambarkan kemurnian, intensitas, dan kekayaan warna. Warna-warna yang sangat jenuh (saturated) adalah warna-warna yang padat dan vibran, dan tidak mengandung abu-abu. Sayangnya, warna-warna tersebut sulit untuk lulus uji rasio kontras warna WCAG (Web Content Accessibility Guidelines). Sebaliknya, warna-warna yang kurang jenuh (desaturated) lebih mungkin untuk memenuhi standar AA, yaitu setidaknya 4.5:1 untuk rasio kontras warna dengan teks utama. Selain itu, warna-warna yang kurang jenuh juga lebih nyaman bagi mata di latar belakang gelap.

## Jaga identitas brand

<p align="center">
  <img src="https://th.bing.com/th/id/OIP.rqBISYw_vgZY8sFpkDPnIQHaEo?rs=1&pid=ImgDetMain" width="50%">
</p>

Warna gelap mendominasi dalam dark mode, jika warna merek Anda berada di sisi yang lebih terang, apakah Anda harus mengubahnya? Material Design (google) menganggap baik-baik saja untuk menggunakan warna merek yang saturated asalkan tidak berlebihan. Gunakan warna-warna ini hanya untuk elemen merek yang paling menonjol, seperti logo atau tombol bermerek. Hal ini akan membantu mempertahankan identitas merek Anda tanpa merusak hirarki visual.

## Hindari mengunakan pure black (hitam pekat)

<p align="center">
  <img src="https://th.bing.com/th/id/OIP.ngCYD3qjOrJxX6q_flKDSQHaE2?rs=1&pid=ImgDetMain" width="50%">
</p>

Hitam pekat bukanlah pilihan yang baik. Secara paradoks, dark mode jarang mengandung hitam pekat, karena dapat sangat merusak keterbacaan. Sebaliknya, Material Design (google) merekomendasikan menggunakan abu-abu gelap (#121212) sebagai warna latar belakang gelap. Selain itu, bayangan drop lebih terlihat jelas di latar belakang abu-abu dan menciptakan kesan kedalaman yang jauh lebih baik.

## Jaga kontras text

<p align="center">
  <img src="https://th.bing.com/th/id/OIP.adVpjdvCaxzD3gCsPgdS2wHaFe?rs=1&pid=ImgDetMain" width="50%">
</p>

Berikan perhatian khusus pada kontras warna teks. Menurut WCAG, rasio kontras warna harusnya tidak kurang dari 4.5:1 untuk teks berukuran normal. Teks berukuran besar (yang setara dengan sekitar 24px atau 18.5px jika tebal) harus memiliki rasio kontras setidaknya 3:1. Juga, ingatlah bahwa teks putih memerlukan rasio 15.8:1.

Gunakan alat pemeriksa kontras [WebAIM](https://webaim.org/resources/contrastchecker/) atau [Coolors](https://coolors.co/contrast-checker/112a46-acc8e5) untuk mengecek apakah rasio kontras warna sudah cukup.

## Perbaiki kontrast warna "Error"

<p align="center">
  <img src="https://thewidlarzgroup.github.io/react-native-notificated/assets/images/error-darkMode-32f76a3e561eaaf7252e67b7dcd4ceaa.png" width="50%">
</p>


Salah satu cara untuk memastikan visibilitas dari element design yang penting dan menarik perhatian adalah menggunakan rasio kontras yang tepat.

Error message dalam aplikasi juga serupa pentingnya. Itulah sebabnya mereka harus memiliki kontras warna yang tinggi dan segera dapat dikenali. Material Design (google) merekomendasikan menggunakan overlay semi-transparan dengan 40% opacity di atas warna merah mode terang untuk "error". Warna kesalahan asli adalah #B00020, yang diubah menjadi #CF6679 dengan overlay 40% putih.

## Gunakan elevasi untuk memberikan efek depth

<p align="center">
  <img src="https://miro.medium.com/max/5600/1*np0nAiO3uIudlUcvcPUwPQ.jpeg" width="50%">
</p>

Depth membantu menciptakan hirarki visual dan menekankan elemen-elemen yang memiliki prioritas tinggi. Sebagai contoh, kamu mungkin ingin menarik perhatian pengguna pada tombol CTA atau notifikasi peringatan. Bagaimana kamu dapat menciptakan ilusi depth dalam mode gelap? Dalam mode terang, desainer biasanya menggunakan bayangan, tapi bayangan tersebut tidak terlalu menonjol di latar belakang gelap.

Praktik terbaik dalam dark mode adalah menciptakan elevasi (ketinggian). Kamu dapat melakukan ini dengan mengembangkan sistem layer dengan warna-warna yang lebih terang untuk level yang lebih tinggi dan lebih gelap untuk level yang lebih rendah. Cara lain untuk melakukannya adalah dengan menerapkan overlay dengan transparansi yang bervariasi untuk hasil yang sama. Gunakan tingkat transparansi yang lebih tinggi untuk elemen-elemen penting seperti tombol dan tingkat yang lebih rendah untuk latar belakang.

## Gunakan bayangan dengan benar

<p align="center">
  <img src="https://monsterspost.com/wp-content/uploads/2020/04/DARK-MODE-UI-DESIGN-9.jpg" width="50%">
</p>

Di light mode, designer memberikan efek depth pada elemen design dengan menggunkaan shadows, akan tetapt di dark mode shadow tidak terlalu efektif untuk memberikan efek depth pada elemen design, dikarenakan bayangan tidka terasa natural jika tidak ada light source di linkungan yang gelap

Sebagai gantinya, gunakan elevasi. Semakin tinggi elevasi suatu permukaan, semakin terang permukaan tersebut. Jika Anda masih ingin menggunakan bayangan, tetaplah menggunakan abu-abu gelap sebagai warna latar belakang. Dibandingkan dengan hitam pekat, permukaan abu-abu gelap dapat jauh lebih baik dalam mengungkapkan kontras, elevasi, dan kedalaman.

## berikan opsi untuk on/off dark mode

<p align="center">
  <img src="https://monsterspost.com/wp-content/uploads/2020/04/DARK-MODE-UI-DESIGN-9.jpg" width="50%">
</p>

Kamu mungkin mulai bertanya-tanya apakah produk Anda bahkan membutuhkan dark mode. Ada banyak alasan mengapa pengguna mungkin ingin beralih ke dark mode. Beberapa orang lebih suka bekerja dan bersantai di lingkungan yang redup, sementara yang lain lebih suka desain gelap. Ada juga manfaat bagi orang-orang dengan gangguan visual tertentu. Manfaat memiliki opsi mode gelap tentu saja jauh lebih besar daripada upaya yang dihabiskan untuk merancangnya.

Ingatlah bahwa pengguna senang memiliki pilihan dan berada dalam kendali. Jadi, berikan mereka pilihan untuk mengubah pengaturan default dan mengaktifkan/menonaktifkan mode gelap!

## Author
Author : [Ifarra](https://github.com/Ifarra)