from selenium.webdriver.common.by import By


class TraditionStatsPageLocators:
    season_filter = By.XPATH, '*//div/div/div[1]/label/div'
    season_filter_value = By.XPATH, '*//select/option[text()="2021-22"]'

