import time
import math
from urllib.parse import urlparse
from hamcrest import assert_that, equal_to
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from features.pageobjects import custom_conditions
from selenium.webdriver.support.select import By
from selenium.webdriver.support.wait import WebDriverWait
from conf.env_setup import EnvSetup
from conf import constants as cc
from features.pageobjects.shared import constants as sc
from features.pageobjects.admin.details import constants as adc


class Page(object):
    VERIFIED_PAGE_COUNT_DEFAULT = 3

    def __init__(self, selenium_webdriver):
        self.driver = selenium_webdriver

    def quit(self):
        self.driver.quit()

    def maximize_window(self):
        self.driver.maximize_window()

    def visit(self, location='', timeout=EnvSetup.PAGE_LOAD_TIMEOUT_SECONDS):
        self.driver.get(EnvSetup.SITE + location)

    def navigate(self, url):
        self.driver.get(url)

    def refresh_page(self):
        self.driver.refresh()

    def click_back_button(self):
        # self.driver.navigation().back()
        self.driver.execute_script('window.history.back()')

    def delete_all_cookies(self, url):
        """
        Delete all cookies of the given domain
        :param url: Domain that cookies have been deleted
        :return:
        """
        self.navigate(url)
        self.driver.delete_all_cookies()

    def get_cookie(self, cookie_name):
        return self.driver.get_cookie(cookie_name)

    def find_elements(self, tuple_selector):
        element_list = self.driver.find_elements(*tuple_selector)
        return element_list

    # TODO: Deprecated. Please use the above method find_elements
    def query_selectors(self, by, selector):
        element = self.driver.find_elements(by, selector)
        return element

    # TODO: Deprecated. Please use the above method find_elements
    def query_selectors_css(self, selector):
        return self.query_selectors(By.CSS_SELECTOR, selector)

    # TODO: Deprecated. Please use the above method find_elements
    def query_selectors_xpath(self, selector):
        return self.query_selectors(By.XPATH, selector)

    # TODO: Deprecated. Please use the above method find_elements
    def query_selectors_tag_name(self, tag_name):
        return self.query_selectors(By.TAG_NAME, tag_name)

    # =========================Handle URL=======================
    def get_current_url_path(self):
        current_url = urlparse(self.driver.current_url)
        current_path = current_url.path
        return current_path

    def get_current_url_fragment(self):
        current_url = urlparse(self.driver.current_url)
        current_fragment = current_url.fragment
        return current_fragment

    def get_current_url(self):
        """
        Get the current url complete path by concatenating both path and fragment
        """
        current_url = urlparse(self.driver.current_url)
        # TODO: Dev team is planning to remove the '#' from the URLs, we need to remove it from here when that occurs
        whole_path = current_url.path + "#" + current_url.fragment
        return whole_path

    def get_element_of_current_url(self, part=None):
        """
        Get a part of the current url complete
        :param self:
        :param part: hostname, path, query or all by geturl
        :return:
        """
        current_url = urlparse(self.driver.current_url)
        element_of_url = None
        if part is None:  # Get whole URL
            element_of_url = current_url.geturl()
        elif part == 'protocol':
            element_of_url = current_url.scheme  # E.g. http, https ...
        elif part == 'hostname':
            element_of_url = current_url.hostname  # E.g. dev.unifiedsocial.com ...
        elif part == 'port':
            element_of_url = current_url.port  # E.g. 8080, 9000 ...
        elif part == 'path':
            element_of_url = current_url.path  # E.g. /app/onboarding
        elif part == 'query':
            element_of_url = current_url.query  # E.g.
        elif part == 'fragment':
            element_of_url = current_url.fragment  # E.g. /facebook/
        return element_of_url

    # ==========================wait elements===============================================
    def wait_for_visibility_of_element(self, by, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located((by, selector)))

    def wait_for_visibility_of_element_by_id(self, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return self.wait_for_visibility_of_element(By.ID, selector, timeout)

    def wait_for_visibility_of_element_by_css(self, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return self.wait_for_visibility_of_element(By.CSS_SELECTOR, selector, timeout)

    def wait_for_visibility_of_element_by_xpath(self, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return self.wait_for_visibility_of_element(By.XPATH, selector, timeout)

    def wait_for_text_to_be_present(self, by, selector, text, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element((by, selector), text))

    def wait_for_text_to_change_in_table(self, locator, text, column_number, row_number,
                                         timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        if isinstance(locator, list):
            for element in locator:
                wait.until(EC.text_to_be_present_in_element(
                    (By.XPATH, sc.TABLE['CELL_POSITION'].format(locator.index(element) + 1, column_number)), text)
                )
        else:
            wait.until(EC.text_to_be_present_in_element(
                (By.XPATH, sc.TABLE['CELL_POSITION'].format(row_number, column_number), text)
            ))

    def wait_for_element_to_click(self, by, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable((by, selector)))

    def click_and_type(self, selector, text=None):
        actions = ActionChains(self.driver)
        actions.click(selector)
        if text is not None:
            actions.send_keys(text)
        actions.perform()

    def move_to_element(self, selector):
        wait = WebDriverWait(self.driver, EnvSetup.SELENIUM_TIMEOUT_SECONDS)
        element = wait.until(EC.presence_of_element_located(selector))
        ActionChains(self.driver).move_to_element(element).perform()

    def double_click(self, selector):
        actions = ActionChains(self.driver)
        actions.double_click(selector)
        actions.perform()

    def clear_and_type(self, by, selector, value=None):
        element = self.wait_for_visibility_of_element(by, selector)
        element.click()
        element.clear()
        if value is not None:
            element.send_keys(value)

    def send_key_and_press_tab(self, selector_tuple, value):
        element = self.wait_for_visibility_of_element_located(selector_tuple)
        element.send_keys(value)
        element.send_keys(Keys.TAB)

    def check_displayed(self, by, selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_visibility_of_element(by, selector, timeout)
        except TimeoutException:
            return False
        return True

    def check_element_exist(self, selector):
        try:
            self.driver.find_element(selector[0], selector[1])
        except NoSuchElementException:
            return False
        return True

    def is_attribute_present(self, selector, attribute_name):
        """
        Check if attribute of a element present
        :param self:
        :param attribute_name: name of attribute to get
        :return:
        """
        element = self.wait_for_visibility_of_element_located(selector)
        result = False
        attribute_value = element.get_attribute(attribute_name)
        if attribute_value is not None:
            result = True
        return result

    def get_text(self, by, selector):
        """
        Return text of a element
        :param self:
        :param by:
        :param selector:
        :return:
        """
        element = self.wait_for_visibility_of_element(by, selector)
        return element.text

    def get_column_list(self, list, column_index):
        """
        Get all elements [column_index] of list
        :param self:
        :param list:
        :param column_index:
        :return:
        """
        names_list = []
        for element in list:
            names_list.append(element[column_index])
        return names_list

    # TODO: it will be replaced by get_attribute_of_element
    def get_attribute(self, by, selector, attribute_name):
        """
        Get attribute of a element
        :param self:
        :param by:
        :param selector:
        :param attribute_name:
        :return: the value of a property with the given name
                 If there is no attribute with that name, None is returned.
        """
        element = self.wait_for_visibility_of_element(by, selector)
        element_attribute = element.get_attribute(attribute_name)
        return element_attribute

    def move_to_element(self, tuple_selector, by_script=False):
        element = self.wait_element_exist(tuple_selector)
        if by_script:
            self.driver.execute_script("arguments[0].scrollIntoView(true);", element)
        else:
            actions = ActionChains(self.driver)
            actions.move_to_element(element)
            actions.perform()

    def select_element_by_text(self, selector, value):
        from selenium.webdriver.support.ui import Select
        element = self.wait_for_visibility_of_element_located(selector)
        select = Select(element)
        select.select_by_visible_text(value)

    # ---------------------------------------------------------:
    # -------------- new approach for locator -----------------:
    # selector will be tuple: (By, locator_value)

    # ---- wait method ------------
    def wait_for_url_fragment_to_be_matched(self, regex, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        WebDriverWait(self.driver, timeout).until(custom_conditions.UrlFragmentToBeMatched(regex))

    def wait_for_number_of_window_handles(self, count, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        WebDriverWait(self.driver, timeout).until(custom_conditions.NumberOfWindowHandles(count))

    def wait_element_exist(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(tuple_selector))

    def wait_for_visibility_of_element_located(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.visibility_of_element_located(tuple_selector))

    def wait_for_invisibility_of_element_located(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.invisibility_of_element_located(tuple_selector))

    def wait_for_text_to_be_present_in_element(self, tuple_selector, text, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element(tuple_selector, text))

    def wait_for_element_to_be_clickable(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.element_to_be_clickable(tuple_selector))

    def wait_for_url_to_be_matched_condition(self, regex, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return WebDriverWait(self.driver, timeout).until(custom_conditions.UrlToBeMatched(regex))


    def wait_for_url_element_to_equal(self, element, expectation, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return WebDriverWait(self.driver, timeout).until(custom_conditions.UrlElementToEqual(element, expectation))


    def wait_for_url_netloc_to_contain(self, sub_string, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return WebDriverWait(self.driver, timeout).until(custom_conditions.UrlNetlocToContain(sub_string))

    def wait_for_attribute_element_to_be(self, selector, attribute, value,
                                         timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        return WebDriverWait(self.driver, timeout).until(
            custom_conditions.ElementAttributeToBe(selector, attribute, value))

    def wait_for_text_to_be_present_in_value_of_element(self, tuple_selector, text,
                                                        timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        # TODO: rename to wait_for_text_to_be_present_in_element_value after replacing all
        """
        An expectation for checking if the given text is present in the element's
        """
        wait = WebDriverWait(self.driver, timeout)
        return wait.until(EC.text_to_be_present_in_element_value(tuple_selector, text))

    def wait_for_table_column_to_contain_only(self, column_index, text, table=None,
                                              timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        WebDriverWait(self, timeout).until(custom_conditions.TableColumnToContainOnly(column_index, text, table))

    def wait_for_all_elements_not_exist(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        WebDriverWait(self, timeout).until(custom_conditions.AllElementsNotExist(tuple_selector))

    def wait_for_number_visible_elements_to_be_matched(self, tuple_selector, number_existed_elements,
                                                       timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        WebDriverWait(self, timeout).until(
            custom_conditions.NumberOfElementsToBeMatched(tuple_selector, number_existed_elements))

    def is_text_present_in_element(self, tuple_selector, text, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_text_to_be_present_in_element(tuple_selector, text, timeout)
            return True
        except TimeoutException:
            return False

    def is_text_present_in_value_of_element(self, tuple_selector, text):
        """
        Return result for checking if the given text is present in the element's
        """
        try:
            self.wait_for_text_to_be_present_in_value_of_element(tuple_selector, text)
            return True
        except TimeoutException:
            return False

    def attribute_element_equals(self, selector, attribute, value, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_attribute_element_to_be(selector, attribute, value, timeout)
            return True
        except TimeoutException:
            return False

    # ---- check method ------------
    def is_element_selected(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.is_selected()

    def is_element_visible(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_visibility_of_element_located(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_invisible(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_invisibility_of_element_located(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_exist(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_element_exist(tuple_selector, timeout)
            return True
        except TimeoutException:
            return False

    def is_element_enabled(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.is_enabled()

    def is_element_disable(self, tuple_selector):
        """
        Check whether or not element is disable
        :param tuple_selector:
        :return:True (disable)/False(enable)
        """
        is_disabled = self.get_attribute_of_element(tuple_selector, 'disabled')
        return False if is_disabled is None else True

    def is_url_fragment_matched(self, regex, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_url_fragment_to_be_matched(regex, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def is_url_matched(self, regex, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_url_to_be_matched_condition(regex, timeout=timeout)
            return True
        except TimeoutException:
            return False

    def url_element_equals(self, element, expectation, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        try:
            self.wait_for_url_element_to_equal(element, expectation, timeout=timeout)
            return True
        except TimeoutException:
            return False


    # ---- action method ------------

    def click_and_select_link_text_from_menu_options(self, dropdown_locator, link_text,
                                                     timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS, move_to_element=False,
                                                     move_to_element_by_script=False):
        self.click_element(dropdown_locator, timeout)
        self.click_element((By.LINK_TEXT, link_text), move_to_element=move_to_element,
                           move_to_element_by_script=move_to_element_by_script)


    @classmethod
    def click_element_directly(cls, element):
        element.click()

    def click_element(self, tuple_selector, move_to_element=False, move_to_element_by_script=False,
                      timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS, by_script=False):
        if move_to_element:
            self.move_to_element(tuple_selector)
        if move_to_element_by_script:
            self.move_to_element(tuple_selector, by_script=True)
        element = self.wait_for_element_to_be_clickable(tuple_selector, timeout)
        if by_script:
            self.driver.execute_script("arguments[0].click();", element)
            self.driver.execute_script("return arguments[0].style", element)
        else:
            element.click()

    def click_elements(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        elements = self.query_selectors(tuple_selector[0], tuple_selector[1])
        for element in elements:
            element.click()

    def type_text(self, tuple_selector, value=None, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        if value:
            element.send_keys(value)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    def clear_and_type_text(self, tuple_selector, value=None, tab=None, enter=None):
        element = self.wait_for_visibility_of_element_located(tuple_selector)
        self.click_element(tuple_selector, move_to_element=True)
        element.clear()
        self.wait_for_text_to_be_present(tuple_selector[0], tuple_selector[1], '')
        if value and value != 'None':
            element.send_keys(value)
        if tab:
            element.send_keys(Keys.TAB)
        if enter:
            element.send_keys(Keys.ENTER)

    def click_on_save_btn(self, wait_invisible=True):
        """
        Click on Save button
        :return:
        """
        save_button_selector = (By.ID, sc.BUTTON['SAVE'])
        self.click_element(save_button_selector)
        if wait_invisible:
            self.wait_for_invisibility_of_element_located(save_button_selector)

    # ---- get information method ------------
    def get_element_text(self, tuple_selector, move_to_element=False, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.text

    def get_moved_elements_text(self, tuple_selector, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(tuple_selector))
        result = []
        for e in elements:
            actions = ActionChains(self.driver)
            actions.move_to_element(e)
            actions.perform()
            result.append(e.text)
        return result

    def get_text_of_elements(self, tuple_selector, move_to_element=False, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        wait = WebDriverWait(self.driver, timeout)
        elements = wait.until(EC.presence_of_all_elements_located(tuple_selector))
        if not move_to_element:
            return self.get_text_list(elements)
        text_list = []
        for e in elements:
            ActionChains(self.driver).move_to_element(e).perform()
            text_list.append(str(e.text))
        return text_list

    @staticmethod
    def get_text_list(list_data):
        """
        Get names of a list
        :param list_data:
        :return:
        """
        name_list = []
        for item in list_data:
            name_list.append(item.text)
        return name_list

    def get_attribute_of_element(self, tuple_selector, attribute, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS,
                                 move_to_element=False):
        """
        Get attribute of element
        :param self:
        :param tuple_selector: tuple selector (By.locator, locator_value)
        :param attribute:
        :param timeout:
        :return:
        """
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_element_exist(tuple_selector, timeout)
        return element.get_attribute(attribute)

    def get_attribute_of_elements(self, tuple_selector, attribute, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        """
            Get all attribute of elements
        :param self:
        :param tuple_selector (By.locator, locator_value)
        :param attribute:
        :param timeout:
        :return:
        """
        self.wait_element_exist(tuple_selector, timeout)
        elements = self.query_selectors(tuple_selector[0], tuple_selector[1])
        return [element.get_attribute(attribute) for element in elements]

    def get_value_of_css_property(self, tuple_selector, attribute_name, timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS,
                                  move_to_element=False):
        """
        Get the value of an attribute of selector
        :param self:
        :param type: variable type of return from attribute when get e.g. status, text ...
        :param attribute_name: name of attribute to get
        :return:
        """
        if move_to_element:
            self.move_to_element(tuple_selector)
        element = self.wait_for_visibility_of_element_located(tuple_selector, timeout)
        return element.value_of_css_property(attribute_name)

    # --------------------------------------------------------

    # Merging CommonActions class
    def get_breadcrumbs(self):
        return self.get_element_text(sc.BREADCRUMBS['BREADCRUMBS_CONTENT'])

    def get_h1_header(self):
        return self.get_element_text((By.CSS_SELECTOR, sc.HEADERS['H1_HEADER']))

    def get_h2_header(self):
        return self.get_element_text(sc.HEADERS['H2_HEADER'])

    def get_h3_header(self):
        return self.get_element_text((By.CSS_SELECTOR, sc.HEADERS['H3_HEADER']))

    def get_h4_header(self):
        return self.get_element_text((By.CSS_SELECTOR, sc.HEADERS['H4_HEADER']))

    def is_snapchat_tab_in_header_visible(self):
        return self.is_element_visible(sc.HEADERS['SNAPCHAT_TAB'])

    def is_snapchat_tab_in_header_invisible(self):
        return self.is_element_invisible(sc.HEADERS['SNAPCHAT_TAB'])

    def is_intelligence_tab_in_header_visible(self):
        return self.is_element_visible(sc.HEADERS['INTELLIGENCE_TAB'])

    def is_intelligence_tab_in_header_invisible(self):
        return self.is_element_invisible(sc.HEADERS['INTELLIGENCE_TAB'])

    def is_link_name_visible(self, link_name):
        return self.is_element_visible((By.LINK_TEXT, link_name))

    def is_link_name_invisible(self, link_name):
        return self.is_element_invisible((By.LINK_TEXT, link_name))

    def get_href_of_embedded_link(self):
        embed_link = self.get_attribute_of_element(sc.EMBED_LINK, 'href')
        return str(embed_link).split('=')[-1]

    def get_target_of_embedded_link(self):
        return self.get_attribute_of_element(sc.EMBED_LINK, 'target')

    def is_confirmation_message_closed(self):
        """
        Check whether or not confirmation is closed after user delete
        :param self:
        :return:
        """
        try:
            modal_body_selector = (By.CSS_SELECTOR, sc.MODAL['MODAL_BODY'])
            self.wait_for_invisibility_of_element_located(modal_body_selector)
            return True
        except TimeoutException:
            return False

    def click_all_checkboxes_on_confirmation_message(self, check_box_number):
        """
        Click all checkboxes on confirmation message
        :param self:
        :return:
        """
        locator = sc.MODAL['MODAL_CHECKBOX']
        self.wait_for_visibility_of_element_located(sc.MODAL['WARNING_YES_BTN'])
        if check_box_number:
            self.wait_for_visibility_of_element_located(locator)
            self.wait_for_number_visible_elements_to_be_matched(locator, check_box_number)
        self.click_elements(sc.MODAL['MODAL_CHECKBOX'])

    def click_yes_button_on_confirmation_message(self):
        """
        Click Yes on confirmation message
        :param self:
        :return:
        """
        self.click_element(sc.MODAL['YES_BTN'], move_to_element=True)

    def wait_for_invisibility_element_of_yes_button(self):
        self.wait_for_invisibility_of_element_located(sc.MODAL['YES_BTN'])

    def click_warning_yes_button_on_confirmation_message(self):
        """
        Click Yes on confirmation message of warning model
        :param self:
        :return:
        """
        self.click_element(sc.MODAL['WARNING_YES_BTN'])

    def click_no_to_cancel(self):
        """
        Click No on confirmation message to cancel the deletion of initiative
        :param self:
        :return:
        """
        self.click_element((By.ID, sc.MODAL['NO_BTN']))
        self.wait_for_invisibility_of_element_located((By.ID, sc.MODAL['NO_BTN']))

    def click_confirm_button_in_warning_modal(self):
        """
        Click Confirm button in warning modal
        :param self:
        :return:
        """
        self.click_element(sc.MODAL['WARNING_YES_BTN'])

    def click_warning_no_button_on_confirmation_message(self):
        """
        Click No on confirmation message of warning model
        :param self:
        :return:
        """
        self.click_element((By.ID, sc.MODAL['WARNING_NO_BTN']))

    def is_no_results_found(self):
        """
        Get the value of users filter
        :return:
        """
        return self.is_element_visible(sc.SELECT_OPTION['NO_RESULTS_FOUND'])

    def get_users_dropdown(self):
        """
        Get the value of users filter
        :return:
        """
        return self.get_element_text((By.CSS_SELECTOR, sc.FILTER['USER']['USER_SELECT']))

    def get_brands_dropdown(self):
        """
        Select brand from Brand drop-down
        :param: brand_option
        """
        return self.get_element_text((By.CSS_SELECTOR, sc.FILTER['BRAND']['BRAND_SELECT']))

    def click_brand_dropdown(self):
        """
        Select brand from Brand drop-down
        :param: brand_option
        """
        self.click_element((By.CSS_SELECTOR, sc.FILTER['BRAND']['BRAND_SELECT']))
        self.wait_for_visibility_of_element(By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS'])

    def select_a_brand_from_dropdown(self, brand_option):
        """
        Select brand from Brand drop-down
        :param: brand_option
        """
        brand_selector = (By.CSS_SELECTOR, sc.FILTER['BRAND']['BRAND_SELECT'])
        self.click_and_select_an_option_from_menu_options(brand_selector, brand_option)

    def select_a_publisher_from_dropdown(self, publisher_option):
        """
        Select publisher from Publisher drop-down
        :param: publisher_option
        """
        self.click_and_select_an_option_from_menu_options((sc.RIGHT_TRAY['BODY']['PUBLISHER_SELECT']), publisher_option)

    def get_initiative_dropdown(self):
        """
        Get value of initiative dropdown
        :return:
        """
        return self.get_element_text((By.CSS_SELECTOR, sc.FILTER['INITIATIVE']['INITIATIVE_SELECT']))

    def select_initiative_from_dropdown(self, initiative_name):
        """
        Select initiative from Initiative dropdown
        :param initiative_name:
        :return:
        """
        initiative_dropdown = (By.CSS_SELECTOR, sc.FILTER['INITIATIVE']['INITIATIVE_SELECT'])
        self.click_and_select_an_option_from_menu_options(initiative_dropdown, initiative_name)
        self.wait_for_loaded_spinners()

    def get_entities_from_list_in_all_pages(self, entity, max_page=VERIFIED_PAGE_COUNT_DEFAULT):
        """
        Get all entities from list in table
        :param self:
        :param entity: initiative, brand, user, line item
        :param max_page:
        return:
        """
        total = int(self.get_element_text(sc.PAGING['RECORD_TOTAL']))
        to = int(self.get_element_text((By.CSS_SELECTOR, sc.PAGING['RECORD_TO'])))
        fulled_page = int(math.ceil(float(total) / to))
        # Get list of entities in the first page
        wait_next_btn = True
        if fulled_page == 1:
            wait_next_btn = False
        entity_names = self.get_entities_from_list_in_current_page(entity, wait_disable_next_btn=wait_next_btn)
        if not entity_names or fulled_page == 1:
            return entity_names
        page = 1
        # Get list of entities in the remaining page
        while page < max_page and page != fulled_page:
            self.click_element((By.CSS_SELECTOR, sc.PAGING['NEXT_PAGE_BTN']))
            self.wait_for_full_loaded_page()
            page += 1
            to = int(self.get_element_text((By.CSS_SELECTOR, sc.PAGING['RECORD_TO'])))
            if total == to:
                wait_next_btn = False
            entity_names += self.get_entities_from_list_in_current_page(entity, wait_disable_next_btn=wait_next_btn)
        else:
            return entity_names

    def get_the_value_of_cell_in_table_list(self, row, col):
        """
        Get the value of a cell in table
        :param self:
        :param row:
        :param col:
        :return:
        """
        cell_value = self.wait_for_visibility_of_element_by_xpath(sc.TABLE['CELL_POSITION'].format(row, col))
        return cell_value.text

    def search_entity(self, text):
        """
        Search entities (Line Item...)
        :param self:
        :return:
        """
        self.type_text(sc.SEARCH_BOX, text, enter=True)
        self.wait_for_full_loaded_page()

    def get_search_textbox(self):
        """
        Get the value of search text box
        :return:
        """
        return self.get_attribute_of_element(sc.SEARCH_BOX, 'value')

    def get_placeholder_of_search_textbox(self):
        """
        Get the value of search text box
        :return:
        """
        return self.get_attribute_of_element(sc.SEARCH_BOX, 'placeholder')

    def search_status_entity(self, status, entity):
        """
        Search status of user, company, brand
        :param self:
        :param status:Active/Disabled
        :param entity:user, company, brand
        :return:
        """
        if entity == 'user':
            status_input = sc.FILTER['USER']['USER_STATUS_INPUT']
            toggle_selector = sc.TABLE['COLUMN_NAMES']['TOGGLE_ON_STATUS'].format(2)
        elif entity == 'company':
            status_input = sc.FILTER['COMPANY']['COMPANY_STATUS_INPUT']
            toggle_selector = sc.TABLE['COLUMN_NAMES']['TOGGLE_ON_STATUS'].format(3)
        elif entity == 'custom metric':
            status_input = sc.FILTER['CUSTOM_METRIC']['CUSTOM_METRIC_STATUS_INPUT']
            toggle_selector = sc.TABLE['COLUMN_NAMES']['TOGGLE_ON_STATUS'].format(2)
        else:
            raise NameError(cc.RAISING_ERRORS['UNDEFINED_ENTITY'].format(entity))

        self.type_text(status_input, status, enter=True)

        # Wait until the first item of status is correct
        if status == 'Disabled':
            toggle_selector_by_css = (By.CSS_SELECTOR, toggle_selector)

            self.wait_for_invisibility_of_element_located(toggle_selector_by_css)
        elif status == 'Active':
            self.wait_for_visibility_of_element_by_css(toggle_selector)
        else:
            raise NameError(cc.RAISING_ERRORS['UNDEFINED_STATUS'].format(status))

    def click_on_submit(self, wait_invisible=True):
        """
        Click on submit button
        """
        self.click_element(sc.BUTTON['SUBMIT'])
        if wait_invisible:
            self.wait_for_invisibility_of_element_located(sc.BUTTON['SUBMIT'])

    def switch_to_a_tab(self, value, closed=None):
        """
        Switch to another tab by window handle or name with option to close the current tab when switch.
        :param self:
        :param value: order number of window handle or window name to parameter for switch
        :param closed: Default is None that keep the current tab and switch to another tab.
        :return:
        """
        if closed is not None:
            self.driver.close()
        self.driver.switch_to.window(self.driver.window_handles[int(value)])

    def get_current_url_of_new_tab(self):
        """
        Get current url of tab
        :param self:
        :return:
        """
        unified_logo_img_selector = (By.ID, sc.UNIFIED_LOGO_IMG)
        self.wait_for_invisibility_of_element_located(unified_logo_img_selector)
        return self.driver.current_url

    def wait_for_loaded_spinners(self):
        """
        Wait the loading spinners are disappear
        :param self:
        :return:
        """
        self.wait_for_all_elements_not_exist(sc.LOADING_SPINNER, timeout=EnvSetup.PAGE_LOAD_TIMEOUT_SECONDS)

    def compare_two_lists(self, actual_list, expected_list, base_on_page=True):
        """
        Compare two lists which is sorted already
        :param self:
        :param actual_list:
        :param expected_list:
        :param base_on_page: (1: compare according to length of actual list, 0: vice versa  )
        :return:
        """
        if base_on_page is False:
            assert_that(len(actual_list), equal_to(len(expected_list)))
            for element in expected_list:
                index = expected_list.index(element)
                assert_that(actual_list[index].strip(), equal_to(element.strip()))
                return

        for element in actual_list:
            index = actual_list.index(element)
            assert_that(element.strip(), equal_to(expected_list[index].strip()))

    def click_all_pendo_guide_next_buttons(self):
        """
        Click on pendo guide next button
        :return:
        """
        while self.is_element_visible(sc.BUTTON['PENDO_GUIDE_NEXT'], timeout=EnvSetup.PENDO_TIMEOUT_SECONDS):
            self.click_element(sc.BUTTON['PENDO_GUIDE_NEXT'])

    def click_on_save_and_add_another_btn(self):
        """
        Click on Save & Add Another button
        :return:
        """
        self.click_element(sc.BUTTON['SAVE_AND_ADD'])

    def click_on_close_alert_message(self):
        """
        Click on close alert message button
        :return:
        """
        self.click_element(sc.BUTTON['CLOSE_ALERT_MESSAGE'])
        self.wait_for_invisibility_of_element_located(sc.BUTTON['CLOSE_ALERT_MESSAGE'])

    def click_on_link_name(self, link_name):
        self.move_to_element((By.LINK_TEXT, link_name), True)
        self.click_element((By.LINK_TEXT, link_name))

    def click_company_dropdown(self):
        """
        Click on the company dropdown
        :return:
        """
        self.click_element(sc.FILTER['COMPANY']['COMPANY_SELECT'])

    def get_company_dropdown(self):
        return self.get_element_text(sc.FILTER['COMPANY']['COMPANY_SELECT'])

    def select_company_from_dropdown(self, company_name):
        """
        Select company from company dropdown
        :return:
        """
        self.click_and_select_an_option_from_menu_options(adc.LINE_ITEM_SHARE_SETTINGS['COMPANY_SELECT'], company_name)

    def select_company_from_dropdown_in_line_item_filter(self, company_name):
        """
        Select company from company dropdown in line item filter
        :return:
        """
        self.click_and_select_an_option_from_menu_options(sc.FILTER['COMPANY']['COMPANY_SELECT'], company_name)

    def run_report(self):
        """
        Locate and click on Run Report button
        """
        self.click_element(sc.BUTTON['RUN_REPORT'])
        self.wait_for_visibility_of_element_located(sc.CHART['HIGHCHARTS'])

    def is_highcharts_displayed(self):
        """
        Check if highcharts component is displayed
        :return: is_displayed: True or False
        """
        return self.is_element_visible(sc.CHART['HIGHCHARTS'])

    # ------------------------ METHODS FOR MODAL ------------------------------------------:
    def click_menu_options_dropdown(self, dropdown_locator, text_inside=None,
                                    frame_dropdown_locator=(By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS']),
                                    timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        if text_inside:
            self.wait_for_text_to_be_present_in_element(dropdown_locator, text_inside, timeout)
        time.sleep(2)
        try:
            self.click_element(dropdown_locator, timeout)
            self.wait_for_invisibility_of_element_located(sc.TYPE_TO_SEARCH)
            self.wait_for_visibility_of_element_located(frame_dropdown_locator, timeout)
        except TimeoutException:
            for i in range(1, 2):
                self.click_menu_options_dropdown(dropdown_locator, frame_dropdown_locator, text_inside,
                                                 timeout)

    def click_and_select_an_option_from_menu_options(self, dropdown_locator, option_name, text_inside=None,
                                                     frame_dropdown_locator=(By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS']),
                                                     timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS, inline_success=False):
        self.click_menu_options_dropdown(dropdown_locator, text_inside, frame_dropdown_locator, timeout)
        value_locator = (By.XPATH, sc.MENU['MENU_OPTION_BY_TEXT'].format(option_name))
        self.click_element(value_locator, timeout)
        self.wait_for_invisibility_of_element_located(frame_dropdown_locator, timeout)
        if inline_success:
            self.wait_for_visibility_of_element_located(sc.MENU['INLINE_SUCCESS'])

    def click_and_select_multi_options_from_menu_options(self, dropdown_locator, option_name, text_inside=None,
                                                         frame_dropdown_locator=(
                                                         By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS']),
                                                         timeout=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        """
        Click and select multi options from menu options
        :param dropdown_locator:
        :param option_name:
        :param text_inside:
        :param frame_dropdown_locator:
        :param timeout:
        :return:
        """
        self.click_menu_options_dropdown(dropdown_locator, text_inside, frame_dropdown_locator, timeout)
        value_locator = (By.XPATH, sc.MENU['MENU_OPTION_BY_TEXT'].format(option_name))
        self.click_element(value_locator, timeout)

    def select_an_option_from_menu_options(self, option_name):
        self.wait_for_visibility_of_element(By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS'])
        self.click_element((By.XPATH, sc.MENU['MENU_OPTION_BY_TEXT'].format(option_name)))
        menu_option_selector = (By.CSS_SELECTOR, sc.MENU['MENU_OPTIONS'])
        self.wait_for_invisibility_of_element_located(menu_option_selector)

    def select_an_option_from_list_options(self, option_name):
        selector = (sc.MODAL['OPTION_BY_TEXT'][0],
                    sc.MODAL['OPTION_BY_TEXT'][1].format(option_name))
        self.click_element(selector)

    def get_all_options_from_menu_options(self):
        return self.get_text_list(self.query_selectors(By.CSS_SELECTOR, sc.MENU['OPTIONS_LIST_LOCATOR']))

    def get_all_options_from_ul_drop_down(self, ul_dropdown_locator_class_name):
        selector = sc.UL_DROP_DOWN['OPTIONS']
        selector = (selector[0], selector[1].format(ul_dropdown_locator=ul_dropdown_locator_class_name))
        return self.get_text_of_elements(selector)

    def select_an_option_from_ul_drop_down(self, option):
        selector = sc.UL_DROP_DOWN['SELECT_OPTION_BY_NAME']
        selector = (selector[0], selector[1].format(option=option))
        self.click_element(selector)

    def get_all_options_from_list_options(self):
        return str(self.get_element_text(sc.MODAL['AVAILABLE_OPTIONS'])).split('\n')

    def remove_selected_placement(self, placement):
        selector = (sc.MODAL['REMOVE_SELECTED_OPTION_BY_TEXT'][0],
                    sc.MODAL['REMOVE_SELECTED_OPTION_BY_TEXT'][1].format(placement))
        self.click_element(selector)

    def get_selected_placements(self):
        placements = str(self.get_element_text(sc.MODAL['SELECTED_CONTAINER']).encode('ascii', 'ignore').
                         decode('ascii'))
        return filter(None, placements.split('\n'))

    def get_modal_title_text(self):
        return self.get_text(By.CSS_SELECTOR, sc.MODAL['TITLE'])

    def click_finish_button(self):
        self.click_element(sc.MODAL['FINISH_BTN'])
        self.wait_for_invisibility_of_element_located(sc.MODAL['FINISH_BTN'])

    def click_apply_change_button(self):
        self.click_element(sc.MODAL['APPLY_CHANGE_BTN'])
        self.wait_for_invisibility_of_element_located(sc.MODAL['APPLY_CHANGE_BTN'])

    def click_cancel_button(self):
        self.click_element(sc.BUTTON['CANCEL'])
        self.wait_for_invisibility_of_element_located(sc.BUTTON['CANCEL'])

    def click_cancel_button_in_admin_section(self):
        self.click_element(adc.BUTTONS['CANCEL_IN_ADMIN_SECTION'])
        self.wait_for_invisibility_of_element_located(adc.BUTTONS['CANCEL_IN_ADMIN_SECTION'])

    def click_delete_button(self):
        self.click_element(sc.MODAL['DELETE_BTN'])
        self.wait_for_invisibility_of_element_located(sc.MODAL['DELETE_BTN'])

    def click_next_button(self):
        self.click_element(sc.BUTTON['NEXT'])
        self.wait_for_invisibility_of_element_located(sc.BUTTON['NEXT'])

    def click_close_button(self):
        item_modal_close_btn_locator = (By.ID, sc.MODAL['CLOSE'])
        self.click_element(item_modal_close_btn_locator)
        self.wait_for_invisibility_of_element_located(sc.MODAL['MODAL_DIALOG'])

    def click_footer_button(self, button_name):
        selector = sc.MODAL['FOOTER_BTN']
        button_selector = (selector[0], selector[1].format(button_name=button_name))
        self.click_element(button_selector)
        self.wait_for_loaded_spinners()

    def is_next_button_not_available(self):
        return not self.is_element_enabled(sc.MODAL['NEXT_BTN'])

    # ------------------------END METHODS FOR MODAL ------------------------------------------:

    # ------------------------ METHODS FOR TABLE ------------------------------------------:

    def get_table_rows(self):
        return self.query_selectors_xpath(sc.TABLE['ROW']['ROWS'])

    def get_table_rows_by_table_row_selector(self, table_row_selector=sc.TABLE['ROW']['UNIFIED_TABLE_ROWS']):
        """
        Get rows of table
        :param table_row_selector:
        :return:
        """
        rows = self.query_selectors(table_row_selector[0], table_row_selector[1])
        return rows

    def get_list_rows_at_column(self, column_index, table=sc.TABLE['ROW']['LIST_UNIFIED_TABLE_COLUMNS']):
        """
        Get all rows of a specific column
        :param column_index:
        :param table: table must be xpath format
        :return:
        """
        list_rows = (By.XPATH, table.format(column_index))
        return self.get_text_of_elements(list_rows)

    def get_table_column_names(self, table_locator=sc.TABLE['TABLE_OBJECT'],
                               col_locator=(By.XPATH, sc.TABLE['COLUMN_NAME_TEXT']),
                               time_out=EnvSetup.SELENIUM_TIMEOUT_SECONDS):
        """
        Get the columns names from table
        :param table_locator: locator for table to get all columns
        :param time_out: limit time to get column names before raising error
        :return: list of columns names texts
        """
        count_loop = 0
        interval_wait = 5
        self.wait_for_visibility_of_element_located(table_locator)
        while True:
            try:
                return self.get_moved_elements_text(col_locator)

            except StaleElementReferenceException:
                time.sleep(interval_wait)
                count_loop += 1
                if (interval_wait * count_loop) > time_out:
                    raise TimeoutException

    def get_dict_of_values_in_table_for_all_rows(self, list_column_name, index_key=0, full_column=False):
        """
        Get all values of table, return to a dict with key is the values of the first column (default)
        :param list_column_name:
        :return:
        TODO: Hung Pham will do refactor this method later
        """
        # Get all rows
        total_records = self.get_record_total_from_list_in_table()
        value_of_key = list_column_name[index_key]
        table_dict = dict()
        number_column = len(list_column_name) - 1
        if full_column:
            number_column += 1
        for row in range(total_records):
            ui_temp_dict = dict()
            for col in range(number_column):
                ui_temp_dict[list_column_name[col]] = self.get_the_value_of_cell_in_table_list(row + 1, col + 1)
            table_dict[ui_temp_dict[value_of_key]] = ui_temp_dict.copy()
        return table_dict

    # ------------------------END METHODS FOR TABLE ------------------------------------------:

    def is_empty_state_image_dislayed(self):
        return self.is_element_visible(sc.EMPTY_STATE['EMPTY_IMAGE'])

    def get_empty_state_message(self):
        return self.get_element_text(sc.EMPTY_STATE['EMPTY_MESSAGE'])

    def get_uprc_empty_state_message(self):
        self.move_to_element(sc.EMPTY_STATE['UPRC_EMPTY_MESSAGE'])
        return self.get_element_text(sc.EMPTY_STATE['UPRC_EMPTY_MESSAGE'])

    def get_empty_state_button_text(self):
        return self.get_element_text(sc.EMPTY_STATE['BUTTON'])

    def click_button_in_empty_state_page(self):
        self.click_element(sc.EMPTY_STATE['BUTTON'])

    # ---------------------- MESSAGE --------------------------------------------------------:
    def get_confirmation_message(self):
        """
        Get confirmation message
        :param self:
        :return:
        """
        confirmation_message = self.wait_for_visibility_of_element_by_css(sc.MODAL['MODAL_BODY'])
        return confirmation_message.text

    def get_success_message(self):
        return self.get_element_text(sc.MESSAGE['SUCCESS'])

    def get_warning_message(self):
        """
        Get warning message
        :return:
        """
        return self.get_element_text(sc.MESSAGE['WARNING'])

    def get_error_message_exclude_close_button(self):
        return self.get_element_text(sc.MESSAGE['DANGER_EXCLUDE_CLOSE_BTN'])

    def get_error_message(self):
        """
        Get error message
        :return:
        """
        return self.get_element_text(sc.MESSAGE['DANGER'])

    def is_link_text_in_table(self, row, column, name):
        locator_type = sc.TABLE['ROW']['LINK_TEXT_CELL'][0]
        locator_value = sc.TABLE['ROW']['LINK_TEXT_CELL'][1].format(
            row=row, column=column, text=name)
        return self.is_element_visible((locator_type, locator_value))

    def is_table_cell_matched(self, column_index, text):
        self.wait_for_visibility_of_element(By.XPATH, sc.TABLE['ROW']['LIST_COLUMNS'].format(column_index))
        cells = self.query_selectors_xpath(sc.TABLE['ROW']['LIST_COLUMNS'].format(column_index))
        for cell in cells:
            try:
                if text not in cell.text:
                    return False
            except StaleElementReferenceException:
                pass
        return True

    def is_toggle_button_on(self, toggle_locator):
        return self.attribute_element_equals(toggle_locator, 'checked', 'true')

    def is_toggle_button_off(self, toggle_locator):
        return self.attribute_element_equals(toggle_locator, 'checked', None)

    def is_tab_activating(self, tab_locator):
        return self.attribute_element_equals(tab_locator, 'class', 'btn btn-default active')

    def get_pseudo_selector(self, locator, style, prop):
        element = self.wait_element_exist(locator)
        script = "return window.getComputedStyle(arguments[0],'{style}').getPropertyValue('{property}')".format(
            style=style, property=prop)
        return self.driver.execute_script(script, element)

    def click_element_at_point(self, pixel_x, pixel_y):
        """
        Click element at point(x,y)
        :param pixel_x:
        :param pixel_y:
        :return:
        """
        script = 'el = document.elementFromPoint({pixel_x}, {pixel_y}); el.click();'.format(pixel_x=pixel_x, pixel_y=pixel_y)
        self.driver.execute_script(script)

    def execute_javascript(self, script=''):
        return self.driver.execute_script(script)
