from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//span[text()='Products']")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item_name")
    ADD_TO_CART_BUTTONS = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_ICON = (By.CLASS_NAME, "shopping_cart_link")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")

    X_LINK = (By.XPATH, "//a[contains(@href, 'twitter')]")
    FACEBOOK_LINK = (By.XPATH, "//a[contains(@href, 'facebook')]")
    LINKEDIN_LINK = (By.XPATH, "//a[contains(@href, 'linkedin')]")

    def get_page_title(self):
        return self.get_text(self.PAGE_TITLE)

    def open_menu(self):
        self.click(self.BURGER_BUTTON)
        self.wait.until(EC.visibility_of_element_located(self.LOGOUT_LINK))

    def logout(self):
        self.open_menu()
        logout_link = self.wait.until(
            EC.presence_of_element_located(self.LOGOUT_LINK)
        )
        self.driver.execute_script("arguments[0].scrollIntoView(true);", logout_link)
        self.driver.execute_script("arguments[0].click();", logout_link)

    def get_sort_dropdown(self):
        return self.find(self.SORT_DROPDOWN)

    def get_item_names(self):
        return [item.text for item in self.find_all(self.INVENTORY_ITEMS)]

    def add_first_item_to_cart(self):
        buttons = self.find_all(self.ADD_TO_CART_BUTTONS)
        buttons[0].click()

    def open_cart(self):
        self.click(self.CART_ICON)

    def get_cart_badge_text(self):
        return self.get_text(self.CART_BADGE)

    def click_x_link(self):
        self.click(self.X_LINK)

    def click_facebook_link(self):
        self.click(self.FACEBOOK_LINK)

    def click_linkedin_link(self):
        self.click(self.LINKEDIN_LINK)

    def switch_to_new_tab(self, old_handles):
        current_handles = self.driver.window_handles
        self.wait.until(lambda d: len(d.window_handles) > len(current_handles) - 1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def dismiss_cookie_banner_if_present(self):
        try:
            cookie_button = self.wait.until(
                EC.element_to_be_clickable((By.ID, "onetrust-accept-btn-handler"))
            )
            cookie_button.click()
        except:
            pass