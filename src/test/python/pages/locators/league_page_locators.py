from appium.webdriver.common.mobileby import MobileBy


# Locator class for LeaguePage
class LeaguePageLocators:
    # Locator for league name
    @staticmethod
    def LEAGUE_NAME(league_name):
        return (MobileBy.XPATH, f"//*[@text='{league_name}']")

    # Locator for standings tab
    STANDINGS_TAB = (MobileBy.XPATH, "//*[@content-desc='Standings']")