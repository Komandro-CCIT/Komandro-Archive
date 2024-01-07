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
