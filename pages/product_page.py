from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def should_be_newYear_url(self):
        assert 'newYear' in self.browser.current_url, 'newYear is not to url'

    def should_be_basket_form(self):
        assert self.is_element_present(*ProductPageLocators.BASKET_FORM), 'BASKET FORM is not presented'

    def should_be_add_basket(self):
        assert self.is_element_present(*ProductPageLocators.ADD_BASKET), 'Button ADD TO BASKET is not presented'

    def click_to_button_add_basket(self):
        button_add_to_basket = self.browser.find_element(*ProductPageLocators.ADD_BASKET)
        button_add_to_basket.click()

    def should_be_message_about_add_basket(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_ADD_BASKET), 'Message about add to basket is not presented'

    def should_be_message_contain_name_product(self):
        name_product = self.browser.find_element(*ProductPageLocators.NAME_PRODUCT).text
        name_product_to_message = self.browser.find_element(*ProductPageLocators.MESSAGE_ADD_BASKET).text
        assert name_product == name_product_to_message, 'Name product is not corrected to message'

    def should_be_message_about_price(self):
        assert self.is_element_present(
            *ProductPageLocators.MESSAGE_PRICE), 'Message about price is not presented'

    def should_be_message_contain_price(self):
        price_to_basket = self.browser.find_element(*ProductPageLocators.PRICE_TO_BASKET).text
        price_product = self.browser.find_element(*ProductPageLocators.PRICE_PRODUCT).text
        assert price_product in price_to_basket, 'Price product is not corrected to basket'
