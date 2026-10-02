from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    def __init__(self,driver):
        self.driver=driver
        self.wait=WebDriverWait(driver,10)

    def open_url(self,url):
        self.driver.get(url)

    def enter_text(self,locator,value):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(value)

    def click_element(self,locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()

    def is_element_displayed(self,locator):
        return self.wait.until(EC.visibility_of_element_located(locator))

    def is_element_enabled(self,locator):
        return self.wait.until(EC.element_to_be_clickable(locator))

    def get_page_title(self):
        return self.driver.title

    def get_current_url(self):
        return self.driver.current_url

    def get_text(self,locator):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        return element.text

    def close_browser(self):
        self.driver.quit()

