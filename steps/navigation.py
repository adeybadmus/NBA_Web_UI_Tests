import time

from behave import *
from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from acceptance.locators.standings_page_locator import StandingsPageLocators
from acceptance.page_models.base_page_model import BasePage
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




