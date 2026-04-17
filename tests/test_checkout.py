from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_checkout_flow(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)
    inventory_page.add_first_item_to_cart()

    cart_page = CartPage(driver)
    cart_page.open_cart()
    cart_page.click_checkout()

    checkout_page = CheckoutPage(driver)
    checkout_page.fill_information("James", "Bond", "12345")
    checkout_page.continue_checkout()
    checkout_page.finish_checkout()

    assert checkout_page.get_success_message() == "Thank you for your order!"