from .base_page import BasePage
from .locators.standings_page_locators import StandingsPageLocators

# StandingsPage class to handle standings-related functionality
class StandingsPage(BasePage):
    # Method to verify standings are displayed
    def verify_standings_displayed(self):
        assert self.driver.find_element(*StandingsPageLocators.STANDINGS_TABLE).is_displayed()
