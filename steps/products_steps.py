from behave import given, when, then


@when('the user selects "{text}" from the sort dropdown')
def step_impl(context, text):
    context.products_page.select_dropdown(text)


@then('the products are displayed in ascending price order')
def step_impl(context):
    context.products_page.verify_product_price_sorted_low_to_high()


@then('the products are displayed in descending alphabetical order')
def step_impl(context):
    context.products_page.verify_product_name_sorted_z_to_a()


