from guest import Guest, LoyaltyStatus
from booking import Booking, BookingStatus
from room import Room, RoomType

print("\n===== Test 1 ======")

guest = Guest(5, "Khalid Al Mansoori", "khalid.mansoori@example.ae", "+971509876543", LoyaltyStatus.GOLD)

room1 = Room(201, RoomType.SUITE, 900, ["WiFi", "Breakfast", "Sea View"], True)
room2 = Room(305, RoomType.DOUBLE, 600, ["WiFi", "City View"], True)

booking1 = Booking(101, guest, room1, "2025-04-01", "2025-04-05", BookingStatus.COMPLETED)
booking2 = Booking(102, guest, room2, "2025-05-10", "2025-05-15", BookingStatus.CONFIRMED)

reservation_history = [booking1, booking2]

for booking in reservation_history:
    print(booking)