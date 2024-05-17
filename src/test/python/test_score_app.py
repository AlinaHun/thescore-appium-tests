import pytest
from pages.search_page import SearchPage
from pages.league_page import LeaguePage
from pages.standings_page import StandingsPage
from pages.home_page import HomePage

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

    # Go to leagues page
    home_page.go_to_leagues_page()

    # Initialize LeaguePage
    league_page = LeaguePage(driver)

    # Select a random league
    random_league = league_page.select_league()

    # Verify NBA league is displayed
    league_page.verify_league_displayed(random_league)

    # Initialize StandingsPage
    standings_page = StandingsPage(driver)
    standings_page.verify_standings_displayed() # Verify standings are displayed

    # Navigate back
    driver.back()

    # Verify NBA league is displayed again
    league_page.verify_league_displayed("NBA")
