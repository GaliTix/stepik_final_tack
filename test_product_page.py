from .pages.product_page import ProductPage

def test_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.should_be_newYear_url()
    page.should_be_basket_form()
    page.should_be_add_basket()
    page.click_to_button_add_basket()
    page.solve_quiz_and_get_code()
    page.should_be_message_about_add_basket()
    page.should_be_message_contain_name_product()
    page.should_be_message_about_price()
    page.should_be_message_contain_price()