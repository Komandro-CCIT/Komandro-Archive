# Excercise 1 : Managing Files

---

Creating and Managing Files and Folder Based on Their Extension

---

Dalam latihan ini, Kalian akan mengatur folder dan file berdasarkan ekstensinya menggunakan perintah Linux.

## Objective

Mempelajari cara mengelola dan mengimplementasikan struktur direktori dengan mengelompokkan file dan subfolder berdasarkan ekstensi ke dalam folder terpisah sesuai jenis file.

## Outcomes 

Peserta akan mampu mengelola file dan folder berdasarkan ekstensi, termasuk memindahkan dan mengatur file secara efisien ke dalam direktori yang sesuai menggunakan perintah Linux.

**1.**  Pada multipass, `launch` atau buka `shell` instance kalian.
  <details>
    <summary>Lihat Solusi</summary>
    <code>multipass --launch lab-excercise</code><br />
    <code>multipass shell lab-excercise</code>
  </details>

<br />

**2**.  Pastikan kalian di `home`, buat tiga buah folder untuk file berbentuk `assets`, `source`  dan `etc` kemudian beri nama belakangnya `folder`.
  <details>
    <summary>Lihat Solusi</summary>
    <code>cd /home/ubuntu</code><br />
    <code>mkdir {assets,sources,etc}-folder</code>
  </details>

<br />

**3**.  Buatlah 5 file `kosong` bernama source berekstensi `.js` dan 5 bernama front, 2 file bernama database dengan ekstensi `.db`, 1 dari ekstensi `.css` bernama style, 5 dari ekstensi `.jpg` bernama gambar, 3 dari `.gif` bernama gif, dan 3 dari `.mp3` bernama audio.
  <details>
    <summary>Lihat Solusi</summary>
    <code>touch {source,front}{1..5}.js ; touch database{1,2}.db</code><br />
    <code>touch style.css ; touch gambar{1..5}.jpg</code><br />
    <code>touch gif{1,2,3}.gif ; touch audio{1..3}.mp3</code>
  </details>

<br />

**4**.  Sekarang coba `konfirmasi` bahwa file kosong dan folder kosong sudah dibuat dan pastikan `tipe` nya
  <details>
    <summary>Lihat Solusi</summary>
    <code>ls -l</code><br />
    <code>file * > etc-folder/type.txt</code><br />
    <code>cat etc-folder/type.txt</code>
  </details>

<br />

**5**.  Kemudian buat folder baru dan buat ini sebagai `subfolder`, yang pertama dibawah assets buat folder bernama audio, image, dan gif folder, lakukan hal yang sama dengan source tetapi dengan nama frontend dan backend folder.
	<details>
	  <summary>Lihat Solusi</summary>
	    <code>mkdir -p assets-folder/{audio,image,gif}</code><br />
	    <code>mkdir -p sources-folder/{frontend,backend}</code>
	</details>

<br />

**6**.  Pindahkan `semua` yang bernama source dan semua file bernama database ke folder `backend` dan pindahkan semua file yang bernama frontend ke folder `frontend`.
	<details>
	  <summary>Lihat Solusi</summary>
	    <code>mv front* *.css sources-folder/frontend</code><br />
	    <code>mv database* *.js sources-folder/backend</code><br />
	</details>

<br />

**7**. Sama seperti tadi, sekarang pindahkan dan `sesuaikan` sisa file yang ada ke direktori masing-masing berdasarkan ekstensinya.
	<details>
	  <summary>Lihat Solusi</summary>
	    <code>mv gif* assets-folder/gif</code><br />
	    <code>mv gambar* assets-folder/image</code><br /> 
	    <code>mv audio* assets-folder/audio</code>
	</details>

<br />

**8**.  Konfirmasi bahwa semua file sudah tergoranisir berdasarkan folder tujuannya serta ekstensinya.
	<details>
	  <summary>Lihat Solusi</summary>
	    <code>ls assets-folder/gif assets-folder/image assets-folder/audio sources-folder/frontend sources-folder/backend > etc-folder/manage-structure.txt</code><br />
	    <code>cat etc-folder/manage-structure.txt</code>
	</details>

**9**.  Jika sudah selesai hapus semua file dan folder yang ada.
	<details>
	  <summary>Lihat Solusi</summary>
	    <code>rm -rf *</code>
	</details>

Selamat kalian sudah bisa menguasai bagaimana caranya mengatur file dan folder berdasarkan ekstensi 🥳.

Shoutout buat kalian yang tidak sama sekali melihat solusi 😎.
