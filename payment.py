import enum

class PaymentMethod(enum.Enum):
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    MOBILE_WALLET = "Mobile Wallet"
    CASH = "Cash"

class Payment:
    def __init__(self, payment_id, invoice, method, amount):
        self.__payment_id = payment_id
        self.__invoice = invoice 
        self.__method = method  
        self.__amount = amount

    def get_payment_id(self):
        return self.__payment_id

    def get_invoice(self):
        return self.__invoice

    def get_method(self):
        return self.__method

    def get_amount(self):
        return self.__amount

    def __str__(self):
        return "Payment ID: " + str(self.__payment_id) + ", Invoice ID: " + str(self.__invoice.get_invoice_id()) + ", Method: " + self.__method.value + ", Amount: AED " + str(self.__amount)
