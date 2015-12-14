from performers import *
from selenium import webdriver
from pyvirtualdisplay import Display


def init():
    #display = Display(visible=1, size=(800, 600))
    #display.start()

    driver = webdriver.Firefox()
    url_performer_map = {
        'http://ad-social.org/vk/earn?type=like': LikesPerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=friend': TaskPagePerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=group': TaskPagePerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=repost': TaskPagePerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=comment': TaskPagePerformer(driver),
    }
    return driver, url_performer_map
