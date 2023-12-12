from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.page_models.base_page_model import BasePage


class FreeAgentTrackerPage(BasePage):
    @property
    def url(self):
        return super(FreeAgentTrackerPage, self).url + '/players/free-agent-tracker/2023'

    @property
    def free_agent_tracker(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.free_agent_tracker_link).click()


    @property
    def select_availability_filter(self):
        return self.driver.find_element(*FreeAgentTrackerPageLocators.availability_dropdown)

