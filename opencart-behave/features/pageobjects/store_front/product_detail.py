from features.pageobjects.store_front import constants
from features.pageobjects.page import Page


class ProductDetail(Page):
    def input_quantity(self, quantity):
        locator = constants.PRODUCT_DETAIL["PRODUCT_QUANTITY"]
        self.clear_and_type_text(locator, value=quantity)

    def add_to_cart(self):
        locator = constants.PRODUCT_DETAIL["ADD_TO_CART"]
        self.click_element(locator)
