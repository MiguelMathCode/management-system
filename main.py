"""This is the main script where test of new implementations have place."""

import logging
from datetime import datetime
from schemas.booking import Booking
from schemas.staff import Employee, Publisher, Subscriber
from helpers.code_generator import code_generator

booking_date = datetime.strptime("12-10-2022", "%d-%m-%Y")

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
info_logger = logging.getLogger(__name__)
i_handler = logging.StreamHandler()
i_handler.setLevel(logging.INFO)
i_format = logging.Formatter(
        "%(asctime)s - %(name)s - %(levelname)s - %(message)s"
        )
i_handler.setFormatter(i_format)
info_logger.addHandler(i_handler)
info_logger.propagate = False


def main():
    """Main function where everything is tested."""
    recep_1 = Employee(
            "Kirito",
            "Kazuto",
            code_generator(6),
            "day",
            Publisher())
    manager_1 = Employee(
            "Asuna",
            "Yuuki",
            code_generator(6),
            "day",
            Subscriber)
    first_booking = Booking(
            name="Miguel Arrocha", nights=2, beds=1, payment_method="cash",
            date=booking_date
            )
    recep_1.publisher.register(manager_1)
    print(first_booking)
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
