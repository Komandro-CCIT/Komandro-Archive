from services.base_service import BaseService
from cores.broker import Broker
from constants.states import AppStates
from time import sleep
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

        # Do code here
        sleep(3)
        # Sample sleep 3 seconds to pretend like code do something

        new_state = AppStates.IDLE.value
        self.broker.set_state(new_state)
        self.logger.info(f"Change state into: {new_state}")
