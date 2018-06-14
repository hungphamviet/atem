from selenium.webdriver.support.select import By

"""
Constants file for common objects and/or locators
"""

PUBLISHER_DROPDOWN_LIST = ['Facebook', 'Snapchat', 'Twitter', 'Pinterest', 'Linkedin', 'Instagram']

HEADERS = {
    'H1_HEADER': 'h1',
    'H3_HEADER': 'h3',
    'H2_HEADER': (By.CSS_SELECTOR, 'h2'),
    'H4_HEADER': 'h4',
    'SNAPCHAT_TAB': (By.ID, 'navLinkSnapChat'),
    'INTELLIGENCE_TAB': (By.ID, 'navLinkIntelligence'),
    'LOGO_ID': (By.ID, 'navLogo')
}

BREADCRUMBS = {
    'BREADCRUMBS_CONTENT': (By.CSS_SELECTOR, '.breadcrumbs')
}

MENU = {
    'SELECT_BOX': (By.CLASS_NAME, 'Select-control'),
    'MENU_OPTIONS': '.Select-menu',
    'MENU_FILTERED_ITEM': (By.CSS_SELECTOR, '.Select-menu > div:nth-child(1)'),
    'MENU_OPTION_BY_TEXT': '//div[contains(@class, "Select-option")][text()="{}"]',
    'INLINE_SUCCESS': (By.CSS_SELECTOR, '.cell-dropdown-wrapper.success'),
    'OPTIONS_LIST_LOCATOR': '.Select-option'
}



SELECT_OPTION = {
    'OPTIONS': (By.XPATH, '//option'),
    'NO_RESULTS_FOUND': (By.XPATH, '//*[text()="No results found"]')
}

MESSAGE = {
    'SUCCESS': (By.CSS_SELECTOR, '.alert.alert-success'),
    'SUCCESS_OPEN': (By.CSS_SELECTOR, '.alert.alert-success-open'),
    'DANGER': (By.CSS_SELECTOR, '.alert.alert-danger'),
    'DANGER_EXCLUDE_CLOSE_BTN': (By.CSS_SELECTOR, '.alert-danger>span,.alert-danger >div'),
    'WARNING': (By.CSS_SELECTOR, '.alert.alert-warning'),
    'EMPTY_MSG': (By.CSS_SELECTOR, '.empty-message'),
    'PUBLISHER_TOKEN_MISSING_MSG': (By.CSS_SELECTOR, '.alert.alert-warning>div'),
    'REFRESH_PUBLISHER_TOKEN_MSG': (By.CSS_SELECTOR, '.alert.alert-warning>a'),
}

BUTTON = {
    'CANCEL': (By.XPATH, "//button[contains(text(),'Cancel')]"),
    'NEXT': (By.ID, 'next'),
    'BACK': 'back',
    'SAVE_AND_ADD': (By.ID, 'btnAddAnother'),
    'SUBMIT': (By.CSS_SELECTOR, 'button[type=submit]'),
    'MSG_YES': 'msgYes',
    'MSG_NO': 'msgNo',
    'SAVE': 'save',
    'EDIT': 'edit',
    'RUN_REPORT': (By.ID, 'runReportBtn'),
    'CLOSE_ALERT_MESSAGE': (By.CSS_SELECTOR, '.close'),
    'PENDO_GUIDE_NEXT': (By.CSS_SELECTOR, 'button[class*=pendo-guide-next]')
}

TAB = {
    'PROPERTY': (By.ID, 'Properties'),
    'BRAND_ACCESS': (By.ID, 'BrandAccess'),
    'PUBLISHER_ACCESS': (By.ID, 'PublisherAccess'),
    'CUSTOM_METRIC_LIBRARY': (By.ID, 'CustomMetricLibrary'),
    'BRANDS': (By.ID, 'Brands'),
    'USER': (By.ID, 'Users'),
    'SETTING': 'Settings',
    'HISTORY': 'History',
    'COMPANY_ACCESS': (By.XPATH, '//li[@id="CompanyAccess"]/a'),  # ID is randomly failing, since DOM gets updated twice
    # we need to use this Xpath instead
    'USER_ACCESS': (By.ID, 'UserAccess'),
    'FAMILIES': (By.ID, 'Families'),
    'INITIATIVES': (By.ID, 'Initiatives'),
    'MARKETS': (By.ID, 'Markets'),
    'CONTENT': '.tab-content'
}

TABLE = {
    'TABLE_OBJECT': (By.CSS_SELECTOR, '.unified-table'),
    'SNAPCHAT_TABLE_OBJECT': (By.CSS_SELECTOR, '.fixedDataTableLayout_main'),
    'BODY_OBJECT': '.unified-table > tbody',
    'TAG': 'table',
    'BODY_TAG': (By.TAG_NAME, 'tbody'),
    'HEADER_NAME_TEXT': '//table/thead/tr/th/div/span[text()="{}"]',
    'COLUMN_NAME_TEXT': '//table[contains(@class,"unified-table")]/thead//th',
    'SNAPCHAT_COLUMN_NAME_TEXT': (By.CSS_SELECTOR, '.cell-content'),
    'LINE ITEM DETAIL': {
        'TABLE_OBJECT': (By.CSS_SELECTOR, '.unified-fixed-table>div'),
        'COLUMN_NAME_TEXT': (By.CSS_SELECTOR, '.unified-fixed-table>div>div>div:nth-child(2) .fixedDataTableCellGroupLayout_cellGroup>div'),
        'CELL_VALUE': (By.CSS_SELECTOR, '.fixedDataTableRowLayout_rowWrapper:nth-child({row}) .fixedDataTableCellGroupLayout_cellGroupWrapper:nth-child(2)>div>div:nth-child({col}) .main-cell'),
    },
    'COLUMN_NAMES': {
        'COMPANY_NAME': 'Company Name',
        'TYPE': 'Type',
        'STATUS': 'Status',
        'BRANDS': 'Brands',
        'USERS': 'Users',
        'LAST_MODIFIED': 'Last Modified',
        'USER_EMAIL': 'User Email',
        'PARENT_COMPANY': 'Parent Company',
        'PROFILE_STATE': 'Profile State',
        'AGENCY_ACCESS': 'Agency Access',
        'USER_ACCESS': 'User Access',
        'DETAIL_LINE_ITEM': ['Budget', 'Campaigns', 'Start Date', 'End Date', 'Goal Count', 'Days Left',
                             'Budget Remaining', 'Overall Pace', '3 Day Average Pace'],
        'PACING_FB_LINE_ITEM': ['Impressions', 'Clicks', 'Shares', 'Likes', 'Video Views', 'Offsite Conversions'],
        'PACING_TW_LINE_ITEM': ['Impressions', 'Clicks', 'Retweet', 'Replies', 'Followers', 'Offsite Conversions',
                                'Card Engagements'],
        'TOGGLE_BTN': (By.CSS_SELECTOR, '.onoffswitch-checkbox + .onoffswitch-label .onoffswitch-switch'),
        # Deprecation. It must be changed to TOGGLE_STATUS_ON so that user input row,col
        'TOGGLE_ON_STATUS': 'tr:nth-child(1) td:nth-child({})>div>div>input.onoffswitch-checkbox:checked + .onoffswitch-label .onoffswitch-switch',
        'TOGGLE_STATUS': (By.CSS_SELECTOR, 'tr:nth-child({row}) td:nth-child({col}) .onoffswitch-checkbox + .onoffswitch-label .onoffswitch-switch'),
    },
    'ROW': {
        'COMPANIES': 'tr:nth-child({}) > td > .primary',
        'BRANDS': 'tr:nth-child({}) > td:nth-child(1) > div:nth-child(1) > a:nth-child(1)',
        'USERS': 'tr:nth-child({}) .avatar',
        'LIST_HYPERLINK_NAME_ROWS': '//table/tbody/tr/td[1]',
        'LIST_NAME_ROWS': (By.XPATH, '//table/tbody/tr/td[1]'),
        'LIST_COLUMNS': '//table/tbody/tr/td[{}]',
        'LIST_UNIFIED_TABLE_COLUMNS': '//table[contains(@class, "unified-table")]/tbody/tr/td[{}]',
        'HYPERLINK_COLUMN_ROWS': '//table/tbody/tr[{row}]/td[{column}]//a',
        'LINK_TEXT_CELL': (By.XPATH, '//table/tbody/tr[{row}]/td[{column}]//a[text()="{text}"]'),
        'ROWS': '//table/tbody/tr',
        'UNIFIED_TABLE_ROWS': (By.CSS_SELECTOR, '.unified-table>tbody>tr'),
        'NOT_CONTAINS': '//table/tbody/tr/td[{column}]/span/span[1][not(contains(text(), "{text}"))]'
    },
    'CELL_POSITION': '//table/tbody/tr[{}]/td[{}]',
    'UNIFIED_TABLE_CELL_POSITION': (By.CSS_SELECTOR, '.unified-table>tbody>tr:nth-child({})>td:nth-child({})'),
    'EMBED_LINK_BY_POSITION': (By.XPATH, '//table[@class[contains(.,"unified-table")]]/tbody/tr[{}]/td[{}]//a'),
    'CELLS': '.unified-table>tbody>tr>td'
}

MODAL = {
    'TITLE': '.modal-title',
    'MODAL_TITLE': (By.CLASS_NAME, 'modal-title'),
    'MODAL_DIALOG': (By.CSS_SELECTOR, '.modal-dialog'),
    'MODAL_BODY': '.modal-body',
    'PRIMARY_MODAL_DIALOG': (By.CSS_SELECTOR, '.primary-modal .modal-dialog'),
    'MODAL_FOOTTER': (By.CLASS_NAME, 'modal-footer'),
    'SUCCESS_MODAL': (By.CSS_SELECTOR, '.success-modal'),
    # Body
    'ROW': 'tr:nth-child({}) > td > .primary',
    'MODAL_CHECKBOX': (By.CSS_SELECTOR, '.modal-body .checkbox  input'),
    'SELECT_BOX': (By.CSS_SELECTOR, '.modal-body .Select'),
    'AVAILABLE_OPTIONS': (By.CSS_SELECTOR, '.available-list-container .selected-container'),
    'SELECTED_CONTAINER': (By.ID, 'selectedPlacement'),
    'OPTION_BY_TEXT': (By.XPATH, '//div[contains(@class, "ribbon")][text()="{}"]'),
    'REMOVE_SELECTED_OPTION_BY_TEXT': (By.XPATH, '//*[@id="selectedPlacement"]/div[./span[text()="{}"]]/button/span'),
    'SEARCHED_RESULT_CONTAINER': (By.CSS_SELECTOR, '#reportLevelSelectableContainer div.ribbon'),
    # Button Footer
    'FINISH_BTN': (By.ID, 'finish'),
    'APPLY_CHANGE_BTN': (By.XPATH, '//button[text()="Apply Change"]'),
    'DELETE_BTN': (By.XPATH, '//button[text()="Delete"]'),
    'NEXT_BTN': (By.XPATH, '//button[text()="Next"]'),
    'CLOSE': 'close',
    'YES_BTN': (By.ID, 'yesBtnConfirmModal'),
    'TIME_ZONE_UPDATE_YES_BTN': (By.ID, 'yesBtnPrimaryModal'),
    'TIME_ZONE_UPDATE_NO_BTN': (By.ID, 'noBtnPrimaryModal'),
    'WARNING_YES_BTN': (By.ID, 'yesBtnActionWarningModal'),
    'WARNING_NO_BTN': 'noBtnActionWarningModal',
    'NO_BTN': 'noBtnConfirmModal',
    'CONFIRM_BTN': (By.XPATH, '//button[text()="Confirm"]'),
    'RIBBON_BTN': (By.CSS_SELECTOR, '#reportLevelSelectableContainer button'),
    'FOOTER_BTN': (By.XPATH, '//button[text()="{button_name}"]')
}

EMPTY_STATE = {
    'EMPTY_IMAGE': (By.CLASS_NAME, 'empty-image'),
    'EMPTY_MESSAGE': (By.CLASS_NAME, 'empty-message'),
    'UPRC_EMPTY_MESSAGE': (By.CSS_SELECTOR, '.uprc-Table-empty-message'),
    'BUTTON': (By.CSS_SELECTOR, 'div.empty-table-content a')
}

URL_FRAGMENT = {
    'CHECKOUT_SUCCESS': 'opencart/index.php?route=checkout/success',
    'DASHBOARD': 'opencart/admin/index.php?route=common/dashboard',
    'ORDER_INFO': 'opencart/admin/index.php?route=sale/order/info'

}

REGEX = {
    'UUID': '[0-9a-f]{8}-[0-9a-f]{4}-[1-5][0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}'
}

NAVIGATION = {
    'ADMIN': {
        'ADMIN_KEY_LINK': (By.ID, 'adminKeyLink'),
        'ADMIN_KEY_DROPDOWN': (By.ID, 'adminDropDown')
    },
    'NAVBAR_ITEM': (By.CSS_SELECTOR, '.nav-item-{item_name}')
}

FILTER = {
    'BRAND': {
        'BRAND_SELECT': '#brand .Select-placeholder',
        'BRAND_SELECT_INPUT': '#brand .Select-input>input',
        'BRAND_OPTIONS': '#brand .Select-menu>div',
        'BRAND_SELECTED': '//div[@id="brand"]//div[@class="Select-menu"]/div[contains(text(), "{}")]',
        'BRAND_TYPE_TO_SEARCH': '//div[@id="brand"]//div[@class="Select-menu"]/div[contains(text(), "Type to Search")]',
    },
    'INITIATIVE': {
        'INITIATIVE_SELECT': '#initiativeSelect .Select-placeholder',
        'INITIATIVE_OPTIONS': '#initiativeSelect .Select-menu>div',
        'INITIATIVE_SELECTED': '//span[@id="initiativeSelect"]//div[@class="Select-menu"]/div[contains(text(), "{}")]',
        'INITIATIVE_TYPE_TO_SEARCH': '//div[@id="initiativeSelect"]//div[@class="Select-menu"]/div[contains(text(), "Type to Search")]'
    },
    'USER': {
        'USER_SELECT': '#userSelect .Select-placeholder',
        'USER_SELECT_INPUT': (By.CSS_SELECTOR, '#userSelect .Select-input>input'),
        'USER_OPTIONS': '#userSelect .Select-menu>div',
        'USER_SELECTED': '//span[@id="userSelect"]//div[@class="Select-menu"]/div[contains(text(), "{}")]',
        'USER_STATUS_INPUT': (By.CSS_SELECTOR, '#userStatus .Select-input>input'),
        'USER_FILTER_VALUE': '//*[@id="userSelect"]/div/div/div[1]'
    },
    'COMPANY': {
        'COMPANY_STATUS_INPUT': (By.CSS_SELECTOR, '#companyStatusListPage .Select-input>input'),
        'COMPANY_STATUS_SELECT': (By.CSS_SELECTOR, '#companyStatusListPage .Select-placeholder'),
        'COMPANY_STATUS_OPTIONS': '#companyStatusListPage .Select-menu>div',
        'COMPANY_STATUS_SELECTED': './/*[@id="companyStatusListPage"]//div[@class="Select-menu"]/div[contains(text(), "{}")]',
        'COMPANY_SELECT': (By.CSS_SELECTOR, '#companySelect .Select-placeholder')
    },
    'CUSTOM_METRIC': {
        'CUSTOM_METRIC_STATUS_INPUT': (By.CSS_SELECTOR, '#metrics_status .Select-input>input'),
    },
    'OPTIMIZATION_GOAL':
        {
            'OPTIMIZATION_SELECT': (By.XPATH, '//div[@class="Dropdown-control"]'),
            'OPTIMIZATION_MENU_SELECT': (By.XPATH, '//div[@class="Dropdown-menu"]//div[text()="{}"]'),
            'OPTIMIZATION_OPTION_SELECT': (By.XPATH, '//div[@class="Dropdown-menu"]/div[@class="group"]//div[text()="{}"]'),
        }
}

ANIMATION = {
    'LOADING': (By.CSS_SELECTOR, '.fa.fa-spinner.fa-spin.loading-icon')
}

PAGING = {
    'RECORD_TOTAL': (By.CSS_SELECTOR, '.pagination-results>span:nth-child(6)'),
    'RECORD_FROM': '.pagination-results>span:nth-child(2)',
    'RECORD_TO': '.pagination-results>span:nth-child(4)',
    'NEXT_PAGE_BTN': '.pagination>li:nth-child(2)>a',
    'DISABLE_NEXT_PAGE_BTN': (By.CSS_SELECTOR, '.pagination li[name="next"][class="disabled"]'),
    'DISABLE_PREVIOUS_PAGE_BTN': (By.CSS_SELECTOR, '.pagination li[name="prev"][class="disabled"]'),
    'PREVIOUS_PAGE_BTN': '.pagination>li:nth-child(1)>a'
}

# Following the new structure of select object from NEW UI of UnifiedSelected.jsx
ENTITY_FILTER = {
    'BRAND': 'brandSelect',
    'INITIATIVE': 'initiativeSelect',
    'USER': 'userSelect',
    'COMPANY': 'companyStatusListPage',
    'VIEW': 'viewSelect',
}

DROP_DOWN = {
    'SELECT': '#{} .Select-placeholder',
    'SELECT_INPUT': '#{} .Select-input>input',
    'MENU': '#{} .Select-menu',
    'OPTIONS': '#{} .Select-menu>div',
    'OPTION_SELECTED': '//span[@id="{}"]//div[@class="Select-menu"]/div[text()="{}"]',
    'TYPE_TO_SEARCH': '//span[@id="{}"]//div[@class="Select-menu"]/div[contains(text(), "Type to Search")]',
    'CLEAR_VALUE': '#{} .Select-clear',
    'ARROW_DOWN': '.fa.fa-chevron-down.select-arrow-down',
    'COMPANY_STATUS': (By.ID, 'companyStatusListPage')
}

UL_DROP_DOWN = {
    'OPTIONS': (By.CSS_SELECTOR, '.{ul_dropdown_locator} .dropdown-menu a'),
    'SELECT_OPTION_BY_NAME': (By.XPATH, '//ul[@class="dropdown-menu"]//li//a[contains(text(),"{option}")]')
}
LOADING_ICON = (By.ID, 'loadingIcon')
LOADING_SPINNER = (By.CSS_SELECTOR, '[class="fa fa-spinner fa-spin"], .spinner')
UNIFIED_LOGO_IMG = '#navLogo'
TYPE_TO_SEARCH = (By.XPATH, '//div[@class="Select-menu"]/div[contains(text(), "Type to Search")]')

CHART = {
    'HIGHCHARTS': (By.CSS_SELECTOR, '.highcharts-container')
}

SEARCH_BOX = (By.CSS_SELECTOR, '.form-control.form-search')
EMBED_LINK = (By.CSS_SELECTOR, '.external-link')
EXPANDABLE_ICON = (By.CSS_SELECTOR, '.fa-plus-circle')
CREATE_INITIATIVE_PAGE = {
    'BRAND_CURRENT_SELECT': (By.CSS_SELECTOR, '.columns-main .form-group .form-control:nth-child(1)')
}
RIGHT_TRAY = {
    'HEADER': {
        'OPEN_COMPLETED_ICON': (By.CSS_SELECTOR, '.right-tray.open .opened'),
        'H3_HEADER': (By.ID, 'tray-title-{}'),
        'CLOSE': (By.ID, 'close-x-{}')
    },
    'FOOTER_BTN': (By.ID, 'btn_{btn_name}-{tray_name}'),
    'BTN_CREATE_INITIATIVE_AND_LINE_ITEM': (By.ID, 'createInitiativeAndLineItem'),
    'BTN_SAVE_CHANGE': (By.ID, 'btn_apply_change-{tray_name}'),
    'BODY': {
        'BRAND_SELECT': (By.CSS_SELECTOR, '#rightTrayBrandSelect .Select-placeholder'),
        'BRAND_CURRENT_SELECT': (By.CSS_SELECTOR, '#initiatives .form-control'),
        'INITIATIVE_NAME': (By.ID, 'initiativeName-initiatives'),
        'INITIATIVE_DROPDOWN': (By.CSS_SELECTOR, '#initiativeSelectCreateLineItem .Select-placeholder'),
        'PUBLISHER_SELECT': (By.CSS_SELECTOR, '#pacingDashPublisherSelect .Select-placeholder'),
        'MARKET_SELECT': (By.CSS_SELECTOR, '#market .Select'),
        'CODIFICATION': (By.ID, 'codification-{}'),
        'CODIFICATION_INPUT': (By.ID, 'codificationInput-{}'),
        'CURRENCY_SELECT': (By.ID, 'currency-{}'),
        'CURRENCY_CURRENT_SELECTED': (By.CSS_SELECTOR, '#currency-{} .Select-placeholder'),
        'RECORD_FEE':  {
            'RECORD_FEE_CHECKBOX': (By.CSS_SELECTOR, 'input[name*="record"]'),
            'FEE_TYPE_DROPBOX': (By.CSS_SELECTOR, 'input[name*="feeType"]+div .Select-value-label, input[name*="feeType"]+div .Select-placeholder'),
            'FEE_TYPE_DISABLE_INPUT': (By.CSS_SELECTOR, 'input[name*="feeType"]:disabled'),
            'FEE_PERCENTAGE': (By.ID, 'feePercentage'),
            'GROSS_BUDGET': (By.ID, 'grossBudget'),
            'FEE_AMOUNT': (By.ID, 'feeAmount'),
            'MEDIA_SPEND': (By.ID, 'mediaSpend'),
        },
    }
}

UPRC_RIGHT_TRAY = {
    'HEADER': {
        'OPEN_COMPLETED_ICON': (By.CSS_SELECTOR, '.uprc-Drawer.is-open'),
        'H3_HEADER': (By.ID, '{tray_name}Title'),
        'CLOSE_BUTTON': (By.CSS_SELECTOR, '.uprc-Drawer-close')
    },
    'FOOTER_BTN': (By.ID, '{tray_name}{btn_name}Button'),
    'BODY': {
        'INITIATIVE_NAME': (By.ID, 'initiativeName'),
        'CODIFICATION': (By.CSS_SELECTOR, '#{tray_name}Codification .codification-label'),
        'CODIFICATION_INPUT': (By.CSS_SELECTOR, '#{tray_name}Codification > div > input'),
        'CURRENCY_SELECT': (By.CSS_SELECTOR, '#{tray_name}CurrencySelect .Select-control'),
        'CURRENCY_SELECTED': (By.CSS_SELECTOR, '#{tray_name}CurrencySelect .Select-value'),
        'MARKET_SELECT': (By.ID, 'react-select-4--value')
    }

}

CALENDAR = {
    'DATE_PICKER_SELECT': (By.CSS_SELECTOR, '.daterangepicker-container'),
    # Left calendar
    # ==================== Start Date
    'START_DAY_ACTIVE': (By.CSS_SELECTOR, '.available.active.start-date'),
    'START_MONTH_ACTIVE': (By.CSS_SELECTOR, '.daterangepicker>div:nth-child(3) .monthselect>option[selected="selected"]'),
    'START_YEAR_ACTIVE': (By.CSS_SELECTOR, '.daterangepicker>div:nth-child(3) .yearselect>option[selected="selected"]'),
    'START_DAY_SELECTED': (By.XPATH, '//div[@class="calendar second left"]//tbody//td[text()="{}"]'),
    'START_MONTH_SELECT': (By.CSS_SELECTOR, '.calendar.second.left .monthselect'),
    'START_MONTH_SELECTED': (By.XPATH, '//div[@class="calendar second left"]//thead/tr[1]/th[2]/select[1]/option[text()="{}"]'),
    'START_YEAR_SELECT': (By.CSS_SELECTOR, '.calendar.second.left .yearselect'),
    'START_YEAR_SELECTED': (By.XPATH, '//div[@class="calendar second left"]//thead/tr[1]/th[2]/select[2]/option[text()="{}"]'),
    # ===================== End Date
    'END_DAY_ACTIVE': (By.CSS_SELECTOR, '.available.active.end-date'),
    'END_MONTH_ACTIVE': (By.CSS_SELECTOR, '.daterangepicker>div:nth-child(2) .monthselect>option[selected="selected"]'),
    'END_YEAR_ACTIVE': (By.CSS_SELECTOR, '.daterangepicker>div:nth-child(2) .yearselect>option[selected="selected"]'),
    'END_DAY_SELECTED': (By.XPATH, '//div[@class="calendar first right"]//tbody//td[text()="{}"]'),
    'END_MONTH_SELECTED': (By.XPATH, '//div[@class="calendar first right"]//thead/tr[1]/th[2]/select[1]/option[text()="{}"]'),
    'END_MONTH_SELECT': (By.CSS_SELECTOR, '.calendar.first.right .monthselect'),
    'END_YEAR_SELECTED': (By.XPATH, '//div[@class="calendar first right"]//thead/tr[1]/th[2]/select[2]/option[text()="{}"]'),
    'END_YEAR_SELECT': (By.CSS_SELECTOR, '.calendar.first.right .yearselect'),
    # Right calendar
    # ===================== Options of calendar such as Lifetime, Today...
    'DATE_PICKER_SELECTED': (By.XPATH, '//div[@class="ranges"]/ul/li[text()="{}"]'),
    'DATE_PICKER_OK_BTN': (By.CSS_SELECTOR, '.daterangepicker .applyBtn')
}

UPRC_CALENDAR = {
    'INPUT_DATE_PICKER_SELECT': (By.CSS_SELECTOR, '.uprc-InputDateRange'),
    'INPUT_DATE_RANGE_PRESETS': (By.CSS_SELECTOR, '.uprc-InputDateRange-presets .btn-sm')
}
