from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from Pages.cart_page import CartPage
from Pages.checkout_page import CheckoutPage
from Pages.login_page import LoginPage
import time
from Pages.products_page import ProductsPage
from utils.excel_util import open_excel_file
import pytest

TEST_DATA_FILE ="Final Project 3 Test Data.xlsx"
TEST_DATA_SHEET="Sheet1"

test_data = open_excel_file(TEST_DATA_FILE,TEST_DATA_SHEET)

@pytest.mark.parametrize("username,password,expected",test_data)

def test_tc001_verify_login_with_redefined_user(driver,username,password,expected):
    login = LoginPage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.login(username, password)
    if expected == "Pass":
        assert "/inventory" in driver.current_url
    elif expected == "Locked user":
        assert login.is_locked_error_message_visible()

def test_tc002_verify_login_with_invalid_credentials(driver):
    login = LoginPage(driver)
    login.open_login_url()
    login.enter_username("admin")
    login.enter_password("admin123")
    login.click_login_button()
    login.is_invalid_error_message_visible()
    print("Logged in with invalid credentials")


def test_tc003_verify_logout(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    login.open_login_url()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()
    assert "sauce" in driver.current_url
    time.sleep(3)
    products.click_logout()

def test_tc004_verify_cart_icon_is_displayed(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.open_login_url()
    login.enter_username("standard_user")
    login.enter_password("secret_sauce")
    login.click_login_button()

    products.is_cart_icon_displayed()
    print("Cart icon is displayed")

def test_tc005_random_products_selection(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    login.open_login_url()
    login.login("standard_user","secret_sauce")
    selected_products = products.get_random_products(4)
    time.sleep(3)
    print("Random products selected:", selected_products)

def test_tc006_add_random_products_to_cart(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    login.open_login_url()
    login.login("standard_user","secret_sauce")
    products.add_random_products_to_cart(4)
    time.sleep(3)
    assert products.check_cart_count()== "4"
    products.click_cart()
    time.sleep(3)
    assert cart.get_cart_list() == 4

def test_tc007_validate_cart_product_details(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    login.open_login_url()
    login.login("standard_user", "secret_sauce")
    products.add_random_products_to_cart(4)
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(products.cart_icon)
    )
    assert products.check_cart_count() == "4"
    products.click_cart()
    time.sleep(3)
    assert cart.get_cart_list() == 4

    cart_products = cart.get_cart_product_details()
    print("Cart's details:", cart_products)

def test_tc008_verify_checkout_and_order(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    cart = CartPage(driver)
    checkout = CheckoutPage(driver)
    login.open_login_url()
    login.login("standard_user", "secret_sauce")
    products.add_random_products_to_cart(4)
    WebDriverWait(driver, 5).until(
        EC.presence_of_all_elements_located(products.cart_icon)
    )
    assert products.check_cart_count() == "4"
    products.click_cart()
    time.sleep(3)
    assert cart.get_cart_list() == 4

    cart_products = cart.get_cart_product_details()
    print("Cart's details:", cart_products)
    time.sleep(3)

    cart.click_checkout()
    time.sleep(3)
    checkout.checkout_process("first","last","8909321")

def test_tc009_sort_products_by_price(driver):

    login = LoginPage(driver)
    products = ProductsPage(driver)

    login.open_url("https://www.saucedemo.com/")

    login.login("standard_user","secret_sauce")

    products.select_sort_option("Price (low to high)")
    time.sleep(3)

    prices = products.get_product_prices()
    time.sleep(3)

    assert prices == sorted(prices)

def test_tc010_verify_reset_app(driver):
    login = LoginPage(driver)
    products = ProductsPage(driver)
    login.open_url("https://www.saucedemo.com/")
    login.login("standard_user","secret_sauce")
    products.click_reset_app()
    print("/nReset App is Clicked")







