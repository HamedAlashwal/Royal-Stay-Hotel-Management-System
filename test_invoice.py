from invoice import Invoice, PaymentStatus
from booking import Booking, BookingStatus
from guest import Guest, LoyaltyStatus
from room import Room, RoomType
from datetime import date

print("\n===== Test 1 ======")

guest = Guest(1, "Ali Khan", "ali.khan@example.ae", "+971501234567", LoyaltyStatus.GOLD)
room = Room(101, RoomType.SINGLE, 350, ["Wi-Fi", "TV"], True)
booking = Booking(10, guest, room, date(2025, 4, 1), date(2025, 4, 5), BookingStatus.CONFIRMED)

invoice = Invoice(1001, booking, 1400, PaymentStatus.PENDING)

print(invoice.get_invoice_id())  # Expected-: 1001
print(invoice.get_booking().get_booking_id())  # Expected-: 10
print(invoice.get_total_amount())  # Expected-: 1400
print(invoice.get_status().value)  # Expected-: Pending

invoice.set_status(PaymentStatus.PAID)

print(invoice.get_status().value)  # Expected-: Paid


print("\n===== Test 2 ======")

guest2 = Guest(2, "Fatima Noor", "fatima.noor@example.ae", "+971502345678", LoyaltyStatus.SILVER)
room2 = Room(202, RoomType.DOUBLE, 500, ["Wi-Fi", "TV", "Mini-Bar"], True)

booking2 = Booking(11, guest2, room2, date(2025, 5, 10), date(2025, 5, 15), BookingStatus.CONFIRMED)

invoice2 = Invoice(1002, booking2, 2700, PaymentStatus.PENDING)

print(invoice2.get_invoice_id())  # Expected-: 1002
print(invoice2.get_booking().get_booking_id())  # Expected-: 11
print(invoice2.get_total_amount())  # Expected-: 2700
print(invoice2.get_status().value)  # Expected-: Pending

invoice2.set_status(PaymentStatus.FAILED)
print(invoice2.get_status().value)  # Expected-: Failed