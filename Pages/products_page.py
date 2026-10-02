from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from Pages.base_page import BasePage
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random

class ProductsPage(BasePage):
    cart_icon = (By.CLASS_NAME, "shopping_cart_link")
    menu_button = (By.ID, "react-burger-menu-btn")
    logout_button = (By.ID, "logout_sidebar_link")
    reset_button = (By.ID, "reset_sidebar_link")
    close_menu_button = (By.ID,"react-burger-cross-btn")
    PRODUCT_NAMES = (By.CLASS_NAME, "inventory_item_name ")
    PRODUCT_PRICES = (By.CLASS_NAME, "inventory_item_price")
    ADD_TO_CART_BTN = (By.XPATH, "//button[contains(text(),'Add to cart')]")
    CART_BADGE = (By.CLASS_NAME, "shopping_cart_badge")
    SORT_DROPDOWN = (By.CLASS_NAME,"product_sort_container")
    RESET_APP = (By.ID,"reset_sidebar_link")


    def click_logout(self):
        self.click_element(self.menu_button)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(self.logout_button)
        )
        self.click_element(self.logout_button)

    def is_cart_icon_displayed(self):
        return self.is_element_displayed(self.cart_icon)

    def click_cart(self):
        self.click_element(self.cart_icon)

    def get_random_products(self, count=4):

        product_names = self.driver.find_elements(*self.PRODUCT_NAMES)
        product_prices = self.driver.find_elements(*self.PRODUCT_PRICES)

        products = []

        for name, price in zip(product_names, product_prices):
            products.append({"name": name.text, "price": price.text})

        return random.sample(products, count)

    def add_random_products_to_cart(self, count=4):
        buttons = self.driver.find_elements(*self.ADD_TO_CART_BTN)
        selected = random.sample(buttons, count)
        for button in selected:
            button.click()

    def check_cart_count(self):
        badge = self.driver.find_element(*self.CART_BADGE)
        return badge.text

    def click_reset_app_button(self):
        self.click_element(self.menu_button)
        self.click_element(self.reset_button)

    def close_menu(self):
        self.click_element(self.close_menu_button)

    def select_sort_option(self,option_text):
        dropdown = Select(self.driver.find_element(*self.SORT_DROPDOWN))
        dropdown.select_by_visible_text(option_text)

    def get_product_prices(self):
        prices = self.driver.find_elements(*self.PRODUCT_PRICES)
        return [float(price.text.replace("$", ""))
                for price in prices]

    def click_reset_app(self):
        self.click_element(self.menu_button)
        self.click_element(self.reset_button)