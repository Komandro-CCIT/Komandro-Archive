5 - Logging
---

Author: Hudya (@perogeremmer)

<br />

# Overview

Ketika membicarakan logging, masih banyak yang tidak merasa bahwa logging itu penting. Padahal kenyataannya, logging itu merupakan proses untuk memahami keadaan aplikasi atau sistem yang dibangun.

Dengan membuat logging yang baik, kita dapat memahami alur dari aplikasi yang kita bangun termasuk mencatat kejadian dari aplikasi kita.

Contoh output logging:

```log
2022-01-09 12:34:32.123456 [INFO] - This is an info message
2022-01-09 12:34:32.123456 [WARNING] - This is a warning message
2022-01-09 12:34:32.123456 [ERROR] - This is an error message
2022-01-09 12:34:32.123456 [CRITICAL] - This is a critical message
```

<br />

Inilah output dari aplikasi yang kita bangun:

```log
2023-02-20 15:00:00.000000 [INFO] - User requesting menu
2023-02-20 15:02:30.250000 [INFO] - User pick menu (Root Beer)
2023-02-20 15:04:10.670000 [INFO] - Waiting user payment for Rp. 15,000.00
2023-02-20 15:07:40.130000 [INFO] - Payment accepted, payment method: QRIS
2023-02-20 15:09:50.340000 [INFO] - Sending order, giving Root Beer
2023-02-20 15:10:55.980000 [INFO] - Transaction closed, back to idle
```

Dapat dilihat bahwa dengan melihat logging, kita dapat memahami keadaan dari aplikasi kita secara berurut, dimulai dari saat pengguna membuka menu, memilih menu, hingga melakukan pembayaran dan menutup transaksi. Pada kasus di atas, sample log yang ditulis adalah contoh aplikasi vending machine dimana ketika pengguna memilih minuman, menunggu pembayaran, lalu melakukan pembayaran dengan metode QRIS, hingga ketika menutup transaksi yang mana pada kasus realnya adalah mengeluarkan minuman.

Dengan membaca log, kita juga dapat melakukan tracking bahwa sebenarnya seberapa lama pengguna melakukan aktivitas dari meminta menu, hingga memilih menu, serta seberapa lama user melakukan pembayaran, hingga mesin tersebut mengeluarkan minuman.

Hal-hal kecil ini seringkali dianggap remeh, padahal kita bisa menghasilkan knowledge untuk sisi bisnis dengan memahami log dari aplikasi yang kita bangun.

Selain itu, biasanya log juga akan digabung dengan payload dari aplikasi agar tim developer dapat memahami sebenarnya nilai yang sedang dikirimkan itu berbentuk seperti apa. Contoh:

```log
2023-02-20 15:00:00.000000 [INFO] - User requesting menu
2023-02-20 15:02:30.250000 [INFO] - User pick menu (Root Beer)
2023-02-20 15:04:10.670000 [INFO] - Waiting user payment for Rp. 15,000.00
                                    Payload: {"user_id": 123, "order_id": 999, "menu": "Root Beer", "payment_due": "15000.00"}
2023-02-20 15:07:40.130000 [INFO] - Payment accepted, payment method: midtrans
                                    Payload: {"user_id": 123, "order_id": 999, "payment_method": "midtrans", "payment_status": "accepted"}
2023-02-20 15:09:50.340000 [INFO] - Sending order, giving Root Beer
                                    Payload: {"order_id": 999, "status": "preparing", "menu": "Root Beer"}
2023-02-20 15:10:55.980000 [INFO] - Transaction closed, back to idle
                                    Payload: {"order_id": 999, "status": "closed"}
```

# Exercise

Secara sederhana, kita dapat membuat log pada python dengan code sebagai berikut:

```python
import logging

# Configure logging
logging.basicConfig(
    filename='app.log',
    level=logging.INFO,
    format='%(asctime)s [%(levelname)s] - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S.%s'
)

logging.info('User requesting menu')
logging.info('User pick menu (Root Beer)')
logging.info('Waiting user payment for Rp. 15,000.00')
logging.info('Payment accepted, payment method: midtrans')
logging.info('Sending order, giving Root Beer')
logging.info('Transaction closed, back to idle')
```

Menggunakan proyek pada materi [4 - event pattern](./4-event-pattern.md), cobalah buat satu file baru bernama `app_log.py` sejajar dengan main.py