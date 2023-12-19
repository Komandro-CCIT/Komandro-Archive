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
