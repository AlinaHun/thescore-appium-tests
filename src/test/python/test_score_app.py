import pytest
from pages.search_page import SearchPage
from pages.league_page import LeaguePage
from pages.standings_page import StandingsPage

# Test case to navigate through the app
def test_league_team_player_navigation(driver):
    search_page = SearchPage(driver) # Initialize SearchPage
    search_page.search_for("NBA") # Search for NBA

    league_page = LeaguePage(driver) # Initialize LeaguePage
    league_page.verify_league_displayed("NBA") # Verify NBA league is displayed

    standings_page = StandingsPage(driver) # Initialize StandingsPage
    standings_page.verify_standings_displayed() # Verify standings are displayed

    driver.back() # Navigate back

    league_page.verify_league_displayed("NBA") # Verify NBA league is displayed again
