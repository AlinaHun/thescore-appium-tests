import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from uamqp.compat import TimeoutException


# BasePage class to define common methods and attributes
class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

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

        for _ in range(5):  # Try scrolling up to 5 times
            try:
                link_element = self.wait.until(EC.presence_of_element_located(link_locator))
                link_element.click()
                return
            except Exception:
                self.scroll_down()
        raise Exception(f"Failed to scroll to or select link with text '{link_text}' after 5 attempts.")

    def scroll_down(self):
        """
        Scrolls down the page using the swipe method.
        """
        try:
            screen_size = self.driver.get_window_size()
            start_x = screen_size['width'] // 2
            start_y = screen_size['height'] * 3 // 4
            end_x = screen_size['width'] // 2
            end_y = screen_size['height'] // 4

            self.driver.swipe(start_x, start_y, end_x, end_y, 1000)
        except Exception as e:
            print(f"Exception occurred: {e}")
