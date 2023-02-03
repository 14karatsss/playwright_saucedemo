from playwright.sync_api import Page, expect
from automationnemo.src.pages.LoginPage import LoginPage


def test_logout(set_up_tear_down) -> None:

    page = set_up_tear_down
    credentials = {'username': 'standard_user', 'password': 'secret_sauce'}
    login_p = LoginPage(page)
    products_p = login_p.do_login(credentials)
    products_p.do_logout()
    expect(login_p.login_button).to_be_visible()
