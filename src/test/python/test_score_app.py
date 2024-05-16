import pytest
from pages.search_page import SearchPage
from pages.league_page import LeaguePage
from pages.standings_page import StandingsPage

def test_league_team_player_navigation(driver):
    search_page = SearchPage(driver)
    search_page.search_for("NBA")

    league_page = LeaguePage(driver)
    league_page.verify_league_displayed("NBA")

    standings_page = StandingsPage(driver)
    standings_page.verify_standings_displayed()

    driver.back()

    league_page.verify_league_displayed("NBA")