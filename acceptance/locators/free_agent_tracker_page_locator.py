from selenium.webdriver.common.by import By


class FreeAgentTrackerPageLocators:
    free_agent_tracker_link = By.LINK_TEXT, 'Free Agent Tracker'
    availability_dropdown = By.CSS_SELECTOR, 'select[name = "Availability"]'
    free_agent_tracker_table = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"]'
    news_data = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"] tr td:nth-child(11)'
    name_data = By.CSS_SELECTOR, 'table[class = "Crom_table__p1iZz"] tr td:nth-child(1)'
    name_search_box = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/main/div[3]/section/div/div[2]/div[1]/div/div[1]/div[1]/label/div/input'
    no_matched_player_error_message = By.XPATH, '//*[@id="__next"]/div[2]/div[2]/main/div[3]/section/div/div[2]/div[1]/div/div[2]'
