@admin @open-cart @dashboard
Feature: Dashboard visibility
  As the admin
  I want to be able to access to Dashboard page
  So that I should see and manage system information from Dashboard interface

  @dashboard-1000
  Scenario: Login to the Dashboard
    Given the user is in Admin page
    When the user logs in as "Admin User"
    Then the user should be redirected to the "Dashboard" page
    And the main menu should display in the Dashboard
    And all widgets should display in the Dashboard

  @dashboard-1005
  Scenario: View User Profile information
    Given the user is in Admin page
    When the user logs in as "Admin User"
    And the user clicks to Your Profile menu item
    Then the header of User Profile page should display as "My Profile"

  @dashboard-1010
  Scenario: View information of an Order
    Given the user is in Admin page
    When the user logs in as "Admin User"
    And the user clicks View Action of an order
    Then the user should be redirected to the "Order Information" page
