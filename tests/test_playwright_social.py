from playwright_pages.login_page import PlaywrightLoginPage


def test_playwright_social_link(page, credentials):
    username, password = credentials

    login_page = PlaywrightLoginPage(page)
    login_page.login(username, password)

    # wait for new tab
    with page.context.expect_page() as new_page_info:
        page.click(".social_twitter a")

    new_page = new_page_info.value

    new_page.wait_for_load_state()

    assert "twitter.com" in new_page.url or "x.com" in new_page.url