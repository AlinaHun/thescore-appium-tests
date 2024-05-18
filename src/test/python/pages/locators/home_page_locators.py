from appium.webdriver.common.mobileby import MobileBy

# Locator class for SearchPage
class HomePageLocators:
    WELCOME_SIGN = (MobileBy.ID, "com.fivemobile.thescore:id/txt_welcome")
    GET_STARTED = (MobileBy.ID, "com.fivemobile.thescore:id/action_button_text")
    ACCEPT_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/accept_button")
    LEAGUES_PAGE = (MobileBy.XPATH, '''(//android.view.ViewGroup[@resource-id="com.fivemobile.thescore:id/navigation_bar_item_labels_group"])[5]''')
    MAYBE_LATER_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/btn_disallow")

