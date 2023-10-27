from lib.get_dates import *
from lib.spaces_repository import *

def test_get_date_ranges():
    s_date = datetime.date(2023, 10, 10)
    e_date = datetime.date(2023, 10, 15)
    res = get_dif_between_dates(s_date, e_date)
    assert res == [
        datetime.date(2023, 10, 10),
        datetime.date(2023, 10, 11),
        datetime.date(2023, 10, 12),
        datetime.date(2023, 10, 13), 
        datetime.date(2023, 10, 14), 
        datetime.date(2023, 10, 15)
        ]
def test_get_date_ranges_2(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    spacelist = space_repo.get_single_space_by_id(1)
    space = spacelist[0]
    s_date = space.available_from
    e_date = space.available_to
    res = get_dif_between_dates(s_date, e_date)
    assert res == [
        datetime.date(2023, 10, 15),
        datetime.date(2023, 10, 16),
        datetime.date(2023, 10, 17),
        datetime.date(2023, 10, 18), 
        datetime.date(2023, 10, 19), 
        datetime.date(2023, 10, 20),
        datetime.date(2023, 10, 21),
        datetime.date(2023, 10, 22),
        datetime.date(2023, 10, 23),
        datetime.date(2023, 10, 24), 
        datetime.date(2023, 10, 25), 
        datetime.date(2023, 10, 26),
        datetime.date(2023, 10, 27),
        datetime.date(2023, 10, 28),
        datetime.date(2023, 10, 29),
        datetime.date(2023, 10, 30), 
        datetime.date(2023, 10, 31), 
        datetime.date(2023, 11, 1),
        datetime.date(2023, 11, 2),
        datetime.date(2023, 11, 3),
        datetime.date(2023, 11, 4),
        datetime.date(2023, 11, 5), 
        datetime.date(2023, 11, 6), 
        datetime.date(2023, 11, 7),
        datetime.date(2023, 11, 8),
        datetime.date(2023, 11, 9),
        datetime.date(2023, 11, 10),
        datetime.date(2023, 11, 11),
        datetime.date(2023, 11, 12), 
        datetime.date(2023, 11, 13), 
        datetime.date(2023, 11, 14),
        datetime.date(2023, 11, 15),
        ]
def test_get_date_ranges_from_db(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    space_repo = SpaceRepository(db_connection)
    spacelist = space_repo.get_single_space_by_id(1)
    space = spacelist[0]
    s_date = space.available_from
    e_date = space.available_to
    dates = get_dif_between_dates(s_date, e_date)
    Booking_repo = BookingRepository(db_connection)
    confirmed_dates =  Booking_repo.get_all_confirmed_dates(1)
    res = [x for x in dates if x not in  confirmed_dates]
    assert res == [
        datetime.date(2023, 10, 15),
        datetime.date(2023, 10, 16),
        datetime.date(2023, 10, 17), 
        datetime.date(2023, 10, 19), 
        datetime.date(2023, 10, 20),
        datetime.date(2023, 10, 21),
        datetime.date(2023, 10, 22),
        datetime.date(2023, 10, 23),
        datetime.date(2023, 10, 24), 
        datetime.date(2023, 10, 25), 
        datetime.date(2023, 10, 26),
        datetime.date(2023, 10, 27),
        datetime.date(2023, 10, 28),
        datetime.date(2023, 10, 29),
        datetime.date(2023, 10, 30), 
        datetime.date(2023, 10, 31), 
        datetime.date(2023, 11, 1),
        datetime.date(2023, 11, 2),
        datetime.date(2023, 11, 3),
        datetime.date(2023, 11, 4),
        datetime.date(2023, 11, 5), 
        datetime.date(2023, 11, 6), 
        datetime.date(2023, 11, 7),
        datetime.date(2023, 11, 8),
        datetime.date(2023, 11, 9),
        datetime.date(2023, 11, 10),
        datetime.date(2023, 11, 11),
        datetime.date(2023, 11, 12), 
        datetime.date(2023, 11, 13), 
        datetime.date(2023, 11, 14),
        datetime.date(2023, 11, 15),
        ]     
        
        

