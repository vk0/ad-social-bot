from time import sleep


class CaptchaSolver:
    def solve(self, captcha_url, driver):
        while driver.find_elements_by_class_name('captcha'):
            sleep(.3)
