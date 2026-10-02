from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CheckoutPage(BasePage):
    first_name = (By.ID,"first-name")
    last_name = (By.ID,"last-name")
    postal_code = (By.ID,"postal-code")
    continue_button = (By.ID,"continue")
    finish_button = (By.ID,"finish")
    order_confirmation = (By.CLASS_NAME,"complete-header")

    def checkout_process(self, first_name, last_name, postal_code):
        self.enter_text(self.first_name, first_name)
        self.enter_text(self.last_name, last_name)
        self.enter_text(self.postal_code, postal_code)
        self.click_element(self.continue_button)
        self.click_element(self.finish_button)

    def get_order_confirmation_text(self):
        element = self.driver.find_element(*self.order_confirmation)
        return element.text



