from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from config import LOGIN_URL


class LoginPage(BasePage):
    USERNAME_INPUT = (By.ID, "user-name")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.XPATH, "//h3[@data-test='error']")

    def open(self):
        super().open(LOGIN_URL)

    def login(self, username, password):
        self.open()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def click_login_without_input(self):
        self.open()
        self.click(self.LOGIN_BUTTON)

    def enter_invalid_username_and_submit(self, username):
        self.open()
        self.type(self.USERNAME_INPUT, username)
        self.click(self.LOGIN_BUTTON)

    def enter_invalid_credentials_and_submit(self, username, password):
        self.open()
        self.type(self.USERNAME_INPUT, username)
        self.type(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)

    def get_login_button(self):
        return self.find(self.LOGIN_BUTTON)

    def get_error_text(self):
        return self.get_text(self.ERROR_MESSAGE)