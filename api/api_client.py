import requests
from config import API_BASE_URL, REQRES_API_KEY


class APIClient:
    def __init__(self, timeout=10):
        self.base_url = API_BASE_URL
        self.timeout = timeout
        self.session = requests.Session()

        if REQRES_API_KEY:
            self.session.headers.update({"x-api-key": REQRES_API_KEY})

    def get(self, endpoint, params=None):
        return self.session.get(
            f"{self.base_url}{endpoint}",
            params=params,
            timeout=self.timeout,
        )

    def post(self, endpoint, json=None):
        return self.session.post(
            f"{self.base_url}{endpoint}",
            json=json,
            timeout=self.timeout,
        )

    def close(self):
        self.session.close()
