from selenium.webdriver.common.by import By

class MainPageLocators():
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")

class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")

class ProductPageLocators():
    BASKET_FORM = (By.CSS_SELECTOR, "#add_to_basket_form")
    ADD_BASKET = (By.CSS_SELECTOR, ".btn-add-to-basket")
    MESSAGE_ADD_BASKET = (By.XPATH, '//div[@id="messages"]//strong')
    NAME_PRODUCT = (By.XPATH, '//div[@class="col-sm-6 product_main"]//h1')
    MESSAGE_PRICE = (By.XPATH, '//div[@id="messages"]//p')
    PRICE_PRODUCT = (By.CSS_SELECTOR, 'p.price_color')
    PRICE_TO_BASKET = (By.XPATH, '//div[@class="basket-mini pull-right hidden-xs"]')

