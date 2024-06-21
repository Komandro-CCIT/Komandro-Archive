8 - Project Vending Machine (Part 2)
---

Author: Hudya (@perogeremmer)

<br />

# Overview

Pada bagian [pertama](8-project-vending-machine-part-1.md), kita sudah membangun struktur dasar untuk membuat websocket server dan client. Sekarang kita akan melanjutkan untuk membuat screen untuk menampilkan QR code transaksi yang ditujukan untuk membayar.

# Code Time

## Menambahkan Library

Untuk membuat QR Pembayaran, kita akan menggunakan library Midtrans. Nah silahkan install librarynya dengan cara memasukkan kode di bawah ini.

```bash
pip install midtransclient
```

> [!NOTE]
> Pastikan sudah mengaktifkan virtualenv dengan perintah `source venv/bin/activate`

## Membuat Akun

Sekarang kamu perlu membuat akun Midtrans. Kunjungi website resmi [Midtrans](https://midtrans.com/) lalu buatlah akun. Setelah masuk, pindahlah ke environment `sandbox`. Environment ini adalah environment untuk ujicoba program sebagai seorang developer, sehingga kamu tidak perlu membayar transaksinya secara real.

Tampilannya akan menjadi seperti ini.

![Alt text](./assets/8-project-vending-machine/1.png)

Sekarang pergi ke `Settings > Access Keys`, disana kamu akan menemukan `Client Key` dan `Server Key`. Simpan kedua key ini pada komputer atau perangkatmu.

## Membuat file .env

File `.env` digunakan untuk menyimpan kredensial yang bersifat rahasia, biasanya file ini tidak akan kita bawa ke repository dan akan didaftarkan ke .gitignore.

Buat file `.env` sejajar dengan `main.py` lalu masukkan kode dibawah ini:

```plain
MIDTRANS_CLIENT_KEY=
MIDTRANS_SERVER_KEY=
```

Masukkan nilai client key dan server key kamu sehingga menjadi seperti ini:

```plain
MIDTRANS_CLIENT_KEY=xxxxxxxxxxxxxxx
MIDTRANS_SERVER_KEY=xxxxxxxxxxxxxxx
```

> [!NOTE]
> Ganti xxxxx dengan key kamu

## Membuat file Library

Setelah menginstall library midtrans, kita perlu untuk membuat file yang menampung library midtrans untuk membuat kode QR pembayaran. Buat file baru bernama `midtrans_payment.py` pada folder `cores/utilities`. Folder utilities akan berada pada folder `cores`, sehingga apabila kamu belum memilikinya, buat saja foldernya. Setelah file dibuat, masukkan kode berikut:

```python
import midtransclient

class MidtransPayment:
    def __init__(
        self, is_production: bool = False, client_key: str = "", server_key: str = ""
    ):
        self.core_api = midtransclient.CoreApi(
            is_production=is_production,
            server_key=server_key,
            client_key=client_key,
        )

    def create_qr(
        self,
        transaction_details: dict = {},
        item_details: list = [],
        customer_details: dict = {},
    ):
        payload = {
            "payment_type": "gopay",
            "item_details": item_details,
            "transaction_details": transaction_details,
            "customer_details": customer_details
        }

        return self.core_api.charge(payload)

    def check_transaction(self, order_id: str):
        """Sample Response
        {
            "status_code" : "200",
            "status_message" : "Success, Credit Card transaction is successful",
            "transaction_id" : "249fc620-6017-4540-af7c-5a1c25788f46",
            "masked_card" : "48111111-1114",
            "order_id" : "example-1424936368",
            "payment_type" : "credit_card",
            "transaction_time" : "2015-02-26 14:39:33",
            "transaction_status" : "capture",
            "fraud_status" : "accept",
            "approval_code" : "1424936374393",
            "signature_key" : "2802a264cb978fbc59f631c68d120cbda8dc853f5dfdc52301c615cf4f14e7a0b09aa...",
            "bank" : "bni",
            "gross_amount" : "30000.00",
            "channel_response_code": "00",
            "channel_response_message": "Approved",
            "card_type": "credit",
            "payment_option_type": "GOPAY_WALLET",
            "shopeepay_reference_number": "103995032913255264",
            "reference_id": "DL-dduIy7XtGtvxJtNNpOfbAt"
        }
        """
        return self.core_api.transactions.status(order_id)
```

## Membuat file Config

Untuk mengakses isi file .env kita memerlukan sebuah file baru yang menjadi class object dari konfigurasi app yang kita bangun. Buat file baru dengan nama `config.py` di dalam folder `cores` lalu masukkan kode berikut:

```python
from dotenv import load_dotenv
import os


class Config:
    load_dotenv()
    MIDTRANS_CLIENT_KEY = os.getenv('MIDTRANS_CLIENT_KEY') or ""
    MIDTRANS_SERVER_KEY = os.getenv('MIDTRANS_SERVER_KEY') or ""
```

Nantinya library dotenv akan membaca file `.env` pada struktur dasar proyek.

## Perubahan kode services

Sekarang kita akan mengubah business logic dari aplikasi yang dibangun. Pertama, kita ubah `base_service.py` yang berada pada folder `services` dengan kode berikut:

```python
from abc import ABC, abstractmethod
from uuid import uuid4
from cores.config import Config


class BaseService(ABC):
    config: Config
    
    def __init__(self):
        self.config = Config()

    @abstractmethod
    def execute(self):
        pass

    def generate_uuid(self):
        return str(uuid4())
```

Nantinya class `BaseService` akan menurunkan objek `config` yang dapat kita akses pada class yang menurunkan sifatnya.

Kemudian buat file baru bernama `order_service.py` dan isi dengan kode berikut:

```python
from services.base_service import BaseService
from cores.app_log import AppLogger
from cores.utilities.midtrans_payment import MidtransPayment
from cores.broker import Broker
from constants.states import AppStates
from constants.redis_prefix import RedisPrefix
from datetime import timedelta
from time import sleep
import json
import websocket


class OrderService(BaseService):
    allowed_states = [AppStates.MENU_CLICKED.value]

    def __init__(self, broker: Broker):
        super().__init__()
        self.broker = broker
        self.logger = AppLogger()
        self.mp = MidtransPayment(
            is_production=False,
            client_key=self.config.MIDTRANS_CLIENT_KEY,
            server_key=self.config.MIDTRANS_SERVER_KEY,
        )
        self.ws = websocket.WebSocket()
        self.ws.connect("ws://0.0.0.0:3333")

    def execute(self):
        state = self.broker.get_state()

        if state not in self.allowed_states:
            return False

        self.logger.info(f"Order service started. State: {self}")

        data = self.broker.read_single_data(RedisPrefix.SELECTED_MENU_DATA.value)
        if not data:
            raise Exception("yyy")

        data = json.loads(data)

        menu = self.broker.read_single_data(RedisPrefix.DRINK_ITEMS.value)
        if not menu:
            raise Exception("yyy")

        menu = json.loads(menu)

        selected_menu = {}
        for item in menu:
            if item["id"] == data["id"]:
                selected_menu = item
                break

        item_details = []
        payload = {
            "id": selected_menu["id"],
            "price": selected_menu["price"],
            "name": selected_menu["name"],
            "quantity": 1,
        }

        item_details.append(payload)

        gross_amount = 0
        gross_amount += selected_menu["price"]

        transaction_details = {
            "order_id": self.generate_uuid(),
            "gross_amount": float(gross_amount),
        }

        customer_details = {
            "first_name": "Buy Drink",
            "last_name": "Customer",
            "email": "customer@buydrink.com",
            "phone": "088888888",
        }

        response = self.mp.create_qr(
            transaction_details=transaction_details,
            item_details=item_details,
            customer_details=customer_details,
        )
        self.logger.info(f"QR created: {response}")

        new_state = AppStates.ORDER_CREATED.value
        self.broker.set_state(new_state)

        payload = {
            "transaction_details": transaction_details,
            "item_details": item_details,
            "customer_details": customer_details,
            "payment_details": response,
        }

        self.broker.create_single_data(
            RedisPrefix.PAYMENT_DETAIL.value,
            values=json.dumps(payload),
            expired=timedelta(hours=1),
        )

        ws_payload = json.dumps({"event": new_state, "values": payload})
        self.ws.send(ws_payload)
        self.logger.info(f"Change state into: {new_state}")
```


## Ubah file index.html

Sekarang kita ubah file index.html dengan kode berikut:

```html
!DOCTYPE html>
<html>

<head>
    <style>
        html,
        body {
            height: 100%;
        }

        body {
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            font-family: sans-serif;
        }

        .title {
            font-weight: bold;
            font-size: 48px;
        }

        .subtitle {
            font-size: 24px;
        }

        h2 {
            text-align: center;
            font-weight: bold;
            padding-bottom: 40px;
            font-size: 48px;
        }

        .card-drink {
            width: 200px;
            border: 1px solid #ddd;
            border-radius: 5px;
            text-align: center;
            cursor: pointer;
        }

        .cards {
            display: flex;
            justify-content: center;
        }

        .image-bottle {
            padding: 10px;
        }
    </style>
</head>

<body>
    <p class="title">Welcome to Drink Machine</p>
    <p class="subtitle">Please tap on the screen to buy a drink</p>
</body>

<script>
    document.body.addEventListener('click', function (evt) {
        if (evt.target.className === 'card-drink') {}
    }, false);

    showHome()

    function connect() {
        return new WebSocket("ws://localhost:3333/ws");
    }

    var ws = connect()
    cur_event = null;

    ws.onclose = function (event) {
        console.log(event)
        console.log("Closed! Connecting in 3 seconds.")
        setTimeout(() => {
            ws = connect()
            showHome()
        }, 3000)
    }

    ws.onerror = function (evt) {
        console.log(event)
        console.log("Error! Connecting in 3 seconds.")
        setTimeout(() => {
            ws = connect()
            showHome()
        }, 3000)

    };

    ws.onopen = function (event) {
    }

    ws.onmessage = function (event) {
        if (event.data.includes("connected")) {
            return
        } else if (event.data.includes("disconnected")) {
            return
        } else if (event.data.includes("closed")) {
            return
        }
        
        var data = {}
        try {
            data = JSON.parse(event.data);
            cur_event = data.event.toString()

            if (data.event === "SHOW_MENU") {
                showMenu(data.values)
            } else if (data.event === "ORDER_CREATED") {
                showPayment(data.values)
            } 
        } catch (e) {
            console.log(e)
        }
    };

    function showHome() {
        document.body.innerHTML = `
        <p class="title">Welcome to Drink Machine</p>
        <p class="subtitle">Please tap on the screen to buy a drink</p>
        `
    }

    function handleBodyClick() {
        if (cur_event != null) {
            return
        }
        
        // Create JSON data    
        var message = {
            event: "SHOW_MENU",
            values: {}
        };

        // Convert to string
        var json = JSON.stringify(message);

        // Send json data
        ws.send(json);
    }

    function showPayment(payload) {
        const payment_details = payload.payment_details

        var qr_url = ""
        for (let item of payment_details.actions) {
            if (item.name === "generate-qr-code") {
                qr_url = item.url
            }
        }

        document.body.innerHTML = `
            <h2 class="title">Please do payment using QRIS</h2>
            <div class="card">
                <img height="350" src="${qr_url}">
            </div>
            <p class="subtitle">You will buy ${payload.item_details[0].name}, 
                the price is Rp ${payload.transaction_details.gross_amount}</p>
            <p class="subtitle">The code will be expired in 15 minutes</p>
        `
    }

    function showMenu(values) {

        var drink = values

        const cardsContainer = document.createElement('div');
        cardsContainer.classList.add('cards');

        values.forEach(drink => {
            const card = document.createElement('div');
            card.classList.add('card-drink');
            card.setAttribute('data-item', drink.id.toString());

            const image = document.createElement('img');
            image.classList.add('image-bottle');
            image.src = drink.icon;
            image.width = 100;

            const name = document.createElement('p');
            name.textContent = drink.name;

            card.appendChild(image);
            card.appendChild(name);
            cardsContainer.appendChild(card);
        });

        const heading = document.createElement('h2');
        heading.textContent = 'Please choose a drink';

        document.body.innerHTML = '';
        document.body.appendChild(heading);
        document.body.appendChild(cardsContainer);

        var cards = document.getElementsByClassName("card-drink");
        for (var i = 0; i < cards.length; i++) {
            cards[i].addEventListener("click", function () {
                cardClicked(this);
            });
        }

    }

    function showLoading() {
        document.body.innerHTML = `
            <h2 class="title">Please wait</h2>
            <p class="subtitle">Creating your payment...</p>
        `
    }

    function cardClicked(element) {
        try {
            var item = element.getAttribute("data-item");

            // Create JSON data    
            var message = {
                event: "ORDER",
                values: {
                    "id": item,
                    "total": 1
                }
            };

            // Convert to string
            var json = JSON.stringify(message);

            showLoading()
            // Send json data
            setTimeout(() => {
                ws.send(json);
            }, 2000)

        } catch (e) {
            console.log(e)
        }
    }

    document.body.onclick = handleBodyClick;
</script>
</html>
```

Sekarang coba jalankan dan lihat hasilnya.