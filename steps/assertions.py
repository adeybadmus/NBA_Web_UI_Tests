from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.locators.standings_page_locator import StandingsPageLocators
from acceptance.page_models.home_page_model import HomePage

use_step_matcher('re')


@Then('I should see overall information for all teams in the current regular season')
def step_impl(context):
    WebDriverWait(context.browser, timeout=2)
    ec_teams = context.browser.find_elements(*StandingsPageLocators.eastern_teams)
    assert isinstance(ec_teams, list)
    context.browser.quit()


@Then('I should navigate to the correct page for "(.*)"')
def step_impl(context, expected_item, i=0):
    list_menu_item = context.browser.find_elements(By.LINK_TEXT, expected_item)
    actual_url = context.browser.current_url

    if expected_item == "In-Season Tournament":
        assert "in-season-tournament/2023" in actual_url, f'"in-season-tournament/2023" is not contained in {actual_url}'

    elif expected_item == "Future Starts Now":
        assert "future-starts-now" in actual_url, f'{expected_item} is not contained in {actual_url}'

    elif expected_item == "NBA Fitness":
        assert "nba-fitness".lower() in actual_url, f'{expected_item} is not contained in {actual_url}'

    elif list_menu_item[i].text == expected_item:
        assert expected_item.lower() in actual_url, f'{expected_item} is not contained in {actual_url}'

    context.browser.quit()


@Then('the New Team detail must be displayed for "(.*)" and they should not change')
def step_impl(context, text, i=0):
    WebDriverWait(context.browser, timeout=2)
    new_team_data = context.browser.find_elements(*FreeAgentTrackerPageLocators.news_data)

    if text == "Signed":
        assert new_team_data[i].text is not None, f'{new_team_data[i].text} is null'

    elif text == "Unsigned":
        assert 'sign' not in new_team_data[i].text.lower(), f'sign not in {new_team_data[i].text}'

    context.browser.quit()


@Then('I should see the record for "(.*)" player name displayed and they should not change')
def step_impl(context, player_name, i=0):

    name_data = context.browser.find_elements(*FreeAgentTrackerPageLocators.name_data)

    if player_name == "valid":
        name_data_value = context.browser.find_elements(*FreeAgentTrackerPageLocators.name_data)[i].text

        assert name_data[i].text == name_data_value, f'{name_data_value} is not = {name_data[i].text}'

    elif player_name == "invalid":
        error_message = context.browser.find_element(*FreeAgentTrackerPageLocators.no_matched_player_error_message)
        assert error_message.text == 'No players matched your selected filters'

    context.browser.quit()

