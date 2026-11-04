from behave import given, when, then

@given('the user is on the Login page')
def steps_impl(context):
    context.login_page.open()


@when('the user enters "{user_text}" as the username')
def steps_impl(context, user_text):
    context.login_page.set_username(user_text)


@when('the user enters "{pass_text}" as the password')
def steps_impl(context, pass_text):
    context.login_page.set_password(pass_text)


@when('the user clicks the Login button')
def steps_impl(context):
    context.login_page.click_button()


@then('the current URL is "{expected_url}"')
def steps_impl(context, expected_url):
    context.login_page.verify_current_url(expected_url)


@then('the login error "{expected_message}"')
def steps_impl(context, expected_message):
    context.login_page.verify_login_error_message(expected_message)