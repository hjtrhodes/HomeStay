import datetime
from decimal import Decimal
from types import NoneType
from lib.spaces_repository import SpaceRepository
from lib.space import Space

"""
When want to see all spaces, including mine
Then the all spaces are shown in a list
"""

def test_show_all_space_including_mine(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)
    
    all_spaces = repo.all()
    
    space_1 = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', Decimal('99.99'), datetime.date(2023, 10, 15), datetime.date(2023, 11, 15), 1)
    space_2 = Space(2, 'City Apartment', 'Modern apartment in the heart of the city.', Decimal('150.00'), datetime.date(2023, 10, 10), datetime.date(2023, 11, 10), 2)
    space_3 = Space(3, 'Beach House', 'Beachfront property with stunning views.', Decimal('200.00'), datetime.date(2023, 10, 20), datetime.date(2023, 11, 20), 3)

    result = [
        space_1, space_2, space_3
        ]
    assert all_spaces == result


"""
When I want to view spaces listed 
Then I view all current spaces avaliable that do not belong to me 
"""

def test_get_all_spaces(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)

    spaces = repo.get_all_spaces(3)  
    test_space_1 = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', Decimal('99.99'), datetime.date(2023, 10, 15), datetime.date(2023, 11, 15), 1)
    test_space_2 = Space(2, 'City Apartment', 'Modern apartment in the heart of the city.', Decimal('150.00'), datetime.date(2023, 10, 10), datetime.date(2023, 11, 10), 2)
    result = [
        test_space_1, test_space_2
        ]

    assert spaces == result 

"""
When I want to view my spaces
Then only the spaces I have listed will be seen
"""

def test_get_all_spaces_by_user_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)

    spaces = repo.get_all_spaces_by_id(2)  
    my_space = Space(2, 'City Apartment', 'Modern apartment in the heart of the city.', Decimal('150.00'), datetime.date(2023, 10, 10), datetime.date(2023, 11, 10), 2)
    result = [my_space]

    assert spaces == result 



"""
When I want to view my spaces
And I have no spaces listed
Then no spaces will be shown 
"""

def test_no_spaces_by_user_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)

    spaces = repo.get_all_spaces_by_id(10)  

    assert spaces == "You have no spaces listed yet"




"""
When I want to add a space to my listings
Then the space is added to the database under my id
"""

def test_create_new_space(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)


    new_space = Space(4, 'Nice Cabin', 'A nice cabin in the woods.', Decimal('1500.00'), datetime.date(2023, 12, 1), datetime.date(2023, 12, 20), 1)
    repo.create(new_space)
    all_spaces = repo.all() 

    space_1 = Space(1, 'Cozy Cottage', 'A charming cottage in the countryside.', Decimal('99.99'), datetime.date(2023, 10, 15), datetime.date(2023, 11, 15), 1)
    space_2 = Space(2, 'City Apartment', 'Modern apartment in the heart of the city.', Decimal('150.00'), datetime.date(2023, 10, 10), datetime.date(2023, 11, 10), 2)
    space_3 = Space(3, 'Beach House', 'Beachfront property with stunning views.', Decimal('200.00'), datetime.date(2023, 10, 20), datetime.date(2023, 11, 20), 3)
    space_4 = Space(4, 'Nice Cabin', 'A nice cabin in the woods.', Decimal('1500.00'), datetime.date(2023, 12, 1), datetime.date(2023, 12, 20), 1)
    
    result = [
        space_1, space_2, space_3, space_4
        ]
    
    assert all_spaces == result

"""
When I want to add a space to my listings
And I have a missing field
Then the space is not added to the database and a message returns 
"""


def test_create_new_space_invalid_info(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)

    new_space = Space(None, None, 'A nice cabin in the woods.', Decimal('1500.00'), datetime.date(2023, 12, 1), datetime.date(2023, 12, 20), 1)
    result = repo.create(new_space)

    assert result == "One or more fields are missing!"



"""
When I click a single space from a list 
Then I see the single space from that user
"""

def test_get_single_space_by_id(db_connection):
    db_connection.seed('seeds/makers_bnb_seed.sql')
    repo = SpaceRepository(db_connection)

    spaces = repo.get_single_space_by_id(2)  
    single_space = Space(2, 'City Apartment', 'Modern apartment in the heart of the city.', Decimal('150.00'), datetime.date(2023, 10, 10), datetime.date(2023, 11, 10), 2)
    result = [single_space]

    assert spaces == result 

        