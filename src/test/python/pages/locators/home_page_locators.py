from appium.webdriver.common.mobileby import MobileBy

# Locator class for SearchPage
class HomePageLocators:
    GET_STARTED = (MobileBy.ID, "com.fivemobile.thescore:id/action_button_text")
    ACCEPT_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/accept_button")
    LEAGUES_PAGE = (MobileBy.ID, "com.fivemobile.thescore:id/navigation_bar_item_large_label_view")

