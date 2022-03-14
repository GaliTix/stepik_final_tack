import math
from selenium.common.exceptions import NoAlertPresentException
from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_url(self):
        assert '/basket/' in self.browser.current_url, '/basket/ is not to url'

    def should_be_message_basket_is_empty(self):
        assert self.is_element_present(*BasketPageLocators.BASKET_EMPTY), \
            "Message basket is empty is not presented"

    def should_not_be_product_to_basket(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCT_TO_BASKET), \
            "Product is presented to basket, but should not be"

    def solve_quiz_and_get_code(self):
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")
