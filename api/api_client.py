import requests
from config import API_BASE_URL, REQRES_API_KEY


class APIClient:
    def __init__(self):
        self.base_url = API_BASE_URL
        self.api_key = REQRES_API_KEY
        self.headers = {
            "x-api-key": self.api_key
        }

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params
        )

    def post(self, endpoint, json=None):
        return requests.post(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            json=json
        )