# Test Strategy

## Purpose

This portfolio project demonstrates practical QA automation across browser and API layers. It focuses on readable test design, reusable page objects, environment-based configuration, and repeatable CI execution.

## Scope

The core suite covers:

- SauceDemo login validation, inventory, cart, sorting, logout, and checkout flows;
- equivalent selected UI checks with Selenium and Playwright;
- ReqRes API status, payload, parametrization, and JSON-schema checks;
- failure evidence through Selenium screenshots, Playwright traces/screenshots, HTML reports, and JUnit results.

Social-link tests validate navigation to external websites. They are marked `external` and excluded from core CI because those sites are outside the application's control and can introduce consent pages, redirects, rate limits, or bot checks.

## Test layers

| Layer | Purpose | Marker |
| --- | --- | --- |
| API | Fast checks of ReqRes endpoints and response contracts | `api` |
| Selenium UI | Browser coverage using explicit waits and Page Object Model | `selenium` |
| Playwright UI | Selected browser coverage using Playwright auto-waiting and network controls | `playwright` |
| Combined smoke | Independent ReqRes API and SauceDemo UI checks in one test | `combined` |
| External navigation | Optional checks of third-party social destinations | `external` |

The combined API/UI smoke test performs two independent checks against ReqRes and SauceDemo. It is not presented as a true cross-system end-to-end flow because the services are unrelated.

## Execution

- Core suite: `pytest -m "not external"`
- API: `pytest -m api`
- Selenium: `pytest -m "selenium and not external"`
- Playwright: `pytest -m "playwright and not external"`
- Combined smoke: `pytest -m combined`
- External navigation: `pytest -m external`

## Quality risks and controls

- Browser timing: Selenium page objects use explicit waits; Playwright relies on locator auto-waiting.
- New windows: tests wait for and select a handle that did not exist before the click.
- Network calls: the API client applies a finite timeout to every request.
- Third-party instability: external navigation tests do not gate pull requests.
- Debugging: CI uploads reports, screenshots, traces, and JUnit results even after failures.

## Current limitations

- SauceDemo and ReqRes are public demonstration services and are not one integrated product.
- The suite is intentionally compact and does not include production concerns such as test-data provisioning, service virtualization, parallel execution, or environment promotion.
- Playwright coverage demonstrates selected patterns rather than mirroring every Selenium scenario.
