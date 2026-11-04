Feature: Cart page functionality

  @cart
  @addToCart
    Scenario: Add Sauce Labs Backpack to the shopping cart
    When the user clicks the Add to cart button for "Sauce Labs Backpack"
    And the user clicks the shopping cart icon
    Then "Sauce Labs Backpack" is displayed


  @cart
  @addTwoProductsToCart
  Scenario: Add two products to the shopping cart
    When the user clicks the Add to cart button for "Sauce Labs Backpack"
    And the user clicks the Add to cart button for "Sauce Labs Fleece Jacket"
    And the user clicks the shopping cart icon
    Then the current URL is "https://www.saucedemo.com/cart.html"



  @cart
  @checkoutFlow
  Scenario: Proceed to checkout from the shopping cart
   When the user clicks the Add to cart button for "Sauce Labs Backpack"
   And the user clicks the shopping cart icon
   And the user clicks the Checkout button
   Then the current URL is "https://www.saucedemo.com/checkout-step-one.html"