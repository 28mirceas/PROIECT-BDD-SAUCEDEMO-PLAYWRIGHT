from playwright.sync_api import Page, expect
from pages.base_page import BasePage


CART_PAGE_URL = "https://www.saucedemo.com/cart.html"


class CartPage(BasePage):
    PRODUCT_ITEM = ".inventory_item"
    CART_LINK = ".shopping_cart_link"
    CART_ITEM = ".cart_item"
    BUTTON_CHECKOUT = "#checkout"

    def __init__(self, page):
        super().__init__(page)


    def add_product_to_cart(self, product_name):
        product_items = self.page.locator(self.PRODUCT_ITEM)
        product_items.first.wait_for(state="visible")
        total_product_items = product_items.all()

        for product_item in total_product_items:
            product_item_name = product_item.inner_text().split('\n', 1)[:1][0]

            if product_item_name == product_name:
                product_name_button = f'//div[text()="{product_name}"]/parent::a/parent::div[@class="inventory_item_label"]/following-sibling::div[@class="pricebar"]//button'
                self.click(product_name_button)


    def click_cart_link(self):
        self.click(self.CART_LINK)


    def click_cart_checkout(self):
        self.click(self.BUTTON_CHECKOUT)


    # ---------Verificari-------------------------

    def verify_cart_item_name(self, expected_cart_item_name):
        cart_items = self.page.locator(self.CART_ITEM)
        cart_items.first.wait_for(state="visible")
        total_cart_items = cart_items.all()

        for cart_item in total_cart_items:
            actual_cart_item_name = cart_item.inner_text().split('\n', 2)[:2][1]

            assert actual_cart_item_name == expected_cart_item_name, (
                f"Expected error: {expected_cart_item_name}, "
                f"but got: {actual_cart_item_name}"
            )