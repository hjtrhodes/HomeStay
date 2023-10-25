from lib.booking import Booking

def test_constructs():
    booking = Booking(1, '2023-10-18','Confirmed', 2, 1)
    assert booking.id == 1
    assert booking.booking_date == '2023-10-18'
    assert booking.booking_status == 'Confirmed'
    assert booking.user_id == 2
    assert booking.space_id == 1


def test_compares():
    user1 = Booking(1, '2023-10-18','Confirmed', 2, 1)
    user2 = Booking(1, '2023-10-18','Confirmed', 2, 1)
    assert user1 == user2


def test_format():
    booking = Booking(1, '2023-10-18','Confirmed', 2, 1)
    assert str(booking) == 'Booking(1, 2023-10-18, Confirmed, 2, 1)'