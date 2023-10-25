class User:
    def __init__(self, id, user_name, user_email, user_password):
        self.id = id
        self.user_name = user_name
        self.user_email = user_email
        self.user_password = user_password

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"User({self.id}, {self.user_name}, {self.user_email}, {self.user_password})"