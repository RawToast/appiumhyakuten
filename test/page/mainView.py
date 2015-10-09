from test.page.utility.assertions import AssertElementExists
from test.page.utility.navigation import EnsureUserNavigatesToSettingsPage, EnsureUserNavigatesToQuizMenu
from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By

BASIC_PARTICLES = "Basic Particles"
EXPLANATORY_PARTICLES = "Explanatory Particles"

class MainView(object):

    _driver = None

    def __init__(self, driver):
        super(MainView, self).__init__()
        self._driver = driver

    # Actions
    def dismiss_alert(self):
        """
        Navigate to the home page
        """
        alert = self._driver.find_element_by_id("OK")
        if alert:
            alert.click()

    @EnsureUserNavigatesToSettingsPage()
    def click_settings(self):
        """
        Press the settings button
        """
        self.button_settings().click()

    @EnsureUserNavigatesToQuizMenu()
    def click_first_quiz(self):
        """
        Press the settings button
        """
        self.button_basic_particles().click()


    def click_explanatory_no(self):
        self.button_explanatory_no().click()

    # Controls
    def button_settings(self):
        return self._driver.find_element_by_id("Settings")

    def navigation_bar(self):
        return ""

    def table_view(self):
        return ""

    #Controls
    @AssertElementExists(element_name=BASIC_PARTICLES)
    def button_basic_particles(self):
        return self._driver.find_element_by_id(BASIC_PARTICLES)

    @AssertElementExists(element_name=EXPLANATORY_PARTICLES)
    def button_explanatory_no(self):
        return self._driver.find_element_by_id(EXPLANATORY_PARTICLES)

    @AssertElementExists(element_name="Settings")
    def button_settings(self):
        return self._driver.find_element_by_id("Settings")

    def label_main_view(self):
        wait = WebDriverWait(self._driver, 10)
        wait.until(presence_of_element_located((By.ID, "Hyakuten")))

        return self._driver.find_element_by_id("Hyakuten")

