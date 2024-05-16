from .base_page import BasePage

class SearchPage(BasePage):
    def search_for(self, query):
        search_box = self.driver.find_element_by_id("search_box_id")
        search_box.click()
        search_box.send_keys(query)