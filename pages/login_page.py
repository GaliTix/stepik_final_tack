from .base_page import BasePage
from .locators import LoginPageLocators




class LoginPage(BasePage):
    def register_new_user(self, email, password):
        input_email = self.browser.find_element(*LoginPageLocators.REGISTER_EMAIL)
        input_email.send_keys(email)
        input_password_1 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_1)
        input_password_1.send_keys(password)
        input_password_2 = self.browser.find_element(*LoginPageLocators.REGISTER_PASSWORD_2)
        input_password_2.send_keys(password)
        register_button = self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON)
        register_button.click()
        assert self.is_element_present(*LoginPageLocators.MESSAGE_LOGIN), 'Message about registration is not presented'

    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert '/login/' in self.browser.current_url, '/login/ is not to url'

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not presented'

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not presented'
