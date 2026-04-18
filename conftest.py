import os
import pytest
from datetime import datetime

import pytest_html
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common.exceptions import WebDriverException, NoSuchWindowException

from api.api_client import APIClient
from config import TEST_EMAIL, TEST_PASSWORD, HEADLESS

load_dotenv()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if HEADLESS:
        options.add_argument("--headless=new")

    prefs = {
        "credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "profile.default_content_setting_values.notifications": 2,
    }

    options.add_experimental_option("prefs", prefs)
    options.add_argument("--disable-save-password-bubble")
    options.add_argument("--disable-notifications")
    options.add_argument("--incognito")
    options.add_argument("--start-maximized")
    options.add_argument("--window-size=1920,1080")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    return TEST_EMAIL, TEST_PASSWORD


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def valid_login_payload():
    return {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka",
    }


@pytest.fixture
def invalid_login_payload():
    return {
        "email": "peter@klaven",
    }


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        driver = item.funcargs.get("driver")
        if driver:
            screenshots_dir = "screenshots"
            os.makedirs(screenshots_dir, exist_ok=True)

            timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
            test_name = item.name.replace("/", "_").replace(" ", "_")
            file_name = f"{test_name}_{timestamp}.png"
            file_path = os.path.join(screenshots_dir, file_name)

            try:
                driver.save_screenshot(file_path)
                print(f"\n[SCREENSHOT] Saved: {file_path}")
            except (NoSuchWindowException, WebDriverException) as e:
                print(f"\n[SCREENSHOT] Could not capture screenshot: {e}")