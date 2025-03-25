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



class LoyaltyProgram:
    def __init__(self, guest, points):
        self.__guest = guest  
        self.__points = points

    def get_guest(self):
        return self.__guest

    def get_points(self):
        return self.__points

    def add_points(self, points):
        self.__points += points

    def redeem_points(self, points):
        if points <= self.__points:
            self.__points -= points
            return True
        return False

    def __str__(self):
        return "Guest: " + self.__guest.get_name() + ", Loyalty Points: " + str(self.__points)

class ServiceType(enum.Enum):
    HOUSEKEEPING = "Housekeeping"
    ROOM_SERVICE = "Room Service"
    TRANSPORTATION = "Transportation"
    LAUNDRY = "Laundry"


class RequestStatus(enum.Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"


class ServiceRequest:
    def __init__(self, request_id, guest, service_type, status):
        self.__request_id = request_id
        self.__guest = guest  
        self.__service_type = service_type  
        self.__status = status 

    def get_request_id(self):
        return self.__request_id

    def get_guest(self):
        return self.__guest

    def get_service_type(self):
        return self.__service_type

    def get_status(self):
        return self.__status

    def set_status(self, status):
        self.__status = status

    def __str__(self):
        return "Request ID: " + str(self.__request_id) + ", Guest: " + self.__guest.get_name() + ", Service: " + self.__service_type.value + ", Status: " + self.__status.value


class Rating(enum.Enum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

class Review:
    def __init__(self, review_id, guest, rating, comment):
        self.__review_id = review_id
        self.__guest = guest
        self.__rating = rating  
        self.__comment = comment

    def get_review_id(self):
        return self.__review_id

    def get_guest(self):
        return self.__guest

    def get_rating(self):
        return self.__rating

    def get_comment(self):
        return self.__comment

    def __str__(self):
        return "Review ID: " + str(self.__review_id) + ", Guest: " + self.__guest.get_name() + ", Rating: " + self.__rating.value + ", Comment: " + self.__comment
