import json

from cores.broker import Broker
from cores.app_log import AppLogger

key = "drink:items"
data =  [
    {
        "id": "ce33fb74-ba55-40c6-99d7-47bef4cd785e",
        "name": "Cola",
        "icon": "assets/images/cola.png",
        "price": 7000
    },
    {
        "id": "4bdfb8e9-2eb7-4db4-9738-a9be7962055f",
        "name": "Lemon",
        "icon": "assets/images/lemon.png",
        "price": 10000
    },
]

r = Broker(db=0)
data = json.dumps(data)
r.create_single_data(key, data)