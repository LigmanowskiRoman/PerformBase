import unittest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from elementium.drivers.se import SeElements


class BaseTestCase(unittest.TestCase):

    browser_type = None
    url = None
    device = None
    width = None
    height = None

    @classmethod
    def setUpClass(cls):
        browser_options = {}
        if cls.browser_type == "Chrome":
            chrome_options = Options()
            chrome_parameters = {}
            if cls.device:
                chrome_parameters["deviceName"] = cls.device
                chrome_options.add_experimental_option("mobileEmulation", chrome_parameters)
            browser_options["chrome_options"] = chrome_options
        cls.wdriver = getattr(webdriver, cls.browser_type)(**browser_options)
        cls.driver = SeElements(cls.wdriver)
        cls.driver.set_window_size(cls.width, cls.height)

    @classmethod
    def tearDownClass(cls):
        cls.wdriver.quit()

