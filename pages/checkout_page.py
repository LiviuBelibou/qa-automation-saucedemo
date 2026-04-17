from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class CheckoutPage(BasePage):
    FIRST_NAME = (By.ID, "first-name")
    LAST_NAME = (By.ID, "last-name")
    POSTAL_CODE = (By.ID, "postal-code")
    CONTINUE_BUTTON = (By.ID, "continue")
    FINISH_BUTTON = (By.ID, "finish")
    SUCCESS_MESSAGE = (By.CLASS_NAME, "complete-header")

    def wait_until_loaded(self):
        self.wait_for_url("checkout-step-one")
        self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))

    def fill_information(self, first, last, zip_code):
        self.wait_until_loaded()

        first_name = self.wait.until(EC.element_to_be_clickable(self.FIRST_NAME))
        first_name.click()
        first_name.clear()
        first_name.send_keys(first)

        last_name = self.wait.until(EC.element_to_be_clickable(self.LAST_NAME))
        last_name.click()
        last_name.clear()
        last_name.send_keys(last)

        postal_code = self.wait.until(EC.element_to_be_clickable(self.POSTAL_CODE))
        postal_code.click()
        postal_code.clear()
        postal_code.send_keys(zip_code)

    def continue_checkout(self):
        self.click(self.CONTINUE_BUTTON)
        self.wait_for_url("checkout-step-two")

    def finish_checkout(self):
        self.click(self.FINISH_BUTTON)
        self.wait_for_url("checkout-complete")

    def get_success_message(self):
        return self.get_text(self.SUCCESS_MESSAGE)