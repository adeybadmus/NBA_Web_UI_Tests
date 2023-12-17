from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.page_models.base_page_model import BasePage
from selenium.webdriver.common.by import By
import string
import random


class FreeAgentTrackerPage(BasePage):
    @property
    def url(self):
        return super(FreeAgentTrackerPage, self).url + '/players'

    @property
    def free_agent_tracker_link(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.free_agent_tracker_link).click()

    @property
    def free_agent_tracker_table(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.free_agent_tracker_table)

    @property
    def news_data(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.news_data)

    @property
    def name_data(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.name_data)

    @property
    def name_search_box(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.name_search_box)

    @property
    def no_matched_player_error_message(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.no_matched_player_error_message)

    @property
    def old_team_filter(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.old_team_filter)

    @property
    def chicago_bulls(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.chicago_bulls)

    @property
    def miami_heat(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.miami_heat)

    @property
    def new_team_filter(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.new_team_filter)

    @property
    def la_clippers(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.la_clippers)

    @property
    def player_position(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.player_position)

    @property
    def player_position_filter(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.player_position_filter)

    @property
    def guard(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.guard)

    def filter_by_old_team(self, old_team):
        old_filters = self.old_team_filter
        old_filters.is_enabled()
        old_filters.click()
        old_team_value_element = f'*//select[@name="OldTeam"] /option[text()={old_team}]'
        old_team_value = self.driver.find_element(By.XPATH, old_team_value_element)
        old_team_value.click()
        old_team_value.is_selected()

    def filter_by_new_team(self, new_team_value):
        advance_filters = self.new_team_filter
        advance_filters.is_displayed()
        advance_filters.click()
        new_team_value_element = f'*//select[@name="NewTeam"] /option[text()={new_team_value}]'
        new_team = self.driver.find_element(By.XPATH, new_team_value_element)
        new_team.click()
        new_team.is_selected()

    def filter_by_player_position(self, position_value):
        player_position_filter = self.player_position_filter
        player_position_filter.is_displayed()
        player_position_filter.click()
        player_position_value_element = f'*//select[@name="PlayerPosition"] /option[text()={position_value}]'
        player_position = self.driver.find_element(By.XPATH, player_position_value_element)
        player_position.click()
        player_position.is_selected()

    def search_valid_player(self, expected_name_data):
        name_search_box = self.name_search_box
        name_search_box.is_displayed()
        name_search_box.clear()
        name_search_box.send_keys(expected_name_data)

    def search_invalid_player(self):
        letters = string.ascii_letters.lower()
        invalid_name_data = ''.join(random.choice(letters) for i in range(10))
        name_search_box = self.name_search_box
        name_search_box.is_displayed()
        name_search_box.clear()
        name_search_box.send_keys(invalid_name_data)

