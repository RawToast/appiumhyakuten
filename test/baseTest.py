import unittest
from appium import webdriver
from test.page.screen import Screen


class BaseTest(unittest.TestCase):
    """
    Base appium test
    """
    driver = None
    screen = None

    def setUp(self):
        """
        Setup test env
        """
        # iOS environment

        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'iPhone 5'
        desired_caps['app'] = '/Users/jim/Library/Developer/Xcode/DerivedData/hyakuten-bgckgfcjicrkmsefycqgvuwklamj/Build/Products/Debug-iphonesimulator/hyakuten.app'
        desired_caps['newCommandTimeout'] = '0'

        self.driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

        self.screen = Screen(self.driver)

    def tearDown(self):
        self.screen.quit()

