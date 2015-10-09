from test.page.utility.testCase import init_test_case


class AssertElementExists(object):
    """
    Decorator to ensure current page
    """
    def __init__(self, element_name="the requested element"):
        self.element_name = element_name

    def __call__(self, function):
        def wrapped_function(*args, **kwargs):
            """The decorator function"""

            # Hold value of the original function
            context = function(*args, **kwargs)
            if not context:
                tc = init_test_case()
                tc.fail("Could not find {}".format(self.element_name))

            # Go back to the caller, with the original response
            return context

        return wrapped_function