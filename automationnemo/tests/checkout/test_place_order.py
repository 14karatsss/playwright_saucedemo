from automationnemo.src.pages.LoginPage import LoginPage
from automationnemo.src.pages.CheckOutPage import CheckoutPage
from playwright.sync_api import expect


def test_place_order(set_up_tear_down) -> None:

    #Verify that user is able to pace an order successfully

    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)

    product_name = "Sauce Labs Fleece Jacket"
    cart_p = products_p.click_add_to_cart_or_remove(product_name)\
        .click_cart_icon()
    checkout_p = cart_p.click_checkout_button()\
        .enter_checkout_details("Fn12", "Ln12", "0011")\
        .click_continue()\
        .click_finish_btn()

    expect(checkout_p.get_confirm_message()).to_have_text("THANK YOU FOR YOUR ORDER")

