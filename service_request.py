import enum

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
