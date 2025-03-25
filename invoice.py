import enum

class PaymentStatus(enum.Enum):
    PENDING = "Pending"
    PAID = "Paid"
    FAILED = "Failed"

class Invoice:
    def __init__(self, invoice_id, booking, total_amount, status=PaymentStatus.PENDING):
        self.__invoice_id = invoice_id
        self.__booking = booking 
        self.__total_amount = total_amount
        self.__status = status

    def get_invoice_id(self):
        return self.__invoice_id

    def get_booking(self):
        return self.__booking

    def get_total_amount(self):
        return self.__total_amount

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return "Invoice ID: " + str(self.__invoice_id) + ", Booking ID: " + str(self.__booking.get_booking_id()) + ", Total: AED " + str(self.__total_amount) + ", Status: " + self.__status.value
