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

