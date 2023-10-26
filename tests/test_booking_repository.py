from lib.booking_repository import *
from datetime import date

def test_get_by_booking_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_booking = test_repo.get_by_booking_id(1)
    assert test_booking.id == 1
    assert test_booking.user_id == 1
    assert test_booking.space_id == 1
    assert test_booking.booking_date == date(2023, 10, 18)
    test_date = date(2023, 10, 18)
    assert test_booking == Booking(1, test_date, "Confirmed", 1, 1) 

def test_if_booking_false(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_booking = test_repo.get_by_booking_id(10)
    assert test_booking == None

def test_get_all_by_user(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    res = test_repo.get_all_by_user_id(2)
   
    assert res == [
        Booking(2, date(2023, 10, 12), 'Denied', 2, 2),
        Booking(4, date(2023, 10, 25), 'Pending', 2, 3),
    ]

def test_get_all_by_space(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    res = test_repo.get_all_by_space_id(2)
    assert res == [
        Booking(2, date(2023, 10, 12), 'Denied', 2, 2),
        Booking(5, date(2023, 10, 25), 'Pending', 3, 2),
    ]
def test_update_booking_status(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_booking = test_repo.get_by_booking_id(3)
    assert test_booking.booking_status == "Pending"
    test_repo.update_status(3, True)
    assert test_repo.get_by_booking_id(3).booking_status == "Confirmed"

def test_update_booking_status_deny(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_booking = test_repo.get_by_booking_id(3)
    assert test_booking.booking_status == "Pending"
    test_repo.update_status(3, False)
    assert test_repo.get_by_booking_id(3).booking_status == "Denied"    

def test_create_booking_request(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_booking = Booking(None, date(2023, 10, 20), "Pending", 2, 3)
    test_repo.create_booking(test_booking)
    result = test_repo.get_by_booking_id(6)
    assert result == Booking(6, date(2023, 10, 20), "Pending", 2, 3)

def test_get_all_confirmed_dates(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    connection = db_connection
    test_repo = Boooking_Repository(connection)
    test_repo.update_status(3, True)
    test_repo.update_status(4, True)
    res = test_repo.get_all_confirmed_by_space(3)
    assert res == [
        Booking(3, date(2023, 10, 25), 'Confirmed', 3, 3),
        Booking(4, date(2023, 10, 25), 'Confirmed', 2, 3),
    ]



    





