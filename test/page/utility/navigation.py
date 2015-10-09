from selenium.webdriver.support.expected_conditions import presence_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from test.page.utility.testCase import init_test_case

# Main page

class EnsureUserIsOnMainPage(object):
    """
    Decorator to ensure the current page is as expected
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            try:
                wait = WebDriverWait(_driver, 10)
                wait.until(presence_of_element_located((By.ID, "Hyakuten")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the main title element, is the user on the main page?")

            # Hold value of the original function
            context = function(*args, **kwargs)

            # Go back to the caller, with the original response
            return context

        return wrapped_function


class EnsureUserNavigatesToMainPage(object):
    """
    Decorator to ensure current page
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            # Hold value of the original function
            context = function(*args, **kwargs)

            try:
                WebDriverWait(_driver, 10).until(presence_of_element_located((By.ID, "Hyakuten")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the main title element, is the user on the main page?")

            # Go back to the caller, with the original response
            return context

        return wrapped_function

# Settings page

class EnsureUserIsOnSettingsPage(object):
    """
    Decorator to ensure current page
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            try:
                wait = WebDriverWait(_driver, 10)
                wait.until(presence_of_element_located((By.ID, "Settings")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the settings element, is the user on the settings page?")

            # Hold value of the original function
            context = function(*args, **kwargs)



            # Go back to the caller, with the original response
            return context

        return wrapped_function


class EnsureUserNavigatesToSettingsPage(object):
    """
    Decorator to ensure current page
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            # Hold value of the original function
            context = function(*args, **kwargs)

            try:
                wait = WebDriverWait(_driver, 10)
                wait.until(presence_of_element_located((By.ID, "Settings")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the settings element, is the user on the settings page?")

            # Go back to the caller, with the original response
            return context

        return wrapped_function


# Quiz Menu


class EnsureUserIsOnQuizMenu(object):
    """
    Decorator to ensure the current page is as expected
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            try:
                wait = WebDriverWait(_driver, 10)
                wait.until(presence_of_element_located((By.ID, "Quiz")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the Quiz element, is the user on the Quiz menu?")

            # Hold value of the original function
            context = function(*args, **kwargs)

            # Go back to the caller, with the original response
            return context

        return wrapped_function


class EnsureUserNavigatesToQuizMenu(object):
    """
    Decorator to ensure current page
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            # Hold value of the original function
            context = function(*args, **kwargs)

            try:
                WebDriverWait(_driver, 10).until(presence_of_element_located((By.ID, "Quiz")))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the Quiz element, is the user on the quiz menu?")

            # Go back to the caller, with the original response
            return context

        return wrapped_function


# The quiz

QUIZ_NOTE = "Select the correct particle to fill in the blank"

class EnsureUserIsOnQuiz(object):
    """
    Decorator to ensure the current page is as expected
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            try:
                wait = WebDriverWait(_driver, 10)
                wait.until(presence_of_element_located((By.ID, QUIZ_NOTE)))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the Quiz Label element, is the user on the Quiz?")

            # Hold value of the original function
            context = function(*args, **kwargs)

            # Go back to the caller, with the original response
            return context

        return wrapped_function


class EnsureUserNavigatesToQuiz(object):
    """
    Decorator to ensure current page
    """
    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""
            _driver = args[0]._driver

            # Hold value of the original function
            context = function(*args, **kwargs)

            try:
                WebDriverWait(_driver, 10).until(presence_of_element_located((By.ID, QUIZ_NOTE)))
            except TimeoutException:
                tc = init_test_case()
                tc.fail("Could not find the Quiz Label element, is the user on the quiz?")

            # Go back to the caller, with the original response
            return context

        return wrapped_function