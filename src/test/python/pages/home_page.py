from .base_page import BasePage
from .locators.home_page_locators import HomePageLocators


# HomePage class to handle search functionality
class HomePage(BasePage):
    # Method to press on get started button
    def get_started(self):
        # Wait for get started button
        self.wait_for_element(HomePageLocators.GET_STARTED)
        get_started = self.driver.find_element(*HomePageLocators.GET_STARTED)
        get_started.click()

    # Method to click search button
    def click_accept_button(self):
        # Wait for accept button
        self.wait_for_element(HomePageLocators.ACCEPT_BUTTON)
        search_button = self.driver.find_element(*HomePageLocators.ACCEPT_BUTTON)
        search_button.click()

    # Method to click leagues page
    def go_to_leagues_page(self):
        # Wait for leagues page
        self.wait_for_element(HomePageLocators.LEAGUES_PAGE)
        search_box = self.driver.find_element(*HomePageLocators.LEAGUES_PAGE)
        search_box.click()

    # Method to click maybe later
    def maybe_later_button_press(self):
        # Wait for maybe later button
        self.wait_for_element(HomePageLocators.MAYBE_LATER_BUTTON)

        # Press on maybe later button.
        maybe_later_button = self.driver.find_element(*HomePageLocators.MAYBE_LATER_BUTTON)
        maybe_later_button.click()
