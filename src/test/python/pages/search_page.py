from .base_page import BasePage
from .locators.search_page_locators import SearchPageLocators

# SearchPage class to handle search functionality
class SearchPage(BasePage):
    # Method to search for a query
    def search_for(self, query):
        search_box = self.driver.find_element(*SearchPageLocators.SEARCH_BOX)
        search_box.click()
        search_box.send_keys(query)

    # Method to click search button
    def click_search_button(self):
        search_button = self.driver.find_element(*SearchPageLocators.SEARCH_BUTTON)
        search_button.click()
