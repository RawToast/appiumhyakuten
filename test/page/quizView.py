from test.page.utility.assertions import AssertElementExists
from test.page.utility.navigation import EnsureUserIsOnQuizMenu, \
    EnsureUserNavigatesToQuiz, EnsureUserNavigatesToQuizMenu

BACK = "Back"
QUIZ_LABEL = "Quiz Label"

class QuizView(object):

    _driver = None

    def __init__(self, driver):
        super(QuizView, self).__init__()
        self._driver = driver

    # Actions
    @EnsureUserIsOnQuizMenu()
    @EnsureUserNavigatesToQuiz()
    def click_quiz(self):
        """
        Press the settings button
        """
        self.button_basic_particles().click()

    @EnsureUserNavigatesToQuizMenu()
    def click_back_button(self):
        self.button_back().click()

    # Controls

    @AssertElementExists(element_name=BACK)
    def button_back(self):
        return self._driver.find_element_by_id(BACK)

    @AssertElementExists(element_name=QUIZ_LABEL)
    def button_video_description(self):
        return self._driver.find_element_by_id(QUIZ_LABEL)

