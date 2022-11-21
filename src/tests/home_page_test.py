import unittest
from selenium import webdriver
from pages.home_page import HomePage


class HomePageTest(unittest.TestCase):
    def __init__(self, driver: webdriver.Chrome, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.driver = driver
        self.home_page = HomePage(self.driver)

    def test_select_class(self) -> None:
        self.home_page.select_class()


if __name__ == '__main__':
    unittest.main()
