class LoyaltyProgram:
    """Represents a loyalty program for a guest."""

    def __init__(self, guest, points):
        self.__guest = guest
        self.set_points(points)

    def get_guest(self):
        """Returns the guest."""
        return self.__guest

    def get_points(self):
        """Returns the loyalty points."""
        return self.__points

    def set_points(self, points):
        """Sets the loyalty points if valid."""
        if points >= 0:
            self.__points = points
        else:
            raise ValueError("Points must be non-negative")

    def add_points(self, points):
        """Adds points if valid."""
        if points > 0:
            self.__points += points
        else:
            raise ValueError("Points to add must be positive")

    def redeem_points(self, points):
        """Redeems points if enough are available."""
        if 0 < points <= self.__points:
            self.__points -= points
            return True
        return False

    def __str__(self):
        """Returns a string representation of the loyalty program."""
        return "Guest: " + self.__guest.get_name() + ", Loyalty Points: " + str(self.__points)
