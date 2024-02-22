from playwright.sync_api import Page, expect
import time

# Tests for your routes go here


"""
We can render the login page
"""


def test_get_login(page, test_web_address):
    page.set_default_timeout(1000)
    # We load a virtual browser and navigate to the /login page
    page.goto(f"http://{test_web_address}/")

    form_tag = page.get_by_placeholder("Email")
    form_tag.fill("playwright@microsoft.com")


"""
Test for login form
"""


def test_login_post_valid_credentials(web_client, db_connection, page):
    db_connection.seed('seeds/homestay_bnb_seed.sql')
    response = web_client.post(
        '/', data={'email': 'bjohnson@email.com', 'password': 'mysecretpassword'})
    page.screenshot(path="screenshot.png", full_page=True)
    assert response.status_code == 302
    assert response.location == '/spaces'


"""
Test that login form redirects to login page if invalid credentials
"""


def test_login_sets_session(web_client, db_connection):
    db_connection.seed('seeds/homestay_bnb_seed.sql')

    response = web_client.post('/', data={
        'email': 'bjohnson@email.com',
        'password': 'mysecretpassword'
    })

    assert response.status_code == 302
    assert response.location == '/spaces'

    with web_client.session_transaction() as session:
        assert session['user_email'] == 'bjohnson@email.com'

def test_login_sets_user_id(web_client, db_connection):
    db_connection.seed('seeds/homestay_bnb_seed.sql')

    response = web_client.post('/', data={
        'email': 'bjohnson@email.com',
        'password': 'mysecretpassword'
    })

    assert response.status_code == 302
    assert response.location == '/spaces'

    with web_client.session_transaction() as session:
        assert session['user_id'] == 1       
        


def test_login_redirects_to_login_if_not_logged_in(page, test_web_address):
    page.goto(f"http://{test_web_address}/spaces")
    assert page.url == f"http://{test_web_address}/"

    """
    test that logout ends the session
    """


def test_logout_ends_session(web_client, db_connection):
    db_connection.seed('seeds/homestay_bnb_seed.sql')
    web_client.post('/', data={
        'email': 'bjohnson@email.com',
        'password': 'mysecretpassword'
    })
    response = web_client.get('/logout')
    assert response.status_code == 302
    assert response.location == '/'


# def test_get_date_to_book(web_client, db_connection, page, test_web_address):
#     db_connection.seed('seeds/makers_bnb_seed.sql')
#     web_client.post('/login', data={
#         'email': 'bjohnson@email.com',
#         'password': 'mysecretpassword'
#     })
#     page.goto(f"http://{test_web_address}/spaces/1")
#     dropdown = page.locator('select#date-dropdown')
#     dropdown.select_option('2023-10-15')
#     page.click("text='Check Availability'")
#     response = web_client.get('/available')
#     assert response.location == '/available'



#def test_view_my_spaces(web_client, db_connection, test_web_address, page):
#    db_connection.seed('seeds/makers_bnb_seed.sql')
#    web_client.post('/login', data={
#        'email': 'bjohnson@email.com',
#        'password': 'mysecretpassword'
#    })
#    
#    page.goto(f"http://{test_web_address}/my-spaces")
#    
#
#    assert page.url == f"http://{test_web_address}/my-spaces"
