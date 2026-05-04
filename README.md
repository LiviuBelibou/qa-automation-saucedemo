🚀 QA Automation Framework (Selenium + Playwright + API)

📌 Overview

This project is a hybrid QA automation framework combining UI and API testing.

I built this project to transition from manual QA into automation and to demonstrate real-world testing scenarios, including UI, API, and CI integration.

It includes:

* UI automation using Selenium (Page Object Model)
* UI automation using Playwright (modern, auto-waiting based approach)
* API testing using requests
* CI/CD integration using GitHub Actions
  
The framework demonstrates end-to-end testing, clean architecture, and practical automation skills.

🛠️ Tech Stack

* Python
* Selenium WebDriver
* Playwright
* pytest
* requests
* jsonschema
* GitHub Actions

🚀 Features

* Page Object Model (POM) for scalable UI automation (Selenium & Playwright)
* API client abstraction for reusable request handling
* Parametrized API tests
* JSON schema validation for API responses
* Multi-tab handling (Selenium & Playwright)
* Network interception (Playwright)
* Headless execution support
* Automatic screenshots on test failure
* HTML test reporting
* Environment-based configuration using .env
* Continuous Integration with GitHub Actions

📊 Test Coverage

* Covers login, cart, checkout, and API validation flows
* Includes UI, API, and hybrid test scenarios
* Runs automatically in CI pipeline

📂 Project Structure

qa-automation-saucedemo/
├── api/                # API client and API tests
├── pages/              # Selenium Page Objects
├── playwright_pages/   # Playwright Page Objects
├── schemas/            # JSON schema validation
├── tests/              # UI, API, and hybrid tests
├── screenshots/        # Failure screenshots
├── reports/            # Test reports
├── conftest.py         # Fixtures and hooks
├── config.py           # Configuration
└── requirements.txt

⚙️ Setup & Installation

git clone https://github.com/LiviuBelibou/qa-automation-saucedemo.git
cd qa-automation-saucedemo

python3 -m venv .venv
source .venv/bin/activate

pip install -r requirements.txt
python -m playwright install

🔐 Environment Variables

Create a .env file in the project root:

BASE_URL=https://www.saucedemo.com
API_BASE_URL=https://reqres.in/api

TEST_EMAIL=standard_user
TEST_PASSWORD=secret_sauce

REQRES_API_KEY=your_api_key_here

HEADLESS=true

▶️ Running Tests

Run all tests:
pytest -v

Run in headless mode:
HEADLESS=true pytest -v

🔄 CI/CD

This project includes a GitHub Actions pipeline that:

* Installs dependencies
* Installs Playwright browsers
* Runs tests in headless mode
* Uses environment secrets for API authentication

⚖️ Selenium vs Playwright

This project includes both Selenium and Playwright implementations to compare:

* Traditional WebDriver-based automation (Selenium)
* Modern auto-waiting and faster execution (Playwright)

This demonstrates understanding of different automation approaches and their trade-offs.

🧠 Key Concepts Demonstrated

* Page Object Model (POM)
* API abstraction layer
* Schema validation
* Environment-based configuration
* Debugging and handling flaky tests
* CI/CD integration
* Playwright network interception

💬 Interview Summary

I built a hybrid automation framework using Python, Selenium, and Playwright for UI testing, and requests for API testing. I implemented Page Object Model, API client abstraction, schema validation, and CI integration with GitHub Actions. I also explored advanced Playwright features like network interception and multi-tab handling.

📌 Notes

* This is a portfolio project demonstrating QA automation skills
* Focus is on scalability, maintainability, and real-world practices
* Designed as a transition from **manual QA to automation
