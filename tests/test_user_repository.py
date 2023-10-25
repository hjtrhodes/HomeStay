from lib.user import User
from lib.user_repository import UserRepository


"""
able to get the username from id
"""


def test_get_user_by_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user = repo.get_by_id(1)
    assert user.user_name == "Bob Johnson"
    assert user.user_email == "bjohnson@email.com"
    assert user.user_password == "mysecretpassword"


def test_get_user_by_email(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user = repo.get_by_email("bjohnson@email.com")
    assert user.user_name == "Bob Johnson"
    assert user.user_email == "bjohnson@email.com"
    assert user.user_password == "mysecretpassword"


def test_email_and_password_correct(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user_login = repo.validate_credentials("bjohnson@email.com", "mysecretpassword")
    assert user_login == True 


"""
login does not work if username is incorrect 
and password is correct
"""

def test_email_incorrect_and_password_correct(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user_login = repo.validate_credentials("johnson@email.com", "mysecretpassword")
    assert user_login == False

"""
login does not work if username is correct 
and password is incorrect
"""

def test_email_correct_and_password_incorrect(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = UserRepository(db_connection)

    user_login = repo.validate_credentials("bjohnson@email.com", "mysecret")
    assert user_login == False