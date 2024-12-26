# 9. Introduction to SaltStack

Author: Hudya

---

## Overview

Setelah mengenal tentang Localstack, kamu akan belajar mengenai salah satu IaC (Infrastructure as Code) yang bernama Salt. Lingkungan engineering ini bisa juga dikatakan dengan **SaltStack**.

## Salt

SaltStack adalah perangkat lunak sumber terbuka berbasis Python yang digunakan untuk otomatisasi TI, manajemen konfigurasi, dan eksekusi tugas jarak jauh. SaltStack menggunakan pendekatan deklaratif, yaitu pengguna menentukan kondisi akhir yang diinginkan, dan alat akan menentukan cara mencapai kondisi tersebut.

SaltStack memiliki beberapa fitur, di antaranya:

- Dapat menggunakan skrip yang ditulis dalam Python, atau merender skrip yang ditulis dalam bahasa lain seperti YAML atau JSON
- Menggunakan arsitektur master-slave dengan agen, atau beroperasi dalam mode tanpa agen
- Klien yang disebut "minion" dapat diperintah dan dikendalikan dari server perintah pusat yang disebut "master"
- Perintah biasanya dikeluarkan ke minion melalui master dengan memanggil skrip klien yang disebut 'salt'

## Pembuatan Server

Pertama kita memerlukan dua buah server, satu akan berfungsi sebagai server, yang satu lagi akan berfungsi sebagai minion.
Buat terlebih dahulu dua buah server dengan multipass:

```bash
multipass launch --name prod-ops-01 --memory 2G --disk 25GB
multipass launch --name prod-app-01 --memory 2G --disk 25GB
```

Kita akan menggunakan dua server, `prod-ops-01` akan berfungsi sebagai server salt sedangkan `prod-app-01` akan berfungsi sebagai minion, atau server yang akan disuruh-suruh untuk melakukan sesuatu.

## Instalasi Salt Master

Masuk ke server `prod-ops-01` lalu masukkan perintah berikut baris perbaris sesuai [tutorial salt](https://docs.saltproject.io/salt/install-guide/en/latest/topics/install-by-operating-system/linux-deb.html):

```bash
# Ensure keyrings dir exists
mkdir -p /etc/apt/keyrings
# Download public key
curl -fsSL https://packages.broadcom.com/artifactory/api/security/keypair/SaltProjectKey/public | sudo tee /etc/apt/keyrings/salt-archive-keyring.pgp
# Create apt repo target configuration
curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt.sources | sudo tee /etc/apt/sources.list.d/salt.sources
```

Kemudian jalankan perintah:

```bash
sudo apt update
```

Sekarang install `salt-master` pada `prod-ops-01`:

```bash
sudo apt install salt-master
```

Tunggu instalasi lalu jalankan perintah berikut untuk memastikan salt sudah terinstall:

```bash
sudo salt --version
```

Hasilnya menjadi seperti ini:

```bash
ubuntu@prod-ops-01:~$ sudo salt --version
salt 3007.1 (Chlorine)
```

Kemudian jalankan perintah berikut untuk memastikan `salt-master` berjalan ketika booting.

```bash
sudo systemctl enable salt-master && sudo systemctl start salt-master
```

## Konfigurasi Salt Master

Kita perlu melakukan konfigurasi untuk Salt Master, pertama masukkan perintah berikut:

```bash
cd /etc/salt
echo "*.salt.ops.int" | sudo tee /etc/salt/autosign.conf
```

Nantinya kita hanya akan otomatis menerima setiap host minion yang memiliki prefix nama `*.salt.ops.int`, mengapa kita perlu setting ini? Karena sebenarnya salt itu perlu menerima minion yang ingin dikelola, pada cloud server misalnya AWS, Google, Alibaba, semua network akan aman karena diatur pada sebuah blok yang bisa disebut VPC (Virtual private Cloud) atau jaringan lokal. Sehingga menkonfigurasi penerimaan host minion otomatis akan tetap aman.

Sekarang kita ubah main config masternya, masukkan perintah berikut:

```bash
sudo nano master
```

Hapus tanda pagar (#) pada sebelah kiri `default_include`, kalian boleh menggunakan `nano` atau `vim` dengan akses sudo.
Save dengan cara `CTRL + SHIFT + X` lalu tekan tombol `enter`.

```text
##### Primary configuration settings #####
##########################################
# This configuration file is used to manage the behavior of the Salt Master.
# Values that are commented out but have an empty line after the comment are
# defaults that do not need to be set in the config. If there is no blank line
# after the comment then the value is presented as an example and is not the
# default.

# Per default, the master will automatically include all config files
# from master.d/*.conf (master.d is a directory in the same directory
# as the main master config file).
default_include: master.d/*.conf
```

Perintah di atas bertujuan agar semua settingan dasar bisa kita tiban dengan file yang berada pada folder `master.d` dengan prefix file `*.conf`

Sekarang kita akan membuat konfigurasi dasar

```bash
cd master.d
sudo nano config.conf
```

Masukkan semua settingan di bawah ini:

```plain
interface: 0.0.0.0

auto_accept: True

autosign_file: /etc/salt/autosign.conf

file_roots:
  base:
    - /srv/salt_roots/salt/base

  dev:
    - /srv/salt_roots/salt/dev
    - /srv/salt_roots/salt/base

  prod:
    - /srv/salt_roots/salt/prod
    - /srv/salt_roots/salt/base


pillar_roots:
  base:
    - /srv/salt_roots/pillar/base

  dev:
    - /srv/salt_roots/pillar/dev
    - /srv/salt_roots/pillar/base

  prod:
    - /srv/salt_roots/pillar/prod
    - /srv/salt_roots/pillar/base
```

Sabar, nanti akan dijelaskan maksudnya apa konfigurasi di atas, tapi yang jelas fokus ke tiga saja terlebih dahulu:

- interface: Setting host ke 0.0.0.0 agar bisa diakses darimanapun
- auto_accept: Otomatis accept minion
- autosign_file: File prefix auto accept untuk host yang diatur.

Setelah selesai jangan lupa untuk restart server saltnya dengan perintah:

```bash
sudo systemctl restart salt-master
```

Kamu bisa memeriksa key minion dengan cara:

```bash
sudo salt-key
```

Hasilnya akan kosong:

```bash
ubuntu@prod-ops-01:~$ sudo salt-key
Accepted Keys:
Denied Keys:
Unaccepted Keys:
Rejected Keys:
```

Tenang saja, kita akan atur setelah minion telah terbuat.

Keluar dari `prod-ops-01` lalu jalankan perintah:

```bash
multipass list
```

Catat IPv4 `prod-ops-01` kalian karena akan dibutuhkan nanti, contoh:

```bash
hudya@perogeremmer-pc:~$ multipass list
Name                    State             IPv4             Image
prod-app-01             Running           10.129.14.5      Ubuntu 24.04 LTS
prod-ops-01             Running           10.129.14.125    Ubuntu 24.04 LTS
```

## Instalasi Salt Minion

Masuk ke `prod-app-01`. Lakukan hal yang sama untuk menginstall minion:

```bash
# Ensure keyrings dir exists
mkdir -p /etc/apt/keyrings
# Download public key
curl -fsSL https://packages.broadcom.com/artifactory/api/security/keypair/SaltProjectKey/public | sudo tee /etc/apt/keyrings/salt-archive-keyring.pgp
# Create apt repo target configuration
curl -fsSL https://github.com/saltstack/salt-install-guide/releases/latest/download/salt.sources | sudo tee /etc/apt/sources.list.d/salt.sources
```

Kemudian jalankan perintah:

```bash
sudo apt update
```

Sekarang install `salt-minion` pada `prod-app-01`:

```bash
sudo apt install salt-minion
```

Sekarang `salt-minion` sudah terinstall, tapi kita perlu menghubungkannya dengan server.

## Konfigurasi Salt Minion

Pertama kita tambahkan host master terlebih dahulu:

```bash
echo "<IPv4> prod-ops.salt.ops.int" | sudo tee -a /etc/hosts
```

Contoh:

```bash
echo "10.129.14.125 prod-ops.salt.ops.int" | sudo tee -a /etc/hosts
```

Sekarang coba ping

```bash
ping prod-ops.salt.ops.int
```

Kalau berhasil akan menjadi seperti ini:

```bash
ubuntu@prod-app-01:/etc/salt/minion.d$ ping prod-ops.salt.ops.int
PING prod-ops.salt.ops.int (10.129.14.125) 56(84) bytes of data.
64 bytes from prod-ops.salt.ops.int (10.129.14.125): icmp_seq=1 ttl=64 time=1.03 ms
64 bytes from prod-ops.salt.ops.int (10.129.14.125): icmp_seq=2 ttl=64 time=0.710 ms
64 bytes from prod-ops.salt.ops.int (10.129.14.125): icmp_seq=3 ttl=64 time=0.850 ms
64 bytes from prod-ops.salt.ops.int (10.129.14.125): icmp_seq=4 ttl=64 time=0.887 ms
64 bytes from prod-ops.salt.ops.int (10.129.14.125): icmp_seq=5 ttl=64 time=0.578 ms
```

Sekarang pergi ke `/etc/salt` dengan cara:

```bash
cd /etc/salt
```

Ubah id minion pada file `minion_id` dengan cara:

```bash
echo "prod-app-01.salt.ops.int" | sudo tee /etc/salt/minion_id
```

Sekarang kita ubah main config minionnya, masukkan perintah berikut:

```bash
sudo nano minion
```

Hapus tanda pagar (#) pada sebelah kiri `default_include`, kalian boleh menggunakan `nano` atau `vim` dengan akses sudo.
Save dengan cara `CTRL + SHIFT + X` lalu tekan tombol `enter`.

```bash
##### Primary configuration settings #####
##########################################
# This configuration file is used to manage the behavior of the Salt Minion.
# With the exception of the location of the Salt Master Server, values that are
# commented out but have an empty line after the comment are defaults that need
# not be set in the config. If there is no blank line after the comment, the
# value is presented as an example and is not the default.

# Per default the minion will automatically include all config files
# from minion.d/*.conf (minion.d is a directory in the same directory
# as the main minion config file).
default_include: minion.d/*.conf
```

Sekarang masukkan perintah berikut:

```bash
cd minion.d
echo "master: prod-ops.salt.ops.int" | sudo tee config.conf
```

Restart minionnya:

```bash
sudo systemctl restart salt-minion
```

## Kembali ke Salt Master

Sekarang masuk kembali ke server salt master, lalu jalankan perintah berikut:

```bash
sudo salt-key
```

Apabila kamu melakukannya dengan benar maka kamu akan menemukan hasil seperti ini:

```bash
ubuntu@prod-ops-01:~$ sudo salt-key
Accepted Keys:
prod-app-01.salt.ops.int
Denied Keys:
Unaccepted Keys:
Rejected Keys:
```

Server `prod-app-01` sudah berhasil kita terima sebagai minion. Sekarang kita juga bisa memastikannya apakah servernnya menyala dengan perintah berikut:

```bash
sudo salt prod-app-* test.ping
```

Hasilnya:

```bash
ubuntu@prod-ops-01:~$ sudo salt prod-app-* test.ping
prod-app-01.salt.ops.int:
    True
```

Kita coba perintahkan minion kita untuk melihat isi direktori /etc/salt

```bash
sudo salt prod-app-* cmd.run "ls /etc/salt"
```

Hasilnya:

```bash
ubuntu@prod-ops-01:~$ sudo salt prod-app-* cmd.run "ls /etc/salt"
prod-app-01.salt.ops.int:
    minion
    minion.d
    minion_id
    pki
    proxy
    proxy.d
```

Kita juga bisa menyuruhnya update apt.

```bash
sudo salt prod-app-* cmd.run "sudo apt update -y"
```

Hasilnya:

```bash
ubuntu@prod-ops-01:~$ sudo salt prod-app-* cmd.run "sudo apt update -y"
prod-app-01.salt.ops.int:
    
    WARNING: apt does not have a stable CLI interface. Use with caution in scripts.
    
    Hit:1 http://archive.ubuntu.com/ubuntu noble InRelease
    Hit:2 http://security.ubuntu.com/ubuntu noble-security InRelease
    Get:3 http://archive.ubuntu.com/ubuntu noble-updates InRelease [126 kB]
    Hit:4 https://packages.broadcom.com/artifactory/saltproject-deb stable InRelease
    Hit:5 http://archive.ubuntu.com/ubuntu noble-backports InRelease
    Fetched 126 kB in 3s (41.4 kB/s)
    Reading package lists...
    Building dependency tree...
    Reading state information...
    44 packages can be upgraded. Run 'apt list --upgradable' to see them.
```

Keren bukan?



