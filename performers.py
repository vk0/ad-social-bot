from utils import click, open_new_window
from random import randrange
from abc import ABCMeta, abstractmethod
from time import sleep


class TaskPagePerformer:
    __metaclass__ = ABCMeta

    after_perform_delay_min_s = 3
    after_perform_delay_max_s = 7
    perform_interval_s = 1

    def __init__(self, driver):
        self._driver = driver
        self.__main_window = driver.current_window_handle  # assume main window focused

    def perform(self):
        perform_buttons = self._driver.find_elements_by_css_selector('.action-bar > .openTask.btn')
        for button in perform_buttons:
            task_window = click(self._driver, button)
            if not task_window:
                continue
            self._driver.switch_to.window(task_window)
            task_url = self._driver.current_url
            print(task_url)
            self._perform_task()
            self._driver.close()
            self._driver.switch_to.window(self.__main_window)
            sleep(randrange(TaskPagePerformer.after_perform_delay_min_s,
                            TaskPagePerformer.after_perform_delay_max_s,
                            1))
            task_window = open_new_window(self._driver, task_url)
            self._driver.switch_to.window(task_window)
            self._rollback()
            self._driver.close()
            self._driver.switch_to.window(self.__main_window)
            sleep(TaskPagePerformer.perform_interval_s)

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

    def _rollback(self):
        self._perform_task()