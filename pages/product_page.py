from .base_page import BasePage
from selenium.webdriver.common.by import By
from .locators import ProductPageLocators

class ProductPage(BasePage):
    def check_add_to_basket(self):
        self.add_to_basket()
        self.should_be_an_acc()
        self.check_product_name()
        self.check_product_price()

    def add_to_basket(self):
        add_product = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_product.click()

    def should_be_an_acc(self):
        self.solve_quiz_and_get_code()

    def check_product_name(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT)
        name_success = self.browser.find_element(*ProductPageLocators.NAME_SUCCESS)
        assert name_product.text == name_success.text, \
            "The product name in the notice does not match the product name in the description"

    def check_product_price(self):
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT)
        price_success = self.browser.find_element(*ProductPageLocators.PRICE_SUCCESS)
        assert price_product.text == price_success.text, \
            "The product price in the notice does not match the product price in the description"
