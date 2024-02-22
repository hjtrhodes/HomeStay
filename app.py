from flask import Flask
import os
from flask import Flask, request, session, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import *
from lib.booking_repository import BookingRepository
from lib.spaces_repository import SpaceRepository
from lib.booking import Booking

# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# == Your Routes Here ==


@app.route('/', methods=['GET'])
def get_login():
    return render_template('login.html')


@app.route('/login', methods=['POST'])
def submit_login():
    connection = get_flask_database_connection(app)
    repo = UserRepository(connection)

    email = request.form['email']
    password = request.form['password']
    user = repo.get_by_email(email)
    if repo.validate_credentials(email, password) == True:
        session['user_email'] = email
        session['user_id'] = user.id
        return redirect("/spaces")


@app.route('/spaces', methods=['GET'])
def get_spaces():
    connection = get_flask_database_connection(app)
    if 'user_email' not in session:
        return redirect("/")
    else:
        space_repo = SpaceRepository(connection)
        spaces = space_repo.all()

        return render_template('spaces.html', spaces=spaces)

@app.route('/my-spaces', methods=['GET'])
def get_my_spaces():
    connection = get_flask_database_connection(app)
    
    if 'user_email' not in session:
        return redirect("/")
    else:
        space_repo = SpaceRepository(connection)
        booking_repo = BookingRepository(connection)
        my_spaces = space_repo.get_all_spaces_by_id(session['user_id'])
        pending_bookings = booking_repo.get_all_by_space_id_if_pending(my_spaces[0].id)
        confirmed_bookings=booking_repo.get_all_confirmed_by_space(my_spaces[0].id)
        return render_template('my-spaces.html', my_spaces=my_spaces, pending_bookings=pending_bookings, confirmed_bookings=confirmed_bookings)

@app.route('/bookingconfirm', methods=['POST'])
def confirm_deny():
    connection = get_flask_database_connection(app)
        
    if 'user_email' not in session:
        return redirect("/")
    else:
        booking_id = request.form.get('booking_id')
        confirm_or_deny = request.form.get('confirm_or_deny')
        
        if booking_id is None or confirm_or_deny is None:
            return "Missing booking_id or confirm_or_deny parameter", 400
        
        booking_repo = BookingRepository(connection)
        booking_repo.update_status(booking_id, confirm_or_deny)
        return redirect("/my-spaces")

@app.route('/spaces/<int:id>', methods=['GET'])
def show_space_detail(id):
    connection = get_flask_database_connection(app)
    if 'user_email' not in session:
        return redirect("/")
    else:
        session['space_id'] = id
        space_repo = SpaceRepository(connection)
        spaces = space_repo.get_single_space_by_id(id)
        
        return render_template('spaces-detail.html', spaces=spaces)


@app.route('/spaces/create', methods=['POST'])
def get_available_date():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_start_date = request.form['booking_start_date']
    booking_end_date = request.form['booking_end_date']
    booking = Booking(None, booking_start_date, booking_end_date, 'Pending', session['user_id'], session['space_id'])
    booking_repo.create_booking(booking)
    return redirect("/bookings")

@app.route('/bookings', methods=['GET'])
def get_requests():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    bookings = booking_repo.get_all_by_user_id(session["user_id"])
    space_ids = [x.space_id for x in bookings]
    spaces = [booking_repo.get_space_for_booking(space_id) for space_id in space_ids]
    return render_template('bookings.html', bookings=bookings, spaces=spaces)

@app.route('/booking/delete', methods=['POST'])
def delete_booking():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    booking_id = request.form.get('booking_id')
    
    if booking_id is None:
        return "Missing booking_id parameter", 400
    
    booking_repo.delete_booking(booking_id)
    return redirect("/bookings")


@app.route('/logout', methods=['GET'])
def get_logout():
    if 'user_email' not in session:
        return redirect("/")
    else:
        session.clear()
        return redirect("/")


# GET /index
# Returns the homepage
# Try it:
#   ; open http://localhost:5000/index
@app.route('/index', methods=['GET'])
def get_index():
    return render_template('index.html')


# These lines start the server if you run this file directly
# They also start the server configured to use the test database
# if started in test mode.
if __name__ == '__main__':
    app.run(debug=True, port=int(os.environ.get('PORT', 5000)))
