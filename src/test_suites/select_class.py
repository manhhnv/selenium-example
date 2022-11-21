import unittest
from selenium import webdriver
from tests.sign_in_test import SignInTest
from tests.home_page_test import HomePageTest


def suite():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    test_suite = unittest.TestSuite()
    test_suite.addTest(SignInTest(driver, 'test_sign_in'))
    test_suite.addTest(HomePageTest(driver, 'test_select_class'))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())
