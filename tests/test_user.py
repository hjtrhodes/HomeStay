from lib.user import User

def test_constructs():
    user = User(1, 'Test Name', 'test@gmail.com', 'test123!')
    assert user.id == 1
    assert user.user_name == 'Test Name'
    assert user.user_email == 'test@gmail.com'
    assert user.user_password == 'test123!'


def test_compares():
    user1 = User(1, 'Test Name', 'test@gmail.com', 'test123!')
    user2 = User(1, 'Test Name', 'test@gmail.com', 'test123!')
    assert user1 == user2


def test_format():
    user = User(1, 'Test Name', 'test@gmail.com', 'test123!')
    assert str(user) == 'User(1, Test Name, test@gmail.com, test123!)'