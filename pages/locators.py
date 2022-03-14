from selenium.webdriver.common.by import By


class BasePageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")
    VIEW_BASKET = (By.XPATH, '//a[@class="btn btn-default"]')
    USER_ICON = (By.CSS_SELECTOR, ".icon-user")


class BasketPageLocators():
    PRODUCT_TO_BASKET = (By.CSS_SELECTOR, ".thumbnail")
    BASKET_EMPTY = (By.XPATH, '//div[@id="content_inner"]//p')


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")
    REGISTER_EMAIL = (By.CSS_SELECTOR, "#id_registration-email")
    REGISTER_PASSWORD_1 = (By.CSS_SELECTOR, "#id_registration-password1")
    REGISTER_PASSWORD_2 = (By.CSS_SELECTOR, "#id_registration-password2")
    REGISTER_BUTTON = (By.XPATH, '//button[@name="registration_submit"]')
    MESSAGE_LOGIN = (By.XPATH, '//div[@class="alertinner wicon"]')
    LOG_IN_EMAIL = (By.CSS_SELECTOR, "#id_login-username")
    LOG_IN_PASSWORD = (By.CSS_SELECTOR, "#id_login-password")
    LOG_IN_BUTTON = (By.XPATH, '//button[@name="login_submit"]')


class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_BASKET = (By.XPATH, '//div[@id="messages"]//strong')
    NAME_PRODUCT = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    MESSAGE_PRICE = (By.XPATH, '//div[@id="messages"]//p')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_TO_BASKET = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]')
