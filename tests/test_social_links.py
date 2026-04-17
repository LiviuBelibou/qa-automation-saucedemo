from selenium.webdriver.support.ui import WebDriverWait
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


def test_x_social_link(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    original_window = driver.current_window_handle
    old_handles = driver.window_handles

    inventory_page.click_x_link()
    inventory_page.switch_to_new_tab(old_handles)
    inventory_page.dismiss_cookie_banner_if_present()

    assert "x.com" in driver.current_url or "twitter.com" in driver.current_url

    driver.close()
    driver.switch_to.window(original_window)


def test_facebook_social_link(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    original_window = driver.current_window_handle
    old_handles = driver.window_handles

    inventory_page.click_facebook_link()
    inventory_page.switch_to_new_tab(old_handles)
    inventory_page.dismiss_cookie_banner_if_present()

    WebDriverWait(driver, 10).until(
        lambda d: "facebook.com" in d.current_url
    )

    assert "facebook.com" in driver.current_url

    driver.close()
    driver.switch_to.window(original_window)


def test_linkedin_social_link(driver, credentials):
    username, password = credentials

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    original_window = driver.current_window_handle
    old_handles = driver.window_handles

    inventory_page.click_linkedin_link()
    inventory_page.switch_to_new_tab(old_handles)
    inventory_page.dismiss_cookie_banner_if_present()

    WebDriverWait(driver, 10).until(
        lambda d: "linkedin.com" in d.current_url
    )

    assert "linkedin.com" in driver.current_url

    driver.close()
    driver.switch_to.window(original_window)