# from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
# from time import sleep
# import random
# from pyvirtualdisplay import Display
# from selenium.webdriver.common.action_chains import ActionChains

# def remove_last_group():
#     groups_action_wrap = driver.find_element_by_id('group_actions_wrap')
#     ActionChains(driver).move_to_element(groups_action_wrap)
#     groups_action_wrap.click()
#     sleep(1)
#     group_actions = driver.find_element_by_class_name('group_actions_item')
#     group_actions[-1].click()

# action_buttons = driver.find_elements_by_css_selector('.fw_like_link.fl_l') or\
#                 driver.find_elements_by_id('pv_like_wrap')
# if action_buttons:
#     action_buttons[0].click()
#     sleep(random.randrange(5, 7, 1))

from init import init
from random import choice
from login import *

driver, url_performer_map = init()

VK('89134113493', 'chan5-rusw$j#huS4e4a', driver).login()
AdSocial(driver).login()

while True:
    url = choice(list(url_performer_map.keys()))
    driver.get(url)
    url_performer_map[url].perform()
