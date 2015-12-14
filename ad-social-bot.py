from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from pyvirtualdisplay import Display
from selenium.webdriver.common.action_chains import ActionChains

def remove_last_group():
    """driver.find_element_by_tag_name('body').send_keys(Keys.ALT + '2')
    groups = driver.find_elements_by_css_selector('#groups_list_groups .group_row_labeled > a')
    sleep(3)
    print(len(groups))
    if len(groups) > 1:
        groups[-1].click()
        #driver.find_element_by_id('group_actions_wrap').click()
        #sleep(1)
        #group_actions = driver.find_element_by_class_name('group_actions_item')
        #group_actions[-1].click()
    driver.find_element_by_tag_name('body').send_keys(Keys.ALT + '1')"""
    groups_action_wrap = driver.find_element_by_id('group_actions_wrap')
    ActionChains(driver).move_to_element(groups_action_wrap)
    groups_action_wrap.click()
    sleep(1)
    group_actions = driver.find_element_by_class_name('group_actions_item')
    group_actions[-1].click()


#display = Display(visible=1, size=(800, 600))
#display.start()

driver = webdriver.Firefox()

print('Loggin to vk')

driver.get('http://vk.com')
email_field = driver.find_element_by_id('quick_email')
pass_field = driver.find_element_by_id('quick_pass')
login_button = driver.find_element_by_id('quick_login_button')

email_field.send_keys('89134113493')
pass_field.send_keys('chan5-rusw$j#huS4e4a')
login_button.click()
sleep(2)

print('Logged')

main_window = driver.current_window_handle

#driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't')
#driver.get('http://vk.com/groups')
#driver.find_element_by_tag_name('body').send_keys(Keys.ALT + '1')

print('Loggin to ad social')

driver.get('http://ad-social.org/')
sleep(5)

use_vk_to_login_button = driver.find_element_by_css_selector(
    'a[data-uloginbutton="vkontakte"].btn.btn-white.btn-big.btn-round')
use_vk_to_login_button.click()
sleep(3)

print('Logged')

sleep(3)

while True:
    driver.get('http://ad-social.org/vk/earn?soc=vk&type=group')
    sleep(3)
    perform_buttons = driver.find_elements_by_css_selector('.action-bar > .openTask.btn')

    for button in perform_buttons:
        button.click()
        sleep(3)
        window_handles = list(driver.window_handles)
        window_handles.remove(main_window)
        if not window_handles:
            continue
        driver.switch_to.window(window_handles[0])
        print(driver.current_url)

        action_buttons = driver.find_elements_by_id('subscribe_button') or\
                        driver.find_elements_by_css_selector('#group_like_module > .flat_button.button_big.button_wide') or\
                        driver.find_elements_by_css_selector('.fw_like_link.fl_l') or\
                        driver.find_elements_by_id('pv_like_wrap')
        if action_buttons:
            action_buttons[0].click()
            driver.switch_to.window(main_window)
            sleep(random.randrange(5, 7, 1))
        sleep(2)
        driver.switch_to.window(window_handles[0])
        sleep(1)
        remove_last_group()
        sleep(1)
        driver.close()
        driver.switch_to.window(main_window)
        sleep(1)

        print(driver.find_element_by_css_selector('a[href="/profile/balance"] > span').text)

#exit_button = driver.find_elements_by_css_selector('a[href="http://ad-social.org/dashboard/logout"]')[0]
#exit_button.click()

