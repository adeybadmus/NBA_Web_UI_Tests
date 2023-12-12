from behave import *
from selenium import webdriver
from acceptance.page_models.free_agent_tracker_page_model import FreeAgentTrackerPage
from acceptance.page_models.home_page_model import HomePage

use_step_matcher('re')


@given('that Nba website is loaded')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = HomePage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()


@when('I am on the HomePage')
def step_impl(context):
    expected_url = 'https://www.nba.com/'
    assert context.browser.current_url == expected_url

@given('I am  on the players traditional page')
def step_impl(context):
    context.browser = webdriver.Chrome()
    page = FreeAgentTrackerPage(context.browser)
    page.driver.get(page.url)
    context.browser.maximize_window()

    expected_url = 'https://www.nba.com/players/free-agent-tracker/2023'
    assert context.browser.current_url == expected_url





