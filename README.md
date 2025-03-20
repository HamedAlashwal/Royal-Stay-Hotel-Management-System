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
