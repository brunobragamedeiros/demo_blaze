import random
import string
import pytest
from pages.base_page import BasePage
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="function")
def context(request):
    url = 'https://demoblaze.com/index.html'

    with sync_playwright() as pw:
        browser = pw.chromium.launch(headless=True)
        ctx = browser.new_context(base_url=url, record_video_dir="videos")
        yield ctx

        ctx.close()
        browser.close()

@pytest.fixture(scope="function")
def page(context):
    page = context.new_page()
    page.set_default_timeout(30000)
    page.set_default_navigation_timeout(50000)
    yield page
    page.close()

@pytest.fixture
def login_random(page, random_username, random_password): 
    base_page = BasePage(page)
    page.goto('/')
    base_page.login_as_new_user(random_username, random_password)

def _random_string(length=10, chars=string.ascii_letters + string.digits):
    return "".join(random.choice(chars) for _ in range(length))

@pytest.fixture
def random_username():
    username = _random_string(8).lower()
    return username

@pytest.fixture
def random_password():
    chars = string.ascii_lowercase + string.ascii_uppercase + string.digits + "!@#$%^&*()?"
    return _random_string(12, chars)