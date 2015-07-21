import unittest
from selenium import webdriver
from elementium.drivers.se import SeElements


class BaseTestCase(unittest.TestCase):

    browser_type = None
    url = None

    @classmethod
    def setUpClass(cls):
        cls.wdriver = getattr(webdriver, cls.browser_type)()
        cls.driver = SeElements(cls.wdriver)

    @classmethod
    def tearDownClass(cls):
        cls.wdriver.quit()
