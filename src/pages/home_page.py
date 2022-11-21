from selenium import webdriver
from pages.base_page import BasePage
from locators.home_page_locator import HomePageLocator
from time import sleep


class HomePage(BasePage):
    def __init__(self, driver: webdriver.Chrome) -> None:
        super().__init__(driver)

    def select_class(self):
        self.dom_utils.\
            wait_element_presence(HomePageLocator.INFINITE_SCROLL_CPN)
        sleep(10)
