from playwright.sync_api import expect
from pages.base_page import BasePage

LOGIN_PAGE_URL = "https://www.saucedemo.com"

class LoginPage(BasePage):
    INPUT_USERNAME = "#user-name"
    INPUT_PASSWORD = "#password"
    BUTTON_LOGIN = "#login-button"
    ERROR_LOGIN_MESSAGE = 'h3[data-test="error"]'

    def __init__(self, page):
        super().__init__(page)

    def open(self):
        self.page.goto(LOGIN_PAGE_URL)

    def set_username(self, text:str):
        self.type(self.INPUT_USERNAME, text)

    def set_password(self, text:str):
        self.type(self.INPUT_PASSWORD, text)

    def click_button(self):
        self.click(self.BUTTON_LOGIN)

    def get_login_error_message_text(self):
        return self.get_text(self.ERROR_LOGIN_MESSAGE)
    

    # ---------Verificari-------------------------

    def verify_login_error_message(self, expected_message):
        expect(self.page.locator(self.ERROR_LOGIN_MESSAGE)).to_have_text(expected_message)


    def login(self, username, password):
        self.set_username(username)
        self.set_password(password)
        self.click_button()
        self.verify_current_url("https://www.saucedemo.com/inventory.html")


