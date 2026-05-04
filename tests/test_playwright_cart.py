from playwright_pages.login_page import PlaywrightLoginPage
from playwright_pages.inventory_page import PlaywrightInventoryPage


def test_playwright_add_to_cart(page, credentials):
    username, password = credentials

    login_page = PlaywrightLoginPage(page)
    login_page.login(username, password)

    inventory_page = PlaywrightInventoryPage(page)

    inventory_page.add_item_by_index(0)
    inventory_page.add_item_by_index(1)

    assert inventory_page.get_cart_badge_text() == "2"