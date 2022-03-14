from .base_page import BasePage
from .locators import BasketPageLocators

class BasketPage(BasePage):
    def check_basket_is_empty(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Products in basket, but they shouldn't be"

    def check_empty_basket_message(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_MESSAGE), \
            "No message"
