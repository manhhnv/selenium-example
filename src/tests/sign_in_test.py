import unittest
from selenium import webdriver
from pages.sign_in_page import SignInPage


class SignInTest(unittest.TestCase):
    url = ''

    def __init__(self, driver: webdriver.Chrome, methodName: str = ...) -> None:
        super().__init__(methodName)
        self.driver = driver

    def setUp(self) -> None:
        self.driver.get(self.url)
        self.sign_in_page = SignInPage(self.driver)

    def test_sign_in(self):
        self.sign_in_page.sign_in()


if __name__ == '__main__':
    unittest.main()
