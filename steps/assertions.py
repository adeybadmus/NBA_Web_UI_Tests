from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from behave import *
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
