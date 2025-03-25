import enum

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

