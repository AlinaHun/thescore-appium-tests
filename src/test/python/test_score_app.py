import pytest
from pages.league_page import LeaguePage
from pages.home_page import HomePage


# Test case to navigate through the app
def test_league_team_player_navigation(driver, config):

    league_name = config["leagues"]["name"]

    # Initialize HomePage
    home_page = HomePage(driver)

    # Initialize LeaguePage
    league_page = LeaguePage(driver)

    # Get started
    home_page.get_started()

    # Accept terms and conditions
    home_page.click_accept_button()

    # Get started
    home_page.get_started()

    # Select the favorite league
    league_page.select_first_league_and_click_continue()

    # Close welcome popup windows
    league_page.close_welcome_popup()

    # Go to leagues page
    home_page.go_to_leagues_page()

    # Scroll to the correct league and select it
    league_page.scroll_to_name(league_name)

    # Verify correct league is displayed
    league_page.verify_opened_name(league_name)

    # Open the sub tab
    league_page.tap_on_sub_tab("STANDINGS")

    # Verify standings are displayed
    league_page.verify_on_correct_tab("STANDINGS")

    # Navigate back
    driver.back()

    # Verify leagues list is displayed again
    league_page.verify_leagues_displayed()
