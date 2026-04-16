from pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class InventoryPage(BasePage):
    PAGE_TITLE = (By.XPATH, "//span[text()='Products']")
    BURGER_BUTTON = (By.ID, "react-burger-menu-btn")
    LOGOUT_LINK = (By.ID, "logout_sidebar_link")
    SORT_DROPDOWN = (By.CLASS_NAME, "product_sort_container")
    INVENTORY_ITEMS = (By.CLASS_NAME, "inventory_item_name")

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