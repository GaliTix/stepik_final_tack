import pytest
import random
import time
from .pages.basket_page import BasketPage
from .pages.product_page import ProductPage
from .pages.login_page import LoginPage


@pytest.mark.parametrize('substring',
                         ["offer0", "offer1", "offer3", "offer4", "offer5", "offer6",
                          pytest.param("offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")), "offer8",
                          "offer9"])
@pytest.mark.need_review
def test_guest_can_add_product_to_basket(browser, substring):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={substring}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_form()
    page.should_be_add_basket()
    page.click_to_button_add_basket()
    basket_page = BasketPage(browser, link)
    basket_page.solve_quiz_and_get_code()
    page.should_be_message_about_add_basket()
    page.should_be_message_contain_name_product()
    page.should_be_message_about_price()
    page.should_be_message_contain_price()

@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_login_page()

@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, link)
    basket_page.should_be_basket_url()
    basket_page.should_not_be_product_to_basket()
    basket_page.should_be_message_basket_is_empty()


@pytest.mark.skip
def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_button_add_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.should_not_be_success_message()


def test_guest_should_see_login_link_on_product_page(browser):
    link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_login_link()


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_button_add_basket()
    page.should_be_disappeared_success_message()


class TestUserAddToBasketFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self, browser):
        email = str(time.time()) + "@fakemail.org"
        count = random.randint(1, 100)
        password = str(time.time() + count)
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()
        page.go_to_login_page()
        login_page = LoginPage(browser, link)
        login_page.should_be_login_page()
        login_page.register_new_user(email, password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_basket_form()
        page.should_be_add_basket()
        page.click_to_button_add_basket()
        page.should_be_message_about_add_basket()
        page.should_be_message_contain_name_product()
        page.should_be_message_about_price()
        page.should_be_message_contain_price()

    def test_user_cant_see_success_message(self, browser):
        link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
        page = ProductPage(browser, link)
        page.open()
        page.should_not_be_success_message()
