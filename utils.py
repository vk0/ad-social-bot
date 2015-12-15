from selenium.webdriver.common.action_chains import ActionChains


def click(driver, element):
    handles_before_click = list(driver.window_handles)
    element.click()
    if driver.window_handles != handles_before_click:
        return (list(set(driver.window_handles) - set(handles_before_click)))[0]


def open_new_window(driver, url):
    handles_before_click = list(driver.window_handles)
    driver.execute_script("$(window.open('{}'))".format(url))
    if driver.window_handles != handles_before_click:
        return (list(set(driver.window_handles) - set(handles_before_click)))[0]


def move_to_element(driver, element):
    ActionChains(driver).move_to_element(element)
