from playwright.sync_api import Page, expect


class BasePage:

    def __init__(self, page:Page):
        self.page = page


    # ---------- Actions ----------
    def type(self, locator:str, text:str):
        self.page.locator(locator).fill(text)


    def click(self,locator):
        self.page.locator(locator).click()


    def select_item_by_text(self, selector:str, text:str):
        self.page.locator(selector).select_option(label=text)


    # ---------Getters-------------
    def get_text(self, locator:str):
        return self.page.locator(locator).inner_text()


    # ---------- URL ----------------
    def verify_current_url(self, expected_url):
        expect(self.page).to_have_url(expected_url)


