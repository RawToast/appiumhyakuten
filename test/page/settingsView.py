from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from test.page.utility.assertions import AssertElementExists
from test.page.utility.navigation import EnsureUserIsOnSettingsPage, EnsureUserNavigatesToMainPage

BACK_BUTTON = "Hyakuten"
AUTO_PLAY_VIDEO = "Auto Play Video"

class SettingsView(object):

    _driver = None


    def __init__(self, driver):
        super(SettingsView, self).__init__()
        self._driver = driver

    # Actions
    @EnsureUserIsOnSettingsPage()
    @EnsureUserNavigatesToMainPage()
    def click_back(self):
        """
        Press the settings button
        """
        self.button_back().click()

    # Controls

    @AssertElementExists(element_name=BACK_BUTTON)
    def button_back(self):
        return self._driver.find_element_by_id(BACK_BUTTON)

    @AssertElementExists(element_name=AUTO_PLAY_VIDEO)
    def button_tweet(self):
        return self._driver.find_element_by_id(AUTO_PLAY_VIDEO)

    def label_settings(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(presence_of_element_located((By.ID, "Settings")))

        return self._driver.find_element_by_id("Settings")

