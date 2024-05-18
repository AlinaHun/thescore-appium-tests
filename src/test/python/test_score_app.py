import pytest
from pages.search_page import SearchPage
from pages.league_page import LeaguePage
from pages.standings_page import StandingsPage
from pages.home_page import HomePage
from pages.base_page import BasePage


# Test case to navigate through the app
def test_league_team_player_navigation(driver):

    # Initialize HomePage
    home_page = HomePage(driver)

    # Get started
    home_page.get_started()

    # Accept terms and conditions
    home_page.click_accept_button()

    # Get started
    home_page.get_started()

    # Initialize LeaguePage
    league_page = LeaguePage(driver)

    # Select the favorite league
    league_page.select_first_league_and_click_continue()

    # Close welcome popup windows
    league_page.close_welcome_popup()

    # Go to leagues page
    home_page.go_to_leagues_page()

    # Scroll to the correct league and select it
    league_page.scroll_to_name("NBA")

    # Verify correct league is displayed
    league_page.verify_opened_name("NBA")

    # Initialize StandingsPage
    standings_page = StandingsPage(driver)

    # Verify standings are displayed
    standings_page.verify_standings_displayed()

    # Navigate back
    driver.back()

    # Verify NBA league is displayed again
    league_page.verify_league_displayed("NBA")
