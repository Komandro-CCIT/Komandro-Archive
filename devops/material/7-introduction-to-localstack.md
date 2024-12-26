# 7. Introduction to Localstack

Author: Hudya

---

## Overview

Setelah mengenal tentang cloud computing, kamu akan belajar mengenai localstack. Pada dasarnya ketika memahami cloud, kita perlu menggunakan layanan yang sudah disediakan di cloud, salah satunya adalah AWS (Amazon Web Service). Masalahnya adalah, menggunakan layanan cloud tersebut akan memerlukan biaya, untuk mahasiswa maka biaya tersebut menjadi tidak make sense.

Lantas, apa yang harus dilakukan? Menggunakan localstack.

## Localstack

[Localstack](https://www.localstack.cloud/) adalah tools yang dibangun oleh komunitas developer untuk membuat simulasi seolah-olah perintahnya sama seperti penggunaan cloud itu sendiri, misalnya AWS.

AWS memiliki tools yang disebut AWS CLI (Command Line Interface) dimana tools ini memungkinkan kita terhubung dengan server AWS dan melakukan tindakan terhadap layanannya. Misalnya saja S3, layanan penyimpanan objek yang dikelola oleh AWS. Dengan menggunakan S3 kita bisa menyimpan objek apapun dari sebuah server menuju cloud.

Layanan S3 bisa dikatakan sebagai Google Drive versi AWS, bedanya S3 tidak memiliki tampilan yang intuitif karena memang tidak diperuntukkan bagi pengguna biasa. Layanan S3 biasanya digunakan oleh software engineer untuk membackup data, menyiapkan release version bundle, dan hal lainnya.

## Konfigurasi Docker

Kita akan menggunakan server multipass dan [dokumentasi](https://docs.localstack.cloud/getting-started/installation/) berikut.

Pertama, pastikan kita telah memiliki docker. Jika belum ada ikuti langkah berikut:

```bash
sudo apt install apt-transport-https ca-certificates curl software-properties-common -y
```

Tambahkan keyring:

```bash
sudo curl -fsSL https://download.docker.com/linux/ubuntu/gpg -o /etc/apt/keyrings/docker.asc
```

Tambahkan Docker repository ke APT source kita:

```bash
echo "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.asc] https://download.docker.com/linux/ubuntu $(. /etc/os-release && echo "$VERSION_CODENAME") stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null
```

Lakukan update

```bash
sudo apt update
```

Terakhir install docker:

```bash
sudo apt-get install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
```
Perintah di atas akan menginstall tools berikut:

- docker-ce: Engine docker community edition.
- docker-ce-cli: Perintah CLI Docker.
- containerd.io: Container yang akan monitor siklus berjalannya container docker.
- docker-buildx-plugin: Tujuannya untuk meningkatkan kinerja pembuatan image.
- docker-compose-plugin: Mengaktifkan docker multi-container dengna file YAML.

> [!NOTE]
> Selanjutnya kita perlu menambahkan docker ke group sudo biar mudah aksesnya tidak perlu pake sudo. 

Kita harus memasukkannya ke sudo, karena beginilah kalau tidak kita lakukan:

```bash
ubuntu@latihan-multipass:~$ docker pull hello-world
Using default tag: latest
permission denied while trying to connect to the Docker daemon socket at unix:///var/run/docker.sock: Post "http://%2Fvar%2Frun%2Fdocker.sock/v1.47/images/create?fromImage=hello-world&tag=latest": dial unix /var/run/docker.sock: connect: permission denied

ubuntu@latihan-multipass:~$ sudo docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
c1ec31eb5944: Pull complete 
Digest: sha256:5b3cc85e16e3058003c13b7821318369dad01dac3dbb877aac3c28182255c724
Status: Downloaded newer image for hello-world:latest
docker.io/library/hello-world:latest
ubuntu@latihan-multipass:~$ 

```

Masukkan perintah berikut step by step:

```bash
sudo groupadd docker
sudo usermod -aG docker $USER
```

Sekarang restart multipassnya dan lihat hasilnya:

```bash
ubuntu@latihan-multipass:~$ docker pull hello-world
Using default tag: latest
latest: Pulling from library/hello-world
Digest: sha256:5b3cc85e16e3058003c13b7821318369dad01dac3dbb877aac3c28182255c724
Status: Image is up to date for hello-world:latest
docker.io/library/hello-world:latest
ubuntu@latihan-multipass:~$ 
```

## Instalasi Localstack

Setelah beres mengurus docker, kita perlu instalasi localstack, masukkan perintah berikut baris perbaris:

```bash
cd /home/ubuntu
curl --output localstack-cli-4.0.0-linux-amd64-onefile.tar.gz \
    --location https://github.com/localstack/localstack-cli/releases/download/v4.0.0/localstack-cli-4.0.0-linux-amd64-onefile.tar.gz
sudo tar xvzf localstack-cli-4.0.0-linux-*-onefile.tar.gz -C /usr/local/bin
```

Sekarang test dengan perintah berikut:

```bash
localstack --version
```

Apabila berhasil akan seperti ini.

```bash
ubuntu@latihan-multipass:~$ localstack --version
LocalStack CLI 4.0.0
ubuntu@latihan-multipass:~$
```

Sekarang jalankan perintah berikut:

```bash
localstack start -d
```

Tunggu hingga layanan localstack terinstall di multipass kita:

```bash
ubuntu@latihan-multipass:~$ localstack start -d

     __                     _______ __             __
    / /   ____  _________ _/ / ___// /_____ ______/ /__
   / /   / __ \/ ___/ __ `/ /\__ \/ __/ __ `/ ___/ //_/
  / /___/ /_/ / /__/ /_/ / /___/ / /_/ /_/ / /__/ ,<
 /_____/\____/\___/\__,_/_//____/\__/\__,_/\___/_/|_|

 💻 LocalStack CLI 4.0.0
 👤 Profile: default

[13:01:41] starting LocalStack in Docker mode 🐳                                                                                     localstack.py:510
           preparing environment                                                                                                     bootstrap.py:1308
           configuring container                                                                                                     bootstrap.py:1316
           container image not found on host                                                                                         bootstrap.py:1297
[13:02:47] download complete                                                                                                         bootstrap.py:1301
           starting container                                                                                                        bootstrap.py:1326
[13:02:49] detaching
```

Kemudian jalankan perintah berikut:

```bash
localstack status services
```

Kamu akan melihat layanan cloud yang sudah aktif:


```bash
ubuntu@latihan-multipass:~$ localstack status services
┏━━━━━━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ Service                  ┃ Status      ┃
┡━━━━━━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ acm                      │ ✔ available │
│ apigateway               │ ✔ available │
│ cloudformation           │ ✔ available │
│ cloudwatch               │ ✔ available │
│ config                   │ ✔ available │
│ dynamodb                 │ ✔ available │
│ dynamodbstreams          │ ✔ available │
│ ec2                      │ ✔ available │
│ es                       │ ✔ available │
│ events                   │ ✔ available │
│ firehose                 │ ✔ available │
│ iam                      │ ✔ available │
│ kinesis                  │ ✔ available │
│ kms                      │ ✔ available │
│ lambda                   │ ✔ available │
│ logs                     │ ✔ available │
│ opensearch               │ ✔ available │
│ redshift                 │ ✔ available │
│ resource-groups          │ ✔ available │
│ resourcegroupstaggingapi │ ✔ available │
│ route53                  │ ✔ available │
│ route53resolver          │ ✔ available │
│ s3                       │ ✔ available │
│ s3control                │ ✔ available │
│ scheduler                │ ✔ available │
│ secretsmanager           │ ✔ available │
│ ses                      │ ✔ available │
│ sns                      │ ✔ available │
│ sqs                      │ ✔ available │
│ ssm                      │ ✔ available │
│ stepfunctions            │ ✔ available │
│ sts                      │ ✔ available │
│ support                  │ ✔ available │
│ swf                      │ ✔ available │
│ transcribe               │ ✔ available │
└──────────────────────────┴─────────────┘
ubuntu@latihan-multipass:~$ 
```

## Instalasi AWS CLI

Sekarang kita perlu menginstall AWS CLI agar bisa berinteraksi, masukkan perintah berikut:

```bash
sudo apt install awscli
```

Sekarang jalankan perintah berikut:

```bash
aws configure --profile default
```

dan lihat yang perlu kalian isi:

```bash
ubuntu@latihan-multipass:~$ aws configure --profile default
AWS Access Key ID [None]: test
AWS Secret Access Key [None]: test
Default region name [None]: eu-west-2
Default output format [None]: 
```

Kita isi Access Key ID dan Secret Access Key dengan `test` lalu region name-nya `eu-west-2` sesuai [dokumentasi localstack](https://docs.localstack.cloud/user-guide/integrations/aws-cli/).

## Membuat Bucket

Setelah berhasil setting konfigurasi yang dibutuhkan mari membuat bucket, bucket adalah folder besar di AWS yang memungkinkan kita menyimpan file yang kita gunakan.


Pertama jalankan perintah ini:

```bash
aws s3 mb s3://my-bucket --endpoint-url http://localhost:4566
```

> [!NOTE]
> Option `--endpoint-url http://localhost:4566` memang dibutuhkan karena secara default AWS mengarahkan URL ke servernya sedangkan kita menggunakan localstack yang berada di local, jadi perlu diberi opsi `--endpoint-url`.

Kamu berhasil membuat bucket bernama `my-bucket`, sekarang kita coba cek apa saja isi filenya:

```bash
aws s3 ls s3://my-bucket --endpoint-url http://localhost:4566
```

Kamu akan menemukan kosong, tidak mengapa kan memang baru dibuat, sekarang coba eksekusi kode berikut baris perbaris.

```bash
cd /home/ubuntu
echo "Hello, World!" > hello-world.txt
aws s3 cp hello-world.txt s3://my-bucket/hello.txt --endpoint-url http://localhost:4566
aws s3 ls s3://my-bucket --endpoint-url http://localhost:4566
```

Kamu akan melihat hasilnya:

```bash
ubuntu@latihan-multipass:~$ aws s3 ls s3://my-bucket --endpoint-url http://localhost:4566
2024-12-26 13:27:58         14 hello.txt
```

File `hello-world.txt` yang berisi teks "Hello, World!" kita upload ke bucket `my-bucket` dengan nama `hello.txt`.

Sekarang jalankan perintah berikut baris perbaris:

```bash
cd /home/ubuntu
mkdir download
cd download/
aws s3 cp s3://my-bucket/hello.txt . --endpoint-url http://localhost:4566
cat hello.txt 
```

Kamu akan melihat hasilnya:

```bash
ubuntu@latihan-multipass:~/download$ cat hello.txt 
Hello, World!
```

Sekarang kamu sudah berhasil melakukan simulasi terhadap layanan S3 dengan Localstack!