from selenium.webdriver.common.by import By


class FreeAgentTrackerPageLocators:
    free_agent_tracker_link = By.LINK_TEXT, 'Free Agent Tracker'
    availability_dropdown = By.CSS_SELECTOR, 'select[name = "Availability"]'
    free_agent_tracker_table = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"]'
    news_data = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"] tr td:nth-child(11)'
    name_data = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"] tr td:nth-child(1)'
    name_search_box = By.XPATH, '*//label[@class="Search_label__InrvZ"]//input'
    no_matched_player_error_message = By.XPATH, '*//section//div[text()="No players matched your selected filters"]'
    old_team_filter = By.CSS_SELECTOR, 'select[name="OldTeam"]'
    chicago_bulls = By.XPATH, '*//select[@name="OldTeam"] /option[text()="Chicago Bulls"]'
    old_team_logo = By.XPATH, '*//table/tbody/tr[1]/td[5]/a'
    miami_heat = By.XPATH, '*//select[@name="OldTeam"] /option[text()="Miami Heat"]'
    new_team_filter = By.CSS_SELECTOR, 'select[name="NewTeam"]'
    la_clippers = By.XPATH, '*//select[@name="NewTeam"] /option[text()="LA Clippers"]'
    new_team_logo = By.XPATH, '*//table/tbody/tr[1]/td[6]/a'
    player_position_filter = By.XPATH, '*//select[@name="PlayerPosition"]'
    guard = By.XPATH, '*//select[@name="PlayerPosition"] /option[text()="Guard"]'
    position_record = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"] tr td:nth-child(2)'
