from test.baseTest import BaseTest


class Dummy_test(BaseTest):
    """
    Dummy appium test
    """
    def test_simple_navigation(self):
        """
        Dummy test
        """
        self.screen.dismiss_first_launch_alert()

        self.screen.navigate_to_settings()

        self.screen.navigate_from_settings_to_main()

        self.screen.navigate_to_quiz_menu()

        self.screen.navigate_from_quiz_menu_to_quiz()

        self.screen.navigate_from_quiz_to_quiz_menu()

