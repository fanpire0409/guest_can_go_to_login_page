import pytest
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage
from .pages.basket_page import BasketPage
import faker
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        login_link = "http://selenium1py.pythonanywhere.com/ru/accounts/login/"
        page = LoginPage(browser, login_link)
        page.open()
        fake = faker.Faker()
        email = fake.email()
        password = str(time.time())
        page.register_new_user(email=email, password=password)
        page.should_be_authorized_user()

    def test_user_cant_see_success_message(self, browser):
        add_product = ProductPage(browser, link)
        add_product.open()
        add_product.should_not_be_success_message()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        add_product = ProductPage(browser, link)
        add_product.open()
        add_product.check_add_to_basket()


@pytest.mark.need_review
@pytest.mark.parametrize('link_offer', [0, 1, 2, 3, 4, 5, 6,
                                        pytest.param(7, marks=pytest.mark.xfail),
                                        8, 9])
def test_guest_can_add_product_to_basket(browser, link_offer):
    link_offer = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{link_offer}"
    add_product = ProductPage(browser, link_offer)
    add_product.open()
    add_product.check_add_to_basket()


@pytest.mark.xfail
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.add_to_basket()
    add_product.should_be_an_acc()
    add_product.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.should_not_be_success_message()


@pytest.mark.xfail
def test_message_disappeared_after_adding_product_to_basket(browser):
    add_product = ProductPage(browser, link)
    add_product.open()
    add_product.add_to_basket()
    add_product.should_be_an_acc()
    add_product.success_message_should_disappear()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()
    login_page = LoginPage(browser, browser.current_url)
    login_page.should_be_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link_local = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = BasketPage(browser, link_local)
    page.open()
    page.go_to_basket()
    page.check_basket_is_empty()
    page.check_empty_basket_message()
