from .base_page import BasePage
from .locators.league_page_locators import LeaguePageLocators

# LeaguePage class to handle league-related functionality
class LeaguePage(BasePage):
    # Method to verify league is displayed
    def verify_league_displayed(self, league_name):
        assert self.driver.find_element(*LeaguePageLocators.LEAGUE_NAME(league_name)).is_displayed()

    # Method to click standings tab
    def click_standings_tab(self):
        standings_tab = self.driver.find_element(*LeaguePageLocators.STANDINGS_TAB)
        standings_tab.click()
