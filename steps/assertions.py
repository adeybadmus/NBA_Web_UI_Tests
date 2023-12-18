from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *

from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.page_models.free_agent_tracker_page_model import FreeAgentTrackerPage
from acceptance.locators.standings_page_locator import StandingsPageLocators
from acceptance.page_models.home_page_model import HomePage
from acceptance.page_models.traditional_stats_page_model import TraditionalStatsPage

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
def step_impl(context, player_name):
    WebDriverWait(context.browser, timeout=2)
    if player_name == "valid":
        context.expected_name_data
        actual_name_data = context.browser.find_element(*FreeAgentTrackerPageLocators.name_data)

        assert actual_name_data.text == context.expected_name_data, f'{actual_name_data.text} is not = {context.expected_name_data}'

    elif player_name == "invalid":
        WebDriverWait(context.browser, timeout=2)
        error_message = context.browser.find_element(*FreeAgentTrackerPageLocators.no_matched_player_error_message)
        assert error_message.text == 'NO PLAYERS MATCHED YOUR SELECTED FILTERS', f'{error_message.text} is not = NO PLAYERS MATCHED YOUR SELECTED FILTERS'
    context.browser.quit()


@Then('I should see the correct stats displayed for "Chicago (.*)" and they should not change')
def step_impl(context, expected_old_team_logo, i=0):
    actual_team_logo = context.browser.find_elements(*FreeAgentTrackerPageLocators.old_team_logo)
    link = actual_team_logo[i].get_attribute('href')
    assert expected_old_team_logo.lower() in link.lower(), f'{expected_old_team_logo} is not contained in {link}'
    context.browser.quit()


@Then('I should see the correct stats displayed for "LA (.*)" and they should not change')
def step_impl(context, expected_new_team_logo, i=0):
    actual_new_team_logo = context.browser.find_elements(*FreeAgentTrackerPageLocators.new_team_logo)
    logo_link = actual_new_team_logo[i].get_attribute('href')
    assert expected_new_team_logo.lower() in logo_link.lower(), f'{expected_new_team_logo} is not contained in {logo_link}'
    context.browser.quit()


@Then('I should see the correct stats displayed for "(.*)" and they should not change')
def step_impl(context, expected_position, i=0):
    actual_position = context.browser.find_elements(*FreeAgentTrackerPageLocators.position_record)
    assert expected_position.lower() in actual_position[
        i].text.lower(), f'{expected_position.lower()} is not contained in {actual_position[i].text.lower()}'
    context.browser.quit()


@Then('I should see the Pills value equal to the correct value "(.*)"')
def step_impl(context, selected_value):
    page = TraditionalStatsPage(context.browser)
    actual_pill = page.validate_pills_value(selected_value)

    assert selected_value.lower() == actual_pill.text.lower(), f'{selected_value.lower()} != {actual_pill.text.lower()}'
    context.browser.quit()


@Then('I should see the Pills values equal to the correct values "(.*)" and "(.*)"')
def step_impl(context, selected_value1, selected_value2):
    page = TraditionalStatsPage(context.browser)
    if selected_value1 == 'In-Season Tournament':
        actual_ist_pill = context.browser.find_element(By.XPATH, '*//div/span[text()="IST"]')
        assert 'IST'.lower() == actual_ist_pill.text.lower(), f'{selected_value1.lower()} != {actual_ist_pill.text.lower()}'
    elif selected_value1 != 'In-Season Tournament':
        actual_pill1 = page.validate_pills_value(selected_value1)
        assert selected_value1.lower() == actual_pill1.text.lower(), f'{selected_value1.lower()} != {actual_pill1.text.lower()}'

    if selected_value2 == 'In-Season Tournament':
        actual_ist_pill = context.browser.find_element(By.XPATH, '*//div/span[text()="IST"]')
        assert 'IST'.lower() == actual_ist_pill.text.lower(), f'ist != {actual_ist_pill.text.lower()}'

    elif selected_value2 != 'In-Season Tournament':
        actual_pill2 = page.validate_pills_value(selected_value2)
        assert selected_value2.lower() == actual_pill2.text.lower(), f'{selected_value2.lower()} != {actual_pill2.text.lower()}'
    context.browser.quit()
