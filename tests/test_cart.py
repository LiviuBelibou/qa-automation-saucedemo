import pytest

from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


pytestmark = pytest.mark.selenium


def test_add_item_to_cart(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    first_item_name = inventory_page.get_item_names()[0]
    inventory_page.add_first_item_to_cart()
    inventory_page.open_cart()

    cart_page = CartPage(driver)

    assert cart_page.get_item_names() == [first_item_name]
