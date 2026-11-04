from behave import when, then

@when('the user clicks the Add to cart button for "{product_name}"')
def steps_impl(context,product_name):
    context.cart_page.add_product_to_cart(product_name)


@when('the user clicks the shopping cart icon')
def steps_impl(context):
    context.cart_page.click_cart_link()

@when('the user clicks the Checkout button')
def steps_impl(context):
    context.cart_page.click_cart_checkout()


@then('"{item_name}" is displayed')
def steps_impl(context, item_name):
    context.cart_page.verify_cart_item_name(item_name)


@then('only "{item_name}" is displayed')
def steps_impl(context, item_name):
    context.cart_page.verify_cart_item_name(item_name)
