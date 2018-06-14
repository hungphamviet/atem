from features.pageobjects.admin.details import constants
from features.pageobjects.page import Page


class UserProfile(Page):

    def get_header(self):
        return self.get_element_text(constants.USER_PROFILE['HEADER'])
