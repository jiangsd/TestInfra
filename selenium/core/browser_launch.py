from selenium import webdriver


def get_driver(browser_name, headless=False):
    return get_local_driver(browser_name, headless)

def get_local_driver(
        browser_name, headless):
    if browser_name == "firefox":
        driver = webdriver.Firefox()
    elif browser_name == "chrome":
        driver = webdriver.Chrome()
    else:
        raise Exception(
            "%s is not a valid browser option for this system!" % browser_name)
    
    return driver
