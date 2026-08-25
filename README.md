# QA Automation Portfolio — Selenium, Playwright and API

## Overview

This hands-on portfolio project demonstrates practical QA automation across UI, API, and CI workflows. It complements my software-testing background with working examples of Selenium WebDriver, Playwright, Python, pytest, API testing, JSON-schema validation, and GitHub Actions.

The repository is deliberately presented as a portfolio framework—not as production framework ownership. Its goal is to show readable test design, reusable components, reliable synchronization, test classification, and repeatable execution.

## What it covers

- Selenium UI tests using Page Object Model and explicit waits
- Playwright UI tests using locators, auto-waiting, and network interception
- ReqRes API tests through a reusable client with request timeouts
- Parametrized assertions and JSON-schema validation
- Environment-based configuration
- Automatic Selenium screenshots after test failures
- Playwright screenshots and traces on failure in CI
- HTML and JUnit reports uploaded as CI artifacts
- Separate markers for API, Selenium, Playwright, and optional external tests
- A clearly labelled combined smoke check for independent API and UI validation

## Technology

- Python 3.11+
- Selenium WebDriver
- Playwright
- pytest and pytest-playwright
- requests
- jsonschema
- GitHub Actions

## Project structure

```text
qa-automation-saucedemo/
├── .github/workflows/     # CI pipeline
├── api/                   # Reusable API client
├── pages/                 # Selenium page objects
├── playwright_pages/      # Playwright page objects
├── schemas/               # API response schemas
├── tests/                 # API and UI tests
├── .env.example           # Configuration template
├── conftest.py            # Shared fixtures and failure evidence
├── config.py              # Environment configuration
├── pytest.ini             # Test discovery and markers
├── requirements.txt       # Pinned dependencies
└── TEST_STRATEGY.md       # Scope, layers, risks, and limitations
```

## Setup

```bash
git clone https://github.com/LiviuBelibou/qa-automation-saucedemo.git
cd qa-automation-saucedemo

python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements.txt
python -m playwright install chromium

cp .env.example .env
```

`REQRES_API_KEY` can be added to `.env` when the API requires one. The key is only attached to requests when a value is configured.

## Running tests

Run the core suite without third-party social-site checks:

```bash
pytest -m "not external"
```

Run a specific layer:

```bash
pytest -m api
pytest -m "selenium and not external"
pytest -m "playwright and not external"
pytest -m combined
```

Run the optional external navigation checks:

```bash
pytest -m external
```

Generate a local self-contained HTML report:

```bash
mkdir -p reports
pytest -m "not external" --html=reports/report.html --self-contained-html
```

For headless Selenium execution, set `HEADLESS=true` in `.env` or before the command.

## CI workflow

GitHub Actions runs the core suite on pushes to `main` and on pull requests. The workflow:

1. creates a Python 3.11 environment on Ubuntu;
2. installs the pinned dependencies and Playwright Chromium;
3. runs all tests except those marked `external`;
4. produces HTML and JUnit reports;
5. retains reports, Selenium screenshots, and Playwright failure evidence as downloadable artifacts.

External social destinations are intentionally excluded from the required CI path because their redirects, consent screens, and anti-bot behavior are outside this project's control.

## Design notes

Selenium and Playwright are both included to demonstrate their different synchronization and page-object approaches. The project does not claim that SauceDemo and ReqRes form one integrated system: the combined smoke test performs independent API and UI checks and is named accordingly.

For the detailed scope, execution model, risks, and limitations, see [TEST_STRATEGY.md](TEST_STRATEGY.md).

## Interview summary

I built this portfolio project to strengthen my automation skills alongside more than ten years of software QA experience. It demonstrates Selenium and Playwright UI testing, reusable page objects, Python/pytest API checks, schema validation, environment configuration, failure evidence, and GitHub Actions execution. I can explain the design choices, current limitations, and the improvements I would make for a production environment.
