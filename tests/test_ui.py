from selenium.webdriver.support.ui import Select
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_sort_products_name_a_to_z(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    dropdown = Select(inventory_page.get_sort_dropdown())
    dropdown.select_by_visible_text("Name (A to Z)")

    item_names = inventory_page.get_item_names()
    assert item_names == sorted(item_names)