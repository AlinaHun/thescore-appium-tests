from .base_page import BasePage

class LeaguePage(BasePage):
    def verify_league_displayed(self, league_name):
        assert self.driver.find_element_by_xpath(f"//*[@text='{league_name}']").is_displayed()