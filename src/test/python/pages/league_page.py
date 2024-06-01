from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from .base_page import BasePage
from .locators.league_page_locators import LeaguePageLocators
from .home_page import HomePage
from selenium.webdriver.support import expected_conditions as EC


# LeaguePage class to handle league-related functionality
class LeaguePage(BasePage):
    # Method to verify league is displayed
    def verify_leagues_displayed(self):
        assert self.driver.find_element(*LeaguePageLocators.LEAGUES_LIST).is_displayed()

    # Method to click standings tab
    def click_standings_tab(self):
        standings_tab = self.driver.find_element(*LeaguePageLocators.STANDINGS_TAB)
        standings_tab.click()

    # Method to scroll to the league
    def scroll_to_name(self, name):
        # Wait for leagues list
        self.wait_for_element(LeaguePageLocators.LEAGUES_LIST_MAIN)

        # Scroll to the specified name
        self.scroll_to_and_select_link(name)

    # Method to select the league
    def click_name(self, name):
        # Click on the specified name
        name_element = self.driver.find_element(*LeaguePageLocators.LEAGUE_NAME(name))
        name_element.click()

    # Method to verify the opened league
    def verify_opened_name(self, name):
        self.wait_for_element(LeaguePageLocators.OPENED_NAME_LOCATOR)

        # Wait until the text of the locator is different from 'Leagues'
        WebDriverWait(self.driver, 10).until_not(
            lambda driver: driver.find_element(*LeaguePageLocators.OPENED_NAME_LOCATOR).text == "Leagues"
        )

        # Verify that the opened name matches the specified name
        opened_name_element = self.driver.find_element(*LeaguePageLocators.OPENED_NAME_LOCATOR)
        opened_name = opened_name_element.text
        assert opened_name == name, f"Expected name: {name}, Actual name: {opened_name}"

    # Method to select the first league and click "continue" button
    def select_first_league_and_click_continue(self):
        # Wait for leagues list
        self.wait_for_element(LeaguePageLocators.LEAGUES_LIST)
        # Find the list of leagues
        elements = self.driver.find_elements(*LeaguePageLocators.LEAGUES_LIST)

        if elements:
            # Click on the first element
            elements[0].click()
            # Click on the "Continue" button
            self.click_continue_button()
        else:
            raise Exception("No elements found in the list")

    # Method to close all welcome pop up windows
    def close_welcome_popup(self):
        # Press maybe later button
        self.click_maybe_later()
        # Click on the "Continue" button
        self.click_continue_button()
        # Click on the "Continue" button
        self.click_continue_button()
        # Press maybe later button
        self.click_maybe_later_sign_up()
        # Click on the "Don't allow" button
        self.click_dont_allow_button()

    # Method to click sub tab page
    def tap_on_sub_tab(self, tab_name):
        tab_locator = (By.XPATH, f"//android.widget.TextView[@text='{tab_name}']")
        self.wait.until(EC.presence_of_element_located(tab_locator)).click()

    # Method to check if on correct page
    def verify_on_correct_tab(self, tab_name):
        tab_locator = (By.XPATH, f"//android.widget.TextView[@text='{tab_name}' and @selected='true']")
        assert self.wait.until(EC.presence_of_element_located(tab_locator)).is_displayed()


