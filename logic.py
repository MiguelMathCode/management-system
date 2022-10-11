# This script contains the logic needed to enter new bookings, reschedule,
# accept, deny, cancel
import datetime
import random
import string
from pydantic import BaseModel


def booking_code_generator(length: int):
    " Function that generates random booking code "
    characters = string.ascii_uppercase + string.digits
    return "".join(random.choice(characters) for i in range(length))


class Bookings(BaseModel):
    " Defining the object Booking and its attributes "
    name: str = None
    nights: int = None
    beds: int = None
    cellphone: str = None
    date: datetime.date = None
    payment_mehtod: str = None
    status: str | None = "Pending for approval"
    booking_code: str = booking_code_generator(6)

    def update_status(self, new_status: str):
        " Defining method that updates booking status "
        self.status = new_status

class Subscriber:
    def __init__(self, name):
        self.name = name

    def poster(self, message):
        " Defining method that post messages "
        print(f"{self.name} got message {message}")


class Publisher:
    " Defining class that publishes messages "
    def __init__(self):
        self.subscribers = set()

    def register(self, who):
        " Defining method to add to specific events "
        self.subscribers.add(who)

    def unregister(self, who):
        " Defining method that unregister object to events "
        self.subscribers.discard(who)

    def dispatch(self, message):
        " Defining messge poster to its registered users "
        for subscriber in self.subscribers:
            subscriber.poster(message)


pub = Publisher()

booking_date = datetime.datetime.strptime("10-11-2022", "%m-%d-%Y").date()

first_booking = Bookings(name="Miguel Arrocha", nights=2, beds=1, cellphone="+50762230196", date=booking_date, payment_mehtod="cash")

hotel_manager = Subscriber("Manager")

pub.register(hotel_manager)

print(first_booking)

first_booking.update_status("Approved")

# print(first_booking)

pub.dispatch(f"Booking code {first_booking.booking_code} were approved to {first_booking.date}")
