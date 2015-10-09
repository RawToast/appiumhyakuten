"""
Navigation class
"""
from appium import webdriver
from test.page.mainView import MainView
from test.page.quizMenuView import QuizMenuView
from test.page.quizView import QuizView
from test.page.settingsView import SettingsView
from test.page.utility.navigation import EnsureUserNavigatesToSettingsPage, EnsureUserIsOnMainPage, \
    EnsureUserNavigatesToMainPage, EnsureUserIsOnSettingsPage, EnsureUserNavigatesToQuizMenu, EnsureUserIsOnQuizMenu, \
    EnsureUserNavigatesToQuiz, EnsureUserIsOnQuiz

_driver = None

class Screen(object):
    _driver = None
    _view = None

    def __init__(self, _driver=None):
        desired_caps = {}
        desired_caps['platformName'] = 'iOS'
        desired_caps['platformVersion'] = '9.0'
        desired_caps['deviceName'] = 'iPhone 5'
        desired_caps[
            'app'] = '/Users/jim/Library/Developer/Xcode/DerivedData/hyakuten-bgckgfcjicrkmsefycqgvuwklamj/Build/Products/Debug-iphonesimulator/hyakuten.app'
        desired_caps['newCommandTimeout'] = '0'


        if not _driver:
            _driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)
        self._driver = _driver
        self._view = MainView(self._driver)

    @EnsureUserNavigatesToMainPage()
    def dismiss_first_launch_alert(self):
        self._view.dismiss_alert()

    @EnsureUserIsOnMainPage()
    @EnsureUserNavigatesToSettingsPage()
    def navigate_to_settings(self):
        self._view.click_settings()
        self._view = SettingsView(self._driver)

    @EnsureUserIsOnSettingsPage()
    @EnsureUserNavigatesToMainPage()
    def navigate_from_settings_to_main(self):
        self._view.click_back()
        self._view = MainView(self._driver)

    @EnsureUserIsOnMainPage()
    @EnsureUserNavigatesToQuizMenu()
    def navigate_to_quiz_menu(self):
        self._view.click_first_quiz()
        self._view = QuizMenuView(self._driver)

    @EnsureUserIsOnQuizMenu()
    @EnsureUserNavigatesToQuiz()
    def navigate_from_quiz_menu_to_quiz(self):
        self._view.click_quiz()
        self._view = QuizView(self._driver)

    @EnsureUserIsOnQuiz()
    @EnsureUserNavigatesToQuizMenu()
    def navigate_from_quiz_to_quiz_menu(self):
        self._view.click_back_button()
        self._view = QuizMenuView(self._driver)

    def quit(self):
        self._driver.quit()

