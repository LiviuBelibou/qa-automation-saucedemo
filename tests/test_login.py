from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_successful_login_redirects_to_inventory(driver, credentials):
    wait = WebDriverWait(driver, 10)
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    wait.until(EC.url_contains("inventory"))
    assert "inventory" in driver.current_url


def test_inventory_page_title_is_visible_after_login(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"


def test_login_button_is_visible_and_enabled(driver):
    login_page = LoginPage(driver)
    login_page.open()

    button = login_page.get_login_button()

    assert button.is_displayed()
    assert button.is_enabled()


def test_logout_redirects_to_login(driver, credentials):
    wait = WebDriverWait(driver, 10)
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.logout()

    wait.until(EC.visibility_of_element_located(LoginPage.USERNAME_INPUT))

    assert "saucedemo.com" in driver.current_url