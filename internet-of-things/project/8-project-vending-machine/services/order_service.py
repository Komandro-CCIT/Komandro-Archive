from services.base_service import BaseService
from cores.broker import Broker
from constants.states import AppStates
from constants.redis_prefix import RedisPrefix
from time import sleep
from cores.app_log import AppLogger
from cores.utilities.midtrans_payment import MidtransPayment
from datetime import timedelta
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
