from typing import Union
from bs4 import BeautifulSoup
from selenium.common.exceptions import WebDriverException
from seleniumwire.webdriver import Chrome

from recipient_from_server.iwebdriver import IWebDriver


class ChromeWebDriver(IWebDriver):
    def __init__(self, path_driver: str) -> None:
        self.__path_driver = path_driver
        self.__driver: Union[None, Chrome] = None

    def get_page_bs(self, url: str) -> BeautifulSoup:
        try:
            if self.__driver is None:
                self.__create()
            self.__driver.get(url)
        except WebDriverException as e:
            print(f"Error - {e}")
            self.get_page_bs(url)
        return BeautifulSoup(self.__driver.page_source, "lxml")

    def close(self) -> None:
        self.__driver.close()
        self.__driver = None

    def __create(self) -> None:
        self.__driver = Chrome(self.__path_driver)
