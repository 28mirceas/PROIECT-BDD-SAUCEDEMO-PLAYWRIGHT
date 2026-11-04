Feature: Products page functionality

  @products
  @productsPrice
    Scenario: Sort products by price (low to high)
      When the user selects "Price (low to high)" from the sort dropdown
      Then the products are displayed in ascending price order

  @products
  @productsName
    Scenario: Sort products by name (Z to A)
      When the user selects "Name (Z to A)" from the sort dropdown
      Then the products are displayed in descending alphabetical order

