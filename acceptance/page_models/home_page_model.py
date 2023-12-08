from acceptance.locators.home_page_locator import HomePageLocators
from acceptance.page_models.base_page_model import BasePage


class HomePage(BasePage):
    @property
    def url(self):
        return super(HomePage, self).url + '/'

    @property
    def click_standing_menu(self):
        return self.driver.find_element(*HomePageLocators.standings_menu)

    @property
    def click_home_page_menu_item(self):
        return self.driver.find_element(*HomePageLocators.homepage_menu_item)
