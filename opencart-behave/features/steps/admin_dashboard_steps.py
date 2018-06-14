from behave import *
from hamcrest import *
from features.pageobjects.admin.details.dashboard import DashboardDetail
from features.pageobjects.admin.details.user_profile import UserProfile


@then('the main menu should display in the Dashboard')
def step_assert_main_menu_visible(context):
    assert_that(DashboardDetail(context.browser).is_main_menu_displayed(),
                equal_to(True), 'Check Total Orders widget')


@then('all widgets should display in the Dashboard')
def step_assert_widgets_visible(context):
    assert_that(DashboardDetail(context.browser).is_total_orders_widget_displayed(),
                equal_to(True), 'Check Total Orders widget')
    assert_that(DashboardDetail(context.browser).is_total_sales_widget_displayed(),
                equal_to(True), 'Check Total Sales widget')
    assert_that(DashboardDetail(context.browser).is_total_customers_widget_displayed(),
                equal_to(True), 'Check Total Customers widget')
    assert_that(DashboardDetail(context.browser).is_people_online_widget_displayed(),
                equal_to(True), 'Check People Online widget')


@step('the user clicks View Action of an order')
def step_click_view_action(context):
    DashboardDetail(context.browser).click_view_action(index=1)


@step('the user clicks to Your Profile menu item')
def step_click_your_profile_menu_item(context):
    DashboardDetail(context.browser).click_user_profile()
    DashboardDetail(context.browser).click_your_profile_menu_item()


@then('the header of User Profile page should display as "{header}"')
def step_assert_user_profile_header(context, header):
    assert_that(UserProfile(context.browser).get_header(), equal_to(header))
