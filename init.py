from performers import *
from selenium import webdriver
from pyvirtualdisplay import Display


def init():
    display = Display(visible=1, size=(1200, 1000))
    display.start()

    driver = webdriver.Firefox()
    url_performer_map = {
        'http://ad-social.org/vk/earn?type=like': LikesPerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=friend': TaskPagePerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=group': CommunitiesPerformer(driver),
        # 'http://ad-social.org/vk/earn?soc=vk&type=repost': TaskPagePerformer(driver),
        'http://ad-social.org/vk/earn?soc=vk&type=comment': CommentsPerformer(driver),
    }
    return driver, url_performer_map
