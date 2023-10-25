from playwright.sync_api import Page, expect

# Tests for your routes go here

"""
We can render the index page
"""
def test_get_index(page, test_web_address):
    # We load a virtual browser and navigate to the /index page
    page.goto(f"http://{test_web_address}/index")

    # We look at the <p> tag
    strong_tag = page.locator("p")

    # We assert that it has the text "This is the homepage."
    expect(strong_tag).to_have_text("This is the homepage.")


"""
We can render the login page
"""
def test_get_login(page, test_web_address):
    page.set_default_timeout(1000)
    # We load a virtual browser and navigate to the /login page
    page.goto(f"http://{test_web_address}/login")

    # We look at the <form> tag
    form_tag = page.locator(".email_label")

    # We assert that it has the text "This is the homepage."
    expect(form_tag).to_have_text("Enter email:")


"""
Test for login form
"""
# def test_submit_login_form(page, db_connection, web_client):
#     page.set_default_timeout(1000)
#     db_connection.seed('seeds/makers_bnb_seed.sql')
#     post_response = web_client.post('/login', data={'email':'bjohnson@email.com','password':'mysecretpassword'})
#     page.click("text='Login'")
#     assert post_response.status_code == 200
#     get_response=web_client.get('/spaces')
#     assert get_response.status_code == 200
#     p_tag = page.locator('p')
#     expect(p_tag).to_have_text("Spaces")


# def test_login_post_valid_credentials(web_client, db_connection, page):
#     db_connection.seed('seeds/makers_bnb_seed.sql')
#     response = web_client.post('/login', data={'email':'bjohnson@email.com','password':'mysecretpassword'})
#     page.screenshot(path="screenshot.png", full_page=True)
#     assert response.status_code == 302
#     assert 'Spaces' in response.location

