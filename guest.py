import enum

class LoyaltyStatus(enum.Enum):
    """Loyalty status options."""
    REGULAR = "Regular"
    SILVER = "Silver"
    GOLD = "Gold"
    PLATINUM = "Platinum"

class Guest:
    """Represents a hotel guest."""

    def __init__(self, guest_id, name, email, phone, loyalty_status):
        self.__guest_id = guest_id
        self.__name = name
        self.__email = email
        self.__phone = phone
        self.set_loyalty_status(loyalty_status)

    def get_guest_id(self):
        """Returns the guest ID."""
        return self.__guest_id

    def get_name(self):
        """Returns the guest name."""
        return self.__name

    def get_email(self):
        """Returns the guest email."""
        return self.__email

    def get_phone(self):
        """Returns the guest phone number."""
        return self.__phone

    def get_loyalty_status(self):
        """Returns the loyalty status."""
        return self.__loyalty_status

    def set_loyalty_status(self, status):
        """Sets the loyalty status if valid."""
        if isinstance(status, LoyaltyStatus):
            self.__loyalty_status = status
        else:
            raise ValueError("Invalid loyalty status")

    def __str__(self):
        """Returns a string representation of the guest."""
        return "Guest ID: " + str(self.__guest_id) + ", Name: " + self.__name + ", Email: " + self.__email + ", Phone: " + self.__phone + ", Loyalty Status: " + self.__loyalty_status.value
