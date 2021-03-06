from selenium.webdriver.common.by import By


class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    PASSWORD_FIRST = (By.CSS_SELECTOR, "#id_registration-password1")
    PASSWORD_SECOND = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.CSS_SELECTOR, "#register_form>button")

class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, ".btn-add-to-basket")
    NAME_SUCCESS = (By.CSS_SELECTOR, ".alertinner strong")
    PRICE_SUCCESS = (By.CSS_SELECTOR, ".alertinner p strong")
    NAME_PRODUCT = (By.CSS_SELECTOR, ".product_main h1")
    PRICE_PRODUCT = (By.CSS_SELECTOR, ".product_main p.price_color")
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, "#messages .alert-success")

class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")

class BasketPageLocators():
    BASKET_BUTTON = (By.CSS_SELECTOR, ".basket-mini a.btn-default")
    PRODUCTS_IN_BASKET = (By.CSS_SELECTOR, ".basket_summary")
    EMPTY_BASKET_MESSAGE = (By.CSS_SELECTOR, "#content_inner>p")
