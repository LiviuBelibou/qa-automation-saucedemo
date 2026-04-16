from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from config import LOGIN_URL


def open_login_page(driver):
    wait = WebDriverWait(driver, 10)
    driver.get(LOGIN_URL)
    wait.until(EC.visibility_of_element_located((By.ID, "email")))


def login(driver, email, password):
    wait = WebDriverWait(driver, 10)

    open_login_page(driver)

    username = wait.until(EC.visibility_of_element_located((By.ID, "email")))
    password_field = wait.until(EC.visibility_of_element_located((By.ID, "password")))
    login_button = wait.until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )

    username.clear()
    username.send_keys(email)

    password_field.clear()
    password_field.send_keys(password)

    login_button.click()


def open_reset_password_page(driver):
    wait = WebDriverWait(driver, 10)

    open_login_page(driver)

    forgot_password_link = wait.until(
        EC.element_to_be_clickable((By.LINK_TEXT, "Forgot password?"))
    )
    forgot_password_link.click()

    wait.until(EC.url_contains("reset"))


def get_error_message(wait):
    return wait.until(
        EC.visibility_of_element_located((By.XPATH, "//p"))
    )

def get_wait(driver, timeout=10):
    return WebDriverWait(driver, timeout)