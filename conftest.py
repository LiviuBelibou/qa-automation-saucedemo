import os
import pytest
from dotenv import load_dotenv
from selenium import webdriver

load_dotenv()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--incognito")

    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    email = os.getenv("TEST_EMAIL", "standard_user")
    password = os.getenv("TEST_PASSWORD", "secret_sauce")
    return email, password