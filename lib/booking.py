class Booking:
    def __init__(self, id, booking_start_date, booking_end_date, trip_length, booking_status, user_id, space_id):
        self.id = id
        self.booking_start_date = booking_start_date
        self.booking_end_date = booking_end_date
        self.trip_length = trip_length
        self.booking_status = booking_status
        self.user_id = user_id
        self.space_id = space_id

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Booking({self.id}, {self.booking_start_date}, {self.booking_end_date}, {self.trip_length}, {self.booking_status}, {self.user_id}, {self.space_id})"