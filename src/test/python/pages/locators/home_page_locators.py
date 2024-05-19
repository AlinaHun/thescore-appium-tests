from appium.webdriver.common.mobileby import MobileBy


# Locator class for SearchPage
class HomePageLocators:
    # Locator for WELCOME sign
    WELCOME_SIGN = (MobileBy.ID, "com.fivemobile.thescore:id/txt_welcome")

    # Locator for GET STARTED button
    GET_STARTED = (MobileBy.ID, "com.fivemobile.thescore:id/action_button_text")

    # Locator for ACCEPT button
    ACCEPT_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/accept_button")

    # Locator for leagues list page
    LEAGUES_PAGE = (MobileBy.XPATH,
                    '''(//android.view.ViewGroup[@resource-id="com.fivemobile.thescore:id/navigation_bar_item_labels_group"])[5]''')

    # Locator for MAYBE LATER button
    MAYBE_LATER_BUTTON = (MobileBy.ID, "com.fivemobile.thescore:id/btn_disallow")
