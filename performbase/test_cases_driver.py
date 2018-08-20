from performbase import BaseTestCase

class SeleniumTestCases(BaseTestCase):

    def test_one(self):
        self.driver.navigate(self.url)
        print("You are currently on {}".format(self.driver.current_url()))