from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_inventory_page_shows_products_after_login(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    item_names = inventory_page.get_item_names()

    assert len(item_names) > 0