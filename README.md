QA Automation Framework (Selenium + Playwright + API)

📌 Overview

This project is a hybrid QA automation framework combining UI and API
testing.

It includes: - UI automation using Selenium (Page Object Model) - UI
automation using Playwright (modern, auto-waiting based approach) - API
testing using requests - CI/CD integration using GitHub Actions

The framework demonstrates end-to-end testing, clean architecture, and
real-world automation practices.

------------------------------------------------------------------------

🛠️ Tech Stack

-   Python
-   Selenium WebDriver
-   Playwright
-   pytest
-   requests
-   jsonschema
-   GitHub Actions

------------------------------------------------------------------------

🚀 Features

-   Page Object Model (POM) for scalable UI automation (Selenium &
    Playwright)
-   API client abstraction for reusable request handling
-   Parametrized API tests
-   JSON schema validation for API responses
-   Multi-tab handling (Selenium & Playwright)
-   Network interception (Playwright)
-   Headless execution support
-   Automatic screenshots on test failure
-   HTML test reporting
-   Environment-based configuration using .env
-   Continuous Integration with GitHub Actions

------------------------------------------------------------------------

📂 Project Structure

qa-automation-saucedemo/ ├── api/ ├── pages/ ├── playwright_pages/ ├──
schemas/ ├── tests/ ├── screenshots/ ├── reports/ ├── conftest.py ├──
config.py └── requirements.txt

------------------------------------------------------------------------

⚙️ Setup & Installation

git clone https://github.com/YOUR_USERNAME/qa-automation-saucedemo.git
cd qa-automation-saucedemo python3 -m venv .venv source
.venv/bin/activate pip install -r requirements.txt python -m playwright
install

------------------------------------------------------------------------

🔐 Environment Variables

BASE_URL=https://www.saucedemo.com API_BASE_URL=https://reqres.in/api
TEST_EMAIL=standard_user TEST_PASSWORD=secret_sauce
REQRES_API_KEY=your_api_key_here HEADLESS=true

------------------------------------------------------------------------

▶️ Running Tests

pytest -v

HEADLESS=true pytest -v

------------------------------------------------------------------------

🔄 CI/CD

The project includes a GitHub Actions pipeline that: - installs
dependencies - installs Playwright browsers - runs tests in headless
mode - uses environment secrets for API authentication

------------------------------------------------------------------------

🧠 Key Concepts Demonstrated

-   Page Object Model (POM)
-   API abstraction layer
-   Schema validation
-   Environment-based configuration
-   Debugging and handling flaky tests
-   CI/CD integration
-   Playwright network interception

------------------------------------------------------------------------

🎯 What This Project Demonstrates

-   Ability to design and structure an automation framework
-   Understanding of UI + API testing integration
-   Experience with CI/CD pipelines and environment configuration
-   Hands-on debugging of real-world issues

------------------------------------------------------------------------

💬 Interview Summary

I built a hybrid automation framework using Python, Selenium, and
Playwright for UI testing, and requests for API testing. I implemented
Page Object Model, API client abstraction, schema validation, and CI
integration with GitHub Actions. I also explored advanced Playwright
features like network interception and multi-tab handling.

------------------------------------------------------------------------

📌 Notes

-   This is a portfolio project demonstrating QA automation skills
-   Focus is on scalability, maintainability, and real-world practices
