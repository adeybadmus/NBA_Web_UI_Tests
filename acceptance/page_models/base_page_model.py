from acceptance.locators.base_page_locator import BasePageLocators
from acceptance.locators.home_page_locator import HomePageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @property
    def url(self):
        return 'https://www.nba.com'

    @property
    def title(self):
        return self.driver.find_element(*BasePageLocators.TITLE)
