from .base_page import BasePage
from .locators.home_page_locators import HomePageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# HomePage class to handle search functionality
class HomePage(BasePage):
    # Method to press on get started button
    def get_started(self):
        # Wait for get started button
        self.wait_for_element(HomePageLocators.GET_STARTED)
        get_started = self.driver.find_element(*HomePageLocators.GET_STARTED)
        get_started.click()

    # Method to click search button
    def click_accept_button(self):
        # Wait for accept button
        self.wait_for_element(HomePageLocators.ACCEPT_BUTTON)
        search_button = self.driver.find_element(*HomePageLocators.ACCEPT_BUTTON)
        search_button.click()

    # Method to click leagues page
    def go_to_leagues_page(self):
        # Wait for leagues page
        self.wait_for_element(HomePageLocators.LEAGUES_PAGE)
        search_box = self.driver.find_element(*HomePageLocators.LEAGUES_PAGE)
        search_box.click()

    def maybe_later_button_press(self):
        # Wait for maybe later button
        self.wait_for_element(HomePageLocators.MAYBE_LATER_BUTTON)
        # Press on maybe later button.
        maybe_later_button = self.driver.find_element(*HomePageLocators.MAYBE_LATER_BUTTON)
        maybe_later_button.click()




# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from .base_page import BasePage
# from .locators.leagues_page_locators import LeaguesPageLocators
#
#
# class LeaguesPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.wait = WebDriverWait(driver, 10)  # 10 seconds wait time, adjust as needed
#
#     def select_first_element_and_click_consiglio(self):
#         # Find the list of elements (adjust locator as per your app's structure)
#         elements = self.driver.find_elements(*LeaguesPageLocators.ELEMENTS_LIST)
#
#         if elements:
#             # Click on the first element
#             elements[0].click()
#
#             # Wait for the Consiglio button to be visible and click it
#             consiglio_button = self.wait.until(
#                 EC.visibility_of_element_located(LeaguesPageLocators.CONSIGLIO_BUTTON)
#             )
#             consiglio_button.click()
#
#             # Add an expectation for the next window, e.g., wait for a specific element in the next window
#             next_window_element = self.wait.until(
#                 EC.visibility_of_element_located(LeaguesPageLocators.NEXT_WINDOW_ELEMENT)
#             )
#         else:
#             raise Exception("No elements found in the list")
#
#     def verify_opened_name(self, name):
#         # Example expectation after clicking an element
#         element = self.wait.until(
#             EC.visibility_of_element_located(LeaguesPageLocators.OPENED_NAME(name))
#         )
#         assert element.text == name, f"Expected {name}, but got {element.text}"


# from selenium.webdriver.common.by import By
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from .base_page import BasePage
# from .locators.leagues_page_locators import LeaguesPageLocators
#
#
# class LeaguesPage(BasePage):
#     def __init__(self, driver):
#         super().__init__(driver)
#         self.wait = WebDriverWait(driver, 10)  # 10 seconds wait time, adjust as needed
#
#     def click_first_element(self):
#         # Get current activity
#         current_activity = self.driver.current_activity
#
#         # Find the list of elements (adjust locator as per your app's structure)
#         elements = self.driver.find_elements(*LeaguesPageLocators.ELEMENTS_LIST)
#
#         if elements:
#             # Click on the first element
#             elements[0].click()
#
#             # Wait for the activity to change
#             self.wait.until(lambda d: d.current_activity != current_activity)
#         else:
#             raise Exception("No elements found in the list")
#
#     def click_consiglio_button(self):
#         # Get current activity
#         current_activity = self.driver.current_activity
#
#         # Wait for the Consiglio button to be visible and click it
#         consiglio_button = self.wait.until(
#             EC.visibility_of_element_located(LeaguesPageLocators.CONSIGLIO_BUTTON)
#         )
#         consiglio_button.click()
#
#         # Wait for the activity to change
#         self.wait.until(lambda d: d.current_activity != current_activity)
#
#     def verify_opened_name(self, name):
#         # Example expectation after clicking an element
#         element = self.wait.until(
#             EC.visibility_of_element_located(LeaguesPageLocators.OPENED_NAME(name))
#         )
#         assert element.text == name, f"Expected {name}, but got {element.text}"
#
#
#
#
#
#
#
#
#
#
#
