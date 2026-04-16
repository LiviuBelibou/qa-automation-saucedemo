from pages.login_page import LoginPage


def test_missing_password_shows_error(driver):
    login_page = LoginPage(driver)
    login_page.enter_invalid_username_and_submit("standard_user")

    assert "Password is required" in login_page.get_error_text()


def test_required_fields_show_error(driver):
    login_page = LoginPage(driver)
    login_page.click_login_without_input()

    assert "Username is required" in login_page.get_error_text()


def test_invalid_credentials_show_error_message(driver):
    login_page = LoginPage(driver)
    login_page.enter_invalid_credentials_and_submit("locked_out_user", "wrong_password")

    assert "Username and password do not match" in login_page.get_error_text()