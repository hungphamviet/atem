from selenium.webdriver.support.select import By

URL = {
    'ADMIN': '/admin',
    'SHOPPING': '/index.php',
    'LOGOUT': '/logout'
}

LOG_IN = {
    'USERNAME_INPUTBOX': (By.NAME, 'username'),
    'PASSWORD_INPUTBOX': (By.NAME, 'password')
}

FORGOT_PAGE = {
    'EMAIL_INPUTBOX': (By.NAME, 'email'),
}

REGISTER_PAGE = {
    'EMAIL': (By.NAME, 'email'),
    'TEMP_PASSWORD': (By.NAME, 'confirmationId'),
    'PASSWORD': (By.NAME, 'password'),
    'CONFIRM_PASSWORD': (By.NAME, 'confirmPassword'),
    'FIRST_NAME': (By.ID, 'firstName'),
    'LAST_NAME': (By.ID, 'lastName'),
    'ERROR_LIST': (By.CSS_SELECTOR, '.alert.alert-danger li')
}
