@open-cart @store-front
Feature: Shopping functionality
  As the end user
  I want to be able to access to Shopping Cart page
  So that I should see and utilize functionalities of shopping cart system

  @shopping-1000
  Scenario: Checkout a product successfully
    Given the user is in Shopping page
    When the user adds product to Cart with information below
      | key      | value  |
      | name     | iPhone |
      | quantity | 5      |
    And the user performs Cart checkout
    And the user selects checkout as "Guest"
    And the user inputs payment details as below
      | key       | value               |
      | firstname | Hung                |
      | lastname  | Pham                |
      | email     | hungpv@gmail.com    |
      | telephone | 123-456-7890        |
      | address1  | 364 Cong Hoa Street |
      | city      | Ho Chi Minh City    |
      | postcode  | 70000               |
      | region    | Moray               |
    And the user completes Delivery method
    And the user completes Terms & Condition agreement
    And the user confirms Checkout
    Then the user should be redirected to the "Checkout Success" page
    And the checkout success content should display as below
    """
    Your order has been placed!
    Your order has been successfully processed!
    Please direct any questions you have to the store owner.
    Thanks for shopping with us online!
    Continue
    """