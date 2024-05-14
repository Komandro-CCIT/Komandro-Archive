6 - Automation Testing
---

Author: Hudya (@perogeremmer)

<br />

# Overview

Setelah membuat aplikasi, kita perlu melakukan pengujian. Pengujian yang dilakukan biasanya bisa bersifat manual dan juga otomatis.

Namun bayangkan, apabila test dilakukan secara manual, berapa banyak waktu yang terbuang untuk melakukan test? Bayangkan apabila kita memiliki 100 kasus dan harus melakukan 100 uji coba? Sangat wasting time. Oleh karena itu, dibuatlah unit testing agar developer bisa fokus mengerjakan code dan melakukan tes secara otomatis.

# Code Time

Pada pengerjaannya, silahkan gunakan repository yang sudah dibuat pada [sample nomor 5](./sample/5-logging/) atau silahkan download kembali apabila belum memilikinya.

Sekarang aktifkan virtualenv lalu install library testing yang akan kita gunakan, yaitu PyTest.

```sh
pip install pytest
```

<br/>

Sekarang kita ubah `broker.py` pada folder `cores` pada bagian init, kita menambahkan parameter db, tujuannya agar kita bisa memilih db mana yang kita gunakan.

```python
class Broker:
    def __init__(self, host="localhost", port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = Redis(host=self.host, port=self.port, db=self.db)

        self.prefix: str = "app:state"
        self.decoding: str = "utf-8"
```

Kita bisa memilih db index 0-15 pada Redis. Nantinya untuk testing kita gunakan db index 9.

Sekarang kita tambahkan juga tiga method berikut pada file yang sama:

```python
def create_single_data(self, key: str, values: object):
    return self.redis_client.set(key, values)

def read_single_data(self, key: str):
    data = self.redis_client.get(key)
    
    if not data:
        return None
    
    return data.decode('utf-8')

def flush_all_data(self, force=False):
    if not force:
        return
    
    self.redis_client.flushdb()
    self.redis_client.flushall()
```

- create_single_data: Untuk membuat data baru yang disimpan dengan key
- read_single_data: Untuk membaca data berdasarkan key yang disimpan
- flush_all_data: Untuk menghapus semua data pada DB, kita gunakan untuk testing saja.

Keseluruhan file akan menjadi sperti ini:

```python
from redis import Redis


class Broker:
    def __init__(self, host="localhost", port=6379, db=0):
        self.host = host
        self.port = port
        self.db = db
        self.redis_client = Redis(host=self.host, port=self.port, db=self.db)

        self.prefix: str = "app:state"
        self.decoding: str = "utf-8"

    def get_state(self):
        state = self.redis_client.get(self.prefix)

        if not state:
            return ""

        state = state.decode(self.decoding)
        return state

    def set_state(self, state: str):
        state = self.redis_client.set(name=self.prefix, value=state)

        return state

    def create_single_data(self, key: str, values: object):
        return self.redis_client.set(key, values)

    def read_single_data(self, key: str):
        data = self.redis_client.get(key)
        
        if not data:
            return None
        
        return data.decode('utf-8')

    def flush_all_data(self, force=False):
        if not force:
            return
        
        self.redis_client.flushdb()
        self.redis_client.flushall()
```

<br />

Sekarang pergi ke `services/order_service.py` dan ubah dengan kode berikut:

```python
from uuid import uuid4
from time import sleep
from cores.broker import Broker
from services.base_service import BaseService
from constants.states import AppStates
from cores.app_log import AppLogger


class OrderService(BaseService):
    allowed_states = [
        AppStates.TRANSACTION_CREATED.value,
        AppStates.TRANSACTION_CANCELED.value,
    ]

    def __init__(self, broker: Broker):
        self.broker = broker
        self.logger = AppLogger()

    def execute(self):
        state = self.broker.get_state()

        if state not in self.allowed_states:
            return False

        self.logger.info(f"Order service started. State: {self}")

        order_id = str(uuid4())
        self.broker.create_single_data("LAST_ORDER", order_id)

        b = Broker()
        b.set_state("create_order")

        new_state = AppStates.IDLE.value
        self.broker.set_state(new_state)
        self.logger.info(f"Change state into: {new_state}")

```

Kita menambahkan dua baris berikut:

```python
order_id = str(uuid4())
self.broker.create_single_data("LAST_ORDER", order_id)
```

Tujuannya agar kita bisa mencoba untuk membuat sample bahwa terdapat order yang masuk, dan disimpan pada redis.

Selanjutnya buat folder bernama `tests` sejajar dengan folder `services`, `logs`, dan lainnya.

```plain
├── constants
├── cores
├── logs
├── tests
```

Buat dua file baru didalam folder tests, yaitu `conftest.py` dan `test_order_service.py`:

`conftest.py`

```python
import pytest
from cores.broker import Broker

@pytest.fixture
def setup_database():
    redis = Broker(db=9)
    redis.flush_all_data(force=True)

    yield

    redis.flush_all_data(force=True)
```

File conftest.py digunakan untuk melakukan konfigurasi dasar pada file yang akan diujicoba. Baris yield menandakan kode akan disispkan ditengah-tengahnya, sehingga asumsinya adalah, pada saat kode test berjalan kedua baris berikut akan jalan terlebih dahulu:

```python
    redis = Broker(db=9)
    redis.flush_all_data(force=True)
```

Bagian ini akan menjalankan redis agar menghapus semua data pada db index ke-9.

Setelahnya `yield`, artinya kode tes berjalan di bagian tersebut

Pada bagian akhir database akan dihapus kembali semuanya karena kita melakukan flush data dengan kode setelah yield:

```python
redis.flush_all_data(force=True)
```

<br />

`test_order_service.py`

```python
from cores.broker import Broker
from services.order_service import OrderService
from constants.states import AppStates


class TestOrderService:
    def test_create_order(self, setup_database):
        redis = Broker(db=9)
        redis.set_state(AppStates.TRANSACTION_CREATED.value)

        os = OrderService(redis).execute()

        state = redis.get_state()
        assert state == "IDLE"

        data = redis.read_single_data("LAST_ORDER")
        assert data != ""
```

Pada file di atas, contoh yang dibuat adalah positive test dimana test digunakan untuk menguji coba pembuatan order pada `order service`.

Pertama, kita membuat state agar berubah menjadi `transaction_created`. Setelahnya kita menjalankan service order agar menjalankan fungsi order service.

setelahnya, kita periksa kembali statenya, apakah kembali ke idle atau tidak, dan kita cek order terakhirnya, apakah kosong atau tidak. Secara teori, id order tidak boleh kosong karena order service telah berjalan dan order service akan membuatkan sample order dimana akan disimpan pada redis dengan key `LAST_ORDER`.

<br />


Sekarang kita coba jalankan dengan kode berikut:

```bash
python -m pytest 
```

Hasilnya adalah sebagai berikut:

```bash
================================ test session starts ================================
platform linux -- Python 3.8.18, pytest-7.4.3, pluggy-1.3.0
rootdir: /home/hudya/code/python/workspace
collected 1 item                                                                    

tests/test_order_service.py .                                                 [100%]

================================= 1 passed in 0.03s =================================
```