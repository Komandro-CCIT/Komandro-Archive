

# 11. Proyek API Automation Testing

**Author**: Fajar Triady Putra (@fajartriadyp)

## Overview

Setelah mempelajari automation testing untuk sebuah UI website, langkah selanjutnya adalah membuat automation sederhana untuk pengujian API. Proyek ini menggunakan API publik dari [Reqres](https://reqres.in/), yang menyediakan berbagai endpoint untuk latihan, seperti `GET`, `POST`, `PUT`, dan `DELETE`.

![alt text](/assets/11-project-simple-automation-api/image.png)

Pada proyek ini, kita akan membuat beberapa test case menggunakan framework `Playwright` dan `Pytest`. Jika tertarik mengeksplorasi API lain, Anda bisa melihat daftar [Public APIs](https://github.com/public-apis/public-apis).

---

## Kenalan dulu dengan Postman

Sebelum melangkah lebih jauh kalian harus mengetahui basic basic penggunakan postman terlebih dahulu. Buat yang belum mengetahui apa itu postman?, postman adalah sebuah alat untuk menguji, mengembangkan dan mendokumentasikan API. untuk sekarang mari kita langsung coba mulai dari awal.

Berikut adalah langkah-langkah dasar untuk memulai menggunakan **Postman**:

---

### **1. Download dan Instal Postman**
- Kunjungi situs resmi Postman di [https://www.postman.com/downloads/](https://www.postman.com/downloads/).
- Pilih versi sesuai dengan sistem operasi Anda (Windows, macOS, atau Linux).
- Setelah selesai diunduh, instal aplikasi seperti biasa.

---

### **2. Membuat Request Pertama**
Setelah menginstal Postman, buka aplikasinya, dan ikuti langkah-langkah berikut untuk membuat request API:

#### **Langkah 1: Membuka Workspace**
- Klik tombol **“New Tab”** di bagian atas workspace untuk memulai request baru.

#### **Langkah 2: Pilih Metode HTTP**
- Pada dropdown di sebelah kiri, pilih metode request seperti:
  - **GET**: Untuk mengambil data dari API.
  - **POST**: Untuk mengirim data ke API.
  - **PUT**: Untuk memperbarui data.
  - **DELETE**: Untuk menghapus data.

#### **Langkah 3: Masukkan URL Endpoint**
- Masukkan URL API yang akan diuji, contohnya:  
  **`https://reqres.in/api/users/2`** untuk request GET.

#### **Langkah 4: Menambahkan Parameter atau Body**
- **Params**: Untuk menambahkan query parameter ke URL.
- **Headers**: Menambahkan informasi header seperti `Content-Type`.
- **Body**: Digunakan untuk mengirim data pada request **POST** atau **PUT**.

#### **Langkah 5: Klik “Send”**
- Setelah semua informasi diisi, klik tombol **Send**.
- Postman akan menampilkan respons dari API di bagian bawah.

---

### **3. Contoh Request API Menggunakan Postman**
Berikut beberapa contoh:

#### **GET Request**
- URL: **`https://reqres.in/api/users/2`**
- Langkah:
  - Pilih metode **GET**.
  - Masukkan URL di kolom yang tersedia.
  - Klik **Send**.
- Hasil: Anda akan melihat respons berupa data user dengan ID 2.

#### **POST Request**
- URL: **`https://reqres.in/api/users`**
- Langkah:
  - Pilih metode **POST**.
  - Masukkan URL di kolom yang tersedia.
  - Klik tab **Body**, pilih **raw**, dan atur tipe menjadi **JSON**.
  - Masukkan payload:
    ```json
    {
      "name": "morpheus",
      "job": "leader"
    }
    ```
  - Klik **Send**.
- Hasil: Anda akan menerima respons dengan detail user yang baru dibuat.

---



## Setup Proyek

Langkah pertama adalah membuat folder proyek baru di komputer Anda. Buka folder tersebut menggunakan VS Code.

### 1. Buat Virtual Environment
Jalankan perintah berikut di terminal untuk membuat virtual environment:
```bash
python -m venv venv
```
Aktifkan environment:
- **Linux/Mac**:
    ```bash
    source venv/bin/activate
    ```
- **Windows**:
    ```bash
    venv\Scripts\activate
    ```

Setelah aktif, Anda akan melihat `(venv)` di awal terminal:
```bash
(venv) C:\Users\acer\Desktop>
```

### 2. Instalasi Framework dan Library
Instal framework `Playwright`:
```bash
pip install playwright
playwright install
```

Tambahkan library `pytest` untuk testing:
```bash
pip install pytest
```

---

## Folder Structure

Berikut adalah struktur folder untuk proyek ini:

```bash
/automation_project
│
├── /tests                  # Semua test case diletakkan di sini
│   ├── test_get_user.py    # Test untuk GET endpoint
│   ├── test_post_user.py   # Test untuk POST endpoint
│   ├── test_put_user.py    # Test untuk PUT endpoint
│   └── test_delete_user.py # Test untuk DELETE endpoint
│
├── /pages                  # Page Object untuk pengujian API
│   └── base_api.py         # Kelas dasar untuk API interaction
│
├── requirements.txt        # File dependencies
├── README.md               # Dokumentasi proyek
└── pytest.ini              # File konfigurasi pytest
```

---

## Test Cases

Berikut adalah beberapa contoh test case untuk pengujian API:

### 1. **GET Request: Mendapatkan Data User**
File: `test_get_user.py`
```python
def test_GET_as_user_success_get_user_data(api_context):
    response = api_context.get("https://reqres.in/api/users/2")
    assert response.status == 200
    response_body = response.json()

    # Validasi data
    assert response_body["data"]["id"] == 2
    assert response_body["data"]["email"] == "janet.weaver@reqres.in"
```

---

### 2. **POST Request: Membuat User Baru**
File: `test_post_user.py`
```python
def test_POST_validate_create_user_response(api_context):
    payload = {"name": "morpheus", "job": "leader"}
    response = api_context.post("https://reqres.in/api/users", data=payload)
    assert response.status == 201
    response_body = response.json()

    # Validasi respons
    assert response_body["name"] == "morpheus"
    assert response_body["job"] == "leader"
```

---

### 3. **PUT Request: Memperbarui Data User**
File: `test_put_user.py`
```python
def test_PUT_update_data_user(api_context):
    payload = {"name": "morpheus", "job": "cleaner"}
    response = api_context.put("https://reqres.in/api/users/2", data=payload)
    assert response.status == 200
    response_body = response.json()

    # Validasi data
    assert response_body["name"] == "morpheus"
    assert response_body["job"] == "cleaner"
```

---

### 4. **DELETE Request: Menghapus User**
File: `test_delete_user.py`
```python
def test_DELETE_remove_data_user(api_context):
    response = api_context.delete("https://reqres.in/api/users/2")
    assert response.status == 204
```

---

## Penjelasan Code

Berikut adalah penjelasan untuk file `test_get_user.py`:

```python
def test_GET_as_user_success_get_user_data(api_context):
    response = api_context.get("https://reqres.in/api/users/2")
    assert response.status == 200
    response_body = response.json()

    # Validasi data
    assert response_body["data"]["id"] == 2
    assert response_body["data"]["email"] == "janet.weaver@reqres.in"
```

### Penjelasan:
1. **`test_GET_as_user_success_get_user_data(api_context)`**
   - Ini adalah sebuah fungsi pengujian untuk metode **GET**.
   - Tujuan: Memastikan bahwa data user dengan ID **2** berhasil diambil dari endpoint API `https://reqres.in/api/users/2`.

2. **`response = api_context.get("https://reqres.in/api/users/2")`**
   - Mengirimkan request **GET** ke endpoint `https://reqres.in/api/users/2` menggunakan **Playwright API Context**.
   - Variabel `response` akan menyimpan hasil respons dari request ini, yang mencakup status code, header, dan body respons.

3. **`assert response.status == 200`**
   - Memastikan bahwa status code dari respons adalah **200 (OK)**.
   - Status ini menunjukkan bahwa request berhasil diproses oleh server.

4. **`response_body = response.json()`**
   - Mengambil body dari respons dalam format **JSON**.
   - Data ini disimpan dalam variabel `response_body` agar bisa digunakan untuk validasi lebih lanjut.

5. **Validasi Data:**
   - **`assert response_body["data"]["id"] == 2`**
     - Memastikan bahwa field `id` dalam objek `data` di respons adalah **2**.
     - Ini menunjukkan bahwa data yang dikembalikan sesuai dengan user yang diminta (ID = 2).

   - **`assert response_body["data"]["email"] == "janet.weaver@reqres.in"`**
     - Memastikan bahwa field `email` dalam objek `data` adalah **`janet.weaver@reqres.in`**.
     - Ini menunjukkan bahwa data email dari user ID **2** sesuai dengan yang diharapkan.

---

### Contoh Respons dari API:
Ketika request **GET** dikirimkan ke `https://reqres.in/api/users/2`, respons yang diharapkan dari server adalah seperti berikut:

```json
{
    "data": {
        "id": 2,
        "email": "janet.weaver@reqres.in",
        "first_name": "Janet",
        "last_name": "Weaver",
        "avatar": "https://reqres.in/img/faces/2-image.jpg"
    },
    "support": {
        "url": "https://reqres.in/#support-heading",
        "text": "To keep ReqRes free, contributions towards server costs are appreciated!"
    }
}
```

### Penjelasan Validasi:
- **`response_body["data"]["id"] == 2`**:
  - Dari JSON di atas, `id` dalam objek `data` memiliki nilai **2**, sehingga validasi ini akan **lulus** jika respons sesuai.

- **`response_body["data"]["email"] == "janet.weaver@reqres.in"`**:
  - Dari JSON di atas, `email` dalam objek `data` memiliki nilai **`janet.weaver@reqres.in`**, sehingga validasi ini juga akan **lulus** jika respons sesuai.

Fungsi ini adalah test case sederhana yang memastikan bahwa:
- Endpoint **GET /users/2** memberikan respons **200 (OK)**.
- Data user yang dikembalikan sesuai dengan user ID **2**, termasuk email yang benar.

Jika salah satu validasi gagal, test case ini akan **gagal**, menunjukkan bahwa ada masalah pada API atau datanya tidak sesuai dengan yang diharapkan.


---
## Menjalankan Tes

Setelah konfigurasi selesai, Anda dapat menjalankan semua test case menggunakan perintah berikut:
```bash
pytest tests/
```

Jika ingin menjalankan tes tertentu:
```bash
pytest tests/test_get_user.py
```

---

##


Yuhuu, ini adalah bagian terakhir dari percobaan simple project api automation pada api collection https://reqres.in/ . selalu diingat bahwa ***pratice make perfect*** jadi mari kita jadikan Komandro sebagai sarana berlatih bersama. 

Segitu saja jika kalian ada pertanyaan mengenai tutorial ini kalian bisa tanya langsung di forum QA Komandro atau bisa reach out langsung author di [ Linkedin](https://www.linkedin.com/in/fajartriadyp). 

Thank you and happy learning 😁😁