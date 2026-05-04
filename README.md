🚀 QA Automation Framework (Selenium + Playwright + API)

📌 Overview

I built this project to transition from manual QA into automation and to showcase real-world testing across UI, API, and CI workflows.

It includes:

- UI automation using Selenium (Page Object Model)
- UI automation using Playwright (modern, auto-waiting approach)
- API testing using requests
- CI/CD integration with GitHub Actions

The framework demonstrates end-to-end test coverage, clean architecture, and practical automation skills. It reflects a real-world QA approach by combining UI and API validation within a CI pipeline.

🛠️ Tech Stack

- Programming Language: Python  
- UI Automation: Selenium WebDriver, Playwright  
- Test Framework: pytest  
- API Testing: requests  
- Data Validation: jsonschema  
- CI/CD Pipeline: GitHub Actions  

🚀 Features

UI Automation:
- Page Object Model (POM) for scalable test design (Selenium & Playwright)
- Multi-tab handling for external navigation validation
- Headless execution support

API Testing:
- Custom API client abstraction for reusable request handling
- Parametrized API tests
- JSON schema validation for response verification

Playwright Enhancements:
- Network interception for request control and validation

Test Infrastructure:
- Automatic screenshots on test failure
- HTML test reporting
- Environment-based configuration using `.env`
- Continuous Integration with GitHub Actions

This feature set reflects a real-world automation framework combining UI, API, and CI practices.

📊 Test Coverage

- Covers core user flows: login, inventory, cart, and checkout  
- Includes UI, API, and hybrid test scenarios  
- Validates API responses using schema validation  
- Executes automatically in CI pipeline (GitHub Actions)  
- Designed to simulate real user behavior across UI and backend layers  

📂 Project Structure

The project follows a modular structure separating UI, API, and test logic for scalability and maintainability.

qa-automation-saucedemo/
├── api/                # API client and API test logic
├── pages/              # Selenium Page Object classes
├── playwright_pages/   # Playwright Page Object classes
├── schemas/            # JSON schemas for API validation
├── tests/              # UI, API, and hybrid test cases
├── screenshots/        # Screenshots captured on test failure
├── reports/            # HTML test reports
├── conftest.py         # Shared fixtures and pytest configuration
├── config.py           # Environment and framework configuration
└── requirements.txt    # Project dependencies

⚙️ Setup & Installation

Ensure Python 3.x is installed before running the setup.

Clone the repository and set up the environment:

git clone https://github.com/LiviuBelibou/qa-automation-saucedemo.git
cd qa-automation-saucedemo

# Create virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Install Playwright browsers
python -m playwright install

🔐 Environment Variables

Create a `.env` file in the project root:

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

This project integrates a GitHub Actions pipeline to automatically execute tests on every push and pull request.

The pipeline:

- Installs project dependencies  
- Installs Playwright browsers  
- Executes tests in headless mode  
- Uses environment secrets for secure API authentication  

This ensures consistent test execution and helps detect issues early in the development workflow. The CI setup mirrors real-world automation workflows used in modern QA environments.

⚖️ Selenium vs Playwright

This project includes both Selenium and Playwright implementations to compare different UI automation approaches.

- Selenium uses a traditional WebDriver-based model, requiring explicit waits and more manual synchronization  
- Playwright provides built-in auto-waiting, faster execution, and better handling of modern web applications  

By implementing both, the project highlights the trade-offs between stability, speed, and maintainability, and demonstrates the ability to work with both legacy and modern automation tools. Playwright was used to explore newer automation patterns, while Selenium reflects industry-standard tooling still widely used in existing frameworks.

🧠 Key Concepts Demonstrated

- Page Object Model (POM) for maintainable and scalable UI test design  
- API abstraction layer for reusable and structured request handling  
- JSON schema validation to ensure API response integrity  
- Environment-based configuration for flexible test execution across environments  
- Debugging and handling flaky tests through improved synchronization and error handling  
- CI/CD integration for automated test execution and early defect detection  
- Playwright network interception for controlling and validating browser network requests  

These concepts reflect practical experience in building maintainable and scalable automation frameworks.

💬 Interview Summary

I built a hybrid automation framework using Python, combining Selenium and Playwright for UI testing and requests for API testing. I designed the framework using Page Object Model, implemented an API client with schema validation, and integrated the tests into a CI pipeline using GitHub Actions. I also explored advanced Playwright features such as network interception and multi-tab handling.

This project helped me gain hands-on experience with real-world automation practices across UI, API, and CI workflows.

📌 Notes

- This is a portfolio project demonstrating QA automation skills  
- Focuses on scalability, maintainability, and real-world practices  
- Designed as a transition from **manual QA to automation**  
- Reflects a hands-on approach to building modern automation frameworks
