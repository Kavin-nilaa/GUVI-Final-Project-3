from Pages.base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    username_field = (By.ID, 'user-name')
    password_field = (By.ID, "password")
    login_button = (By.ID, "login-button")
    locked_error = (By.XPATH, "//h3[contains(text(),'locked out')]")
    invalid_error = (By.XPATH, "//h3[@data-test='error']")  # generic error

    def open_login_url(self):
        self.open_url("https://www.saucedemo.com/")

    def enter_username(self, username):
        self.enter_text(self.username_field, username)

    def enter_password(self, password):
        self.enter_text(self.password_field, password)

    def get_error_message(self, locator):
        return self.get_text(locator)

    def click_login_button(self):
        self.click_element(self.login_button)

    def is_locked_error_message_visible(self):
        return self.is_element_displayed(self.locked_error)

    def is_invalid_error_message_visible(self):
        return self.is_element_displayed(self.invalid_error)

    def login(self,username,password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login_button()
