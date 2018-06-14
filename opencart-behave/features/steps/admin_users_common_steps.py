import json
from features.pageobjects.login.login import LoginPage
import logging
from urllib.parse import urlparse
from behave import *
from hamcrest import *
from conf.env_setup import EnvSetup
from conf import constants as cc
from features.pageobjects.shared import constants as sc
from features.pageobjects.page import Page
logger = logging.getLogger()


@given('the user is in Admin page')
def step_visit_login_page(context):
    context.browser.get('http://localhost/opencart/admin/')


@step('the user logs in as "{role}"')
def step_login_successfully(context, role):
    """
    Execute and store log-in session
    """
    json_data = open('./conf/users.json')
    user_data = json.load(json_data)

    username = user_data[role]['username']
    password = user_data[role]['password']
    context.execute_steps(u'''
        Given the user input username "{username}"
        And the user input password "{password}"
        And the user click Submit button at Login page
    '''.format(username=username, password=password))


@step('the user input username "{username}"')
def step_input_user_name(context, username):
    LoginPage(context.browser).input_username(username)


@step('the user input password "{password}"')
def step_input_password(context, password):
    LoginPage(context.browser).input_password(password)


@step('the user click Submit button at Login page')
def step_click_submit(context):
    LoginPage(context.browser).click_submit()


@then('I am still in the "{page}" page')
@then('I am redirected to the "{page}" page')
@then('the user should be redirected to the "{page}" page')
def step_assert_redirect_to_a_page(context, page):
    if page == 'Dashboard':
        path =sc.URL_FRAGMENT['DASHBOARD']
        expected_url = urlparse(EnvSetup.SITE + path)
        assert_that(Page(context.browser).get_current_url_path(), equal_to(expected_url.path))

    elif page == 'Order Information':
        path =sc.URL_FRAGMENT['ORDER_INFO']
        expected_url = urlparse(EnvSetup.SITE + path)
        assert_that(Page(context.browser).get_current_url_path(), equal_to(expected_url.path))

    elif page == 'Checkout Success':
        assert_that(Page(context.browser).url_element_equals('query', 'route=checkout/success'), equal_to(True))
    else:
        raise NameError(cc.RAISING_ERRORS['UNDEFINED_PAGE'].format(page))
