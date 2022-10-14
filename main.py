from datetime import datetime
from schemas.booking import Booking
import logging

booking_date = datetime.strptime("12-10-2022", "%d-%m-%Y")

logging.basicConfig()
logging.root.setLevel(logging.NOTSET)
logging.basicConfig(level=logging.NOTSET)
info_logger = logging.getLogger(__name__)
i_handler = logging.StreamHandler()
i_handler.setLevel(logging.INFO)
i_format = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
i_handler.setFormatter(i_format)
info_logger.addHandler(i_handler)
info_logger.propagate = False


def main():
    first_booking = Booking(name="Miguel Arrocha", nights=2, beds=1, payment_method="cash", date=booking_date)
    print(first_booking)
    first_booking.update_status(new_status="approved")
    print(first_booking)


if __name__ == "__main__":
    try:
        info_logger.info('I started')
        main()
    except Exception as e:
        info_logger.exception('Oh no!')
    info_logger.info('Done!')
