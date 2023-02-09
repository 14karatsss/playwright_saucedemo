from automationnemo.src.pages.CartPage import CartPage


class ProductListPage:

    def __init__(self, page):
        self.page = page
        self._product_header = page.locator("#header_container > div.header_secondary_container > span")
        self._burger_menu = page.locator("button#react-burger-menu-btn")
        self._logout_btn = page.locator("#logout_sidebar_link")
        self._add_to_cart_btn = page.locator("//div[text()='Sauce Labs Bike Light']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")
        self._cart_icon = page.locator("#shopping_cart_container > a")

    @property
    def product_header(self):
        """It returns locator or selector for product header text"""
        return self._product_header

    def click_burger_menu_btn(self):
        """This will click on Burger menu icon from header"""
        self._burger_menu.click()

    def click_logout(self):
        """This will click on logout"""
        self._logout_btn.click()

    def do_logout(self):
        """Logout from the sauce demo"""
        self.click_burger_menu_btn()
        self.click_logout()

    def get_add_or_remove_prod_form_to_cart_locator(self, product):
        """This will return locator of Add to cart button or Remove button"""
        return self.page.locator(f"//div[text()='{product}']/ancestor::div[@class='inventory_item_label']/following-sibling::div//button")

    def click_add_to_cart_or_remove(self, product):
        self.get_add_or_remove_prod_form_to_cart_locator(product).click()
        return self

    def click_cart_icon(self):
        self._cart_icon.click()
        return CartPage(self.page)
