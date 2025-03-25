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

