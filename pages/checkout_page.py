from playwright.sync_api import Page, expect
from pages.base_page import BasePage

class CheckoutPage(BasePage):
    CART_ITEM_PRICE = ".inventory_item_price"
    INPUT_FIRST_NAME = "#first-name"
    INPUT_LAST_NAME = "#last-name"
    INPUT_POSTAL_CODE = "#postal-code"
    BUTTON_CONTINUE = "#continue"
    TOTAL_ITEMS_PRICE = ".summary_subtotal_label"


    def __init__(self, page):
        super().__init__(page)


    def calculate_total_price(self):
        total_cart_items_price = 0
        cart_items_price = self.page.locator(self.CART_ITEM_PRICE)
        cart_items_price.first.wait_for(state="visible")
        cart_items_price = cart_items_price.all()

        for cart_item_price in cart_items_price:
            item_price = float(cart_item_price.inner_text().replace("$", ""))
            total_cart_items_price += item_price
        return total_cart_items_price


    def set_checkout_first_name(self, text):
        self.type(self.INPUT_FIRST_NAME, text)


    def set_checkout_last_name(self, text):
        self.type(self.INPUT_LAST_NAME, text)


    def set_checkout_postal_code(self, text):
        self.type(self.INPUT_POSTAL_CODE, text)


    def click_checkout_continue(self):
        self.click(self.BUTTON_CONTINUE)


    def get_checkout_items_price(self):
        text = self.get_text(self.TOTAL_ITEMS_PRICE)
        price = text.split("$")[1]
        return float(price)


    # ---------Verificari-------------------------

    def verify_total_checkout_items_price(self):
        expected_total_items_price = self.calculate_total_price()
        actual_total_items_price = self.get_checkout_items_price()

        assert actual_total_items_price == expected_total_items_price, (
            f"Expected error: {expected_total_items_price}, "
            f"but got: {actual_total_items_price}"
        )



