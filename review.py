import enum

class Rating(enum.Enum):
    ONE_STAR = 1
    TWO_STAR = 2
    THREE_STAR = 3
    FOUR_STAR = 4
    FIVE_STAR = 5

class Review:
    def __init__(self, review_id, guest, rating, comment):
        self.__review_id = review_id
        self.__guest = guest
        self.__rating = rating  
        self.__comment = comment

    def get_review_id(self):
        return self.__review_id

    def get_guest(self):
        return self.__guest

    def get_rating(self):
        return self.__rating

    def get_comment(self):
        return self.__comment

    def __str__(self):
        return "Review ID: " + str(self.__review_id) + ", Guest: " + self.__guest.get_name() + ", Rating: " + self.__rating.value + ", Comment: " + self.__comment
