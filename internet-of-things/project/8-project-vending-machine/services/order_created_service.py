from services.base_service import BaseService
from cores.broker import Broker
from constants.states import AppStates
from constants.redis_prefix import RedisPrefix
from time import sleep
from cores.app_log import AppLogger
from cores.utilities.midtrans_payment import MidtransPayment
import json
import websocket
from datetime import timedelta


class OrderCreatedService(BaseService):
    allowed_states = [AppStates.ORDER_CREATED.value]

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

        self.logger.info(f"Order created service started. State: {self}")

        data = self.broker.read_single_data(RedisPrefix.PAYMENT_DETAIL.value)
        if not data:
            raise Exception("yyy")

        data = json.loads(data)

        order_id = data["payment_details"]["order_id"]

        attempt = 0
        response = None
        new_state = AppStates.PAYMENT_SUCCESS.value
        while attempt < 40:
            response = self.mp.check_transaction(order_id=order_id)
            self.logger.info(f"Check status from Midtrans: {response}")

            status_code = int(response["status_code"])
            if status_code == 200:
                break
            elif status_code == 201:
                attempt += 1
                sleep(1)
            else:
                new_state = AppStates.PAYMENT_FAILED.value
                break

        status_code = int(response["status_code"])
        if status_code != 200:
            new_state = AppStates.PAYMENT_FAILED.value
            self.logger.error(f"Error payment midtrans! Response: {response}")
            self.broker.set_state(new_state)
            return

        self.logger.info(f"Payment finished: {response}")
        self.broker.set_state(new_state)

        ws_payload = json.dumps({"event": new_state, "values": response})
        self.ws.send(ws_payload)
        self.logger.info(f"Change state into: {new_state}")
