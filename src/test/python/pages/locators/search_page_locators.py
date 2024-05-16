from appium.webdriver.common.mobileby import MobileBy

# Locator class for SearchPage
class SearchPageLocators:
    SEARCH_BOX = (MobileBy.ID, "search_box_id")
    SEARCH_BUTTON = (MobileBy.ID, "search_button_id")
