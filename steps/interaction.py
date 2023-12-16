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


@When('I search a "(.*)" player name')
def step_impl(context, player_name):
    page = FreeAgentTrackerPage(context.browser)
    if player_name == "valid":
        page.name_data.is_displayed()
        context.expected_name_data = page.name_data.text
        page.name_search_box.is_displayed()
        page.name_search_box.clear()
        page.name_search_box.send_keys(context.expected_name_data)

    elif player_name == "invalid":
        letters = string.ascii_letters.lower()
        invalid_name_data = ''.join(random.choice(letters) for i in range(10))
        page.name_search_box.is_displayed()
        page.name_search_box.clear()
        page.name_search_box.send_keys(invalid_name_data)


@When('I filter by Old team values "Chicago Bulls"')
def step_impl(context):
    page = FreeAgentTrackerPage(context.browser)
    page.old_team_filter.is_displayed()
    page.old_team_filter.click()
    page.chicago_bulls.click()
    page.chicago_bulls.is_selected()


@When('I filter by New team values "LA Clippers"')
def step_impl(context):
    page = FreeAgentTrackerPage(context.browser)
    page.new_team_filter.is_displayed()
    page.new_team_filter.click()
    page.la_clippers.click()
    page.la_clippers.is_selected()


@When('I filter by Position values "Guard"')
def step_impl(context):
    page = FreeAgentTrackerPage(context.browser)
    page.player_position_filter.is_displayed()
    page.player_position_filter.click()
    page.guard.click()
    page.guard.is_selected()

