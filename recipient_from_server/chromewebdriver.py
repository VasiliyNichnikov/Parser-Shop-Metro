from typing import Any

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from recipient_from_server.iwebdriver import IWebDriver


class ChromeWebDriver(IWebDriver):
    @property
    def driver(self) -> webdriver.Chrome:
        return self.__driver

    def __init__(self, path_driver: str) -> None:
        self.__path_driver = path_driver
        self.__driver = None

    def create(self, options: Options, dc: DesiredCapabilities = None) -> None:
        self.__driver = webdriver.Chrome(self.__path_driver, chrome_options=options, desired_capabilities=dc)
