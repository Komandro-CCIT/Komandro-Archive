from cores.broker import Broker
from constants.states import AppStates
from constants.redis_prefix import RedisPrefix
from datetime import timedelta
import json


class WebsocketEvents:
    def __init__(self, event: str, payload: dict):
        self.event = event
        self.payload = payload

        db = 0
        self.redis = Broker(db=db)

    def execute(self):
        events = {
            "SHOW_MENU": self.choose_menu,
            "ORDER": self.order,
        }

        if self.event not in events:
            return False

        return events[self.event]()

    def choose_menu(self):
        prefix = RedisPrefix.DRINK_ITEMS.value

        res = self.redis.read_single_data(prefix)

        data = {}
        if res:
            data = json.loads(res)

        return {"event": "SHOW_MENU", "values": data}

    def order(self):
        payload = self.payload

        data = {"id": payload.get("id")}

        data = json.dumps(data)
        self.redis.create_single_data(
            RedisPrefix.SELECTED_MENU_DATA.value, data, expired=timedelta(hours=24)
        )
        self.redis.set_state(AppStates.MENU_CLICKED.value)

        return {"EVENT": "MENU_CLICKED", "values": {}}
