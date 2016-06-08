from selenium import webdriver as Webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.proxy import *
from elementium.drivers.se import SeElements


class WebDriverInstance(object):

    __instance = None

    def __new__(self, *args, **kwargs):
        return self.getInstance(self, *args, **kwargs)

    def __init__(self, *args, **kwargs):
        self.getInstance(self, *args, **kwargs)

    @staticmethod
    def chrome_proxy(proxy):
        proxy = {
            "httpProxy": proxy,
            "ftpProxy": proxy,
            "sslProxy": proxy,
            "noProxy": None,
            "proxyType": "MANUAL",
            "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }
        return proxy

    @staticmethod
    def firefox_proxy(proxy):
        proxy = Proxy({
            'proxyType': ProxyType.MANUAL,
            'httpProxy': proxy,
            'ftpProxy': proxy,
            'sslProxy': proxy,
            'noProxy': ''})
        return proxy

    @classmethod
    def getInstance(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls, *args, **kwargs)
            browser_options = {}
            if kwargs["browser_type"] == "Chrome":
                if kwargs["device"]:
                    chrome_options = Options()
                    chrome_parameters = dict()
                    chrome_parameters["deviceName"] = kwargs["device"]
                    chrome_options.add_experimental_option("mobileEmulation", chrome_parameters)
                    browser_options["chrome_options"] = chrome_options
                if "proxy" in kwargs and type(kwargs["proxy"]) is str:
                    desired_capabilities = Webdriver.DesiredCapabilities.CHROME.copy()
                    desired_capabilities['proxy'] = WebDriverInstance.chrome_proxy(kwargs["proxy"])
                    browser_options["desired_capabilities"] = desired_capabilities
                cls.webdriver = Webdriver.Chrome(**browser_options)
            elif kwargs["browser_type"] == "Firefox":
                proxy = None
                if "proxy" in kwargs and type(kwargs["proxy"]) is str:
                    proxy = WebDriverInstance.firefox_proxy(kwargs["proxy"])
                cls.webdriver = Webdriver.Firefox(proxy=proxy)
            else:
                cls.webdriver = getattr(Webdriver, kwargs["browser_type"])
            cls.driver = SeElements(cls.webdriver)
            cls.driver.set_window_size(kwargs["width"], kwargs["height"])
        return cls.__instance.driver
