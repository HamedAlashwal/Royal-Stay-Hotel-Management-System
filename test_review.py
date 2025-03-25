from guest import Guest, LoyaltyStatus
from review import Review, Rating


print("\n===== Test 1 ======")
guest1 = Guest(7, "Ayesha Al Ketbi", "ayesha.ketbi@example.ae", "+971502345678", LoyaltyStatus.SILVER)
review1 = Review(301, guest1, Rating.FOUR_STAR, "Great stay, very comfortable.")
print(review1)

print("\n===== Test 2 ======")

guest2 = Guest(8, "Hassan Al Zarooni", "hassan.zarooni@example.ae", "+971501234567", LoyaltyStatus.GOLD)
review2 = Review(302, guest2, Rating.THREE_STAR, "Good service but room was small.")
print(review2)
