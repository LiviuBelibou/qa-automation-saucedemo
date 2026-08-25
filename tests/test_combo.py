import pytest

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage


pytestmark = pytest.mark.combined


def test_independent_api_and_ui_smoke_checks(driver, credentials, api_client):
    username, password = credentials

    api_payload = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }

    api_response = api_client.post("/login", json=api_payload)

    assert api_response.status_code == 200
    assert "token" in api_response.json()

    login_page = LoginPage(driver)
    login_page.login(username, password)

    inventory_page = InventoryPage(driver)

    assert inventory_page.get_page_title() == "Products"
