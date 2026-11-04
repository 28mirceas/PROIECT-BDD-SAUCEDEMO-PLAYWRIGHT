Feature: Checkout page functionality

  @cart
  @totalPrice
  Scenario: Verify total price of the cart products
    When the user clicks the Add to cart button for "Sauce Labs Backpack"
    And the user clicks the Add to cart button for "Sauce Labs Fleece Jacket"
    And the user clicks the shopping cart icon
    And the user clicks the Checkout button
    And the user enters "John" as the first name
    And the user enters "Doe" as the last name
    And the user enters "01234" as the zip/postal code
    And the user clicks to continue button
    Then the current URL is "https://www.saucedemo.com/checkout-step-two.html"
    And the sum of the displayed product prices is equal to the total calculated at checkout