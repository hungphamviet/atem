__author__ = 'hungpv'

from hamcrest.core.base_matcher import BaseMatcher

class FilteredBy(BaseMatcher):
    def __init__(self, filtered_str):
        self.filtered_str = filtered_str

    def _matches(self, str_list):
        for item in str_list:
            if self.filtered_str.lower() not in item.lower():
                return False
        return True

    def describe_to(self, description):
        description.append_text('the list contains items filtered by "{}"'.format(self.filtered_str))

def filtered_by(filtered_str):
    return FilteredBy(filtered_str)
