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
    WebDriverWait(context.browser, timeout=2)
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


@When('I search a "(.*)" player name')
def step_impl(context, player_name):
    page = FreeAgentTrackerPage(context.browser)
    if player_name == "valid":
        # expected_name_data = page.search_valid_player()
        # context.expected_name_data = expected_name_data

        name_data = page.name_data
        name_data.is_displayed()
        context.expected_name_data = name_data.text
        page.search_valid_player(context.expected_name_data)
        # name_search_box = page.name_search_box
        # name_search_box.is_displayed()
        # name_search_box.clear()
        # name_search_box.send_keys(context.expected_name_data)

    elif player_name == "invalid":
        page.search_invalid_player()


@When('I filter by Old team values (.*)')
def step_impl(context, old_team):
    page = FreeAgentTrackerPage(context.browser)
    page.filter_by_old_team(old_team)


@When('I filter by New team values (.*)')
def step_impl(context, new_team):
    page = FreeAgentTrackerPage(context.browser)
    page.filter_by_new_team(new_team)


@When('I filter by Position values (.*)')
def step_impl(context, position):
    page = FreeAgentTrackerPage(context.browser)
    WebDriverWait(context.browser, timeout=2)
    page.filter_by_player_position(position)

