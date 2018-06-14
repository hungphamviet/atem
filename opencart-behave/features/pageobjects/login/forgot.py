from features.pageobjects.page import Page
from features.pageobjects.login import constants
from features.pageobjects.shared import constants as sc
from conf import constants as cc


class ForgotPage(Page):
    def input_email(self, email):
        self.send_key_and_press_tab(constants.FORGOT_PAGE['EMAIL_INPUTBOX'], email)

    def submit(self):
        self.click_element(sc.BUTTON['SUBMIT'])
        self.wait_for_text_to_be_present_in_element(sc.MESSAGE['SUCCESS_OPEN'], cc.RESET_PASSWORD_MESSAGE)

    def next(self):
        self.click_element(sc.BUTTON['NEXT'])
        self.wait_for_text_to_be_present_in_element(sc.MESSAGE['SUCCESS'], cc.RESET_PASSWORD_SUCCESS_MESSAGE)
