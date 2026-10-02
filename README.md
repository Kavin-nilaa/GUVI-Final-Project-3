# Final Project 3 – Automated Testing of E-commerce Web Application

## Project Title
Automated Testing of the Web Application – [SauceDemo](https://www.saucedemo.com/)

---

## Objective
The objective of this project is to **automate testing** of the demo e-commerce web application, ensuring that core functionalities such as login, product selection, cart operations, and checkout processes work as expected.

The automation framework simulates user interactions including:
- Logging in with different user roles
- Navigating the product catalog
- Adding items to the cart
- Completing the purchase flow
- Validating UI content and system responses

---

## Scope
- Simulate real-time user behavior for multiple user roles  
- Validate functional flows: login, cart management, checkout  
- Random product interactions to simulate diverse purchase paths  
- Ensure correctness of UI content, product data, and order summary  
- Generate readable test execution reports  

---

## Preconditions
- Tests include both **positive and negative test data**  
- **Data-driven** and **keyword-driven** strategies for flexibility  
- Proper handling of **dynamic waits** for enhanced test stability  

---

## Test Suite
The following test cases are implemented:

1. **Login with predefined users** – Verify login behavior for different roles.  
2. **Login with invalid credentials** – Validate system response to unauthorized access.  
3. **Logout functionality** – Ensure proper redirection to login screen.  
4. **Cart icon visibility** – Confirm cart icon is always accessible post-login.  
5. **Random product selection** – Select 4 random products and log their details.  
6. **Add products to cart** – Validate cart count matches selected items.  
7. **Cart product details** – Ensure cart items match added products.  
8. **Checkout process** – Complete checkout, capture order summary, and validate confirmation.  
9. **Sorting functionality** – Verify product sorting by criteria (e.g., price, name).  
10. **Reset App State** – Ensure cart and selections are cleared when reset is triggered.  

---

## Tech Stack
- **Language:** Python  
- **Framework:** Selenium WebDriver  
- **Testing Tool:** Pytest  
- **IDE:** PyCharm  
- **Utilities:** WebDriverWait, Random module, Excel data-driven input  

---

## Project Structure
Final Project 3/
│── .venv/                     # Virtual environment
│── Pages/                     # Page Object classes
│   ├── base_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── login_page.py
│   └── products_page.py
│── reports/                   # Test execution reports
│── Tests/                     # Test cases
│   └── test_login.py
│── utils/                     # Utilities and setup
│   ├── excel_util.py
│   ├── conftest.py
│   └── driver_setup.py
│── Final Project 3 Test Case.xlsx   # Test case documentation
│── Final Project 3 Test Data.xlsx   # Test data inputs
│── README.md                  # Project documentationFinal Project 3/
