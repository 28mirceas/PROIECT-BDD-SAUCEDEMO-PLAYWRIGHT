# SauceDemo UI Automation with Playwright and Behave

## Project Overview

This project contains automated UI tests for the [SauceDemo](https://www.saucedemo.com/) web application, using Python, Playwright, and Behave.

The project follows the **Behavior-Driven Development (BDD)** approach, with test scenarios written in Gherkin syntax and implemented using Python step definitions.

The **Page Object Model (POM)** design pattern is used to organize page interactions and improve code reusability and maintainability.

This project was developed as a practical exercise in UI test automation and test automation architecture.

## Technologies Used

* **Python 3.9** — programming language
* **Playwright 1.60.0** — browser automation
* **Behave 1.3.3** — BDD testing framework
* **Gherkin** — readable test scenario syntax
* **Page Object Model (POM)** — test automation design pattern
* **Chromium** — browser used for test execution

## Project Structure

```text
PROIECT-BDD-SAUCEDEMO-PLAYWRIGHT/
│
├── features/
│   ├── cart.feature
│   ├── checkout.feature
│   ├── login.feature
│   └── products.feature
│
├── steps/
│   ├── cart_steps.py
│   ├── checkout_steps.py
│   ├── login_steps.py
│   └── products_steps.py
│
├── pages/
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
│
├── browser.py
├── environment.py
├── behave.ini
└── requirements.txt
```

### Folder and File Description

**`features/`**

Contains Gherkin feature files describing the application behavior and test scenarios.

* `login.feature` — login functionality and error handling
* `products.feature` — product sorting functionality
* `cart.feature` — shopping cart operations and navigation to checkout
* `checkout.feature` — checkout flow and total price verification

**`steps/`**

Contains Python step definitions that connect Gherkin steps to the corresponding automation code.

**`pages/`**

Contains Page Object Model classes responsible for page-specific interactions.

* `base_page.py` — shared page interaction methods
* `login_page.py` — login page interactions
* `products_page.py` — product page interactions
* `cart_page.py` — shopping cart interactions
* `checkout_page.py` — checkout page interactions

**`browser.py`**

Handles browser initialization and cleanup using Playwright.

**`environment.py`**

Contains Behave hooks for test setup and cleanup.

**`behave.ini`**

Contains the Behave configuration, including the HTML formatter mapping.

**`requirements.txt`**

Lists the Python dependencies required to run the project.

## Automated Test Coverage

The project currently includes **8 BDD scenarios** covering four functional areas.

### 1. Login

* Successful login using valid credentials
* Verification of the error message for a locked-out user
* Verification of the resulting URL after successful and unsuccessful login attempts

### 2. Products

* Sorting products by price, from low to high
* Sorting products by name, from Z to A

### 3. Shopping Cart

* Adding a single product to the shopping cart
* Adding multiple products to the shopping cart
* Navigating from the shopping cart to the checkout page

### 4. Checkout

* Completing the checkout information form
* Verifying that the sum of the displayed product prices matches the total calculated at checkout

## Prerequisites

Before running the tests, make sure you have installed:

* Python 3.9 or a compatible Python version
* pip
* Git

## Installation

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
```

Navigate to the project directory:

```bash
cd PROJECT-BDD-SAUCEDEMO-PLAYWRIGHT
```

### 2. Create a virtual environment

```bash
python -m venv .venv
```

### 3. Activate the virtual environment

On Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 4. Install the dependencies

```bash
python -m pip install -r requirements.txt
```

### 5. Install the Playwright browser

```bash
python -m playwright install chromium
```

## Running the Tests

To execute all Behave scenarios, run:

```bash
python -m behave
```

To run a specific feature file, use:

```bash
python -m behave features/login.feature
```

You can replace `login.feature` with `products.feature`, `cart.feature`, or `checkout.feature` to run the tests for a specific functional area.

## Design Approach

The project uses the **Page Object Model (POM)** to separate page interactions from test steps.

The main responsibilities are:

* **Feature files:** describe the expected behavior using Gherkin.
* **Step definitions:** implement the actions and checks associated with each scenario.
* **Page objects:** encapsulate page-specific interactions and reusable methods.
* **Browser setup and hooks:** manage browser initialization and test cleanup.

This separation helps keep the test automation code organized, reusable, and easier to maintain.

## Learning Objectives

This project provides practical experience with:

* Python-based UI test automation
* Playwright's synchronous API
* Behavior-Driven Development using Behave
* Writing Gherkin scenarios
* Applying the Page Object Model
* Organizing a multi-file test automation project
* Automating login, product sorting, shopping cart, and checkout scenarios

## Future Improvements

Potential future improvements include:

* Expanding test coverage with additional positive and negative scenarios
* Configuring and generating HTML test reports
* Integrating automated tests into a CI/CD pipeline
* Improving test reporting and execution documentation

## Application Under Test

[SauceDemo](https://www.saucedemo.com/)
