from lib.user import User
from lib.user_repository import UserRepository


"""
able to get the username from id
"""

# ('Bob Johnson', 'bjohnson@email.com', 'mysecretpassword');

def test_get_user_by_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user = repo.get_by_id(1)
    assert user.user_name == "Bob Johnson"
    assert user.user_email == "bjohnson@email.com"
    assert user.user_password == "mysecretpassword"


"""
login works when username and password
are correct based on the database information
"""



"""
login does not work if username is incorrect 
and password is correct
"""


"""
login does not work if username is correct 
and password is incorrect
"""