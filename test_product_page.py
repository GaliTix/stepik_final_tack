import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize('substring',
                         ["offer0", "offer1", "offer3", "offer4", "offer5", "offer6",
                          pytest.param("offer7", marks=pytest.mark.xfail(reason="fixing this bug right now")), "offer8",
                          "offer9"])
def test_add_product_to_basket(browser, substring):
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo={substring}"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_basket_form()
    page.should_be_add_basket()
    page.click_to_button_add_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_basket()
    page.should_be_message_contain_name_product()
    page.should_be_message_about_price()
    page.should_be_message_contain_price()


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


@pytest.mark.xfail(reason="fixing this bug right now")
def test_message_disappeared_after_adding_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
    page = ProductPage(browser, link)
    page.open()
    page.click_to_button_add_basket()
    page.should_be_disappeared_success_message()
