import enum

class PaymentStatus(enum.Enum):
    """Payment status options."""
    PENDING = "Pending"
    PAID = "Paid"
    FAILED = "Failed"

class Invoice:
    """Represents an invoice for a booking."""

    def __init__(self, invoice_id, booking, total_amount, status=PaymentStatus.PENDING):
        self.__invoice_id = invoice_id
        self.__booking = booking
        self.set_total_amount(total_amount)
        self.set_status(status)

    def get_invoice_id(self):
        """Returns the invoice ID."""
        return self.__invoice_id

    def get_booking(self):
        """Returns the associated booking."""
        return self.__booking

    def get_total_amount(self):
        """Returns the total amount."""
        return self.__total_amount

    def get_status(self):
        """Returns the payment status."""
        return self.__status

    def set_status(self, status):
        """Sets the payment status if valid."""
        if isinstance(status, PaymentStatus):
            self.__status = status
        else:
            raise ValueError("Invalid payment status")

    def set_total_amount(self, total_amount):
        """Sets the total amount if valid."""
        if total_amount >= 0:
            self.__total_amount = total_amount
        else:
            raise ValueError("Total amount must be non-negative")

    def __str__(self):
        """Returns a string representation of the invoice."""
        return "Invoice ID: " + str(self.__invoice_id) + ", Booking ID: " + str(self.__booking.get_booking_id()) + ", Total: AED " + str(self.__total_amount) + ", Status: " + self.__status.value
