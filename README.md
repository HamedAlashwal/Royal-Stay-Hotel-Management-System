# Royal Stay Hotel Management System  

## UML Class Diagram  
This system helps manage hotel bookings, guest details, payments, and other services.

![UML Diagram](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/Royal%20Stay%20Hotel%20Management%20System%20-%20UML.png)  

## Classes and Relationships  

### **Main Classes**  
- **Room** → Stores room details like type, price, and availability.  
- **Guest** → Stores guest information and booking history.  
- **Booking** → Stores reservations, check-in, and check-out details.  
- **Invoice** → Stores bills for each booking.  
- **Payment** → Stores payment details for invoices.  
- **LoyaltyProgram** → Stores guest reward points.  
- **ServiceRequest** → Stores extra service requests from guests.  
- **Review** → Stores guest feedback about their stay.  

### **Relationships**  
- A **guest** can have **many bookings**. (*One-to-Many*)
- A **booking** is linked to **one room**. (*One-to-One* )
- A **booking** creates **one invoice** (*One-to-One (Composition)*)
- An **invoice** is paid through **one payment method**. (*One-to-One*)  
- A **guest** has **one loyalty account**. (*One-to-One*)
- A **guest** can make **many service requests**. (*One-to-Many*)
- A **guest** can write **many reviews**. (*One-to-Many*)  


## Test Cases  

### [**Booking Class Tests** ](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_booking.py) 

- **Test 1:** Ensures that a booking is correctly created with valid guest and room details, including ID, check-in, and check-out dates.  
- **Test 2:** Verifies that the check-out date of an existing booking can be updated successfully.  

### [**Guest Class Tests** ](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_guest.py) 

- **Test 1:** Checks if guest objects store correct details, including guest ID, name, email, phone number, and loyalty status.  
- **Test 2:** Confirms that a guest’s loyalty status can be modified and reflects the correct updated value.  

### [**Room Class Tests**  ](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_room.py)

- **Test 1:** Ensures room objects store correct details such as room number, type, amenities, price, and availability.  
- **Test 2:** Verifies that room availability can be changed and reflects the updated status.  

### [**Invoice Class Tests**  ](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_invoice.py)

- **Test 1:** Validates that an invoice correctly links to a booking and stores the correct amount and payment status.  
- **Test 2:** Checks if the payment status of an invoice can be updated properly.  

### [**Review Class Tests**  ](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_review.py)

- **Test 1:** Ensures a review object stores correct details, including guest information, rating, and review text.  
- **Test 2:** Verifies that different guests can submit reviews with various ratings and feedback.

### [**Reservation History and Cancellation**](https://github.com/HamedAlashwal/Royal-Stay-Hotel-Management-System/blob/main/test_history_cancellation.py)  

- **Test 1** - Checks if a guest's reservation history is stored correctly. The test creates two bookings for the same guest and prints them to ensure they are recorded properly.  
- **Test 2** - Verifies that a booking can be canceled and that the room becomes available again after cancellation.
