from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def get_by_id(self, id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row['id'], row['user_name'], row['user_email'], row['user_password'])
        