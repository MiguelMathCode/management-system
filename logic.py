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
    status: str = None


book1 = Bookings("Miguel", 2, 1, "+ 507 6223 0196", np.datetime64("2022-10-02"), "cash", "Waiting")

print(f"{book1.name} wants to stay {book1.nights} with us. He asked for {book1.beds} beds for his stay, his phone is {book1.cellphone}, he wants to stay on {book1.date}, he is going to pay {book1.payment_mehtod}, status of booking {book1.status}")
