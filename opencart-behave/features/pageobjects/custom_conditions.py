import re
from urllib.parse import urlparse
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.support.select import By


class NumberOfWindowHandles(object):
    def __init__(self, count):
        self.count = count

    def __call__(self, driver):
        return len(driver.window_handles) == self.count


class UrlFragmentToBeMatched(object):
    """ An expectation for checking if the given regular expression is matched in the current URL fragment.
    """

    def __init__(self, regex):
        self.regex = regex

    def __call__(self, driver):
        regex_object = re.compile(self.regex)
        current_url = urlparse(driver.current_url)
        match_object = re.match(regex_object, current_url.fragment)
        if bool(match_object):
            return match_object
        return False


class UrlToBeMatched(object):
    """ An expectation for checking if the given regular expression is matched in the current URL.
    """

    def __init__(self, regex):
        self.regex = regex

    def __call__(self, driver):
        regex_object = re.compile(self.regex)
        match_object = re.match(regex_object, driver.current_url)
        if bool(match_object):
            return driver.current_url
        return False


def get_url_element(driver, element):
        current_url = urlparse(driver.current_url)
        if element == 'protocol':
            return current_url.scheme  # E.g. http, https ...
        if element == 'hostname':
            return current_url.hostname  # E.g. dev.unifiedsocial.com ...
        if element == 'port':
            return current_url.port  # E.g. 8080, 9000 ...
        if element == 'path':
            return current_url.path  # E.g. /app/onboarding
        if element == 'query':
            return current_url.query  # E.g.
        if element == 'fragment':
            return current_url.fragment  # E.g. /facebook/


class UrlElementToEqual(object):
    def __init__(self, element, expected):
        self.part = element
        self.expected = expected

    def __call__(self, driver):
        current = get_url_element(driver, self.part)
        return current == self.expected


class UrlNetlocToContain(object):
    def __init__(self, string):
        self.string = string

    def __call__(self, driver):
        return self.string in urlparse(driver.current_url).netloc


class ElementAttributeToBe(object):
    def __init__(self, tuple_selector, attribute, value):
        self.by = tuple_selector[0]
        self.locator = tuple_selector[1]
        self.attribute = attribute
        self.value = value

    def __call__(self, driver):
        web_element = driver.find_element(self.by, self.locator)
        if web_element.get_attribute(self.attribute) == self.value:
            return web_element
        return False


class AllElementsNotExist(object):
    def __init__(self, tuple_selector):
        self.by = tuple_selector[0]
        self.locator = tuple_selector[1]

    def __call__(self, browser):
        elements = browser.query_selectors(self.by, self.locator)
        return True if len(elements) == 0 else False


class NumberOfElementsToBeMatched(object):
    def __init__(self, tuple_selector, number_of_elements):
        self.by = tuple_selector[0]
        self.locator = tuple_selector[1]
        self.number = number_of_elements

    def __call__(self, browser):
        browser.wait_for_visibility_of_element_located((self.by, self.locator))
        elements = browser.query_selectors(self.by, self.locator)
        return True if len(elements) == self.number else False


class ElementTextToBeMatchedWithStringIgnored(object):
    def __init__(self, locator, text, string_ignored):
        self.locator = locator
        self.text = text
        self.string_ignored = string_ignored

    def __call__(self, driver):
        try:
            element_text = driver.find_element(self.locator[0], self.locator[1]).text
            element_text = str(element_text.encode('ascii', 'ignore').decode('ascii')). \
                replace(self.string_ignored, '')
            return self.text in element_text
        except StaleElementReferenceException:
            return False
