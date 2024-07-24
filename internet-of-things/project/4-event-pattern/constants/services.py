from enum import Enum

class Services(Enum):
    ORDER_SERVICE = "ORDER"
    INVOICE_SERVICE = "INVOICE"
    
all_services = [i.value for i in Services]