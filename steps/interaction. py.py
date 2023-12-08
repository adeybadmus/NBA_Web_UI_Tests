from behave import *
from selenium.webdriver.common.by import By

from acceptance.locators.home_page_locator import HomePageLocators
from acceptance.locators.standings_page_locator import StandingsPageLocators

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
