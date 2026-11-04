from playwright.sync_api import Page, expect
from pages.base_page import BasePage


PRODUCTS_PAGE_URL = "https://www.saucedemo.com/inventory.html"


class ProductsPage(BasePage):

    ITEM_PRICE = ".inventory_item_price"
    ITEM_NAME = ".inventory_item_name"
    DROPDOWN_SORT = ".product_sort_container"

    def __init__(self, page):
        super().__init__(page)


    def select_dropdown(self, text:str):
        self.select_item_by_text(self.DROPDOWN_SORT, text)


    def verify_product_price_sorted_low_to_high(self):
        elements = self.page.locator(self.ITEM_PRICE)
        elements.first.wait_for(state="visible")
        total_elements = elements.all()

        list_elements_price = []

        for item in total_elements:
            price = item.inner_text().replace("$","").strip()
            list_elements_price.append(float(price))

        expected = sorted(list_elements_price)

        assert list_elements_price == expected, f"Product price not sorted: {list_elements_price}"



    def verify_product_name_sorted_z_to_a(self):
        elements = self.page.locator(self.ITEM_NAME)
        elements.first.wait_for(state="visible")
        total_elements = elements.all()

        list_elements_name = []

        for item in total_elements:
            name = item.inner_text()
            list_elements_name.append(name)

        expected = sorted(list_elements_name, reverse=True)
        assert list_elements_name == expected, f"Product price not sorted: {list_elements_name}"





