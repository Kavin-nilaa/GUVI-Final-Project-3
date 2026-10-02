import os
from datetime import datetime
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.edge.service import Service as EdgeService
from selenium.webdriver.edge.options import Options as EdgeOptions

from driver_setup import get_driver
from utils.excel_util import write_test_result

TEST_CASE_FILE = "Final Project 3 Test Case.xlsx"
TEST_CASE_SHEET = "Sheet1"

def pytest_addoption(parser):
    parser.addoption(
        "--browser", action="store", default="chrome",
        help="Browser option: chrome, firefox, edge, safari"
    )

@pytest.fixture
def driver(request):

    browser = request.config.getoption("--browser")
    driver = get_driver(browser)
    yield driver

    screenshot_dir = os.path.join("reports", "screenshots")
    os.makedirs(screenshot_dir, exist_ok=True)
    screenshot_name = f"{request.node.name}_{datetime.now().strftime('%Y%m%d_%H%M%S')}.png"
    driver.save_screenshot(os.path.join(screenshot_dir, screenshot_name))

    driver.quit()

@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call":
        # Extract test case ID from function name
        parts = item.name.split("_")
        test_case_id = parts[1].upper() if len(parts) > 1 else item.name.upper()

        # Decide result based on pytest outcome
        result = "Passed" if report.passed else "Failed"

        # Update Excel
        write_test_result(TEST_CASE_FILE, TEST_CASE_SHEET, test_case_id, result)
