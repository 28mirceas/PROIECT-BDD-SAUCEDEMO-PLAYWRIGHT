Feature: Login page functionality

  Background: Login page is open
    Given the user is on the Login page


  @login
  Scenario: Successful login with valid credentials
    When the user enters "standard_user" as the username
    And the user enters "secret_sauce" as the password
    And the user clicks the Login button
    Then the current URL is "https://www.saucedemo.com/inventory.html"


  @negativeLogin
  Scenario: Login fails for a locked out user
    When the user enters "locked_out_user" as the username
    When the user enters "secret_sauce" as the password
    When the user clicks the Login button
    Then the current URL is "https://www.saucedemo.com/"
    And the login error "Epic sadface: Sorry, this user has been locked out."




