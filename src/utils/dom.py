from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from typing import Tuple
from typing import List


class DomUtils(object):
    max_secs = 10

    def __init__(self, driver: webdriver.Chrome) -> None:
        self.driver = driver

    def find_element(self, pair: Tuple[str, str]) -> WebElement:
        try:
            return self.driver.find_element(pair[0], pair[1])
        except NoSuchElementException:
            print('No element has DOM % %', pair[0], pair[1])
            self.driver.close()

    def find_elements(self, pair: Tuple[str, str]) -> List[WebElement]:
        try:
            return self.driver.find_elements(pair[0], pair[1])
        except NoSuchElementException:
            print('No element has DOM % %', pair[0], pair[1])
            self.driver.close()

    def wait_element_presence(self, pair: Tuple[str, str]) -> None:
        try:
            WebDriverWait(self.driver, self.max_secs).\
                until(EC.presence_of_element_located(pair))
        except NoSuchElementException:
            print('Timeout! No element has DOM % %', pair[0], pair[1])

    def wait_elements_presence(self, pair: Tuple[str, str]) -> None:
        try:
            WebDriverWait(self.driver, self.max_secs).\
                until(EC.presence_of_all_elements_located(pair))
        except NoSuchElementException:
            print('Timeout! No element has DOM % %', pair[0], pair[1])
