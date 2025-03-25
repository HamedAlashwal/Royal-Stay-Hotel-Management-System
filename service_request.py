import enum

class ServiceType(enum.Enum):
    """Service type options."""
    HOUSEKEEPING = "Housekeeping"
    ROOM_SERVICE = "Room Service"
    TRANSPORTATION = "Transportation"
    LAUNDRY = "Laundry"

class RequestStatus(enum.Enum):
    """Request status options."""
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class ServiceRequest:
    """Represents a service request made by a guest."""

    def __init__(self, request_id, guest, service_type, status):
        self.__request_id = request_id
        self.__guest = guest
        self.set_service_type(service_type)
        self.set_status(status)

    def get_request_id(self):
        """Returns the request ID."""
        return self.__request_id

    def get_guest(self):
        """Returns the guest."""
        return self.__guest

    def get_service_type(self):
        """Returns the service type."""
        return self.__service_type

    def get_status(self):
        """Returns the request status."""
        return self.__status

    def set_service_type(self, service_type):
        """Sets the service type if valid."""
        if isinstance(service_type, ServiceType):
            self.__service_type = service_type
        else:
            raise ValueError("Invalid service type")

    def set_status(self, status):
        """Sets the request status if valid."""
        if isinstance(status, RequestStatus):
            self.__status = status
        else:
            raise ValueError("Invalid request status")

    def __str__(self):
        """Returns a string representation of the service request."""
        return "Request ID: " + str(self.__request_id) + ", Guest: " + self.__guest.get_name() + ", Service: " + self.__service_type.value + ", Status: " + self.__status.value
