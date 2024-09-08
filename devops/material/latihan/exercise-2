# Excercise 2: Creating Backup Files with Timestamp Along With Source and Destination Folder
***

#### Dalam latihan ini, Kalian akan mencoba membuat file menggunakan stempel waktu, serta menentukan folder source dan destination menggunakan perintah Linux.

**Objective:**

Memahami dan mempraktikkan pembuatan file cadangan dengan stempel waktu menggunakan perintah Linux, serta mengatur folder sumber (source) dan tujuan (destination) untuk menyimpan file tersebut.

**Outcomes:**

Peserta akan dapat membuat file cadangan dengan stempel waktu yang unik, menentukan dan menggunakan direktori sumber dan tujuan yang berbeda, serta mengembangkan pemahaman yang lebih baik tentang manajemen file dan direktori di lingkungan Linux.

**1.**  Di Multipass, jalankan perintah `launch` dan buka `shell` instance kalian, lalu pastikan kalian berada di direktori `home`.
  <details>
    <summary>Lihat Solusi</summary>
    <code>multipass shell lab-excercise</code><br />
    <code>cd /home/ubuntu</code>
  </details>

<br />

**2.**  Buatlah sebuah folder `Projects` yang berisikan 1 file kosong bernama `telltime` berekstensikan `.sh`. 
  <details>
    <summary>Lihat Solusi</summary>
    <code>mkdir Projects ; touch Projects/telltime.sh</code>
  </details>

<br />

**3.**  Buka file kosong yang baru didalam source folder dengan `vim` lalu buat function sederhana untuk menampilkan waktu menggunakan command `date`.
  <details>
    <summary>Lihat Solusi</summary>
    <pre>#!/bin/bash

function show_time() {
  echo "Current time: $(date)"
}

show_time</pre></details>

<br />

**4.**  Pastikan scriptnya bisa di `execute` dan coba jalankan scriptnya. 
  <details>
    <summary>Lihat Solusi</summary>
    <code>chmod +x Projects/telltime.sh</code><br />
    <code>Projects/telltime.sh</code>
  </details>

<br />

**5.**  Sekarang buatlah sebuah folder baru bernama `Backups` dan buat juga `subfoldernya` dengan nama tahun 2024. 
  <details>
    <summary>Lihat Solusi</summary>
    <code>mkdir -p Backups/2024</code>
  </details>

<br />

**6.**  Buat variabel global bernama `TIMESTAMP` di commandline interface, beri valuenya dengan command `date` dan spesifikan waktunya berdasarkan `YYYY-MM-D_Dhh:mm:ss` gunakan man untuk melihat formatnya lalu pastikan variabelnya terbuat. 
  <details>
    <summary>Lihat Solusi</summary>
    <code>TIMESTAMP=$(date "+%Y-%m-%d_%H:%M:%S")</code><br />
    <code>echo $TIMESTAMP</code>
  </details>

<br />

**7.**  Sekarang `Backup` file `telltime.sh` dengan folder `Backups/2024` sebagai destination dan beri ekstensi `tar.gz` menggunakan perintah `tar` linux, gunakan man untuk caranya, dan beri nama file backup tersebut dengan variabel `TIMESTAMP` yang baru dibuat.
  <details>
    <summary>Lihat Solusi</summary>
    <code>cd Projects ; tar -c -f ../Backups/2024/$TIMESTAMP.tar.gz telltime.sh</code>
  </details>

<br />

**8.**  Buka kembali file `telltime.sh` dengan vim lalu tambahkan fitur input masukan nama dan berikan output menyapa serta memberi tahu waktu yang sekarang.
  <details>
    <summary>Lihat Solusi</summary>
    <pre>#!/bin/bash

function show_time() {
	  read -p "Please enter your name: " name
	  echo "Hello, $name!"
	  echo "Right now is $(date) at Asia/Jakarta timezone"
	}
	
show_time</pre></details>

<br />

**9.**  Coba jalankan script `telltime.sh` lalu backup lagi filenya dengan cara yang sama sebelumnya tetapi jalankan variabel `TIMESTAMP` lagi sebelum membackup, kemudian hapus `telltime.sh` nya.
  <details>
    <summary>Lihat Solusi</summary>
	<code>./telltime.sh</code><br />
	<code>TIMESTAMP=$(date "+%Y-%m-%d_%H:%M:%S") ; tar -cf ../Backups/2024/$TIMESTAMP.tar.gz telltime.sh</code><br />
	<code>rm telltime.sh</code></details>

<br />

**10.**  Selanjutnya `ekstrak` script yang sebelumnya dihapus dengan file `backup` yang sudah dibuat dengan menggunakan perintah `tar` kedalam `source` directory, lihat man untuk caranya.
  <details>
    <summary>Lihat Solusi</summary>
	<code>tar -x -f ../Backups/2024/#archiveyangterbaru -C /home/ubuntu/Projects</code>
  </details>

<br />

**11.**  Terakhir hapus semua file dan folder yang ada.
  <details>
    <summary>Lihat Solusi</summary>
	<code>cd .. ; rm -rf *</code>
  </details>

<br />

Selamat kalian sudah bisa menguasai caranya membackup sebuah file berdasarkan source dan destination folder 🥳.

Salute buat kalian yang sama sekali tidak melihat solusi 😎.
