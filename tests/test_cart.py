from pages.login_page import LoginPage
from selenium.webdriver.common.by import By


def test_add_item_to_cart(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    # click first "Add to cart"
    add_button = driver.find_element(By.XPATH, "(//button[contains(text(),'Add to cart')])[1]")
    add_button.click()

    # open cart
    cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()

    # verify item is in cart
    item = driver.find_element(By.CLASS_NAME, "inventory_item_name")

    assert item.is_displayed()