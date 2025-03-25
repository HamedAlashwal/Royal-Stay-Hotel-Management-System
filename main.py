import enum

class RoomType(enum.Enum):
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

class Room:
    def __init__(self, room_number, room_type, price_per_night, amenities, available):
        self.__room_number = room_number
        self.__room_type = room_type 
        self.__price_per_night = price_per_night
        self.__amenities = amenities
        self.__available = available

    def get_room_number(self):
        return self.__room_number

    def get_room_type(self):
        return self.__room_type

    def get_price_per_night(self):
        return self.__price_per_night

    def get_amenities(self):
        return self.__amenities

    def is_available(self):
        return self.__available

    def set_availability(self, status):
        self.__available = status

    def __str__(self):
        return "Room " + str(self.__room_number) + " (" + self.__room_type.value + ") - AED " + str(self.__price_per_night) + "/night, Available: " + str(self.__available)



class LoyaltyStatus(enum.Enum):
    REGULAR = "Regular"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class Guest:
    def __init__(self, guest_id, name, email, phone, loyalty_status):
        self.__guest_id = guest_idx
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.__loyalty_status = loyalty_status

    def get_guest_id(self):
        return self.__guest_id

    def get_name(self):
        return self.__name

    def get_email(self):
        return self.__email

    def get_phone(self):
        return self.__phone

    def get_loyalty_status(self):
        return self.__loyalty_status

    def set_loyalty_status(self, status):
        self.__loyalty_status = status

    def __str__(self):
        return "Guest ID: " + str(self.__guest_id) + ", Name: " + self.__name + ", Email: " + self.__email + ", Phone: " + self.__phone + ", Loyalty Status: " + self.__loyalty_status.value


class BookingStatus(enum.Enum):
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"
    COMPLETED = "Completed"

class Booking:
    def __init__(self, booking_id, guest, room, check_in, check_out, status):
        self.__booking_id = booking_id
        self.__guest = guest  
        self.__room = room 
        self.__check_in = check_in  
        self.__check_out = check_out  
        self.__status = status

    def get_booking_id(self):
        return self.__booking_id

    def get_guest(self):
        return self.__guest

    def get_room(self):
        return self.__room

    def get_check_in(self):
        return self.__check_in

    def get_check_out(self):
        return self.__check_out

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return "Booking ID: " + str(self.__booking_id) + ", Guest: " + self.__guest.get_name() + ", Room: " + str(self.__room.get_room_number()) + ", Check-in: " + str(self.__check_in) + ", Check-out: " + str(self.__check_out) + ", Status: " + self.__status.value

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
