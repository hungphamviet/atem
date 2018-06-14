from features.pageobjects.store_front import constants
from features.pageobjects.page import Page


class ProductCheckout(Page):
    def select_checkout_option(self, option):
        locator = constants.PRODUCT_CHECKOUT["CHECKOUT_OPTION"]
        locator = (locator[0], locator[1].format(value=option))
        self.click_element(locator)

    def complete_checkout_option(self):
        locator = constants.PRODUCT_CHECKOUT["BUTTON_ACCOUNT"]
        self.click_element(locator)

    def input_payment_firstname(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_FIRST_NAME"]
        self.clear_and_type_text(locator, value)

    def input_payment_lastname(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_LAST_NAME"]
        self.clear_and_type_text(locator, value)

    def input_payment_email(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_EMAIL"]
        self.clear_and_type_text(locator, value)

    def input_payment_telephone(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_TELEPHONE"]
        self.clear_and_type_text(locator, value)

    def input_payment_address1(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_ADDRESS_1"]
        self.clear_and_type_text(locator, value)

    def input_payment_city(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_CITY"]
        self.clear_and_type_text(locator, value)

    def input_payment_postcode(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_POSTCODE"]
        self.clear_and_type_text(locator, value)

    def select_payment_region(self, value):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_REGION"]
        self.select_element_by_text(locator, value)

    def complete_payment_details(self):
        locator = constants.PRODUCT_CHECKOUT["BUTTON_GUEST"]
        self.click_element(locator)

    def complete_delivery_method(self):
        locator = constants.PRODUCT_CHECKOUT["BUTTON_SHIPPING_METHOD"]
        self.click_element(locator)

    def select_tnc_agreement(self):
        locator = constants.PRODUCT_CHECKOUT["PAYMENT_METHOD_AGREE"]
        self.click_element(locator)

    def complete_tnc_agreement(self):
        locator = constants.PRODUCT_CHECKOUT["BUTTON_PAYMENT_METHOD"]
        self.click_element(locator)

    def confirm_checkout(self):
        locator = constants.PRODUCT_CHECKOUT["BUTTON_CONFIRM"]
        self.click_element(locator)

    def get_checkout_success_content(self):
        locator = constants.PRODUCT_CHECKOUT["CHECKOUT_SUCCESS_CONTENT"]
        return self.get_element_text(locator)
