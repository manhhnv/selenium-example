from selenium import webdriver
from utils.dom import DomUtils


class BasePage(object):
    max_secs = 10

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.dom_utils = DomUtils(driver)
        self.driver = driver
