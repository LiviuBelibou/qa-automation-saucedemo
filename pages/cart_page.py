from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")

    def open_cart(self):
        self.click(self.CART_ICON)
        self.wait_for_url("cart")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-one")