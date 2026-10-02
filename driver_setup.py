from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.firefox.service import Service as FirefoxService
from selenium.webdriver.edge.service import Service as EdgeService
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager

def get_driver(browser_name = "chrome"):
    browser_name = browser_name.lower()

    if browser_name == "chrome":
        driver = webdriver.Chrome(service = ChromeService(ChromeDriverManager().install()))
        driver.maximize_window()
        return driver
    elif browser_name == "firefox":
        driver = webdriver.Firefox(service = FirefoxService(GeckoDriverManager().install()))
        driver.maximize_window()
        return driver
    elif browser_name == "edge":
        driver = webdriver.Edge(service = EdgeService(EdgeChromiumDriverManager().install()))
        driver.maximize_window()
        return driver
    elif browser_name == "safari":
        driver = webdriver.Safari()
        driver.maximize_window()
        return driver
    else:
        raise Exception(f"Browser '{browser_name}' is not supported")
