import enum

class Rating(enum.Enum):
    """Rating options."""
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

class Review:
    """Represents a guest review."""

    def __init__(self, review_id, guest, rating, comment):
        self.__review_id = review_id
        self.__guest = guest
        self.set_rating(rating)
        self.__comment = comment

    def get_review_id(self):
        """Returns the review ID."""
        return self.__review_id

    def get_guest(self):
        """Returns the guest."""
        return self.__guest

    def get_rating(self):
        """Returns the rating."""
        return self.__rating

    def get_comment(self):
        """Returns the comment."""
        return self.__comment

    def set_rating(self, rating):
        """Sets the rating if valid."""
        if isinstance(rating, Rating):
            self.__rating = rating
        else:
            raise ValueError("Invalid rating")

    def __str__(self):
        """Returns a string representation of the review."""
        return "Review ID: " + str(self.__review_id) + ", Guest: " + self.__guest.get_name() + ", Rating: " + str(self.__rating.value) + " Stars, Comment: " + self.__comment
