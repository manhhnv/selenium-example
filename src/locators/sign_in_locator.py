from selenium.webdriver.common.by import By


class SignInPageLocator(object):
    SIGN_IN_FORM = (By.TAG_NAME, "form")
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    SIGN_IN_BTN = (By.XPATH, "//form//button[@type='submit']")
