from selenium import webdriver as Webdriver
from selenium.webdriver.chrome.options import Options
from elementium.drivers.se import SeElements


class WebDriverInstance(object):

    __instance = None

    def __new__(self, *args, **kwargs):
        return self.getInstance(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.getInstance(self, *args, **kwargs)

    @classmethod
    def getInstance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
            browser_options = {}
            if kwargs["browser_type"] == "Chrome" and kwargs["device"]:
                chrome_options = Options()
                chrome_parameters = dict()
                chrome_parameters["deviceName"] = kwargs["device"]
                chrome_options.add_experimental_option("mobileEmulation", chrome_parameters)
                browser_options["chrome_options"] = chrome_options
            cls.webdriver = getattr(Webdriver, kwargs["browser_type"])(**browser_options)
            cls.driver = SeElements(cls.webdriver)
            cls.driver.set_window_size(kwargs["width"], kwargs["height"])
        return cls.__instance.driver
