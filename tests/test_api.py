import pytest
from dotenv import load_dotenv
from api.api_client import APIClient
from jsonschema import validate
from schemas.users_schema import USERS_SCHEMA


load_dotenv()


def test_get_users():
    client = APIClient()
    response = client.get("/users", params={"page": 2})

    assert response.status_code == 200

    data = response.json()
    assert len(data["data"]) > 0


def test_login_success(api_client, valid_login_payload):

    response = api_client.post("/login", json=valid_login_payload)

    assert response.status_code == 200

    assert "token" in response.json()

def test_login_missing_password(api_client, invalid_login_payload):

    response = api_client.post("/login", json=invalid_login_payload)

    assert response.status_code == 400

    assert "error" in response.json()


@pytest.mark.parametrize(

    "payload, expected_status, expected_key, expected_value",

    [

        (

            {"email": "eve.holt@reqres.in", "password": "cityslicka"},

            200,

            "token",

            None,

        ),

        (

            {"email": "peter@klaven"},

            400,

            "error",

            "Missing password",

        ),

    ],

)

def test_login_api_variations(api_client, payload, expected_status, expected_key, expected_value):

    response = api_client.post("/login", json=payload)

    assert response.status_code == expected_status

    data = response.json()

    assert expected_key in data

    if expected_value is not None:

        assert expected_value in data[expected_key]


def test_get_users_schema(api_client):
    response = api_client.get("/users", params={"page": 2})

    assert response.status_code == 200

    data = response.json()
    validate(instance=data, schema=USERS_SCHEMA)


@pytest.mark.parametrize(

    "payload_fixture, expected_status",

    [

        ("valid_login_payload", 200),

        ("invalid_login_payload", 400),

    ],

)

def test_login_parametrized(api_client, request, payload_fixture, expected_status):

    payload = request.getfixturevalue(payload_fixture)

    response = api_client.post("/login", json=payload)

    assert response.status_code == expected_status