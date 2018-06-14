from features.pageobjects.login import constants as lc
import logging
from behave import *
from hamcrest import *
from features.pageobjects.store_front.home import ShoppingHome
from features.pageobjects.store_front.product_detail import ProductDetail
from features.pageobjects.store_front.product_checkout import ProductCheckout
from features.steps.lib.step_utils import table_to_dictionary
logger = logging.getLogger()


@given('the user is in Shopping page')
def step_visit_shopping_page(context):
    context.browser.get('http://localhost/opencart')


@step('the user selects product named "{product_name}"')
def step_select_product(context, product_name):
    ShoppingHome(context.browser).select_product(product_name)


@step('the user inputs product quantity as "{product_quantity}"')
def step_input_quantity(context, product_quantity):
    ProductDetail(context.browser).input_quantity(product_quantity)


@step('the user adds product to Cart')
def step_add_to_cart(context):
    ProductDetail(context.browser).add_to_cart()


@step('the user adds product to Cart with information below')
def step_add_to_cart(context):
    details = table_to_dictionary(context.table)
    context.execute_steps(u'''
        When the user selects product named "{name}"
        And the user inputs product quantity as "{quantity}"
        And the user adds product to Cart
    '''.format(name=details['name'], quantity=details['quantity']))


@step('the user performs Cart checkout')
def step_checkout_cart(context):
    ShoppingHome(context.browser).checkout()


@step('the user selects checkout as "{option}"')
def step_checkout_as(context, option):
    ProductCheckout(context.browser).select_checkout_option(option.lower())
    ProductCheckout(context.browser).complete_checkout_option()


@step('the user inputs payment details as below')
def step_input_payment_details(context):
    details = table_to_dictionary(context.table)
    ProductCheckout(context.browser).input_payment_firstname(details['firstname'])
    ProductCheckout(context.browser).input_payment_lastname(details['lastname'])
    ProductCheckout(context.browser).input_payment_email(details['email'])
    ProductCheckout(context.browser).input_payment_telephone(details['telephone'])
    ProductCheckout(context.browser).input_payment_address1(details['address1'])
    ProductCheckout(context.browser).input_payment_city(details['city'])
    ProductCheckout(context.browser).input_payment_postcode(details['postcode'])
    ProductCheckout(context.browser).select_payment_region(details['region'])
    ProductCheckout(context.browser).complete_payment_details()


@step('the user completes Delivery method')
def step_complete_delivery_method(context):
    ProductCheckout(context.browser).complete_delivery_method()


@step('the user completes Terms & Condition agreement')
def step_agree_tac(context):
    ProductCheckout(context.browser).select_tnc_agreement()
    ProductCheckout(context.browser).complete_tnc_agreement()


@step('the user confirms Checkout')
def step_confirm_checkout(context):
    ProductCheckout(context.browser).confirm_checkout()


@then('the checkout success content should display as below')
def step_verify_checkout_success_content(context):
    actual_message = ProductCheckout(context.browser).get_checkout_success_content()
    assert_that(actual_message, equal_to(context.text))
