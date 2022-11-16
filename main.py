"""This is the main script where test of new implementations have place."""

import logging
import logging.config
from datetime import datetime
from schemas.booking import Booking
from schemas.staff import Employee, Publisher, Subscriber
from helpers.code_generator import code_generator

booking_date = datetime.strptime("12-10-2022", "%d-%m-%Y")

logging.config.fileConfig("log.conf")
info_logger = logging.getLogger("console")


def main():
    """Main function where everything is tested."""
    recep_1 = Employee(
            name="Kirito",
            surname="Kazuto",
            employee_id=code_generator(6),
            shift="day",
            publisher=Publisher())
    manager_1 = Employee(
            name="Asuna",
            surname="Yuuki",
            employee_id=code_generator(6),
            shift="day",
            subscriber=Subscriber)
    first_booking = Booking(
            name="Miguel Arrocha", nights=2, beds=1, payment_method="cash",
            date=booking_date
            )
    recep_1.publisher.register(manager_1)
    first_booking.update_status(new_status="approved")
    recep_1.publisher.dispatch(
            f"Booking {first_booking.booking_code} has just been {first_booking.status}"
            )


if __name__ == "__main__":
    try:
        info_logger.info('I started')
        main()
    except Exception:
        info_logger.exception('Oh no!')
    info_logger.info('Done!')
