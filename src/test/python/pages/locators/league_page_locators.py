from appium.webdriver.common.mobileby import MobileBy
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# Locator class for LeaguePage
class LeaguePageLocators:
    # Locator for league name
    @staticmethod
    def LEAGUE_NAME(league_name):
        # Assuming the name is identified by text
        return MobileBy.XPATH, f"//*[@text='{league_name}']"

    # Locator for the opened name element
    OPENED_NAME_LOCATOR = (MobileBy.ID, "com.fivemobile.thescore:id/titleTextView")

    # Locator for standings tab
    STANDINGS_TAB = (MobileBy.XPATH, '''//android.widget.TextView[@text="STANDINGS"]''')

    # Leagues list on "choose your favorite league" page
    LEAGUES_LIST = (MobileBy.ID, "com.fivemobile.thescore:id/recyclerView")

    # Continue button on "choose your favorite league" page
    CONTINUE_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/btn_primary")
