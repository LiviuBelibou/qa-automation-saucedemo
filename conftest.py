import pytest
from selenium import webdriver
import os
from dotenv import load_dotenv
load_dotenv()

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def credentials():
    email = os.getenv("TEST_EMAIL")
    password = os.getenv("TEST_PASSWORD")

    assert email is not None, "TEST_EMAIL is not set"
    assert password is not None, "TEST_PASSWORD is not set"

    return email, password