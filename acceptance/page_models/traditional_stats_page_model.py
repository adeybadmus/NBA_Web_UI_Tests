from acceptance.locators.traditional_stats_page_locator import TraditionalStatsPageLocators
from acceptance.page_models.base_page_model import BasePage
from selenium.webdriver.common.by import By
import string
import random


class TraditionalStatsPage(BasePage):
    @property
    def url(self):
        return super(TraditionalStatsPage, self).url + '/stats/teams/traditional'

    @property
    def season_filter(self):
        return self.driver.find_element(*TraditionalStatsPageLocators.season_filter)

    @property
    def season_type_filter(self):
        return self.driver.find_element(*TraditionalStatsPageLocators.season_type_filter)

    @property
    def per_mode_filter(self):
        return self.driver.find_element(*TraditionalStatsPageLocators.season_type_filter)

    @property
    def season_segment_filter(self):
        return self.driver.find_element(*TraditionalStatsPageLocators.season_type_filter)

    def select_filter_value(self, filter_type,  value):
        if filter_type != 'season_segment':
            return self.driver.find_element(By.XPATH, f'*//select/option[text()="{value}"]')

        elif filter_type == 'season_segment':
            return self.driver.find_element(By.XPATH, f'*//optgroup/option[text()="{value}"]')

    def validate_pills_value(self, value):
        return self.driver.find_element(By.XPATH, f'*//div/span[text()="{value}"]')

    def filter_by_season(self, filter_type, value):
        season_filter = self.season_filter
        season_filter.is_enabled()
        season_filter.click()
        season_value = self.select_filter_value(filter_type, value)
        season_value.click()
        season_value.is_selected()

    def filter_by_season_type(self, filter_type, value):
        season_type_filter = self.season_type_filter
        season_type_filter.is_enabled()
        season_type_filter.click()
        season_type_value = self.select_filter_value(filter_type, value)
        season_type_value.click()
        season_type_value.is_selected()

    def filter_by_per_mode(self, filter_type, value):
        per_mode_filter = self.per_mode_filter
        per_mode_filter.is_enabled()
        per_mode_filter.click()
        per_mode_value = self.select_filter_value(filter_type, value)
        per_mode_value.click()
        per_mode_value.is_selected()

    def filter_by_season_segment(self, filter_type, value):
        season_segment_filter = self.season_segment_filter
        season_segment_filter.is_enabled()
        season_segment_filter.click()
        season_segment_value = self.select_filter_value(filter_type, value)
        season_segment_value.click()
        season_segment_value.is_selected()
