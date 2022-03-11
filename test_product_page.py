import pytest
from .pages.product_page import ProductPage

#link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
#link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"

@pytest.mark.parametrize('link', [0, 1, 2, 3, 4, 5, 6,
                                  pytest.param(7, marks=pytest.mark.xfail),
                                  8, 9])
def test_guest_can_add_product_to_basket(browser, link):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link}"
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.check_add_to_basket()

@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.add_to_basket()
    add_product.should_be_an_acc()
    add_product.should_not_be_success_message()

def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.should_not_be_success_message()

@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1"
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.add_to_basket()
    add_product.should_be_an_acc()
    add_product.should_be_success_message()
