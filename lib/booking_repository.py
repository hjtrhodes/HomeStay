from lib.booking import Booking
from datetime import date
class Boooking_Repository():
    def __init__(self, connection):
        self._connection = connection

    def get_by_booking_id(self, booking_id):
        rows = self._connection.execute('SELECT * from bookings WHERE id = %s', [booking_id])
        for row in rows:
            if booking_id == row['id']:
                return Booking(row['id'], row['booking_date'], row['booking_status'], row['user_id'], row['space_id'])
            else:
                return False

    def _get_all(self):
        rows = self._connection.execute('SELECT * from bookings')
        bookings = []
        for row in rows:
            item = Booking(row['id'], row['booking_date'], row['booking_status'], row['user_id'], row['space_id'])
            bookings.append(item)

        return bookings
    def get_all_by_user_id(self, id):
        return [x for x in self._get_all() if x.user_id == id]
    
    def get_all_by_space_id(self, id):
        return [x for x in self._get_all() if x.space_id == id]
    
    def get_all_confirmed_by_space(self, space_id):
        return [x for x in self.get_all_by_space_id(space_id) if x.booking_status == "Confirmed"]




    def update_status(self, booking_id, confirm_or_deny):
        if confirm_or_deny == True:

            self._connection.execute("UPDATE bookings SET booking_status = 'Confirmed' WHERE id = %s", [booking_id])
        elif confirm_or_deny == False:
            self._connection.execute("UPDATE bookings SET booking_status = 'Denied' WHERE id = %s", [booking_id])

    def create_booking(self, booking):
        rows = self._connection.execute("INSERT INTO bookings (booking_date, booking_status, user_id, space_id) VALUES (%s, 'Pending', %s, %s) RETURNING id", [
                                    booking.booking_date, booking.user_id, booking.space_id]) 
        row = rows[0]
        booking.id = row["id"]
        return booking    



        