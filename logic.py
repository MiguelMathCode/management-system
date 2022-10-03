# This script contains the logic needed to enter new bookings, reschedule,
# accept, deny, cancel
import numpy as np
from dataclasses import dataclass


@dataclass
class Bookings:
    name: str = None
    nights: int = None
    beds: int = None
    cellphone: str = None
    date: np.datetime64 = None
    payment_mehtod: str = None
    status: str = "Pending for approval"


name = input("Enter name of booking: ")
nights = int(input("Enter amount of nights you want to stay: "))
beds = int(input("Enter amount of beds you want to your stay: "))
cellphone = input("Please enter your phone number: ")
date = np.datetime64(input("Enter date of your stay: "))
payment_mehtod = input("Enter your payment method: ")

book = Bookings(name, nights, beds, cellphone, date, payment_mehtod)


print(book.name, book.nights, book.cellphone, book.date, book.payment_mehtod, book.status)

book.status = "Accepted"

print(book.status)
