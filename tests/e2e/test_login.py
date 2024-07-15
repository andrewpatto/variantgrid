import os
import re
from playwright.sync_api import Page, expect

# get URL through environment variable
URL = os.environ.get("URL", "http://localhost/")

def test_register_link(page: Page):
    page.goto(URL)
    expect(page).to_have_title(re.compile("MediaCMS"))
    # create a locator
    get_started = page.get_by_role("link", name="REGISTER")
    # Expect an attribute "to be strictly equal" to the value.
    expect(get_started).to_have_attribute("href", "/accounts/signup/")
    # Click the get started link.
    get_started.click()
    # Expects the URL to contain intro.
    expect(page).to_have_url(re.compile(".*signup"))

def test_login_link(page: Page):
    page.goto(URL)
    expect(page).to_have_title(re.compile("MediaCMS"))
    get_started = page.get_by_role("link", name="SIGN IN")
    expect(get_started).to_have_attribute("href", "/accounts/login/")
    get_started.click()
    expect(page).to_have_url(re.compile(".*login"))
