# Selenium Python Automation Framework

UI automation framework built with Python, Selenium, and pytest using the Page Object Model (POM) design pattern.

## Tech Stack
- Python
- Selenium WebDriver
- pytest
- Page Object Model (POM)
- BasePage pattern
- python-dotenv

## Project Structure
```text
selenium_learning/
├── conftest.py
├── config.py
├── pages/
│   ├── base_page.py
│   ├── inventory_page.py
│   └── login_page.py
└── tests/
    ├── test_inventory.py
    ├── test_login.py
    ├── test_login_validation.py
    └── test_ui.py