import string
import random

from behave import *
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

from acceptance.locators.free_agent_tracker_page_locator import FreeAgentTrackerPageLocators
from acceptance.locators.home_page_locator import HomePageLocators
from acceptance.locators.standings_page_locator import StandingsPageLocators
from acceptance.page_models.free_agent_tracker_page_model import FreeAgentTrackerPage

use_step_matcher('re')


@When('click "Standings" on the menu')
def step_impl(context):
    context.browser.find_element(*HomePageLocators.standings_menu).click()
    eastern_conference = context.browser.find_element(*StandingsPageLocators.eastern_conference)
    eastern_conference.is_displayed()


@When('click on "(.*)" on the menu')
def step_impl(context, item):
    menu_item = context.browser.find_element(By.LINK_TEXT, item)
    menu_item.is_displayed()
    menu_item.click()


@When('click "Players" on the menu')
def step_impl(context):
    context.browser.find_element(*HomePageLocators.players_menu).click()


@When('I click on "Fire Agent Tracker"')
def step_impl(context):
    free_agent_tracker = context.browser.find_element(*FreeAgentTrackerPageLocators.free_agent_tracker_link)
    free_agent_tracker.is_displayed()
    free_agent_tracker.click()


@When('I select the "(.*)" for Availability')
def step_impl(context, text):
    select = Select(context.browser.find_element(*FreeAgentTrackerPageLocators.availability_dropdown))
    select.select_by_visible_text(text)


@When('I search a valid the a "(.*)"')
def step_impl(context, player_name, i=0):
    if player_name == "valid":
        expected_name = context.browser.find_elements(*FreeAgentTrackerPageLocators.name_data)[i].text
        search_box = context.browser.find_element(*FreeAgentTrackerPageLocators.name_search_box)
        search_box.clear()
        WebDriverWait(context.browser, timeout=2)
        search_box.send_keys(expected_name)
        WebDriverWait(context.browser, timeout=2)
        actual_name_data = context.browser.find_elements(*FreeAgentTrackerPageLocators.name_data)
        assert actual_name_data[i].text == expected_name, f'{expected_name} is not = {actual_name_data[i].text}'

    elif player_name == "invalid":
        letters = string.ascii_letters.lower()
        invalid_name_data = ''.join(random.choice(letters) for i in range(10))
        search_box = context.browser.find_element(*FreeAgentTrackerPageLocators.name_search_box)
        search_box.clear()
        WebDriverWait(context.browser, timeout=2)
        search_box.send_keys(invalid_name_data)
        WebDriverWait(context.browser, timeout=2)
        error_message = context.browser.find_element(*FreeAgentTrackerPageLocators.no_matched_player_error_message)
        assert error_message.text == 'NO PLAYERS MATCHED YOUR SELECTED FILTERS', f'{ error_message.text} is not = NO PLAYERS MATCHED YOUR SELECTED FILTERS'
