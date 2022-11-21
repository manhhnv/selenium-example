from selenium.webdriver.common.by import By


class HomePageLocator(object):
    INFINITE_SCROLL_CPN = (By.CSS_SELECTOR, ".infinite-scroll-component div")
    VIEW_BUTTON = (By.XPATH, "//button[contains(text(), 'View') and @type='button']")