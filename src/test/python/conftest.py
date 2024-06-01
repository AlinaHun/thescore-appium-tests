import pytest
from appium import webdriver
from pages.base_page import BasePage
from pages.locators.home_page_locators import HomePageLocators
import yaml


def load_config():
    with open('''src/test/python/data.yaml''') as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": r"C:\Users\grand\thescore-appium-tests\src\test\appium\score.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)

    # Wait for the app to start before running tests
    base_page = BasePage(driver)
    base_page.wait_for_app_to_start(HomePageLocators.WELCOME_SIGN)

    yield driver
    driver.quit()


@pytest.fixture(scope="session")
def config():
    return load_config()
