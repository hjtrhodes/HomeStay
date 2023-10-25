from lib.user import User

class UserRepository():
    def __init__(self, connection):
        self._connection = connection
    
    def get_by_id(self, id):
        rows = self._connection.execute('SELECT * from users WHERE id = %s', [id])
        row = rows[0]
        return User(row['id'], row['user_name'], row['user_email'], row['user_password'])

    def get_by_email(self, email):
        rows = self._connection.execute('SELECT * from users WHERE user_email = %s', [email])
        for row in rows:
            if email == row['user_email']:
                return User(row['id'], row['user_name'], row['user_email'], row['user_password'])
            else:
                return False

    def validate_credentials(self, email, password):
        user = self.get_by_email(email)
        
        if user:
            if user.user_password == password:
                return True
        return False