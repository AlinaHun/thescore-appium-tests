import pytest
from appium import webdriver

@pytest.fixture(scope="module")
def driver():
    desired_caps = {
        "platformName": "Android",
        "deviceName": "Pixel 3a API 34",
        "app": "src/test/appium/score.apk",
        "automationName": "UiAutomator2"
    }
    driver = webdriver.Remote("http://127.0.0.1:4723/", desired_caps)
    yield driver
    driver.quit()