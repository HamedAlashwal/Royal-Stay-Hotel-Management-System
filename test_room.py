from room import Room, RoomType

# Test 1
room1 = Room(101, RoomType.SINGLE, ["Wi-Fi", "TV"], 300, True)
room2 = Room(202, RoomType.SUITE, ["Wi-Fi", "Mini-Bar", "TV"], 800, False)

print("\n===== Test 1 ======")
print(room1.get_room_number())  # Expected-: 101
print(room1.get_room_type())  # Expected-: RoomType.SINGLE
print(room1.get_amenities())  # Expected-: ["Wi-Fi", "TV"]
print(room1.get_price())  # Expected-: 300
print(room1.is_available())  # Expected-: True

print(room2.get_room_number())  # Expected-: 202
print(room2.get_room_type())  # Expected-: RoomType.SUITE
print(room2.get_amenities())  # Expected-: ["Wi-Fi", "Mini-Bar", "TV"]
print(room2.get_price())  # Expected-: 800
print(room2.is_available())  # Expected-: False

# Test 2
print("\n===== Test 2 ======")
room1.set_availability(False)
print(room1.is_available() == False)  # Expected-: Condition must be True
