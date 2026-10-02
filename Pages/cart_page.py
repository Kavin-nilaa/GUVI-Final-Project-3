from Pages.base_page import BasePage
from selenium.webdriver.common.by import By


class CartPage(BasePage):
    CART_ITEMS = (By.CLASS_NAME,"cart_item")
    CART_PRODUCT_NAMES = (By.CLASS_NAME,"inventory_item_name")
    CART_PRODUCT_PRICES = (By.CLASS_NAME,"inventory_item_price")
    CHECK_OUT = (By.ID,"checkout")

    def get_cart_list(self):
        items = self.driver.find_elements(*self.CART_ITEMS)
        return len(items)

    def get_cart_product_details(self):
        names = self.driver.find_elements(*self.CART_PRODUCT_NAMES)
        prices = self.driver.find_elements(*self.CART_PRODUCT_PRICES)

        cart_products = []

        for name, price in zip(names, prices):
            cart_products.append({"name": name.text, "price": price.text})
        return cart_products

    def click_checkout(self):
        self.click_element(self.CHECK_OUT)


