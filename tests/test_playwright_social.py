import pytest

from playwright_pages.inventory_page import PlaywrightInventoryPage
from playwright_pages.login_page import PlaywrightLoginPage


pytestmark = [pytest.mark.playwright, pytest.mark.external]


def test_playwright_social_link(page, credentials):
    username, password = credentials

    login_page = PlaywrightLoginPage(page)
    login_page.login(username, password)

    inventory_page = PlaywrightInventoryPage(page)
    new_page = inventory_page.click_twitter()
    new_page.wait_for_load_state()

    assert "twitter.com" in new_page.url or "x.com" in new_page.url
