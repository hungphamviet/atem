def before_all(context):
    pass


def before_feature(context, feature):
    pass


def before_scenario(context, scenario):
    context = init_browser_session(context)
    context.browser.maximize_window()


def init_browser_session(context):
    from features.browser.browsers import Browser
    context.browser = Browser().make_browser()
    return context


def after_scenario(context, scenario):
    context.browser.quit()


def after_all(context):
    pass
