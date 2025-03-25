import enum

class BookingStatus(enum.Enum):
    """Booking status options."""
    PENDING = "Pending"
    CONFIRMED = "Confirmed"
    CANCELED = "Canceled"
    COMPLETED = "Completed"

class Booking:
    """Represents a hotel booking."""

    def __init__(self, booking_id, guest, room, check_in, check_out, status):
        self.__booking_id = booking_id
        self.__guest = guest  
        self.__room = room 
        self.__check_in = check_in  
        self.set_check_out(check_out)
        self.set_status(status)

    def get_booking_id(self):
        """Returns the booking ID."""
        return self.__booking_id

    def get_guest(self):
        """Returns the guest."""
        return self.__guest

    def get_room(self):
        """Returns the room."""
        return self.__room

    def get_check_in(self):
        """Returns the check-in date."""
        return self.__check_in

    def get_check_out(self):
        """Returns the check-out date."""
        return self.__check_out

    def get_status(self):
        """Returns the booking status."""
        return self.__status

    def set_status(self, status):
        """Sets the booking status if valid."""
        if isinstance(status, BookingStatus):
            self.__status = status
        else:
            raise ValueError("Invalid status")

    def set_check_out(self, check_out):
        """Sets the check-out date if valid."""
        if check_out >= self.__check_in:
            self.__check_out = check_out  
        else:
            raise ValueError("Check-out date must be after check-in date")

    def __str__(self):
        """Returns a string representation of the booking."""
        return "Booking ID: " + str(self.__booking_id) + ", Guest: " + self.__guest.get_name() + ", Room: " + str(self.__room.get_room_number()) + ", Check-in: " + str(self.__check_in) + ", Check-out: " + str(self.__check_out) + ", Status: " + self.__status.value
