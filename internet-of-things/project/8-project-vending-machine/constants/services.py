from enum import Enum

class Services(Enum):
    ORDER_SERVICE = "ORDER"
    ORDER_CREATED_SERVICE = "ORDER_CREATED"
    INVOICE_SERVICE = "INVOICE"
    
all_services = [i.value for i in Services]