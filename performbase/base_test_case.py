import atexit
import unittest
import time
from .web_driver_instance import WebDriverInstance


class BaseTestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        if cls.browser_type:
            cls.driver = WebDriverInstance(browser_type=cls.browser_type,
                                           device=cls.device,
                                           width=cls.width, height=cls.height,
                                           proxy=getattr(cls, "proxy", None))
        cls.pageObjectInit()

    @classmethod
    def pageObjectInit(cls):
        pass

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        total_time = time.time() - self.start_time
        print("took %.3f s" % total_time)


def all_done():
    if WebDriverInstance._WebDriverInstance__instance is not None:
        WebDriverInstance.driver.browser.quit()


atexit.register(all_done)
