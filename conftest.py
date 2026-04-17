import os
import base64
import pytest
import pytest_html
from datetime import datetime
from dotenv import load_dotenv
from selenium import webdriver
from selenium.common import NoSuchWindowException, WebDriverException

load_dotenv()


@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()

    if os.getenv("HEADLESS") == "true":
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

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()


@pytest.fixture
def credentials():
    email = os.getenv("TEST_EMAIL", "standard_user")
    password = os.getenv("TEST_PASSWORD", "secret_sauce")
    return email, password


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