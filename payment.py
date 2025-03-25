import enum

class PaymentMethod(enum.Enum):
    """Payment method options."""
    CREDIT_CARD = "Credit Card"
    DEBIT_CARD = "Debit Card"
    MOBILE_WALLET = "Mobile Wallet"
    CASH = "Cash"

class Payment:
    """Represents a payment for an invoice."""

    def __init__(self, payment_id, invoice, method, amount):
        self.__payment_id = payment_id
        self.__invoice = invoice
        self.set_method(method)
        self.set_amount(amount)

    def get_payment_id(self):
        """Returns the payment ID."""
        return self.__payment_id

    def get_invoice(self):
        """Returns the associated invoice."""
        return self.__invoice

    def get_method(self):
        """Returns the payment method."""
        return self.__method

    def get_amount(self):
        """Returns the payment amount."""
        return self.__amount

    def set_method(self, method):
        """Sets the payment method if valid."""
        if isinstance(method, PaymentMethod):
            self.__method = method
        else:
            raise ValueError("Invalid payment method")

    def set_amount(self, amount):
        """Sets the payment amount if valid."""
        if amount > 0:
            self.__amount = amount
        else:
            raise ValueError("Amount must be positive")

    def __str__(self):
        """Returns a string representation of the payment."""
        return "Payment ID: " + str(self.__payment_id) + ", Invoice ID: " + str(self.__invoice.get_invoice_id()) + ", Method: " + self.__method.value + ", Amount: AED " + str(self.__amount)
