from appium.webdriver.common.mobileby import MobileBy

# Locator class for StandingsPage
class StandingsPageLocators:
    STANDINGS_TABLE = (MobileBy.XPATH, '''(//androidx.viewpager.widget.ViewPager[@resource-id="com.fivemobile.thescore:id/viewPager"])[2]/android.view.ViewGroup''')
