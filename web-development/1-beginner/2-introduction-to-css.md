| **Author**       | **Editor** |
|------------------|------------|
| HasthoRahtomo    | Ifarra     |

---

# Styling

Pada chapter ini kamu akan belajar mengenai CSS untuk mempercantik tampilan HTML. Terdapat banyak kode yang menghasilkan beragam efek yang dapat kamu gunakan. Mari kita mulai!

## Menghubungkan HTML dengan CSS

Langkah pertama yang harus kita lakukan untuk dapat menggunakan HTML dengan CSS adalah dengan menghubungkan keduanya menggunakan kode berikut. Terdapat tiga cara untuk menggunakan CSS untuk file HTML mu, yaitu inline dan eksternal CSS.

Pertama pastikan kamu memiliki struktur folder sebagai berikut:

### **Eksternal CSS**

Buat struktur folder hingga menjadi sebagai berikut, jangan lupa buat file `styles.css` pada folder css.

```plain
latihan/
├── index.html
├── css/
│   └── styles.css
```

Kemudian masukkan kode berikut pada `styles.css`.

```css
h1 {
    color: red;
}
```

Sekarang ubah file `index.html` kamu agar menjadi seperti ini:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>External CSS</title>
    <link rel="stylesheet" href="css/styles.css">
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

### **Internal CSS**

Berbeda dengan styling secara eksternal, internal css mengarah kepada tag `<style>` yang bisa kalian tulis di di dalam `<head>` tag, contoh:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Internal CSS</title>
    <style>
        h1 {
            color: green;
        }
    </style>
</head>
<body>
    <h1>Hello World</h1>
</body>
</html>
```

### **Inline CSS**

Berbeda dari eksternal CSS, inline css tidak membutuhkan file eksternal untuk digunakan. Kita dapat menggunakan atribut style, sebagai contoh:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Inline CSS</title>
</head>
<body>
    <h1 style="color: blue;">Hello World</h1>
</body>
</html>
```

## **Font Family**

Font-family adalah kode CSS pertama yang akan kamu pelajari, font-family digunakan untuk mengubah gaya font/model font. Terdapat banyak tipe font yang dapat kamu pakai, seperti "arial", "sans-serif", "serif", "helvetica", dll. Kamu juga dapat menggunakan font dari internet. Perhatikan kode berikut.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Family</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="font-family: Helvetica;">Komandro</h2>
</body>
```

Jalankan dan lihat perbedaannya.

## **Font Size**

Digunakan untuk mengatur ukuran dari text, kamu dapat mencoba kode
berikut.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Size</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="font-size: 40px;">Komandro</h2>
</body>
```

Coba jalankan dan lihat hasilnya.

## **Font Weight**

Digunakan untuk mengatur Ketebalan dari text, kamu dapat memilih ketebalan text dari light hingga bold, kamu juga dapat memasukan satuan ukuran.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Font Weight</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="font-size: 40px;">Komandro</h2>
</body>
```

## Text-align

Digunakan untuk mengatur posisi dari text, kamu dapat mencoba kode berikut.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Align</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="text-align: center;">Komandro</h2>
    <h2 style="text-align: right;">Komandro</h2>
</body>
```

## **Color**

Digunakan untuk mengubah warna dari font mu.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Text Color</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="color: green;">Komandro</h2>
</body>
```

## **Background-color**

Digunakan untuk mengubah warna latar belakang dari elemen.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Background Color</title>
</head>
<body>
    <h2>Komandro</h2>
    <h2 style="background-color: green;">Komandro</h2>
</body>
```

## **Background-image**

Digunakan untuk menjadikan gambar yang kita inginkan menjadi background untuk elemen yang kita inginkan. Perhatikan kode berikut dan lihat hasilnya.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Background Color</title>
</head>
<body>
    <h2 style="background-image:
        url(https://cdn.oneesports.gg/cdn-data/2022/01/GenshinImpact_Zhongli_drinking_tea.jpg);">
    Komandro </h2>
</body>
```

## **Border**

Digunakan untuk membuat batas border pada ujung element, banyak tipe border yang dapat kamu gunakan, berikut adalah beberapa contoh border yang dapat kamu gunakan dan cara menggunakannya.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Background Color</title>
</head>
<body>
    <h2 style="border: 1px solid black;"> Komandro</h2>
    <h2 style="border: 2px dashed black;"> Komandro</h2> 
    <h2 style="border: 2px dotted black;"> Komandro</h2>
    <h2 style="border: 3px double black;"> Komandro</h2>
</body>  
```

## **Margin dan Padding**

Margin adalah kode untuk mengatur jarak antara elemen dengan elemen lain diluarnya, sedangkan padding adalah kode untuk mengatur jarak antara pembungkus dan elemennya.

![](./assets/18.png)

Terdapat empat arah untuk menentukan ukuran margin dan padding.

- Top: mengatur jarak pada arah atas.
- left: mengatur jarak pada arah kiri.
- bottom: mengatur jarak pada arah bawah.
- right: mengatur jarak pada arah kanan.

Kamu dapat menggunakannya adalah seperti contoh berikut.

- Margin-top
- Margin-bottom  
- Margin-left
- Padding-top
- Padding-right
- Padding-bottom

Untuk penjelasan yang lebih jelas perhatikan kode berikut.

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Margin dan Padding</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f0f0f0; color: #333; margin: 0; padding: 20px;">
    <div style="background-color: #fff; padding: 20px; border: 1px solid #ccc;">
        <h1 style="color: #0066cc; text-align: center;">Contoh Margin dan Padding</h1>
        <p style="background-color: #e0f7fa; margin: 20px 0; padding: 10px; border: 1px solid #0066cc;">
            Ini adalah contoh elemen dengan margin.
        </p>
        <p style="background-color: #ffeb3b; padding: 20px; border: 1px solid #ff9800;">
            Ini adalah contoh elemen dengan padding.
        </p>
        <div style="background-color: #c8e6c9; margin: 20px; padding: 20px; border: 1px solid #4caf50;">
            Ini adalah contoh elemen dengan margin dan padding.
        </div>
    </div>
</body>
</html>
```

## **Width dan Height**

Adalah kode yang dipakai untuk mengatur lebar dan tinggi dari sebuah elemen. Width, adalah kode untuk mengatur kelebaran yang bersifat statis. Height, adalah kode untuk mengatur Ketinggian yang bersifat statis.

Contoh kode:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Width dan Height</title>
</head>
<body style="font-family: Arial, sans-serif; background-color: #f0f0f0; color: #333; margin: 0; padding: 20px;">
    <div style="background-color: #fff; padding: 20px; border: 1px solid #ccc;">
        <h1 style="color: #0066cc; text-align: center;">Contoh Width dan Height</h1>
        
        <div style="background-color: #e0f7fa; width: 200px; height: 100px; margin: 20px 0; padding: 10px; border: 1px solid #0066cc;">
            Ini adalah contoh elemen dengan width 200px dan height 100px.
        </div>
        
        <div style="background-color: #ffeb3b; width: 50%; height: 150px; padding: 20px; border: 1px solid #ff9800;">
            Ini adalah contoh elemen dengan width 50% dan height 150px.
        </div>
        
        <div style="background-color: #c8e6c9; width: 300px; height: 200px; margin: 20px; padding: 20px; border: 1px solid #4caf50;">
            Ini adalah contoh elemen dengan width 300px dan height 200px.
        </div>
    </div>
</body>
</html>
```

## Class dan ID

Kamu dapat menggunakan class dan ID untuk memanggil/selector variabel yang terkandung didalamnya. Selector class ditandai dengan titik (.) dan selector ID ditandai dengan pagar (#). Contoh kode:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Internal CSS dengan Class dan ID</title>
    <style>
        /* CSS untuk elemen dengan ID */
        #header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* CSS untuk elemen dengan Class */
        .container {
            background-color: #f9f9f9;
            padding: 20px;
            border: 1px solid #ddd;
            margin: 20px 0;
        }

        .box {
            background-color: #e0f7fa;
            width: 200px;
            height: 100px;
            margin: 10px;
            padding: 10px;
            border: 1px solid #0066cc;
            display: inline-block;
        }

        .highlight {
            background-color: #ffeb3b;
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="header">
        <h1>Contoh Internal CSS dengan Class dan ID</h1>
    </div>

    <div class="container">
        <div class="box">
            Ini adalah elemen dengan class "box".
        </div>
        <div class="box highlight">
            Ini adalah elemen dengan class "box" dan "highlight".
        </div>
        <div class="box">
            Ini adalah elemen dengan class "box".
        </div>
    </div>
</body>
</html>
```

## **Hover**

Mengacu pada keadaan ketika pengguna mengarahkan kursor mouse mereka ke elemen HTML tertentu, seperti tautan (link) atau elemen yang dapat diinteraksi. Saat pengguna mengarahkan kursor ke elemen tersebut, terkadang tindakan atau perubahan visual khusus bisa saja terjadi dan ini disebut `hover effect`. Perhatikan kode berikut:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Contoh Hover dengan CSS</title>
    <style>
        /* CSS untuk elemen dengan ID */
        #header {
            background-color: #4CAF50;
            color: white;
            text-align: center;
            padding: 20px;
        }

        /* CSS untuk elemen dengan Class */
        .container {
            background-color: #f9f9f9;
            padding: 20px;
            border: 1px solid #ddd;
            margin: 20px 0;
        }

        .box {
            background-color: #e0f7fa;
            width: 200px;
            height: 100px;
            margin: 10px;
            padding: 10px;
            border: 1px solid #0066cc;
            display: inline-block;
            transition: background-color 0.3s, transform 0.3s;
        }

        /* Efek Hover */
        .box:hover {
            background-color: #0066cc;
            color: white;
            transform: scale(1.1);
        }

        .highlight {
            background-color: #ffeb3b;
            color: #333;
            font-weight: bold;
        }
    </style>
</head>
<body>
    <div id="header">
        <h1>Contoh Hover dengan CSS</h1>
    </div>

    <div class="container">
        <div class="box">
            Hover saya!
        </div>
        <div class="box highlight">
            Hover saya juga!
        </div>
        <div class="box">
            Hover saya!
        </div>
    </div>
</body>
</html>
```

## **Menentukan Posisi Item**

Kita dapat mengatur posisi elemen dengan menghitung ukuran elemen dan ukuran layar kita. Berikut adalah poin poin penting dalam menentukan posisi item:

- Apabila menggunakan satuan persen sebagai ukuran (%), pastikan total keseluruhannya adalah 100%.
- Apabila menggunakan satuan pixel (px), pastikan total keseluruhannya sesuai dengan lebar layar.

Contoh Kode:

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Menentukan Posisi Item</title>
    <style>
        body {
            text-align: center;
            font-family: Arial, sans-serif;
        }
        .image-container {
            margin: 0 auto;
            width: 100%;
        }
        .centered-image {
            width: 30%;
            margin-left: 35%;
            margin-right: 35%;
        }
    </style>
</head>
<body>
    <h1>Menentukan Posisi Item</h1>
    <div class="image-container">
        <img src="https://www.ligagame.tv/templates/yootheme/cache/genshin-impact-zhongli_10461-ccede73b.webp"
             alt="Genshin Impact Zhongli" class="centered-image">
    </div>
    <p>Gambar berada di tengah karena margin kiri dan kanan masing-masing bernilai 35%, dan gambar berukuran 30%.</p>
</body>
</html>
```

Ayo mencoba! Ubah posisi agar gambar berada di arah kanan lalu ubah gambar ke arah kiri. Sebagai clue, kamu dapat melihat pada bagian `margin` dan `width` pada kode di atas! Untuk implementasi dari materi ini, kalian bisa cek ke bagian [jawaban exercise](./exercise/2-introduction-to-css/).
