import time
import random
from appium.webdriver.common.touch_action import TouchAction
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


# BasePage class to define common methods and attributes
from uamqp.compat import TimeoutException


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def scroll_down(self):
        # Adjust these coordinates based on your screen size and layout
        start_x = 500
        start_y = 1500
        end_x = 500
        end_y = 500
        actions = TouchAction(self.driver)
        actions.press(x=start_x, y=start_y).move_to(x=end_x, y=end_y).release().perform()

    def get_all_names(self, resource_id):
        all_names = set()
        end_of_page = False
        while not end_of_page:
            elements = self.driver.find_elements_by_id(resource_id)
            new_names = {element.text for element in elements}
            if new_names.issubset(all_names):
                end_of_page = True
            else:
                all_names.update(new_names)
                self.scroll_down()
                # Wait for the page to load after scrolling
                time.sleep(1)
        return list(all_names)


    def wait_for_page_change(self, old_page):
        """
        Waits for a page change by comparing the page source before and after an action.
        """
        for _ in range(10):  # Check for up to 10 seconds
            time.sleep(1)
            new_page = self.driver.page_source
            if old_page != new_page:
                return
        raise TimeoutException("Page did not change within the given time")

    def wait_for_element(self, locator):
        """
        Waits for an element to be present in the DOM.
        """
        self.wait.until(EC.presence_of_element_located(locator))
    #
    # def wait_for_element_to_disappear(self, locator):
    #     """
    #     Waits for an element to disappear from the DOM.
    #     """
    #     self.wait.until_not(EC.presence_of_element_located(locator))

    def wait_for_app_to_start(self, locator):
        """
        Waits for the application to start by waiting for a specific element to be present.
        """
        self.wait.until(EC.presence_of_element_located(locator))

    def click_maybe_later(self):
        """
        Clicks on the "Maybe Later" button if present on the page.
        """
        maybe_later_button_locator = (By.ID, "com.fivemobile.thescore:id/btn_disallow")
        try:
            maybe_later_button = self.wait.until(EC.element_to_be_clickable(maybe_later_button_locator))
            maybe_later_button.click()
        except Exception as e:
            print("Maybe Later button not found on the page.")
            print(e)

    def click_maybe_later_sign_up(self):
        """
        Clicks on the "Maybe Later" button if present on the page.
        """
        maybe_later_button_locator = (By.ID, "com.fivemobile.thescore:id/btn_secondary")
        try:
            maybe_later_button = self.wait.until(EC.element_to_be_clickable(maybe_later_button_locator))
            maybe_later_button.click()
        except Exception as e:
            print("Maybe Later button not found on the page.")
            print(e)

    def click_continue_button(self):
        """
        Clicks on the "Continue" button if present on the page.
        """
        continue_button_locator = (By.ID, "com.fivemobile.thescore:id/action_button_text")
        try:
            continue_button = self.wait.until(EC.element_to_be_clickable(continue_button_locator))
            continue_button.click()
        except Exception as e:
            print("Continue button not found on the page.")
            print(e)

    def click_dont_allow_button(self):
        """
        Clicks on the "Don't Allow" button if present on the page.
        """
        dont_allow_button_locator = (By.ID, "com.android.permissioncontroller:id/permission_deny_button")
        try:
            dont_allow_button = self.wait.until(EC.element_to_be_clickable(dont_allow_button_locator))
            dont_allow_button.click()
        except Exception as e:
            print("Don't Allow button not found on the page.")
            print(e)

    def scroll_to_and_select_link(self, link_text):
        """
        Scrolls to the specified link text and selects it.
        """
        xpath = f"//android.widget.TextView[@resource-id='com.fivemobile.thescore:id/league_name_text' and @text='{link_text}']"
        link_locator = (By.XPATH, xpath)

        try:
            link_element = self.wait.until(EC.visibility_of_element_located(link_locator))
            # Scroll to the link element
            self.driver.execute_script("arguments[0].scrollIntoView();", link_element)
            # Click on the link element
            link_element.click()
        except Exception as e:
            print(f"Failed to scroll to or select link with text '{link_text}'.")
            print(e)







