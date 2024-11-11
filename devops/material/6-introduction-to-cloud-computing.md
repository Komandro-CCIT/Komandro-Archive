# 6. Introduction to Cloud Computing

Author: Hudya

---

## Overview

Setelah mempelajari tools demi tools, sekarang kamu akan mempelajari sedikit teori tentang cloud computing.

Cloud computing pada dasarnya adalah penggunaan sumber daya komputasi (seperti server, penyimpanan, database, jaringan, perangkat lunak, dan layanan lainnya) melalui internet, tanpa perlu mengakses atau mengelola infrastruktur fisik secara langsung.

Mungkin kamu pernah mendengar, atau kenal dengan orang yang bekerja di bidang IT dan dekat dengan server. Tentu pernah mendengar betapa dinginnya ruang server.

Nah ruang server yang berada di dekat orang IT tersebut belum tentu dikatakan sebagai cloud computing, karena akses ke server harus melalui internet. Artinya orang IT yang mengakses server secara langsung melalui jaringan yang sama tidak dapat dikatakan dengan Cloud Computing.

Ada banyak penyedia layanan cloud computing dari perusahaan besar seperti Amazon Web Service, Google Cloud Computing, Microsoft Azure, Alibaba Cloud.

Provider lokal juga menyediakan layanan cloud computing seperti DewaWeb, IDCloudhost, Niagahoster, dan lainnya.

## Keuntungan

Penggunaan Cloud Computing sangat menguntungkan, terutama untuk para startup yang baru membuat produk secara online.

Kamu sebagai indiehacker atau bahkan programmer yang sedang belajar juga dapat menggunakan cloud computing.

Nah mengapa sebagian perusahaan menggunakan cloud computing?

- **Skalabilitas**: Cloud computing memungkinkan pengguna untuk dengan mudah meningkatkan atau menurunkan kapasitas server sesuai kebutuhan.
- **Pay-as-you-go**: Pengguna hanya membayar untuk sumber daya yang mereka gunakan tanpa memikirkan listriknya.
- **Aksesibilitas**: Sumber daya dapat diakses dari mana saja dengan koneksi internet.
- **Keandalan**: Penyedia layanan cloud biasanya menjamin bahwa server tidak akan down.
- **Keamanan**: Penyedia layanan cloud umumnya memiliki sistem keamanan yang canggih salah satunya adalah pencegahan serangan DDoS.
- **Jenis layanan**: Ada berbagai jenis layanan cloud, seperti Infrastructure as a Service (IaaS), Platform as a Service (PaaS), dan Software as a Service (SaaS).
- **Shared resources**: Sumber daya biasanya dibagi di antara banyak pengguna, meskipun secara logis terpisah.

## Diagram Cloud Computing

Teori bagaimana menggambarkan akses pengguna ke cloud computing itu sederhana. Perhatikan diagram di bawah ini.

```mermaid
graph LR
    A[Pengguna] -->|Internet| B(Cloud)
    B --> C[Aplikasi]
    C --> F[Database]

    subgraph "Layanan Cloud"
    C
    F
    end
```

Pengguna akan mengakses layanan cloud melalui internet dimana layanan cloud yang kita bisa anggap server (Virtual machine) berisi aplikasi atau database.

## Latihan

Sebenarnya untuk berlatih Cloud Computing, secara tidak langsung kamu sudah melakukannya, yaitu dengan **Multipass**.

Multipass kita simulasikan sebagai sebuah server agar dapat kalian akses secara langsung, meskipun tidak dapat dikatakan sebagai cloud computing, namun experience yang kalian dapatkan akan sama saja.

Kalian bisa mengakses server melalui IP Address pada saat menampilkannya melalui perintah `multipass list`.

Menggunakan perintah `sudo ssh username@ip-address` kalian akan diminta memasukkan password.

Selanjutnya, kamu dapat menggunakan public key dan private key.

```mermaid
sequenceDiagram
    participant Client
    participant Server

    Note over Client,Server: Authentication Process
    Client->>Server: Request connection
    Server->>Client: Challenge
    Client->>Client: Sign challenge with private key
    Client->>Server: Send signed challenge
    Server->>Server: Verify signature with public key
    Server->>Client: Grant access if verified
```

Proses autentikasi ini jauh lebih aman dibandingkan menggunakan password, karena:

1. Tidak ada password yang dikirim melalui jaringan.
2. Private key tetap di komputer pengguna, sulit dicuri.
   Kunci sangat panjang dan kompleks, hampir mustahil ditebak.
3. Tahan terhadap serangan brute force dan phishing.
4. Lebih mudah mengelola akses pengguna.
5. Memungkinkan login otomatis yang aman.

Bagaimana cara menggeneratenya?

Pertama, bukalah powershell apabila menggunakan windows atau terminal apabila kamu menggunakan mac / linux.

Kedua, pergi ke sebuah folder yang kamu ingin simpan di tempat tersebut keynya. Kemudian masukan perintah berikut:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

apabila bermasalah, sepertinya sistem kamu tidak support algoritma Ed25519, maka kita ganti dengan:

```bash
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"
```

> [!NOTE]
> Harap ganti `your_email@example.com` dengan email kamu.

Nantinya kamu akan ditanya mau disimpan dengan nama apa, misalnya tulis saja `my-key`.

Kemudian kamu akan ditanya password, cukup tekan tombol enter saja dan tidak perlu diberi password.

Kemudian tekan tombol enter sekali lagi untuk konfirmasi.

Masukkan perintah `dir` atau `ls` untuk melihat isi folder kamu.

![Alt text](./assets/6-introduction-to-cloud-computing/1.gif)

Berdasarakan gambar di atas, kamu dapat melihat terdapat dua buah file, yaitu `my-key` sebagai private key dan `my-key.pub` sebagai public key.

Kurang lebih isi private key saya seperti ini:

```plain
-----BEGIN OPENSSH PRIVATE KEY-----
b3BlbnNzaC1rZXktdjEAAAAABG5vbmUAAAAEbm9uZQAAAAAAAAABAAACFwAAAAdzc2gtcn
NhAAAAAwEAAQAAAgEAzw+
.
-----END OPENSSH PRIVATE KEY-----
```

Dan isi public keynya seperti ini:

```plain
ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAACAQDPD6m4RT/pwRYp57g20pQ37z0+zTWlOpR1C+3kGz2iwA98dbJSIHgS0Ljl5/Rpq/lPyHEvenrl1jQrffUKutUzto8N83nYcICD9HZn7IceoOZSz9jkjBPgRDOl0wuozRMBwI/2lxpsXia8fsvvkM96mKuVV+Ovvlls+Ui9NIkW40m3pNHMc+2SIcvyayIJEF0shnVgvSOJvCNCdMOudv/Z4PcSam2x5AZzt9K7CuMlzpuuvce4t9fsdwo6uVHbF3RVuhgMSf5wIN8zG3hNvfM1w78hXrvlE4sxTbaotgeqZNAH2kp+9kYrp8SJP7n8lBp7jesJCD3AFW0/4MxV+M5Jwsq5mv9P95k6p1I/NUKyQolL/pjxr9PAqbvc+iXb1gwoBQcp5Zx8vLLA0EldnUoeZuPMbdqqbIOvrhL1DyukanOreKbDM+81fCW2Q5fJgqVNcsIW0oYaW5kqrTC9fpYGObUiN7F+Nu5+zmPH5tfHa3H1sKx7qeYJ05YJnLcDdF1AJ090FgQ0hdi9EpUeX+s4Wo/wY9wc52RQzOO2516GFIxZavIF72yL2agiCyjfWQfnclurwGUjExna3XGX9ys6c19ZzANoP5J9S49MNck2oMV9cw9D6wEaiP5CKfgr0BcksYalHqaEd/tdtcSoI4yYhM3zJqh+vuzmWs8MPKKkqw== mhudyaramadhana@gmail.com
```

Key ini akan digunakan untuk melakukan autentikasi, public key akan disimpan di server tujuan, sedangkan private key akan disimpan pada mesin kalian.

Sekarang pergi ke server multipass kalian lalu masuk ke folder `/home/ubuntu/.ssh`. Perhatikan GIF berikut:

![Alt text](./assets/6-introduction-to-cloud-computing/2.gif)

Kita masukkan isi key public yang telah dibuat pada file bernama `authorized_keys` di folder `.ssh` menggunakan `nano`.

Sekarang kamu bisa SSH menuju servermu dengan public key.

Perintahnya adalah:

```bash
sudo ssh -i privatekeynya username@ip-multipass
```

Perhatikan contoh di bawah ini:

```bash
hudya@Zorin-OS-Hudya:~/Documents/.ssh$ multipass list
Name                    State             IPv4             Image
my-server               Running           10.222.49.159    Ubuntu 24.04 LTS

hudya@Zorin-OS-Hudya:~/Documents/.ssh$ sudo ssh -i my-key ubuntu@10.222.49.159
[sudo] password for hudya:

The authenticity of host '10.222.49.159 (10.222.49.159)' can't be established.
ECDSA key fingerprint is SHA256:TZaueNcVEPxKx0Ghg8ryTE/aeZP1dVuwve2HKK5Rh5U.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
```

Kemudian apabila berhasil kamu akan melihat servermu seperti ini:

```bash
Warning: Permanently added '10.222.49.159' (ECDSA) to the list of known hosts.
Welcome to Ubuntu 24.04.1 LTS (GNU/Linux 6.8.0-45-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/pro

 System information as of Mon Nov 11 16:29:20 WIB 2024

  System load:  0.08               Processes:             122
  Usage of /:   14.8% of 23.17GB   Users logged in:       0
  Memory usage: 26%                IPv4 address for ens3: 10.222.49.159
  Swap usage:   0%

 * Strictly confined Kubernetes makes edge and IoT secure. Learn how MicroK8s
   just raised the bar for easy, resilient and secure K8s cluster deployment.

   https://ubuntu.com/engage/secure-kubernetes-at-the-edge

Expanded Security Maintenance for Applications is not enabled.

19 updates can be applied immediately.
To see these additional updates run: apt list --upgradable

Enable ESM Apps to receive additional future security updates.
See https://ubuntu.com/esm or run: sudo pro status


*** System restart required ***
Last login: Mon Nov 11 16:15:41 2024 from 10.222.49.1
ubuntu@my-server:~$
```
