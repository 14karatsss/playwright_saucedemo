class CheckoutPage:

    def __init__(self, page):
        self.page = page
        self._first_name = page.locator("#first-name")
        self._second_name = page.locator("#last-name")
        self._zip_code = page.locator("#postal-code")
        self._continue_btn = page.locator("#continue")
        self._finish_btn = page.locator("#finish")
        self._confirm_msg = page.locator("#checkout_complete_container > h2")

    def enter_first_name(self, f_name):
        self._first_name.fill(f_name)
        return self

    def enter_last_name(self, l_name):
        self._second_name.fill(l_name)
        return self

    def enter_zip(self, zip_code):
        self._zip_code.fill(zip_code)
        return self

    def enter_checkout_details(self, f_name, l_name, zip_code):
        self.enter_first_name(f_name) \
            .enter_last_name(l_name). \
            enter_zip(zip_code)
        return self

    def click_continue(self):
        self._continue_btn.click()
        return self

    def click_finish_btn(self):
        self._finish_btn.click()
        return self

    def confirm_form_and_continue(self, f_name, l_name, zip_code):
        self.enter_checkout_details(f_name, l_name, zip_code)
        self.click_continue()
        self.click_finish_btn()

    #@property
    def get_confirm_message(self):
        return self._confirm_msg
