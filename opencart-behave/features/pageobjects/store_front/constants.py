from selenium.webdriver.support.select import By

PRODUCT_HOME = {
    "PRODUCT_NAME": (By.LINK_TEXT, "{name}"),
    "CART": (By.ID, "cart"),
    "CHECKOUT": (By.PARTIAL_LINK_TEXT, "Checkout")
}

PRODUCT_DETAIL = {
    "PRODUCT_QUANTITY": (By.ID, "input-quantity"),
    "ADD_TO_CART": (By.ID, "button-cart")
}

PRODUCT_CHECKOUT = {
    "CHECKOUT_OPTION": (By.CSS_SELECTOR, "input[value={value}]"),
    "BUTTON_ACCOUNT": (By.ID, "button-account"),

    "PAYMENT_FIRST_NAME": (By.ID, "input-payment-firstname"),
    "PAYMENT_LAST_NAME": (By.ID, "input-payment-lastname"),
    "PAYMENT_EMAIL": (By.ID, "input-payment-email"),
    "PAYMENT_TELEPHONE": (By.ID, "input-payment-telephone"),
    "PAYMENT_ADDRESS_1": (By.ID, "input-payment-address-1"),
    "PAYMENT_CITY": (By.ID, "input-payment-city"),
    "PAYMENT_POSTCODE": (By.ID, "input-payment-postcode"),
    "PAYMENT_REGION": (By.ID, "input-payment-zone"),
    "BUTTON_GUEST": (By.ID, "button-guest"),

    "PAYMENT_METHOD_AGREE": (By.CSS_SELECTOR, "input[name=agree]"),
    "BUTTON_PAYMENT_METHOD": (By.ID, "button-payment-method"),
    "BUTTON_SHIPPING_METHOD": (By.ID, "button-shipping-method"),
    "BUTTON_CONFIRM": (By.ID, "button-confirm"),
    "CHECKOUT_SUCCESS_CONTENT": (By.CSS_SELECTOR, "div#content.col-sm-12"),

}
