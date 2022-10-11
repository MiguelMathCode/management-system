# This script contains the logic needed to enter new bookings, reschedule,
# accept, deny, cancel
import datetime
from pydantic import BaseModel


class Bookings(BaseModel):
    name: str = None
    nights: int = None
    beds: int = None
    cellphone: str = None
    date: str = None
    payment_mehtod: str = None
    status: str | None = "Pending for approval"


first_booking = Bookings(name="Miguel Arrocha", nights=2, beds=1, cellphone="+50762230196", date="2022-10-11", payment_mehtod="cash")

print(first_booking)
