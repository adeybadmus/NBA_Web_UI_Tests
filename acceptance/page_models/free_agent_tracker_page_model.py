from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.page_models.base_page_model import BasePage


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


