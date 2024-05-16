from .base_page import BasePage

class StandingsPage(BasePage):
    def verify_standings_displayed(self):
        assert self.driver.find_element_by_xpath("//*[@content-desc='Standings']").is_displayed()