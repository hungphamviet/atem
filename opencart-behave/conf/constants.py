from conf.env_setup import EnvSetup
from urllib.parse import urlparse

"""
Constants file for fixed values that are referred from selector or assert.
"""

#   +-------------------------------------------------------------------+
#   | Constant Value of default value of selector or from Initialize DB |
#   +-------------------------------------------------------------------+

INIT_BRAND_NAME = "Xbox"
DEFAULT_PASSWORD = "Unified@123"
INIT_CLIENT_COMPANY_NAME = "Anheuser-Busch InBev"
INIT_AGENCY_COMPANY_NAME = '22squared'
INIT_TIME_ZONE = '(GMT-05:00) America/New York'
INIT_CURRENCY = 'USD - United States dollar'

ACTION_LIST = ['delete', 'disable', 're-activate']

TOGGLE_STATUS = {
    'on': ['active', 're-active'],
    'off': ['delete', 'disable'],
    'muted': ['muted'],
    'unmuted': ['unmuted']
}

REPORT_DISPLAY_MODE_OPTIONS = ['Combination', 'Title', 'Name', 'Image', 'Body', 'CTA', 'Link', 'Object URL',
                               'Source Link']
REPORT_DISPLAY_OPTIONS = ['Details', 'Performance', 'Optimization']

PREDEFINED_DATE_RANGE = {'Lifetime': {'start_date_delta': 'N/A', 'end_date_delta': 'N/A'},
                         'Today': {'start_date_delta': 0, 'end_date_delta': 0},
                         'Yesterday': {'start_date_delta': 1, 'end_date_delta': 1},
                         'Last 3 Days': {'start_date_delta': 3, 'end_date_delta': 1},
                         'Last 7 Days': {'start_date_delta': 7, 'end_date_delta': 1},
                         'Last 14 Days': {'start_date_delta': 14, 'end_date_delta': 1},
                         'Last 30 Days': {'start_date_delta': 30, 'end_date_delta': 1},
                         'Last Month': {'start_date_delta': 31, 'end_date_delta': 1},
                         'This Month': {'start_date_delta': 1, 'end_date_delta': 30}
                         }

PREDEFINED_FEATURE_VALUES = {
    'CREATED_INITIATIVE_OBJECT': 'Created Initiative Object',
    'STATUS_ENABLED': 'Enabled',
    'STATUS_DISABLED': 'Disabled'
}

#   +---------------------+
#   | Login page messages |
#   +---------------------+

RESET_PASSWORD_MESSAGE = 'A security code has been sent to the email address provided. Please follow email instructions.'
RESET_PASSWORD_SUCCESS_MESSAGE = 'Password Reset! Please login.'
REGISTRATION_CONFIRM_MESSAGE = 'Registration Complete! Please login.'

#   +-----------------------+
#   | Empty State messages  |
#   +-----------------------+

EMPTY_STATE_MESSAGE_NO_INITIATIVE = 'We could not find any initiatives.'
EMPTY_STATE_MESSAGE_NO_LINE_ITEM = 'We could not find any line items.'
EMPTY_STATE_MESSAGE_NO_LINE_ITEM_IN_INITIATIVE_DETAIL = 'You have no Line Items. To manage investment in the Unified Platform, create line items and sync publisher campaigns.'
EMPTY_STATE_MESSAGE_NO_CAMPAIGN = 'This Line Item needs Campaigns.'
EMPTY_STATE_BUTTON_TEXT_CREATE_INITIATIVE = 'Create Initiative'
EMPTY_STATE_BUTTON_TEXT_CREATE_LINE_ITEM = 'Create Line Item'
EMPTY_STATE_BUTTON_TEXT_SYNC_CAMPAIGNS = 'Sync Campaigns'


#   +----------------+
#   | Raise message  |
#   +----------------+

RAISING_ERRORS = {
    'UNDEFINED_PAGE': 'Page "{}" is not defined',
    'UNDEFINED_ENTITY': 'Entity "{}" is not defined',
    'EMPTY_ENTITY': 'Entity "{}" is empty',
    'UNDEFINED_USER_TYPE': 'User type "{}" is not defined',
    'UNDEFINED_COMPANY_TYPE': 'Company type "{}" is not defined',
    'UNDEFINED_BRAND': 'Brand "{}" is not defined',
    'UNDEFINED_STATUS': 'Status "{}" is not defined',
    'UNDEFINED_PROFILE_STATUS': 'Profile Status "{}" is not defined',
    'UNDEFINED_INITIATIVE': 'Initiative "{}" is not defined',
    'UNDEFINED_NAME': 'Name "{}" is not defined',
    'UNDEFINED_PUBLISHER_VIEW': 'View "{view}" is not defined in {publisher}',
    'UNDEFINED_PUBLISHER_TAB': 'Tab "{tab}" is not defined in {publisher}',
    'UNDEFINED_ACTION': 'Action "{}" is not defined',
    'UNDEFINED_STATE': 'State "{}" is not defined',
    'UNDEFINED_LOCATOR': 'Locator "{}" is not defined',
    'UNDEFINED_ATTRIBUTE': 'Attribute "{}" does not exist',
    'UNDEFINED_PUBLISHER': 'Publisher "{}" does not exist',
    'UNDEFINED_PREDEFINED_DATE_RANGE': 'Date range "{}" does not exist',
    'UNDEFINED_TAB': 'Tab {} is not defined',
    'UNDEFINED_METRIC': 'Metric {} is not defined',
    'INVALID_BRAND': 'Brand "{}" must be empty',
    'REQUIRED_DATA_TABLE': 'Data table must be input',
    'SYNCED_CAMPAIGN_DISPLAYING': 'The synced campaign "{}" should not be displayed',
    'INVALID_VIEW_OPTION': 'view option {} is not defined',
    'REQUIRED_FIELDS': 'Required information: "{}"',
    'TIME_OUT': 'Timeout. Page is not loaded',
    'EMAIL_TIME_OUT': 'Timeout. Email not found',
    'UNRETRIEVED_VALUE': 'Cannot get value of {} field',
    'NOT_MATCHED_VALUE': 'Value of {} field is not matched',
}

#   +------------------------+
#   | Publisher Information  |
#   +------------------------+

PUBLISHER = {
    'FACEBOOK': {
        'PAGE': 'Captain KoKo'
    },
    'INSTAGRAM': {
        'PAGE': 'Captain KoKo'
    }
}

#   +------------------+
#   | Currencies List  |
#   +------------------+

CURRENCIES_LIST = {
    'AED': 'United Arab Emirates dirham',
    'ARS': 'Argentine peso',
    'AUD': 'Australian dollar',
    'BOB': 'Boliviano',
    'BRL': 'Brazilian real',
    'CAD': 'Canadian dollar',
    'CHF': 'Swiss franc',
    'CLP': 'Chilean peso',
    'CNY': 'Chinese yuan',
    'COP': 'Colombian peso',
    'CRC': 'Costa Rican colon',
    'CZK': 'Czech koruna',
    'DKK': 'Danish krone',
    'EUR': 'Euro',
    'GBP': 'Pound sterling',
    'GTQ': 'Guatemalan quetzal',
    'HKD': 'Hong Kong dollar',
    'HNL': 'Honduran lempira',
    'HUF': 'Hungarian forint',
    'IDR': 'Indonesian rupiah',
    'ILS': 'Israeli new shekel',
    'INR': 'Indian rupee',
    'ISK': 'Icelandic króna',
    'JPY': 'Japanese yen',
    'KRW': 'South Korean won',
    'MOP': 'Macanese pataca',
    'MXN': 'Mexican peso',
    'MYR': 'Malaysian ringgit',
    'NIO': 'Nicaraguan córdoba',
    'NOK': 'Norwegian krone',
    'NZD': 'New Zealand dollar',
    'PEN': 'Peruvian nuevo sol',
    'PHP': 'Philippine peso',
    'PLN': 'Polish złoty',
    'PYG': 'Paraguayan guaraní',
    'QAR': 'Qatari riyal',
    'RON': 'Romanian new leu',
    'RUB': 'Russian rouble',
    'SAR': 'Saudi riyal',
    'SEK': 'Swedish krona',
    'SGD': 'Singapore dollar',
    'THB': 'Thai baht',
    'TRY': 'Turkish lira',
    'TWD': 'New Taiwan dollar',
    'USD': 'United States dollar',
    'UYU': 'Uruguayan peso',
    'VEF': 'Venezuelan bolívar fuerte',
    'VND': 'Vietnamese dong',
    'ZAR': 'South African rand'
}

#   +-----------------------+
#   | Calendar Date Picker  |
#   +-----------------------+

CALENDAR_DATE_PICKER = {
    # Value is defined for scenario mapping to which date number is select on calendar picker
    'TODAY': 'Today',
    'TOMORROW': 'Next day'
}

#   +------------+
#   | URL PAGES  |
#   +------------+

URL = {
    'HOME_PAGE': '/',
    'ONBOARDING_PAGE': '/app/onboarding',
    'LIST_PAGES': {
        'USER_PROFILE_SETTINGS_PAGE': '/app/profile/#/profile/{user_id}/settings',
        'ADV_INITIATIVE_LIST_PAGE': '/app/advertising/#/dashboard/initiatives',
        'ADV_CAMPAIGNS_LIST_PAGE': '/app/advertising/#dashboard-new/campaigns',
        'PACING_DASHBOARD_PAGE': '/app/advertising/#/pacing-dashboard',
        'LINE_ITEM_LIST_DETAIL_VIEW_PAGE': '/app/advertising/#/dashboard/lineitems/details',
        'ADMIN_INITIATIVE_LIST_PAGE': '/app/admin/#/list/initiatives',
        'USER_LIST_PAGE': '/app/admin/#/list/users',
        'USER_BRAND_LIMITATIONS_PAGE': '/app/admin/#/details/users/{email}/BrandLimitations',
        'BRAND_LIST_PAGE': '/app/admin/#/list/brands',
        'COMPANY_LIST_PAGE': '/app/admin/#/list/companies',
        'INTELLIGENCE_DASHBOARD': '/app/intelligence/#/dashboard',
        'CREATE_INITIATIVE_PAGE': '/app/advertising/#/create/initiative',
        'OPTIMIZATION_SETTING_PAGE': '/app/advertising/#/sync/{line_item_id}?mode=optimization#step-3',
        'LINE_ITEM_DETAIL_VIEW': '/app/advertising/#/dashboard/lineitems/details',
        'CREATE_USER_PAGE': '/app/admin/#/create/user',
        'INTELLIGENCE_DASHBOARD_TEMPLATES_PAGE': '/app/intelligence/#/dashboard/templates'
    },
    'FORM_PAGES': {
        'CREATE_COMPANY_PAGE': '/app/admin/#/create/company',
    },
    'REPORT': {
        'FB_PAID_REPORT': '/app/intelligence/#/report/paid-performance-facebook',
        'TW_PAID_REPORT': '/app/intelligence/#/report/paid-performance-twitter',
        'LI_PAID_REPORT': '/app/intelligence/#/report/paid-performance-linkedin',
        'IN_PAID_REPORT': '/app/intelligence/#/report/paid-performance-instagram',
        'SC_PAID_REPORT': '/app/intelligence/#/report/paid-performance-snapchat',
        'FB_COMPETITIVE_REPORT': '/app/intelligence/#/report/competitive-facebook',
        'TW_COMPETITIVE_REPORT': '/app/intelligence/#/report/competitive-twitter',
        'FB_SEGMENTATION_REPORT': '/app/intelligence/#/report/segmentation-facebook',
        'BENCHMARK_REPORT': '/app/intelligence/#/report/benchmarks',
        'REPORT_TEMPLATE': '/app/intelligence/#/report/templates'
    },
}

PAGE_LIST = {
    'All Companies': URL['LIST_PAGES']['COMPANY_LIST_PAGE'],
    'All Brands': URL['LIST_PAGES']['BRAND_LIST_PAGE'],
    'All Users': URL['LIST_PAGES']['USER_LIST_PAGE'],
    'Users Details': URL['LIST_PAGES']['USER_BRAND_LIMITATIONS_PAGE'],
    'All Initiatives': URL['LIST_PAGES']['ADMIN_INITIATIVE_LIST_PAGE'],
    'Advertising Initiative List': URL['LIST_PAGES']['ADV_INITIATIVE_LIST_PAGE'],
    'Advertising Campaigns List': URL['LIST_PAGES']['ADV_CAMPAIGNS_LIST_PAGE'],
    'Pacing Dashboard': URL['LIST_PAGES']['PACING_DASHBOARD_PAGE'],
    'Line Item List Detail View': URL['LIST_PAGES']['LINE_ITEM_LIST_DETAIL_VIEW_PAGE'],
    'Home': URL['HOME_PAGE'],
    'Onboarding': URL['ONBOARDING_PAGE'],
    'Create Initiative': URL['LIST_PAGES']['CREATE_INITIATIVE_PAGE'],
    'Line Item Detail View': URL['LIST_PAGES']['LINE_ITEM_DETAIL_VIEW'],
    'Create User': URL['LIST_PAGES']['CREATE_USER_PAGE']
}

GMAIL_API = {
    'service_name': 'gmail',
    'version': 'v1'
}

#   +---------------+
#   | BUTTON NAMES  |
#   +---------------+

COMPANIES = {
    'AGENCY_GRANT_ACCESS_BTN_NAME': 'Request Brand Access'
}

COMPANY_TYPE_SUPPORTED = ['client', 'agency', 'group', 'vendor', 'publisher']

# DATA SAMPLE
CLIENT_1_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-1': {
                'name': 'QE-Initiative-test-1',
                'brandID': 'QE-Brand-1',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
        'QE-Initiative-test-2': {
                'name': 'QE-Initiative-test-2',
                'brandID': 'QE-Brand-1',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

CLIENT_2_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-3': {
                'name': 'QE-Initiative-test-3',
                'brandID': 'QE-Brand-2',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
        'QE-Initiative-test-4': {
                'name': 'QE-Initiative-test-4',
                'brandID': 'QE-Brand-2',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

CLIENT_3_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-5': {
                'name': 'QE-Initiative-test-5',
                'brandID': 'QE-Brand-3',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
        'QE-Initiative-test-6': {
                'name': 'QE-Initiative-test-6',
                'brandID': 'QE-Brand-3',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

AGENCY_1_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-7': {
                'name': 'QE-Initiative-test-7',
                'brandID': 'QE-Brand-2',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
        'QE-Initiative-test-8': {
                'name': 'QE-Initiative-test-8',
                'brandID': 'QE-Brand-1',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

AGENCY_2_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-9': {
                'name': 'QE-Initiative-test-9',
                'brandID': 'QE-Brand-2',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

AGENCY_3_INITIATIVE_SAMPLE = {
        'QE-Initiative-test-10': {
                'name': 'QE-Initiative-test-10',
                'brandID': 'QE-Brand-4',
                'budget': 0,
                'currency': 'USD',
                'foreignID': ''
        },
}

CLIENT_1_LINE_ITEM_SAMPLE = {
        'QE-Line-item-FB-1-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-1-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 133928.57,
            'feeType': 'Cost Plus',
            'fee': 10,
            'feePercentage': 8.5,
            'totalBudget': 15000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-TW-1-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'twitter',
            'name': 'QE-Line-item-TW-1-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 143928.57,
            'feeType': 'Cost Plus',
            'fee': 15,
            'feePercentage': 15,
            'totalBudget': 17000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'BOB'
        },
        'QE-Line-item-FB-7-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-7-08012016-07/30/2017',
            'mediaType': 'Paid',
            'feeType': 'Cost Plus',
            'fee': 39,
            'feePercentage': 19,
            'totalBudget': 31000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-SC-3-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'snapchat',
            'name': 'QE-Line-item-SC-3-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 2,
            'feeType': 'Cost Plus',
            'fee': 39,
            'feePercentage': 19,
            'totalBudget': 31000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-IG-4-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'instagram',
            'name': 'QE-Line-item-IG-4-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 0,
            'feeType': 'Cost Plus',
            'fee': 39,
            'feePercentage': 19,
            'totalBudget': 31000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-FB-4-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-4-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 273928.57,
            'feeType': 'Cost Plus',
            'fee': 39,
            'feePercentage': 19,
            'totalBudget': 31000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

CLIENT_2_LINE_ITEM_SAMPLE = {
        'QE-Line-item-IG-1-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-3',
            'publisher': 'instagram',
            'name': 'QE-Line-item-IG-1-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 153928.57,
            'feeType': 'Percent of Spend',
            'fee': 21,
            'feePercentage': 17,
            'totalBudget': 19000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-FB-5-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-3',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-5-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 173928.57,
            'feeType': 'Percent of Spend',
            'fee': 25,
            'feePercentage': 12,
            'totalBudget': 21000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

CLIENT_3_LINE_ITEM_SAMPLE = {
        'QE-Line-item-SC-1-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-1',
            'publisher': 'snapchat',
            'name': 'QE-Line-item-SC-1-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 193928.57,
            'feeType': 'Cost Plus',
            'fee': 27,
            'feePercentage': 17,
            'totalBudget': 23000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-FB-2-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-2',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-2-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 213928.57,
            'feeType': 'Cost Plus',
            'fee': 30,
            'feePercentage': 19,
            'totalBudget': 25000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

AGENCY_1_LINE_ITEM_SAMPLE = {
        'QE-Line-item-IG-2-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-7',
            'publisher': 'instagram',
            'name': 'QE-Line-item-IG-2-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 233928.57,
            'feeType': 'Cost Plus',
            'fee': 32,
            'feePercentage': 12,
            'totalBudget': 27000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-TW-2-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-7',
            'publisher': 'twitter',
            'name': 'QE-Line-item-TW-2-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 253928.57,
            'feeType': 'Cost Plus',
            'fee': 35,
            'feePercentage': 18,
            'totalBudget': 29000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

AGENCY_2_LINE_ITEM_SAMPLE = {
        'QE-Line-item-FB-6-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-9',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-6-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 273928.57,
            'feeType': 'Cost Plus',
            'fee': 39,
            'feePercentage': 19,
            'totalBudget': 31000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-SC-2-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-9',
            'publisher': 'snapchat',
            'name': 'QE-Line-item-SC-2-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 293928.57,
            'feeType': 'Cost Plus',
            'fee': 41,
            'feePercentage': 25,
            'totalBudget': 33000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

AGENCY_3_LINE_ITEM_SAMPLE = {
        'QE-Line-item-FB-3-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-10',
            'publisher': 'facebook',
            'name': 'QE-Line-item-FB-3-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 313928.57,
            'feeType': 'Cost Plus',
            'fee': 43,
            'feePercentage': 27,
            'totalBudget': 36000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
        'QE-Line-item-IG-3-08012016-07/30/2017': {
            'initiativeID': 'QE-Initiative-test-10',
            'publisher': 'instagram',
            'name': 'QE-Line-item-IG-3-08012016-07/30/2017',
            'mediaType': 'Paid',
            'mediaSpend': 333928.57,
            'feeType': 'Cost Plus',
            'fee': 46,
            'feePercentage': 29,
            'totalBudget': 38000,
            'startDate': '2017-07-30T00:00:00+00:00',
            'endDate': '2018-07-29T00:00:00+00:00',
            'currency': 'USD'
        },
}

CLIENT_1_WATCH_LINE_ITEM_SAMPLE = {
        'Client 1 watch QE-Line-item-FB-2-08012016-07/30/2017': {
            'line_item_id': 'QE-Line-item-FB-2-08012016-07/30/2017',
        },
}
CLIENT_3_WATCH_LINE_ITEM_SAMPLE = {
        'Client 2 watch QE-Line-item-FB-1-08012016-07/30/2017': {
            'line_item_id': 'QE-Line-item-FB-1-08012016-07/30/2017',
        },
        'Client 2 watch QE-Line-item-TW-1-08012016-07/30/2017': {
            'line_item_id': 'QE-Line-item-TW-1-08012016-07/30/2017',
        },
}
AGENCY_1_WATCH_LINE_ITEM_SAMPLE = {
        'Agency 1 watch QE-Line-item-FB-6-08012016-07/30/2017': {
            'line_item_id': 'QE-Line-item-FB-6-08012016-07/30/2017',
        },
}

# Share line item for sample users
SHARE_LINE_ITEM_TO_COMPANIES_SAMPLE = {
     'QE-Line-item-FB-1-08012016-07/30/2017 - QE-Agency-Group1': {
         'companyName': 'QE-Agency-Group1',
         'companyID': '',
         'accessRight': 'ReadOnly',
         'serviceType': 'AgencyHolding',
         'financialView': 'GrossBudget'
     },
     'QE-Line-item-FB-1-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'ReadOnly',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'NoFinancial'
     },
     'QE-Line-item-FB-1-08012016-07/30/2017 - QE-Agency-Agency2': {
         'companyName': 'QE-Company-Agency2',
         'companyID': '',
         'accessRight': 'FullAccess',
         'serviceType': 'AgencyHolding',
         'financialView': 'NetBudget'
     },
     'QE-Line-item-FB-7-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'ReadOnly',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'NoFinancial'
     },
     'QE-Line-item-SC-3-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'FullAccess',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'AllCosts'
     },
     'QE-Line-item-IG-4-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'FullAccess',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'AllCosts'
     },
     'QE-Line-item-FB-4-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'FullAccess',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'AllCosts'
     },
     'QE-Line-item-IG-1-08012016-07/30/2017 - QE-Agency-Group1': {
         'companyName': 'QE-Agency-Group1',
         'companyID': '',
         'accessRight': 'ReadOnly',
         'serviceType': 'AgencyHolding',
         'financialView': 'NoFinancial'
     },
     'QE-Line-item-IG-1-08012016-07/30/2017 - QE-Company-Agency1': {
         'companyName': 'QE-Company-Agency1',
         'companyID': '',
         'accessRight': 'FullAccess',
         'serviceType': 'AgencyOfRecord',
         'financialView': 'NoFinancial'
     },
}

# Pacing data for sample users

# Saved report for Iheart user
IHEART_USER_SAVED_REPORT_SAMPLE = {
     'Older Conservative Males, LA': {
         'reportID': 'audience-creator-saved-audience-report',
         'name': 'Older Conservative Males, LA',
         'parameters': {
             'ages': '65+',
             'description': 'Male, 65+, Republican, 102.7 KIIS-FM LA',
             'gender': 'M',
             'isUnique': 'true',
             'selected_units': {
                 '185': {
                     'call_letter': 'KIIS-FM',
                     'format': 'CHRPOP',
                     'index': 784.18,
                     'market': 'Los Angeles',
                     'opacity': 1,
                     'seg_pct': 0.8599,
                     'station_name': '102.7 KIIS-FM Los Angeles',
                     'stream_id': 185,
                     'title': '102.7 KIIS-FM Los Angeles - Los Angeles',
                     'user_num': 8.599386e+06
                 },
                 'keyList': [185]
             },
             'target_cohort': {
                 'category': 'Political \u003e Conservative',
                 'cohort': 'Republican',
                 'cohort_id': 2}
         },
         'publisher': 'unified'
     },

     'Young Female Democrats, NY': {
        'reportID': 'audience-creator-saved-audience-report',
        'name': 'Young Female Democrats, NY',
        'parameters': {
            'ages': '18-24,25-34',
            'description': 'Female, 18-34, Democrat, Z100-NY',
            'gender': 'F',
            'isUnique': 'true',
            'selected_units': {
                '1469': {
                    'call_letter': 'WHTZ-FM',
                    'format': 'CHRPOP',
                    'index': 490.8,
                    'market': 'New York',
                    'opacity': 1,
                    'seg_pct': 1.7967,
                    'station_name': 'Z100',
                    'stream_id': 1469,
                    'title': 'Z100 - New York',
                    'user_num': 1.7967158e+07
                },
                'keyList': [1469]},
            'target_cohort': {
                'category': 'Political \u003e Liberal',
                'cohort': 'Democrat',
                'cohort_id': 1
            }
        },
        'publisher': 'unified'
     },
}

CLIENT_1_LINE_ITEM_WITH_PACING_DATA = {
    'QE-Line-item-FB-1-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-1',
        'brand_name': 'QE-Brand-1',
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-1-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-FB-1-08012016-07/30/2017',
        'media_budget': 1000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 4,
        'actual_days_num': 3,
        'true_pacing_pct': 65,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 101,
        'spent_to_date': 102,
        'budget_remain': 80,
        'budget_complete_pct': 21,
        'budget_at_risk': 200,
        'avg_daily_spend_target': 81,
        'open_media_budget': 72,
        'open_media_budget_pct': 19,
    },
    'QE-Line-item-TW-1-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-1',
        'brand_name': 'QE-Brand-1',
        'publisher': 'twitter',
        'lineitem_id': 'QE-Line-item-TW-1-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-TW-1-08012016-07/30/2017',
        'media_budget': 10000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 4,
        'actual_days_num': 3,
        'true_pacing_pct': 50,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 15,
        'spent_to_date': 160,
        'budget_remain': 900,
        'budget_complete_pct': 50,
        'budget_at_risk': 400,
        'avg_daily_spend_target': 181,
        'open_media_budget': 262,
        'open_media_budget_pct': 25,
    },
    'QE-Line-item-FB-2-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-1',
        'brand_name': 'QE-Brand-1',
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-2-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-FB-2-08012016-07/30/2017',
        'media_budget': 10000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 4,
        'actual_days_num': 3,
        'true_pacing_pct': 50,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 80,
        'spent_to_date': 160,
        'budget_remain': 900,
        'budget_complete_pct': 50,
        'budget_at_risk': 400,
        'avg_daily_spend_target': 181,
        'open_media_budget': 262,
        'open_media_budget_pct': 25,
    }
}

CLIENT_1_LINE_ITEM_WITH_GOAL_DATA = {
    'QE-Line-item-FB-1-08012016-07/30/2017': {
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-1-08012016-07/30/2017',
        'goal_id': 'Goal test 1',
        'position_id': 1,
        'indicator_name': 'Test_Indicator name 1',
        'target': 2,
        'result_val': 0,
        'tracking_value': 12,
        'tracking_pct': 100,
        'daily_target': 2,
        'is_disabled': False,
        'metric_type': 'Test metric 1',
    },
    'QE-Line-item-TW-1-08012016-07/30/2017': {
        'publisher': 'twitter',
        'lineitem_id': 'QE-Line-item-TW-1-08012016-07/30/2017',
        'goal_id': 'Goal test 2',
        'position_id': 1,
        'indicator_name': 'Test_Indicator name 2',
        'target': 6,
        'result_val': 1,
        'tracking_value': 100,
        'tracking_pct': 85.5,
        'daily_target': 9,
        'is_disabled': False,
        'metric_type': 'Test metric 2',
    },
    'QE-Line-item-FB-2-08012016-07/30/2017': {
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-2-08012016-07/30/2017',
        'goal_id': 'Goal test 2',
        'position_id': 1,
        'indicator_name': 'Test_Indicator name 3',
        'target': 6,
        'result_val': -4,
        'tracking_value': -100,
        'tracking_pct': 85.5,
        'daily_target': 9,
        'is_disabled': False,
        'metric_type': 'Test metric 2',
    }
}

CLIENT_2_LINE_ITEM_WITH_PACING_DATA = {
    'QE-Line-item-IG-1-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'publisher': 'instagram',
        'lineitem_id': 'QE-Line-item-IG-1-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-IG-1-08012016-07/30/201',
        'media_budget': 1000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 4,
        'actual_days_num': 3,
        'true_pacing_pct': 65,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 101,
        'spent_to_date': 102,
        'budget_remain': 80,
        'budget_complete_pct': 21,
        'budget_at_risk': 200,
        'avg_daily_spend_target': 81,
        'open_media_budget': 72,
        'open_media_budget_pct': 19,
    },
    'QE-Line-item-FB-5-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-5-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-FB-5-08012016-07/30/2017',
        'media_budget': 10000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 4,
        'actual_days_num': 3,
        'true_pacing_pct': 50,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 15,
        'spent_to_date': 160,
        'budget_remain': 900,
        'budget_complete_pct': 50,
        'budget_at_risk': 400,
        'avg_daily_spend_target': 181,
        'open_media_budget': 262,
        'open_media_budget_pct': 25,
    },
}

CLIENT_2_LINE_ITEM_WITH_GOAL_DATA = {
    'QE-Line-item-IG-1-08012016-07/30/2017': {
        'publisher': 'instagram',
        'lineitem_id': 'QE-Line-item-IG-1-08012016-07/30/2017',
        'goal_id': 'Goal test 1',
        'position_id': 1,
        'indicator_name': 'Test_Indicator name 1',
        'target': 2,
        'result_val': 0,
        'tracking_value': 12,
        'tracking_pct': 100,
        'daily_target': 2,
        'is_disabled': False,
        'metric_type': 'Test metric 1',
    },
    'QE-Line-item-FB-5-08012016-07/30/2017': {
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-5-08012016-07/30/2017',
        'goal_id': 'Goal test 2',
        'position_id': 1,
        'indicator_name': 'Test_Indicator name 2',
        'target': 6,
        'result_val': 1,
        'tracking_value': 100,
        'tracking_pct': 85.5,
        'daily_target': 9,
        'is_disabled': False,
        'metric_type': 'Test metric 2',
    },
}

AGENCY_1_LINE_ITEM_WITH_PACING_DATA = {
    'QE-Line-item-IG-2-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'publisher': 'instagram',
        'lineitem_id': 'QE-Line-item-IG-2-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-IG-2-08012016-07/30/2017',
        'media_budget': 1000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 10,
        'actual_days_num': 3,
        'true_pacing_pct': 65,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 101,
        'spent_to_date': 102,
        'budget_remain': 80,
        'budget_complete_pct': 21,
        'budget_at_risk': 10,
        'avg_daily_spend_target': 81,
        'open_media_budget': 72,
        'open_media_budget_pct': 19,
    },
    'QE-Line-item-TW-2-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'publisher': 'twitter',
        'lineitem_id': 'QE-Line-item-TW-2-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-TW-2-08012016-07/30/2017',
        'media_budget': 10000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': 0.00,
        'actual_days_num': 3,
        'true_pacing_pct': 50,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 15,
        'spent_to_date': 160,
        'budget_remain': 900,
        'budget_complete_pct': 50,
        'budget_at_risk': 0.00,
        'avg_daily_spend_target': 181,
        'open_media_budget': 262,
        'open_media_budget_pct': 25,
    },
}

AGENCY_2_LINE_ITEM_WITH_PACING_DATA = {
    'QE-Line-item-FB-6-08012016-07/30/2017': {
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'publisher': 'facebook',
        'lineitem_id': 'QE-Line-item-FB-6-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-FB-6-08012016-07/30/2017',
        'media_budget': 1000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': -10,
        'actual_days_num': 3,
        'true_pacing_pct': 65,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 101,
        'spent_to_date': 102,
        'budget_remain': 80,
        'budget_complete_pct': 21,
        'budget_at_risk': -5,
        'avg_daily_spend_target': 81,
        'open_media_budget': 72,
        'open_media_budget_pct': 19,
    },
    'QE-Line-item-SC-2-08012016-07/30/2017': {
        'brand_id': 'QE-Line-item-SC-2-08012016-07/30/2017',
        'brand_name': 'QE-Brand-2',
        'publisher': 'snapchat',
        'lineitem_id': 'QE-Line-item-SC-2-08012016-07/30/2017',
        'lineitem_foreign_id': '',
        'lineitem_name': 'QE-Line-item-SC-2-08012016-07/30/2017',
        'media_budget': 10000.0,
        'end_date': '2018-07-29T00:00:00+00:00',
        'start_date': '2017-07-30T00:00:00+00:00',
        'days_remain': -1,
        'is_5days_end': 1,
        'avg_3day_media_spend': 2,
        'yesterday_media_spent': -5,
        'actual_days_num': 3,
        'true_pacing_pct': 50,
        'pacing_status': 'Undefined',
        'pacing_status_key': 1,
        'is_underpasing': 1,
        'is_overpacing': 0,
        'pacing_trend_pct': 15,
        'spent_to_date': 160,
        'budget_remain': 900,
        'budget_complete_pct': 50,
        'budget_at_risk': -10,
        'avg_daily_spend_target': 181,
        'open_media_budget': 262,
        'open_media_budget_pct': 25,
    },
}

# Investment Dashboard data
INVESTMENT_DASHBOARD_BRAND_DATA = {
    'QE-Brand-1': {
        'start_date': '2018-01-01',
        'brand_id': 'QE-Brand-1',
        'brand_name': 'QE-Brand-1',
        'currency': 'USD',
        'facebook_media_spend': 25000,
        'facebook_video_media_spend': 20000,
        'facebook_impressions': 40000,
        'facebook_engagements': 41000,
        'facebook_video_views': 30000,
        'facebook_video_campaign_views': 46000,
        'facebook_cpm': 5,
        'facebook_cpe': 4,
        'facebook_cpv': 3,
        'twitter_media_spend': 25000,
        'twitter_video_media_spend': 26000,
        'twitter_impressions': 42000,
        'twitter_engagements': 43000,
        'twitter_video_views': 32000,
        'twitter_video_campaign_views': 47000,
        'twitter_cpm': 4,
        'twitter_cpe': 3,
        'twitter_cpv': 2,
        'instagram_media_spend': 26000,
        'instagram_video_media_spend': 25000,
        'instagram_impressions': 43000,
        'instagram_engagements': 44000,
        'instagram_video_views': 43000,
        'instagram_video_campaign_views': 44000,
        'instagram_cpm': 3,
        'instagram_cpe': 2,
        'instagram_cpv': 1,
        'pinterest_media_spend': 27000,
        'pinterest_video_media_spend': 28000,
        'pinterest_impressions': 44000,
        'pinterest_engagements': 45000,
        'pinterest_video_views': 44000,
        'pinterest_video_campaign_views': 45000,
        'pinterest_cpm': 2,
        'pinterest_cpe': 2,
        'pinterest_cpv': 1,
        'snapchat_media_spend': 28000,
        'snapchat_video_media_spend': 29000,
        'snapchat_impressions': 45000,
        'snapchat_engagements': 46000,
        'snapchat_video_views': 47000,
        'snapchat_video_campaign_views': 46000,
        'snapchat_cpm': 3,
        'snapchat_cpe': 2,
        'snapchat_cpv': 1,
    },
    'QE-Brand-2': {
        'start_date': '2017-12-12',
        'brand_id': 'QE-Brand-2',
        'brand_name': 'QE-Brand-2',
        'currency': 'AUD',
        'facebook_media_spend': 25000,
        'facebook_video_media_spend': 20000,
        'facebook_impressions': 40000,
        'facebook_engagements': 41000,
        'facebook_video_views': 30000,
        'facebook_video_campaign_views': 46000,
        'facebook_cpm': 5,
        'facebook_cpe': 4,
        'facebook_cpv': 3,
        'twitter_media_spend': 25000,
        'twitter_video_media_spend': 26000,
        'twitter_impressions': 42000,
        'twitter_engagements': 43000,
        'twitter_video_views': 32000,
        'twitter_video_campaign_views': 47000,
        'twitter_cpm': 4,
        'twitter_cpe': 3,
        'twitter_cpv': 2,
        'instagram_media_spend': 26000,
        'instagram_video_media_spend': 25000,
        'instagram_impressions': 43000,
        'instagram_engagements': 44000,
        'instagram_video_views': 43000,
        'instagram_video_campaign_views': 44000,
        'instagram_cpm': 3,
        'instagram_cpe': 2,
        'instagram_cpv': 1,
        'pinterest_media_spend': 27000,
        'pinterest_video_media_spend': 28000,
        'pinterest_impressions': 44000,
        'pinterest_engagements': 45000,
        'pinterest_video_views': 44000,
        'pinterest_video_campaign_views': 45000,
        'pinterest_cpm': 2,
        'pinterest_cpe': 2,
        'pinterest_cpv': 1,
        'snapchat_media_spend': 28000,
        'snapchat_video_media_spend': 29000,
        'snapchat_impressions': 45000,
        'snapchat_engagements': 46000,
        'snapchat_video_views': 47000,
        'snapchat_video_campaign_views': 46000,
        'snapchat_cpm': 3,
        'snapchat_cpe': 2,
        'snapchat_cpv': 1,
    },
}
