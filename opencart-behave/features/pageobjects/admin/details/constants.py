from selenium.webdriver.support.select import By

DASHBOARD = {

    'USER_PROFILE_ICON': (By.XPATH, '//img[@id="user-profile"]/..'),
    'MENU_ITEM_YOUR_PROFILE': (By.LINK_TEXT, 'Your Profile'),

    'MAIN_MENU': (By.ID, 'menu'),
    'TOTAL_ORDERS': (By.XPATH, '//div[@class="tile-heading" and text()="Total Orders "]/..'),
    'TOTAL_SALES': (By.XPATH, '//div[@class="tile-heading" and text()="Total Sales "]/..'),
    'TOTAL_CUSTOMERS': (By.XPATH, '//div[@class="tile-heading" and text()="Total Customers "]/..'),
    'PEOPLE ONLINE': (By.XPATH, '//div[@class="tile-heading" and text()="People Online"]/..'),

    'ORDER_TABLE': {
        'VIEW_ACTION': (By.XPATH, '//table/tbody/tr[{index}]/td[6]/a'),
    }
}

USER_PROFILE = {
    'HEADER': (By.CSS_SELECTOR, '.page-header h1'),
}


#############################################


"""
Constants for detail pages of Brand, Company and User
"""

# ============================================== BRAND DETAIL ==========================================================

BRAND_DETAIL = {
    'BRAND_NAME': (By.CSS_SELECTOR, '.inline-edit-container>span>span'),
    'COMPANY_NAME': (By.CSS_SELECTOR, '#brandDetailCompanyName+span'),
    'SUCCESS_BRAND_ATTRIBUTE': 'ContentEditable is-success text-success',
    'REVERT_OPTION': (By.CSS_SELECTOR, '.edit-revert'),
    'UPDATE_BRAND_ERROR_MESSAGE': (By.CSS_SELECTOR, '.edit-error.is-error'),
    'RESET_OPTION': (By.CSS_SELECTOR, '.inline-edit-container>span .edit-error'),
}


FAMILIES = {
    'FAMILY_SEARCH_BOX': (By.ID, 'brandFamilySearchBox'),
    'CREATE_FAMILY_BTN': (By.ID, 'CreateUserButton'),
    'ADD_BRAND_TO_FAMILY_BTN': (By.ID, 'AddBrandtoFamily'),
    'FAMILY_NAME_FIELD': (By.ID, 'familyName')
}

PROPERTIES = {
    'PROPERTY_SEARCH_BOX': (By.ID, 'brandPropertySearchBox'),
    'PROPERTY_LINK': (By.CSS_SELECTOR, '.fa.fa-external-link'),
    'ADD_PROPERTY_LINK': (By.ID, 'CreateNewProperty'),
    'PROPERTY_TITLE': (By.ID, 'propertyTitle'),
    'PROPERTY_URL': (By.ID, 'propertyUrl'),
    'SELECTED_CONTAINER': (By.CSS_SELECTOR, '.selected-container'),
    'PROPERTY_TYPE_SELECT_CONTROL': (By.CSS_SELECTOR, '#propertyType .Select-control'),
}

LINE_ITEM_SHARE_SETTINGS = {
    'COLUMN_HEADER': ['Sharing from...', 'Type', 'Sharing to...', 'Type ', 'Functional Access', 'Financial Access', 'Service Type', 'Count', 'Actions'],
    'COMPANY_SELECT': (By.CSS_SELECTOR, '#sharingCompanySelect .Select-placeholder'),
    'SHARE_SETTING_BTN': (By.ID, 'ConfigureShareSetting'),
    'LINE_ITEM_SHARE_SETTINGS_LNK': (By.ID, 'LineItemShareSettings'),
    'COMPANY_SHARING_SELECT': (By.ID, 'sharingCompanySelect'),
    'RIBBON_SELECT': (By.CSS_SELECTOR, '.selected-container .ribbon'),
    'CONFIGURE_CONNECTED_INTEL_BTN': (By.ID, 'ConfigureConnectedIntelligence'),
    'SHARED_COMPANY_LINK': (By.CSS_SELECTOR, '[href*="#/details/companies/{company_id}/BrandAccess"]'),
    'COMPANY_SHARING_FROM': (By.CSS_SELECTOR, 'td[data-th="Sharing from..."]>div'),
    'COMPANY_SHARING_FROM_LINK': (By.CSS_SELECTOR, 'td[data-th="Sharing from..."] .primary'),
    'COMPANY_SHARING_FROM_TYPE': (By.CSS_SELECTOR, 'td[data-th="Type"]>div'),
    'COMPANY_SHARING_TO': (By.CSS_SELECTOR, 'td[data-th="Sharing to..."]>div'),
    'COMPANY_SHARING_TO_LINK': (By.CSS_SELECTOR, 'td[data-th="Sharing to..."] .primary'),
    'COMPANY_SHARING_TO_TYPE': (By.CSS_SELECTOR, 'td[data-th="Type "]>div'),
    'FUNCTIONAL_ACCESS': (By.CSS_SELECTOR, 'td[data-th="Functional Access"] .Select-placeholder'),
    'FINANCIAL_ACCESS': (By.CSS_SELECTOR, 'td[data-th="Financial Access"] .Select-placeholder'),
    'SERVICE_TYPE': (By.CSS_SELECTOR, 'td[data-th="Service Type"] .Select-placeholder'),
    'COUNT': (By.CSS_SELECTOR, 'td[data-th="Count"]>div'),
    'ACTION_BTN': (By.CSS_SELECTOR, '#bodyWrapper  table  .dropdown-menu-right'),
    'ACTIONS': {
        'ACTIONS_BY_COMPANY_ID': (By.ID, 'Actions_{sharing_company_id}{shared_company_id}')
    }
}

COMPANY_ACCESS = {
    'COLUMN_HEADER': ['Company Name', 'Type', 'Brand', 'Users', 'Last Modified']
}

MESSAGE = {
    'BRAND_NAME_UPDATE_EXISTS': '{name} already exists in our system. Please search for the record if you wish to make changes.'
}

# ============================================== COMPANY DETAIL ========================================================

COMPANY_DETAIL = {
    'COMPANY_TYPE_VALUE': (By.ID, 'companyTypeHeaderValue'),
    'COMPANY_NAME': (By.CSS_SELECTOR, '.ContentEditable'),
    'COMPANY_NAME_SUCCESS_EDITED': (By.CSS_SELECTOR, '.ContentEditable.is-final'),
    'SUCCESS_COMPANY_ATTRIBUTE': 'ContentEditable is-success text-success',
    'REVERT_OPTION': (By.CSS_SELECTOR, '.edit-revert'),
    'HEADER': '.category',
    'COMPANY_STATUS_SWITCH': (By.CSS_SELECTOR, '#companyAccess .onoffswitch-switch'),
    'COMPANY_STATUS_CHECKBOX': (By.CSS_SELECTOR, '#companyAccess .onoffswitch-checkbox'),
    'CUSTOMER_STATUS': (By.CSS_SELECTOR, '#companyIsCustomer .onoffswitch-switch'),
}

PLATFORM_CONFIGURATION = {
    'TAB_HEADER': (By.CSS_SELECTOR, '.tab-content h3'),
    'DEFAULT_OPTIONS': {
        'HEADER': 'Platform Access Control',
        'ONBOARDING_STATUS': True,
        'CAMPAIGN_STATUS': False,
        'REPORT_STATUS': True,
        'REPORT_FEATURE_ACCESS': {
            'BENCHMARKS': False,
            'PAID_MEDIA_REPORTS': True,
            'COMPETITIVE_REPORTS': False,
            'AUDIENCE_ANALYSIS': False,
            'ORGANIC_REPORTS': False
        },
        'SNAPCHAT_STATUS': True,
    },
    'DEFAULT_CAMPAIGNS_SETTINGS': {
        'FEATURE_ACCESS': {
            'INITIATIVE_PACING': True,
            'LINE_ITEMS_PACING': True,
            'CAMPAIGN_PACING': False,
            'OPTIMIZER': True,
        },
        'ADDITIONAL_SETTINGS': {
            'PRICE_TYPE': 'Percentage',
            'PERCENT_TYPE': 'Select...',
            'PERCENT': '0.00'
        },
    },
    'CAMPAIGN': {
        'CAMPAIGN_TOGGLE_STATUS': (By.ID, 'statusSwitch_investmentManagerSwitcher'),
        'CAMPAIGN_TOGGLE': (By.CSS_SELECTOR, '#investmentManager .onoffswitch .onoffswitch-label'),
        'PRICE_TYPE_SELECT': (By.CSS_SELECTOR, '#priceType .Select-placeholder'),
        'PERCENT_TYPE_SELECT': (By.CSS_SELECTOR, '#percentType .Select-placeholder'),
        'INITIATIVE_PACING_TOGGLE_STATUS': (By.ID, 'statusSwitch_pacing_initiativesCheckbox'),
        'LINE_ITEMS_PACING_TOGGLE_STATUS': (By.ID, 'statusSwitch_pacing_line_itemsCheckbox'),
        'CAMPAIGN_PACING_TOGGLE_STATUS': (By.ID, 'statusSwitch_pacing_campaignsCheckbox'),
        'OPTIMIZER_TOGGLE_STATUS': (By.ID, 'statusSwitch_optimizerCheckbox'),
    },
    'ONBOARDING': {
        'ONBOARDING_TOGGLE_STATUS': (By.ID, 'statusSwitch_onboardingAccessSwithcer'),
    },
    'REPORT': {
        'REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_repotsAccessSwitcher'),
        'BENCHMARKS_REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_benchmarks'),
        'PAID_REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_paid'),
        'COMPETITIVE_REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_competitive'),
        'AUDIENCE_ANALYSIS_REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_audience_analysis'),
        'ORGANIC_REPORT_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_organic'),
    },
    'SNAPCHAT': {
        'SNAPCHAT_TOGGLE': (By.CSS_SELECTOR, '#snapchatApplication .onoffswitch .onoffswitch-label'),
        'SNAPCHAT_TOGGLE_STATUS': (By.ID, 'statusSwitch_snapchatApplicationSwitcher'),
        'SNAPCHAT_APPLICATION_SUCCESS_SAVE': (By.CSS_SELECTOR, '#snapchatApplication .success.visible'),
    },
    'PERCENT': (By.ID, 'percentValue'),
    'PERCENT_UNIT': (By.ID, 'percentUnit'),
    'SUCCESS_NOTIFICATION_TOGGLE_STATUS_CHANGE': (By.CSS_SELECTOR, '.success.visible'),
    'REPORTS_ACCESS': {
        'REPORTS_STATUS_SWITCH': (By.CSS_SELECTOR, '#reportsAccess .onoffswitch'),
        'REPORT_TOGGLE_STATUS': (By.CSS_SELECTOR, '#statusSwitch_repotsAccessSwitcher'),
        'REPORT_ACCESS_TOGGLE_STATUS': (By.ID, 'statusSwitch_reports_{report_name}'),
        'REPORTS_FEATURE_STATUS': (By.CSS_SELECTOR, 'label[for="statusSwitch_reports_{}"] .onoffswitch-switch')
    },
}

BRAND_ACCESS = {
    'ADD_GRANT_BTN': (By.ID, 'AddGrand'),
    'GRANT_ACCESS_BTN': (By.ID, 'GrantAccess'),
}

PUBLISHER_ACCESS = {
    'PUBLISHER_ACCESS': (By.ID, 'publisher_{publisher}'),
    'PUBLISHER_ACCESS_TOGGLE': (By.ID, 'statusSwitch_{publisher}'),
    'PUBLISHER_STATUS': (By.CSS_SELECTOR, 'label[for="statusSwitch_{publisher}"]'),
}

USERS = {
    'ADD_USER_BTN': (By.ID, 'CreateUserButton'),
}

BUTTONS = {
    'CREATE_USER_BTN': (By.ID, 'CreateUserButton'),
    'CANCEL_IN_ADMIN_SECTION': (By.ID, 'cancel'),
}


CUSTOM_METRIC_LIBRARY = {
    'CREATE_CUSTOM_METRIC_BTN': (By.ID, 'addMetricsBtn'),
    # table
    'METRIC_NAME': (By.ID, 'CustomMetricLibraryMetricName_{metric_id}'),
    'PUBLISHER': (By.CSS_SELECTOR, '#metric_{metric_id} > span'),
    'CUSTOM_METRIC_STATUS_SWITCH': (By.CSS_SELECTOR, '[data-reactid*="{id}"] .onoffswitch-switch'),
    'CUSTOM_METRIC_STATUS_CHECKBOX': (By.CSS_SELECTOR, '[data-reactid*="{id}"] .onoffswitch-checkbox'),
    'METRIC_SEARCH_BOX': (By.ID, 'metricsSearchBox'),
}


# ============================================== USER DETAIL ========================================================

USER_PROFILE_CONNECTIONS = {
    'ACTIONS_DROPDOWN': (By.ID, 'actions_{publisher}'),
    'ADD_CONNECTION': (By.CSS_SELECTOR, '[href="/app/onboarding"]')
}

UPDATE_USER = {
    'FIRST_NAME': 'firstName',
    'LAST_NAME': 'lastName',
    'HEADER_CLASS': '.media-heading',
    'SUCCESS_CLASS': '.alert-success',
}

RESET_PASSWORD_PAGE = {
    'EMAIL_INPUT': (By.NAME, 'email'),
    'SECURITY_CODE_INPUT': (By.ID, 'confirmationId'),
    'NEW_PASSWORD_INPUT': (By.ID, 'newPasswordInput'),
    'CONFIRM_NEW_PASSWORD_INPUT': (By.ID, 'confirmNewPasswordInput')
}

UPDATE_USER_NOTIFICATIONS = {
    'PHONE_NUMBER': (By.ID, 'phone'),
    'PHONE_NUMBER_CHECKBOX': (By.ID, 'phoneCheck'),
    'NOTIFICATION_BOX_CLASS': '.alert',
    'SUCCESS_NOTIFICATION_CLASS': (By.CSS_SELECTOR, '.alert-success')
}

USER_DETAILS = {
    'CONNECTIONS_TAB': (By.ID, 'Connections'),
    'USER_DETAILS_BRAND_LIMITATIONS': (By.ID, 'BrandLimitations'),
}
