from selenium.webdriver.common.by import By


class StandingsPageLocators:
    eastern_conference = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/section[2]/div/div[2]/h2'
    eastern_teams = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/div[2]/section[2]/div/div[2]/div[2]/table/tbody/tr'

