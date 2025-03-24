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
        self.__guest_id = guest_id
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
