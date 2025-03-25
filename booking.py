import enum

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

    def set_check_out(self, check_out):
        self.__check_out = check_out  
        
    def __str__(self):
        return "Booking ID: " + str(self.__booking_id) + ", Guest: " + self.__guest.get_name() + ", Room: " + str(self.__room.get_room_number()) + ", Check-in: " + str(self.__check_in) + ", Check-out: " + str(self.__check_out) + ", Status: " + self.__status.value
