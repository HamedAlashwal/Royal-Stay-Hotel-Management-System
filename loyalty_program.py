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
