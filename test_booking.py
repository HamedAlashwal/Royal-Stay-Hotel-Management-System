from booking import Booking, BookingStatus
from guest import Guest, LoyaltyStatus
from room import Room, RoomType
from datetime import date

print("\n===== Test 1 ======")

guest = Guest(1, "Ali Hassan", "ali.hassan@example.ae", "+971501234567", LoyaltyStatus.REGULAR)
room = Room(101, RoomType.SINGLE, 350, ["Wi-Fi", "TV"], True)

booking = Booking(1, guest, room, date(2025, 3, 28), date(2025, 3, 30), BookingStatus.PENDING)

print(booking.get_booking_id())  # Expected-: 1
print(booking.get_guest().get_name())  # Expected-: Ali Hassan
print(booking.get_room().get_room_number())  # Expected-: 101
print(booking.get_check_in())  # Expected-: 2025-03-28
print(booking.get_check_out())  # Expected-: 2025-03-30

print("\n===== Test 2 ======")

booking.set_check_out(date(2025, 4, 1))
print(booking.get_check_out())  # Expected-: 2025-04-01
