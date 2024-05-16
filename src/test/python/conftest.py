import pytest
from appium import webdriver

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "emulator-5554",
        "app": "appium/thescore.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
    yield driver
    driver.quit()