
import argparse

from cores.broker import Broker
from constants.services import Services, all_services
from services.order_service import OrderService
from services.invoice_service import InvoiceService
from time import sleep


class Main:
    def __init__(self):
        self.redis = Broker()

    def execute(self, service: str):
        try:
            service = service.upper()
            if service not in all_services:
                print(f"Service is not found. Input: {service}")

            app = None
            if service == Services.ORDER_SERVICE.value:
                app = OrderService(broker=self.redis)
            elif service == Services.INVOICE_SERVICE.value:
                app = InvoiceService(broker=self.redis)

            print(f"Service {app} started....")
            while True:
                app.execute()
                sleep(0.5)
        except Exception as e:
            print(e)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Processing app service.")
    parser.add_argument("--service", type=str, required=True, help="Service of app")

    args = parser.parse_args()
    m = Main()
    m.execute(args.service)
