from utils import click, open_new_window
from random import randrange
from abc import ABCMeta, abstractmethod
from time import sleep
from captcha import CaptchaSolver
from utils import move_to_element


class TaskPagePerformer:
    __metaclass__ = ABCMeta

    before_rollback_delay_min_s = 1
    before_rollback_delay_max_s = 5
    perform_interval_s = 1
    after_perform_rollback_delay_s = 1

    def __init__(self, driver):
        self._driver = driver
        self.__main_window = driver.current_window_handle  # assume main window focused
        self.__captcha_solver = CaptchaSolver()

    def perform(self):
        perform_buttons = self._driver.find_elements_by_css_selector('.action-bar > .openTask.btn')
        for button in perform_buttons:
            task_window = click(self._driver, button)
            if not task_window:
                continue
            self._driver.switch_to.window(task_window)
            task_url = self._driver.current_url
            task_performed = self._perform_task()
            if task_performed:
                sleep(TaskPagePerformer.after_perform_rollback_delay_s)
                if self.__is_captcha_required():
                    print('Captcha detected')
                    self.__captcha_solver.solve('', self._driver)
                    print('Captcha solved')
                self._driver.close()
                self._driver.switch_to.window(self.__main_window)
                sleep(randrange(TaskPagePerformer.before_rollback_delay_min_s,
                                TaskPagePerformer.before_rollback_delay_max_s,
                                1))
                task_window = open_new_window(self._driver, task_url)
                self._driver.switch_to.window(task_window)
                self._rollback()
                sleep(TaskPagePerformer.after_perform_rollback_delay_s)
            self._driver.close()
            self._driver.switch_to.window(self.__main_window)
            print(self.__get_scores())
            sleep(TaskPagePerformer.perform_interval_s)

    def __is_captcha_required(self):
        return len(self._driver.find_elements_by_class_name('captcha')) > 0

    def __get_scores(self):
        return self._driver.find_element_by_css_selector('a[href="/profile/balance"] > span').text

    @abstractmethod
    def _perform_task(self):
        pass

    @abstractmethod
    def _rollback(self):
        pass


class LikesPerformer(TaskPagePerformer):
    def _perform_task(self):
        like_buttons = self._driver.find_elements_by_css_selector('.fw_like_link.fl_l') or\
                 self._driver.find_elements_by_id('pv_like_wrap')
        if like_buttons:
            like_buttons[0].click()
            return True
        return False

    def _rollback(self):
        self._perform_task()


class CommunitiesPerformer(TaskPagePerformer):
    delay_after_group_actions_click_s = .5
    delay_after_public_actions_click_s = .5

    def _perform_task(self):
        enter_buttons_selector = '#group_like_module > button.flat_button.button_big.button_wide'
        enter_buttons = self._driver.find_elements_by_css_selector(enter_buttons_selector)
        subscribe_buttons = self._driver.find_elements_by_id('subscribe_button')
        action_buttons = enter_buttons + subscribe_buttons
        if action_buttons:
            action_buttons[0].click()
            return True
        return False

    def _rollback(self):
        if not self.__leave_group():
            self.__leave_public()

    def __leave_group(self):
        group_actions_btns = self._driver.find_elements_by_id('group_actions_btn')
        leave_buttons_selector = '.group_actions_inner > .group_actions_item:last-child'
        leave_buttons = self._driver.find_elements_by_css_selector(leave_buttons_selector)

        if not (group_actions_btns and leave_buttons):
            return False

        move_to_element(self._driver, group_actions_btns[0])
        group_actions_btns[0].click()
        sleep(CommunitiesPerformer.delay_after_group_actions_click_s)
        leave_buttons[0].click()
        return True

    def __leave_public(self):
        public_actions_btns = self._driver.find_elements_by_class_name('public_actions_btn')
        leave_buttons_selector = '.public_actions_inner > .public_actions_item:first-child'
        leave_buttons = self._driver.find_elements_by_css_selector(leave_buttons_selector)

        if not (public_actions_btns and leave_buttons):
            return False

        move_to_element(self._driver, public_actions_btns[0])
        public_actions_btns[0].click()
        sleep(CommunitiesPerformer.delay_after_public_actions_click_s)
        leave_buttons[0].click()
        return True
