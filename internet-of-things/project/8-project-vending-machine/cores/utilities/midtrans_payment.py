import midtransclient


class MidtransPayment:
    def __init__(
        self, is_production: bool = False, client_key: str = "", server_key: str = ""
    ):
        self.core_api = midtransclient.CoreApi(
            is_production=is_production,
            server_key=server_key,
            client_key=client_key,
        )

    def create_qr(
        self,
        transaction_details: dict = {},
        item_details: list = [],
        customer_details: dict = {},
    ):
        payload = {
            "payment_type": "gopay",
            "item_details": item_details,
            "transaction_details": transaction_details,
            "customer_details": customer_details
        }

        return self.core_api.charge(payload)

    def check_transaction(self, order_id: str):
        """Sample Response
        {
            "status_code" : "200",
            "status_message" : "Success, Credit Card transaction is successful",
            "transaction_id" : "249fc620-6017-4540-af7c-5a1c25788f46",
            "masked_card" : "48111111-1114",
            "order_id" : "example-1424936368",
            "payment_type" : "credit_card",
            "transaction_time" : "2015-02-26 14:39:33",
            "transaction_status" : "capture",
            "fraud_status" : "accept",
            "approval_code" : "1424936374393",
            "signature_key" : "2802a264cb978fbc59f631c68d120cbda8dc853f5dfdc52301c615cf4f14e7a0b09aa...",
            "bank" : "bni",
            "gross_amount" : "30000.00",
            "channel_response_code": "00",
            "channel_response_message": "Approved",
            "card_type": "credit",
            "payment_option_type": "GOPAY_WALLET",
            "shopeepay_reference_number": "103995032913255264",
            "reference_id": "DL-dduIy7XtGtvxJtNNpOfbAt"
        }
        """
        return self.core_api.transactions.status(order_id)
