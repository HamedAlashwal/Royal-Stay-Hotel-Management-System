import enum

class RoomType(enum.Enum):
    """Room type options."""
    SINGLE = "Single"
    DOUBLE = "Double"
    SUITE = "Suite"

class Room:
    """Represents a hotel room."""

    def __init__(self, room_number, room_type, price_per_night, amenities, available):
        self.__room_number = room_number
        self.set_room_type(room_type)
        self.set_price(price_per_night)
        self.__amenities = amenities
        self.set_availability(available)

    def get_room_number(self):
        """Returns the room number."""
        return self.__room_number

    def get_room_type(self):
        """Returns the room type."""
        return self.__room_type

    def get_price(self):
        """Returns the price per night."""
        return self.__price

    def get_amenities(self):
        """Returns the list of amenities."""
        return self.__amenities

    def is_available(self):
        """Returns availability status."""
        return self.__available

    def set_room_type(self, room_type):
        """Sets the room type if valid."""
        if isinstance(room_type, RoomType):
            self.__room_type = room_type
        else:
            raise ValueError("Invalid room type")

    def set_price(self, price_per_night):
        """Sets the price per night if valid."""
        if price_per_night > 0:
            self.__price = price_per_night
        else:
            raise ValueError("Price must be positive")

    def set_availability(self, status):
        """Sets the availability status."""
        if isinstance(status, bool):
            self.__available = status
        else:
            raise ValueError("Availability must be a boolean value")

    def __str__(self):
        """Returns a string representation of the room."""
        return "Room " + str(self.__room_number) + " (" + self.__room_type.value + ") - AED " + str(self.__price) + "/night, Available: " + str(self.__available)
