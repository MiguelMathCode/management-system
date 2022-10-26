" This file defines the booking schema as a class and its attributes "
import datetime
from helpers.code_generator import code_generator
from dataclasses import dataclass


@dataclass
class Booking():
    " Defining the class Booking and its attributes "
    name: str = None
    nights: int = None
    beds: int = None
    cellphone: str = None
    date: datetime.date = None
    payment_method: str = None
    status: str = "Pending for approval"
    booking_code: str = code_generator(6)

    def update_status(self, new_status: str):
        " Method to change the status of Booking "
        self.status = new_status

@dataclass
class Booking_:
    " Defining the class Booking and its attributes "
    name: str = None
    nights: int = None
    beds: int = None
    cellphone: str = None
    date: datetime.date = None
    payment_method: str = None
    status: str = "Pending for approval"
    booking_code: str = code_generator(6)
