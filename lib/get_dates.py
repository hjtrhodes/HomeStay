from lib.booking_repository import Boooking_Repository
from lib.spaces_repository import SpaceRepository
from datetime import timedelta
from lib.space import Space
from lib.booking import Booking
import datetime

s_date = datetime.date(2023, 10, 10)
e_date = datetime.date(2023, 10, 15)

def get_dif_between_dates(start_date, end_date):
    
    date_list = []

    while start_date <= end_date:
    
        date_list.append(start_date)
        start_date += timedelta(days=1)
    return date_list


