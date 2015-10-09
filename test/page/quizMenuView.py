from test.page.utility.assertions import AssertElementExists
from test.page.utility.navigation import EnsureUserIsOnQuizMenu, \
    EnsureUserNavigatesToQuiz


QUIZ = "Quiz"
VIDEO_DESCRIPTION = "Explanatory Particles"

class QuizMenuView(object):

    _driver = None

    def __init__(self, driver):
        super(QuizMenuView, self).__init__()
        self._driver = driver

    # Actions
    @EnsureUserIsOnQuizMenu()
    @EnsureUserNavigatesToQuiz()
    def click_quiz(self):
        """
        Press the settings button
        """
        self.button_basic_particles().click()

    def click_explanatory_no(self):
        self.button_video_description().click()

    # Controls

    @AssertElementExists(element_name=QUIZ)
    def button_basic_particles(self):
        return self._driver.find_element_by_id(QUIZ)

    @AssertElementExists(element_name=VIDEO_DESCRIPTION)
    def button_video_description(self):
        return self._driver.find_element_by_id(VIDEO_DESCRIPTION)

