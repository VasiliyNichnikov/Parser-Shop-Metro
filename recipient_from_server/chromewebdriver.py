from typing import Union

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

from recipient_from_server.iwebdriver import IWebDriver


class ChromeWebDriver(IWebDriver):
    def __init__(self, path_driver: str, url: str) -> None:
        self.__path_driver = path_driver
        self.__url = url

    def run(self, options: Options) -> Union[int, list[Union[int, str]]]:
        with webdriver.Chrome(self.__path_driver, chrome_options=options) as driver:
            driver.get(self.__url)
            return driver.page_source
