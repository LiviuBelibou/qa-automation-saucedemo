from pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CHECKOUT_BUTTON = (By.ID, "checkout")
    REMOVE_BUTTONS = (By.XPATH, "//button[contains(text(),'Remove')]")
    CONTINUE_SHOPPING_BUTTON = (By.ID, "continue-shopping")

    def open_cart(self):
        self.click(self.CART_ICON)
        self.wait_for_url("cart")

    def click_checkout(self):
        self.click(self.CHECKOUT_BUTTON)
        self.wait_for_url("checkout-step-one")

    def get_remove_buttons_count(self):
        return len(self.driver.find_elements(*self.REMOVE_BUTTONS))

    def is_continue_shopping_visible(self):
        return self.find(self.CONTINUE_SHOPPING_BUTTON).is_displayed()
    
    def remove_first_item(self):
        buttons = self.find_all(self.REMOVE_BUTTONS)
        buttons[0].click()

    def remove_all_items(self):
         while self.get_remove_buttons_count() > 0:
            self.driver.find_elements(*self.REMOVE_BUTTONS)[0].click()