from features.pageobjects.page import Page
from features.pageobjects.login import constants
from features.pageobjects.shared import constants as sc


class LoginPage(Page):
    def input_username(self, username):
        self.clear_and_type_text(constants.LOG_IN['USERNAME_INPUTBOX'], value=username)

    def input_password(self, password):
        self.clear_and_type_text(constants.LOG_IN['PASSWORD_INPUTBOX'], value=password)

    def click_submit(self):
        self.click_element(sc.BUTTON['SUBMIT'])

    def log_out(self):
        self.visit(constants.URL['LOGOUT'])
        self.wait_for_visibility_of_element_located(sc.MESSAGE['SUCCESS'])

    def get_current_message(self):
        message = self.wait_for_visibility_of_element_located(sc.MESSAGE['SUCCESS']).text
        return message

    def get_current_open_success_message(self):
        message = self.wait_for_visibility_of_element_located(sc.MESSAGE['SUCCESS_OPEN']).text
        return message
