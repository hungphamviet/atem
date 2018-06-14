from features.pageobjects.store_front import constants
from features.pageobjects.page import Page


class ShoppingHome(Page):
    def select_product(self, product_name):
        locator = constants.PRODUCT_HOME["PRODUCT_NAME"]
        locator = (locator[0], locator[1].format(name=product_name))
        self.click_element(locator)

    def checkout(self):
        locator = constants.PRODUCT_HOME["CART"]
        self.click_element(locator)
        locator = constants.PRODUCT_HOME["CHECKOUT"]
        self.click_element(locator)
