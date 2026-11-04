from behave import when, then

@when('the user enters "{first_name}" as the first name')
def steps_impl(context,first_name):
    context.checkout_page.set_checkout_first_name(first_name)

@when('the user enters "{last_name}" as the last name')
def steps_impl(context,last_name):
    context.checkout_page.set_checkout_last_name(last_name)

@when('the user enters "{postal_code}" as the zip/postal code')
def steps_impl(context,postal_code):
    context.checkout_page.set_checkout_postal_code(postal_code)

@when('the user clicks to continue button')
def steps_impl(context):
    context.checkout_page.click_checkout_continue()

@then('the sum of the displayed product prices is equal to the total calculated at checkout')
def steps_impl(context):
    context.checkout_page.verify_total_checkout_items_price()