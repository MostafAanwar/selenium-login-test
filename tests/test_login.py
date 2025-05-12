import pytest
from pages.login_page import LoginPage
from utils.driver_setup import get_driver
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

@pytest.fixture
def driver():
    driver = get_driver()
    yield driver
    driver.quit()

def test_valid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("tomsmith", "SuperSecretPassword!")
    assert "You logged into a secure area!" in page.get_flash_message()

def test_invalid_login(driver):
    page = LoginPage(driver)
    page.load()
    page.login("wronguser", "wrongpass")
    assert "Your username is invalid!" in page.get_flash_message()
