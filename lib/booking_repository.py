from lib.booking import Booking
from datetime import date
from lib.space import Space
class BookingRepository():
    def __init__(self, connection):
        self._connection = connection

    def get_by_booking_id(self, booking_id):
        rows = self._connection.execute('SELECT * from bookings WHERE id = %s', [booking_id])
        for row in rows:
            if booking_id == row['id']:
                return Booking(row['id'], row['booking_start_date'], row['booking_end_date'], row['trip_length'], row['booking_status'], row['user_id'], row['space_id'])
            else:
                return False

    def _get_all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_start_date'], row['booking_end_date'], row['trip_length'], row['booking_status'], row['user_id'], row['space_id'])
            bookings.append(item)

        return bookings
    def get_all_by_user_id(self, id):
        return [x for x in self._get_all() if x.user_id == id]
    
    def get_all_by_space_id(self, id):
        return [x for x in self._get_all() if x.space_id == id]
    
    def get_all_by_space_id_if_pending(self, id):
        return [x for x in self._get_all() if x.space_id == id and x.booking_status == "Pending"]
    
    def get_all_confirmed_by_space(self, space_id):
        return [x for x in self.get_all_by_space_id(space_id) if x.booking_status == "Confirmed"]

    def get_all_confirmed_dates(self, space_id):
        return [x.booking_date for x in self.get_all_by_space_id(space_id) if x.booking_status == "Confirmed"]

    def update_status(self, booking_id, confirm_or_deny):
        if confirm_or_deny == "True":

            self._connection.execute("UPDATE bookings SET booking_status = 'Confirmed' WHERE id = %s", [booking_id])
        
        elif confirm_or_deny == "False":
            self._connection.execute("UPDATE bookings SET booking_status = 'Denied' WHERE id = %s", [booking_id])

    def create_booking(self, booking):
        trip_length = (booking.booking_end_date - booking.booking_start_date).days
        rows = self._connection.execute("INSERT INTO bookings (booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id) VALUES (%s, %s, %s, 'Pending', %s, %s) RETURNING id", [
                                    booking.booking_start_date, booking.booking_end_date, trip_length, booking.user_id, booking.space_id]) 
        row = rows[0]
        booking.id = row["id"]
        booking.trip_length = trip_length
        return booking

    def get_space_for_booking(self, space_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [space_id])
        for row in rows:
            if space_id == row['id']:
                return Space(row['id'], row['space_name'], row['space_description'], row['space_image_url'], row['price_per_night'], row['user_id'])
        return None
    
    
