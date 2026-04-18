import os
from dotenv import load_dotenv

load_dotenv()

BASE_URL = os.getenv("BASE_URL", "https://www.saucedemo.com")
LOGIN_URL = BASE_URL

API_BASE_URL = os.getenv("API_BASE_URL", "https://reqres.in/api")
TEST_EMAIL = os.getenv("TEST_EMAIL", "standard_user")
TEST_PASSWORD = os.getenv("TEST_PASSWORD", "secret_sauce")
REQRES_API_KEY = os.getenv("REQRES_API_KEY")
HEADLESS = os.getenv("HEADLESS", "false").lower() == "true"