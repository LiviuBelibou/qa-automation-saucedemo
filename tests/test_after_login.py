from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from conftest import driver
from pages.cart_page import CartPage
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_page_header(driver, credentials):

    username, password = credentials
    login_page = LoginPage(driver)
    login_page.login(username, password)

    # Act
    inventory_page = InventoryPage(driver)
    assert inventory_page.get_page_title() == "Products"

def test_page_logo(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_logo_visible()


def test_page_logo_text(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_logo_text() == "Swag Labs"

def test_cart_icon(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_cart_icon_visible()

def test_burger_menu_displayed(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.is_burger_menu_visible()

def test_cart_number_of_items(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(1)

    assert int(inventory_page.get_cart_badge_text()) == 2

def test_cart_shows_two_added_items(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(1)

    cart_page = CartPage(driver)
    cart_page.open_cart()

    assert int(inventory_page.get_cart_badge_text()) == 2
    assert cart_page.get_remove_buttons_count() == 2
    assert cart_page.is_continue_shopping_visible()


def test_remove_items_from_cart(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(1)

    cart_page = CartPage(driver)
    cart_page.open_cart()

    cart_page.remove_first_item()

    assert int(inventory_page.get_cart_badge_text()) == 1

def test_remove_all_items_from_cart(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(1)

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.remove_all_items()

    assert cart_page.get_remove_buttons_count() == 0