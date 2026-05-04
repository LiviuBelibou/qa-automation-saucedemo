from config import BASE_URL


class PlaywrightLoginPage:
    USERNAME_INPUT = "#user-name"
    PASSWORD_INPUT = "#password"
    LOGIN_BUTTON = "#login-button"
    PAGE_TITLE = ".title"

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(BASE_URL)

    def login(self, username, password):
        self.open()
        self.page.fill(self.USERNAME_INPUT, username)
        self.page.fill(self.PASSWORD_INPUT, password)
        self.page.click(self.LOGIN_BUTTON)

    def get_page_title(self):
        return self.page.locator(self.PAGE_TITLE).inner_text()