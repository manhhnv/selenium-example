from selenium import webdriver
from pages.base_page import BasePage
from locators.sign_in_locator import SignInPageLocator
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class SignInPage(BasePage):

    def __init__(self, driver: webdriver.Chrome) -> None:
        super().__init__(driver)

    def sign_in(self):
        # wait for DOM rendered
        WebDriverWait(self.driver, self.max_secs)\
            .until(EC.presence_of_element_located(SignInPageLocator.SIGN_IN_FORM))

        self.type_credential()
        self.click_sign_in()
        # sleep(5)

    def type_credential(self):
        # find username input and password input
        username_ip = self.dom_utils.\
            find_element(SignInPageLocator.USERNAME_INPUT)
        pwd_ip = self.dom_utils.\
            find_element(SignInPageLocator.PASSWORD_INPUT)
        # typing
        username_ip.send_keys('username')
        pwd_ip.send_keys('password')

    def click_sign_in(self):
        # find submit button
        sign_in_btn = self.dom_utils.\
            find_element(SignInPageLocator.SIGN_IN_BTN)
        ActionChains(self.driver).click(sign_in_btn).perform()
