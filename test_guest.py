from guest import Guest, LoyaltyStatus

guest1 = Guest(1, "Ali Hassan", "ali.hassan@gmail.com", "+971501234567", LoyaltyStatus.REGULAR)
guest2 = Guest(2, "Fatima Noor", "fatima.noor@gmail.com", "+971502345678", LoyaltyStatus.GOLD)


print("\n===== Test 1 ======")
print(guest1.get_guest_id())  # Expected-: 1
print(guest1.get_name())  # Expected-: Ali Hassan
print(guest1.get_email())  # Expected-: ali.hassan@gmail.com
print(guest1.get_phone())  # Expected-: +971501234567
print(guest1.get_loyalty_status())  # Expected-: LoyaltyStatus.REGULAR

print(guest2.get_guest_id())  # Expected-: 2
print(guest2.get_name())  # Expected-: Fatima Noor
print(guest2.get_email())  # Expected-: fatima.noor@gmail.com
print(guest2.get_phone())  # Expected-: +971502345678
print(guest2.get_loyalty_status())  # Expected-: LoyaltyStatus.GOLD


print("\n===== Test 2 ======")
guest1.set_loyalty_status(LoyaltyStatus.SILVER)
print(guest1.get_loyalty_status())  # Expected-: LoyaltyStatus.SILVER
