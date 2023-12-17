from selenium.webdriver.common.by import By


class StandingsPageLocators:
    eastern_conference = By.XPATH, '*//div[@class="Crom_base__f0niE"] /h2[text()="Eastern Conference"]'
    eastern_teams = By.XPATH, '*//div[@class="Crom_base__f0niE"] //table/tbody/tr'

