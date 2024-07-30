1 - Docker Introduction
---

Author : 

<br/>

## Overview


Setelah kalian mempelajari bagaimana cara build dan deploy aplikasi pada materi sebelumnya, pada materi kali ini kalian akan belajar bagaimana cara mengemas, mendistribusikan dan menjalankan suatu aplikasi menggunakan docker.

## Docker
[<img src="../assets/docker-Logo.png">](docker.com)
Docker merupakan sebuah platform open-source yang memungkinkan developer untuk mengemas dan menjalankan aplikasi di dalam environment yang terisolasi bernama container. Nah container yang terisolasi ini bagaikan "wadah" yang menampung suatu aplikasi sehingga tidak tumpah ke "wadah" lain dalam suatu sistem.

## Arsitektur Docker

Docker menggunakan arsitektur client-server. Docker client akan mengirimkan request ke Docker daemon untuk menjalankan request tersebut, Docker daemon dapat berjalan di mesin yang sama atau secara remote tergantung preferensi dari developer.

## Alasan Menggunakan Docker
>Kenapa sih pas development aplikasi pakai docker?
<br/>

Docker menawarkan kelebihan dalam melakukan proses pengembangan aplikasi, contohnya :
- Standarisasi Environment Aplikasi : Dengan menggunakan docker environment untuk menjalankan dapat distandarisasi untuk semua developer, sehingga mengurangi masalah "Di punyaku jalan kok".
- Mempermudah distribusi dan deployment : Aplikasi yang dikemas menggunakan docker dapat dijalankan dimana saja asal ada docker.
- Container lebih ringan dibanding virtual machine : Karena container tidak memerlukan OS baru untuk setiap instances yang dijalankan.

## Instalasi Docker

WIP