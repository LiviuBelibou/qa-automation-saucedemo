from playwright_pages.login_page import PlaywrightLoginPage

def test_block_images_during_login(page, credentials):

    username, password = credentials

    page.route("**/*.{png,jpg,jpeg}", lambda route: route.abort())

    login_page = PlaywrightLoginPage(page)

    login_page.login(username, password)

    assert "inventory" in page.url


def test_login_navigation_response_is_successful(page, credentials):

    username, password = credentials

    login_page = PlaywrightLoginPage(page)

    with page.expect_navigation() as navigation_info:

        login_page.login(username, password)

    response = navigation_info.value

    assert response is not None

    assert response.status == 200

    assert "inventory" in page.url