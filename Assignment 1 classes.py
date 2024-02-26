from datetime import datetime
from enum import Enum

#defined enums for gender options and seat types
class Gender(Enum):
    FEMALE = "Female"
    MALE = "Male"

class SeatType(Enum):
    ECONOMY = "Economy"
    BUSINESS = "Business"
    FIRST_CLASS = "First Class"

#Passenger class to encapsulate attributes about a flight passenger
class Passenger:
    ''' A class to represent a passenger '''
    def __init__(self, name, gender, passport_number, email, contact_number, has_checked_baggage=False):
        #Initializing passenger attributes
        self.__name = name
        self.__gender = gender
        self.__passport_number = passport_number
        self.__email = email
        self.__contact_number = contact_number
        self.__has_checked_baggage = has_checked_baggage

    #getter and setter methods for each attribute to provide controlled access
    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        self.__gender = gender

    def get_passport_number(self):
        return self.__passport_number

    def set_passport_number(self, passport_number):
        self.__passport_number = passport_number

    def get_email(self):
        return self.__email

    def set_email(self, email):
        self.__email = email

    def get_contact_number(self):
        return self.__contact_number

    def set_contact_number(self, contact_number):
        self.__contact_number = contact_number

    def get_has_checked_baggage(self):
        return self.__has_checked_baggage

    def set_has_checked_baggage(self, has_checked_baggage):
        self.__has_checked_baggage = has_checked_baggage

# Flight Class
class Flight:
    ''' A class that represents an airline flight with departure and arrival details '''
    def __init__(self, flight_number, departure_airport, arrival_airport, departure_time, arrival_time):
        #Initializing flight attributes with provided values
        self.__flight_number = flight_number
        self.__departure_airport = departure_airport
        self.__arrival_airport = arrival_airport
        self.__departure_time = departure_time
        self.__arrival_time = arrival_time

    #getter and setter for the attributes
    def get_flight_number(self):
        return self.__flight_number

    def set_flight_number(self, flight_number):
        self.__flight_number = flight_number

    def get_departure_airport(self):
        return self.__departure_airport

    def set_departure_airport(self, departure_airport):
        self.__departure_airport = departure_airport

    def get_arrival_airport(self):
        return self.__arrival_airport

    def set_arrival_airport(self, arrival_airport):
        self.__arrival_airport = arrival_airport

    def get_departure_time(self):
        return self.__departure_time

    def set_departure_time(self, departure_time):
        self.__departure_time = departure_time

    def get_arrival_time(self):
        return self.__arrival_time

    def set_arrival_time(self, arrival_time):
        self.__arrival_time = arrival_time

# Ticket Class
class Ticket:
    ''' A class that represents a flight ticket issued to a passenger, including its attributes '''
    def __init__(self, ticket_id, passenger_name, flight_reference, issue_date, price, seat_type=SeatType.FIRST_CLASS):
        #Initializing Ticket attributes
        self._ticket_id = ticket_id
        self._passenger_name = passenger_name
        self._flight_reference = flight_reference
        self._issue_date = issue_date
        self._price = price
        self._seat_type = seat_type

    #getter and setter for the attributes
    def get_ticket_id(self):
        return self._ticket_id

    def set_ticket_id(self, ticket_id):
        self._ticket_id = ticket_id

    def get_passenger_name(self):
        return self._passenger_name

    def set_passenger_name(self, passenger_name):
        self._passenger_name = passenger_name

    def get_flight_reference(self):
        return self._flight_reference

    def set_flight_reference(self, flight_reference):
        self._flight_reference = flight_reference

    def get_issue_date(self):
        return self._issue_date

    def set_issue_date(self, issue_date):
        self._issue_date = issue_date

    def get_price(self):
        return self._price

    def set_price(self, price):
        if price < 0:
            return f"Price cannot be negative."
        self._price = price

    def get_seat_type(self):
        return self._seat_type

    def set_seat_type(self, seat_type):
        if seat_type not in SeatType:
            return f"Invalid seat type."
        self._seat_type = seat_type

# BoardingPass Class, inherits from Ticket
class BoardingPass(Ticket):
    ''' A class inheriting from the Ticket class, representing a boarding pass. '''
    def __init__(self, seat_number, boarding_group, gate_number, boarding_time, zone, ticket_id, passenger_name, flight_reference, issue_date, price, seat_type):
        # Initialize parent class with common ticket attributes
        super().__init__(ticket_id, passenger_name, flight_reference, issue_date, price, seat_type)
        # Initialize BoardingPass-specific attributes
        self.__seat_number = seat_number
        self.__boarding_group = boarding_group
        self.__gate_number = gate_number
        self.__boarding_time = boarding_time
        self.__zone = zone

    #getter and setter for the boarding pass attributes
    def get_seat_number(self):
        return self.__seat_number

    def set_seat_number(self, seat_number):
        self.__seat_number = seat_number

    def get_boarding_group(self):
        return self.__boarding_group

    def set_boarding_group(self, boarding_group):
        self.__boarding_group = boarding_group

    def get_gate_number(self):
        return self.__gate_number

    def set_gate_number(self, gate_number):
        self.__gate_number = gate_number

    def get_boarding_time(self):
        return self.__boarding_time

    def set_boarding_time(self, boarding_time):
        self.__boarding_time = boarding_time

    def get_zone(self):
        return self.__zone

    def set_zone(self, zone):
        self.__zone = zone

# Baggage Class
class Baggage:
    '''Represents baggage associated with a passenger, including weight, dimensions, and any extra fees.'''
    def __init__(self, baggage_id, weight, dimensions, passenger_id, extra_fee=0):
        # Initialize baggage ID, weight, dimensions, associated passenger ID, and optionally extra fees
        self.__baggage_id = baggage_id
        self.__weight = weight
        self.__dimensions = dimensions
        self.__passenger_id = passenger_id
        self.__extra_fee = extra_fee

    #getter and setter for the baggage attributes
    def get_baggage_id(self):
        return self.__baggage_id

    def set_baggage_id(self, baggage_id):
        self.__baggage_id = baggage_id

    def get_weight(self):
        return self.__weight

    def set_weight(self, weight):
        self.__weight = weight
        self.calculate_fee()

    def get_dimensions(self):
        return self.__dimensions

    def set_dimensions(self, dimensions):
        self.__dimensions = dimensions

    def get_passenger_id(self):
        return self.__passenger_id

    def set_passenger_id(self, passenger_id):
        self.__passenger_id = passenger_id

    #Updating the extra fee for the baggage
    def get_extra_fee(self):
        return self.__extra_fee

    def set_extra_fee(self, extra_fee):
        self.__extra_fee = extra_fee

    #Calculating any extra fee based on the baggage weight
    def calculate_fee(self):
        #Checking if the baggage weight exceeds the standard weight limit of 20kg
        if self.__weight > 20:
            #Calculates excess weight by subtracting the limit (20) from the actual weight
            excess_weight = self.__weight - 20
            #Calculates the extra fee based on the excess weight. each kilogram above the limit costs 150 AED.
            self.__extra_fee = excess_weight * 150  #Assuming a rate of 150 AED per excess kilogram
        else:
            #If the baggage does not exceed the weight limit, no extra fee is charged
            self.__extra_fee = 0

    #Process payment for any extra baggage fees
    def pay_for_extra_baggage(self):
        #First, calculate the extra fee based on the current weight of the baggage
        self.calculate_fee()
        #If there's an extra fee to be charged...
        if self.__extra_fee > 0:
            # Print a message indicating the extra fee amount and confirm the charge
            print(f"Extra baggage fee of {self.__extra_fee} AED charged for {self.__weight}kg.")
            return True  #Return True to indicate an extra fee was charged
        else:
            #If there is no extra fee needed, printing the following
            print("No extra baggage fee required.")
            return False  #Return False to indicate no extra fee was charged


#displaying the usage of each class using getters

def displayPassenger(passenger):
    print("\n=== Passenger Information ===")
    print("Name:", passenger.get_name())
    print("Gender:", passenger.get_gender().name)  # .name to get the name of the Enum member in this case gender
    print("Passport Number:", passenger.get_passport_number())
    print("Email:", passenger.get_email())
    print("Contact Number:", passenger.get_contact_number())
    print("Has Checked Baggage:", "Yes" if passenger.get_has_checked_baggage() else "No")

def displayFlight(flight):
    print("\n=== Flight Information ===")
    print("Flight Number:", flight.get_flight_number())
    print("Departure Airport:", flight.get_departure_airport())
    print("Arrival Airport:", flight.get_arrival_airport())
    print("Departure Time:", flight.get_departure_time())
    print("Arrival Time:", flight.get_arrival_time())

def displayTicket(ticket):
    print("\n=== Ticket Information ===")
    print("Ticket ID:", ticket.get_ticket_id())
    print("Passenger Name:", ticket.get_passenger_name())
    print("Flight Reference:", ticket.get_flight_reference())
    print("Issue Date:", ticket.get_issue_date())
    print("Price:", ticket.get_price())
    print("Seat Type:", ticket.get_seat_type().name)  # .name to get the name of the Enum member in this case which seat type

def displayBoardingPass(boardingPass):
    print("\n=== Boarding Pass Information ===")
    #Inherits and displays Ticket info using the overridden or inherited methods from Ticket
    print("Ticket ID:", boardingPass.get_ticket_id())
    print("Passenger Name:", boardingPass.get_passenger_name())
    print("Flight Reference:", boardingPass.get_flight_reference())
    print("Issue Date:", boardingPass.get_issue_date())
    print("Price:", boardingPass.get_price())
    print("Seat Type:", boardingPass.get_seat_type().name)  # Enum name for readability
    # Boarding Pass specific information
    print("Seat Number:", boardingPass.get_seat_number())
    print("Boarding Group:", boardingPass.get_boarding_group())
    print("Gate Number:", boardingPass.get_gate_number())
    print("Boarding Time:", boardingPass.get_boarding_time())
    print("Zone:", boardingPass.get_zone())


def displayBaggage(baggage):
    print("\n=== Baggage Information ===")
    print("Baggage ID:", baggage.get_baggage_id())
    print("Weight:", baggage.get_weight())
    print("Dimensions:", baggage.get_dimensions())
    print("Passenger ID:", baggage.get_passenger_id())
    print("Extra Fee:", baggage.get_extra_fee())

#Example instances
passenger = Passenger("James Smith", Gender.MALE, "P123456789", "JamesSmith@Gmail.com", "+1234567890", True)
flight = Flight("FL100", "CHI", "JFK", "2024-01-01 09:00", "2024-01-01 12:00")
ticket = Ticket("629", passenger.get_name(), flight.get_flight_number(), "2024-01-01", 500 , SeatType.FIRST_CLASS)
boardingPass = BoardingPass("12A", "1", "G5", "2024-01-01 08:00", "A", ticket.get_ticket_id(), ticket.get_passenger_name(), ticket.get_flight_reference(), ticket.get_issue_date(), ticket.get_price(), ticket.get_seat_type())
baggage = Baggage("B1000", 21, "45x55x25", passenger.get_passport_number())
baggage.calculate_fee()  # fee calculation added on

#Display information using the display functions
displayPassenger(passenger)
displayFlight(flight)
displayTicket(ticket)
displayBoardingPass(boardingPass)
displayBaggage(baggage)
