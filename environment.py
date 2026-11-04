from browser import Browser
from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def before_scenario(context, scenario):
    context.browser = Browser()
    context.login_page = LoginPage(context.browser.page)
    context.products_page = ProductsPage(context.browser.page)
    context.cart_page = CartPage(context.browser.page)
    context.checkout_page = CheckoutPage(context.browser.page)

    if "products" in scenario.tags or "cart" in scenario.tags:
        context.login_page.open()
        context.login_page.login("standard_user", "secret_sauce")


def after_scenario(context, scenario):
    if hasattr(context, "browser") and context.browser:
        context.browser.close()
        context.browser = None



