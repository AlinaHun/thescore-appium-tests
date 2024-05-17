from .base_page import BasePage
from .locators.home_page_locators import HomePageLocators


# HomePage class to handle search functionality
class HomePage(BasePage):
    # Method to press on get started button
    def get_started(self):
        get_started = self.driver.find_element(*HomePageLocators.GET_STARTED)
        get_started.click()

    # Method to click search button
    def click_accept_button(self):
        search_button = self.driver.find_element(*HomePageLocators.ACCEPT_BUTTON)
        search_button.click()

    # Method to click leagues page
    def go_to_leagues_page(self):
        search_box = self.driver.find_element(*HomePageLocators.LEAGUES_PAGE)
        search_box.click()
















