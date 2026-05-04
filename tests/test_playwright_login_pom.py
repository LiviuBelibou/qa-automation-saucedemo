from playwright_pages.login_page import PlaywrightLoginPage


def test_playwright_login_with_pom(page, credentials):
    username, password = credentials

    login_page = PlaywrightLoginPage(page)
    login_page.login(username, password)

    assert "inventory" in page.url
    assert login_page.get_page_title() == "Products"