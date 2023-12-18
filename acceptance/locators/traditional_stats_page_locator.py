from selenium.webdriver.common.by import By


class TraditionalStatsPageLocators:
    season_filter = By.XPATH, '*//div/div/div[1]/label/div'
    season_type_filter = By.XPATH, '*//div/div/div[2]/label/div'
    per_mode_filter = By.XPATH, '*//div/div/div[3]/label/div'
    season_segment_filter = By.XPATH, '*//div/div/div[4]/label/div'
    season_pill = By.XPATH, '*//div/span[text()="2016-17"]'

