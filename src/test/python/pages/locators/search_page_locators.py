from appium.webdriver.common.mobileby import MobileBy


# Locator class for SearchPage
class SearchPageLocators:
    LEAGUES_PAGE = (MobileBy.ID, "com.fivemobile.thescore:id/navigation_bar_item_large_label_view")
    SEARCH_BUTTON = (MobileBy.ID, "search_button_id")
