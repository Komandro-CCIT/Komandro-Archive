from services.base_service import BaseService
from cores.broker import Broker
from constants.states import AppStates
from time import sleep


class InvoiceService(BaseService):
    allowed_states = [AppStates.ORDER_CANCELED.value, AppStates.ORDER_PAID.value]

    def __init__(self, broker: Broker):
        self.broker = broker

    def execute(self):
        state = self.broker.get_state()
        if state not in self.allowed_states:
            return False

        print(f"Invoice service started. State: {self}")

        # Do code here
        sleep(3)
        # Sample sleep 3 seconds to pretend like code do something

        new_state = AppStates.IDLE.value
        self.broker.set_state(new_state)
        print(f"Change state into: {new_state}")
