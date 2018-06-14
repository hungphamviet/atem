from features.pageobjects.admin.details import constants
from features.pageobjects.page import Page


class DashboardDetail(Page):

    def is_main_menu_displayed(self):
        return self.is_element_visible(constants.DASHBOARD['MAIN_MENU'])

    def is_total_orders_widget_displayed(self):
        return self.is_element_visible(constants.DASHBOARD['TOTAL_ORDERS'])

    def is_total_sales_widget_displayed(self):
        return self.is_element_visible(constants.DASHBOARD['TOTAL_SALES'])

    def is_total_customers_widget_displayed(self):
        return self.is_element_visible(constants.DASHBOARD['TOTAL_CUSTOMERS'])

    def is_people_online_widget_displayed(self):
        return self.is_element_visible(constants.DASHBOARD['PEOPLE ONLINE'])

    def click_user_profile(self):
        locator = constants.DASHBOARD['USER_PROFILE_ICON']
        self.click_element(locator)

    def click_your_profile_menu_item(self):
        locator = constants.DASHBOARD['MENU_ITEM_YOUR_PROFILE']
        self.click_element(locator)

    def click_view_action(self, index):
        locator = constants.DASHBOARD['ORDER_TABLE']['VIEW_ACTION']
        locator = (locator[0], locator[1].format(index=index))
        self.click_element(locator)

