import time
import random
from appium.webdriver.common.touch_action import TouchAction


# BasePage class to define common methods and attributes
class BasePage:
    def __init__(self, driver):
        self.driver = driver

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

    def select_random_name(self, resource_id):
        names = self.get_all_names(resource_id)
        random_name = random.choice(names)
        elements = self.driver.find_elements_by_id(resource_id)
        for element in elements:
            if element.text == random_name:
                element.click()
                break
        return random_name

