from flask import Flask
import os
from flask import Flask, request, session, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import *
from lib.booking_repository import BookingRepository
from lib.spaces_repository import SpaceRepository
from lib.get_dates import *

# Create a new Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = 1800  # 30 minutes

# == Your Routes Here ==


@app.route('/login', methods=['GET'])
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
        return redirect("/login")
    else:
        space_repo = SpaceRepository(connection)
        spaces = space_repo.all()

        return render_template('spaces.html', spaces=spaces)

@app.route('/my-spaces', methods=['GET'])
def get_my_spaces():
    connection = get_flask_database_connection(app)
    
    if 'user_email' not in session:
        return redirect("/login")
    else:
        space_repo = SpaceRepository(connection)
        my_spaces = space_repo.get_all_spaces_by_id(session['user_id'])
        return render_template('my-spaces.html', my_spaces=my_spaces)

@app.route('/spaces/<int:id>', methods=['GET'])
def show_space_detail(id):
    connection = get_flask_database_connection(app)
    if 'user_email' not in session:
        return redirect("/login")
    else:
        session['space_id'] = id
        space_repo = SpaceRepository(connection)
        spaces = space_repo.get_single_space_by_id(id)
        booking_repo = BookingRepository(connection)
        l_space = space_repo.get_single_space_by_id(id)
        a_space = l_space[0]
        all_dates = get_dif_between_dates(a_space.available_from, a_space.available_to)
        booked_dates = booking_repo.get_all_confirmed_dates(id)
        dates = [x for x in all_dates if x not in  booked_dates]
        
        return render_template('spaces-detail.html', spaces=spaces, dates=dates)


@app.route('/spaces/create', methods=['POST'])
def get_available_date():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    date = request.form['date']
    booking = Booking(None, date, 'Pending', session['user_id'], session['space_id'])
    booking_repo.create_booking(booking)
    return redirect("/spaces")

@app.route('/bookings', methods=['GET'])
def get_requests():
    connection = get_flask_database_connection(app)
    booking_repo = BookingRepository(connection)
    bookings = booking_repo.get_all_by_user_id(session["user_id"])
    space_ids = [x.space_id for x in bookings]
    spaces = [booking_repo.get_space_by_booking_id(space_id) for space_id in space_ids]


    return render_template('bookings.html', bookings=bookings, spaces=spaces)






    


@app.route('/logout', methods=['GET'])
def get_logout():
    if 'user_email' not in session:
        return redirect("/login")
    else:
        session.clear()
        return redirect("/login")


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
