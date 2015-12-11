import atexit
import unittest
import time
from selenium import webdriver as Webdriver
from selenium.webdriver.chrome.options import Options
from elementium.drivers.se import SeElements


class BaseTestCase(unittest.TestCase):

    browser_type = None
    url = None
    device = None
    width = None
    height = None
    webdriver = None

    @classmethod
    def setUpClass(cls):
        if BaseTestCase.webdriver is None:
            browser_options = {}
            BaseTestCase.url = cls.url
            if cls.browser_type == "Chrome" and cls.device:
                chrome_options = Options()
                chrome_parameters = {}
                chrome_parameters["deviceName"] = cls.device
                chrome_options.add_experimental_option("mobileEmulation", chrome_parameters)
                browser_options["chrome_options"] = chrome_options
            BaseTestCase.webdriver = getattr(Webdriver, cls.browser_type)(**browser_options)
            BaseTestCase.driver = SeElements(BaseTestCase.webdriver)
            cls.driver.set_window_size(cls.width, cls.height)

    def setUp(self):
        self.start_time = time.time()

    def tearDown(self):
        total_time = time.time() - self.start_time
        print "took %.3f s" % total_time


def all_done():
    if BaseTestCase.webdriver != None:
        BaseTestCase.webdriver.quit()

atexit.register(all_done)
