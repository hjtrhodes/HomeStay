from flask import Flask
import os
from flask import Flask, request, session, redirect, render_template
from lib.database_connection import get_flask_database_connection
from lib.user_repository import *
from lib.booking_repository import Boooking_Repository
from lib.spaces_repository import SpaceRepository


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
