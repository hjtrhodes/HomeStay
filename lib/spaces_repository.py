from lib.space import Space

class SpaceRepository:
    def __init__(self, connection):
        self._connection = connection

    def get_all_spaces(self, given_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id != %s', [given_id])
        spaces = []

        for row in rows:
            space = Space(row["id"],row["space_name"],row["space_description"],row["price_per_night"],row["available_from"],row["available_to"],row["user_id"])
            spaces.append(space)
        return spaces
        
    


    def create(self, new_space):
        if (
            new_space.space_name is None or
            new_space.space_description is None or
            new_space.price_per_night is None or
            new_space.available_from is None or
            new_space.available_to is None or
            new_space.user_id is None
        ):
            return "One or more fields are missing!"


        rows = self._connection.execute(
            'INSERT INTO spaces (space_name, space_description, price_per_night, available_from, available_to, user_id) VALUES (%s, %s, %s, %s, %s, %s) RETURNING id',
            [new_space.space_name, new_space.space_description, new_space.price_per_night, new_space.available_from, new_space.available_to, new_space.user_id]
        )

        row = rows[0]
        new_space.id = row["id"]
        return new_space


    def all(self):
        rows = self._connection.execute('SELECT * FROM spaces')
        spaces = []

        for row in rows:
            space = Space(row["id"],row["space_name"],row["space_description"],row["price_per_night"],row["available_from"],row["available_to"],row["user_id"])
            spaces.append(space)
        return spaces


    def get_all_spaces_by_id(self, given_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [given_id])
        spaces = []

        for row in rows:
            space = Space(row["id"],row["space_name"],row["space_description"],row["price_per_night"],row["available_from"],row["available_to"],row["user_id"])
            spaces.append(space)
        
        if spaces != []:
            return(spaces)
        else:
            return "You have no spaces listed yet"

    def get_single_space_by_id(self, given_id):
        rows = self._connection.execute('SELECT * FROM spaces WHERE id = %s', [given_id])
        spaces = []

        for row in rows:
            space = Space(row["id"],row["space_name"],row["space_description"],row["price_per_night"],row["available_from"],row["available_to"],row["user_id"])
            spaces.append(space)
        
        if spaces != []:
            return(spaces)
        else:
            return "Space not found"