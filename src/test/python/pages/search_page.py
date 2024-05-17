from .base_page import BasePage
from .locators.search_page_locators import SearchPageLocators

# SearchPage class to handle search functionality
class SearchPage(BasePage):
    # Method to search for a query
    def go_to_leagues_page(self):
        search_box = self.driver.find_element(*SearchPageLocators.LEAGUES_PAGE)
        search_box.click()

    # Method to click search button
    def click_search_button(self):
        search_button = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button.click()
