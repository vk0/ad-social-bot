from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import random
from pyvirtualdisplay import Display

display = Display(visible=1, size=(800, 600))
display.start()

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

print('Loggin to ad social')

driver.get('http://ad-social.org/')
sleep(5)

use_vk_to_login_button = driver.find_element_by_css_selector(
    'a[data-uloginbutton="vkontakte"].btn.btn-white.btn-big.btn-round')
use_vk_to_login_button.click()
sleep(3)

print('Logged')

while True:
    driver.get('http://ad-social.org/vk/earn?type=like')
    sleep(3)
    perform_buttons = driver.find_elements_by_css_selector('.action-bar > .openTask.btn')
    main_window = driver.current_window_handle
    if perform_buttons:
        for button in perform_buttons:
            button.click()
            sleep(3)
            window_handles = list(driver.window_handles)
            window_handles.remove(main_window)
            if not window_handles:
                continue
            driver.switch_to.window(window_handles[0])

            action_buttons = driver.find_elements_by_css_selector('.fw_like_link.fl_l') or\
                            driver.find_elements_by_id('pv_like_wrap')
            if action_buttons:
                action_buttons[0].click()
                sleep(random.randrange(5, 7, 1))
            sleep(2)
            driver.close()
            sleep(1)
            driver.switch_to.window(main_window)
            print(driver.find_element_by_css_selector('a[href="/profile/balance"] > span').text)
    else:
        print('No tasks. Sleep 2 minute zzzzzzzz')
        sleep(120)

#exit_button = driver.find_elements_by_css_selector('a[href="http://ad-social.org/dashboard/logout"]')[0]
#exit_button.click()

