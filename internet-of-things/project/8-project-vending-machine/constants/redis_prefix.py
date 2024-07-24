from enum import Enum


class RedisPrefix(Enum):
    SELECTED_MENU_DATA = "menu:clicked"
    DRINK_ITEMS = "drink:items"
    PAYMENT_DETAIL = "payment:detail"
    FAILED_PAYMENT = "payment:failed"
