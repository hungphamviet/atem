from features.pageobjects.page import Page
from features.pageobjects.login import constants
from features.pageobjects.shared import constants as sc


class RegisterPage(Page):
    def input_temp_password(self, password):
        self.type_text(constants.REGISTER_PAGE['TEMP_PASSWORD'], password)

    def input_email(self, email):
        self.type_text(constants.REGISTER_PAGE['EMAIL'], email)

    def input_password(self, password):
        self.type_text(constants.REGISTER_PAGE['PASSWORD'], password)

    def input_confirm_password(self, confirm_password):
        self.type_text(constants.REGISTER_PAGE['CONFIRM_PASSWORD'], confirm_password)

    def input_first_name(self, first_name):
        self.type_text(constants.REGISTER_PAGE['FIRST_NAME'], first_name)

    def input_last_name(self, last_name):
        self.type_text(constants.REGISTER_PAGE['LAST_NAME'], last_name)

    def get_register_validation_error_lists(self):
        return self.get_text_of_elements(constants.REGISTER_PAGE['ERROR_LIST'])

    def next(self):
        self.click_element(sc.BUTTON['NEXT'])
