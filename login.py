from time import sleep


class VK:
    delay_after_login_s = 2

    def __init__(self, login, password, driver):
        self.__login = login
        self.__password = password
        self.__driver = driver

    def login(self):
        print('VK login...')
        self.__driver.get('http://vk.com')
        email_field = self.__driver.find_element_by_id('quick_email')
        pass_field = self.__driver.find_element_by_id('quick_pass')
        login_button = self.__driver.find_element_by_id('quick_login_button')

        email_field.send_keys(self.__login)
        pass_field.send_keys(self.__password)
        login_button.click()
        sleep(VK.delay_after_login_s)
        print('Success!')


class AdSocial:
    delay_after_login_s = 2

    def __init__(self, driver):
        self.__driver = driver
        self.__use_vk_to_login_button_selector = 'a[data-uloginbutton="vkontakte"].btn.btn-white.btn-big.btn-round'

    def login(self):
        print('Ad social login...')
        self.__driver.get('http://ad-social.org/')
        use_vk_to_login_button = self.__driver.find_element_by_css_selector(self.__use_vk_to_login_button_selector)
        use_vk_to_login_button.click()
        sleep(VK.delay_after_login_s)
        print('Success!')
