from typing import Union
from time import sleep
from bs4 import BeautifulSoup
from seleniumwire.webdriver import Chrome
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import WebDriverException

from recipient_from_server.iwebdriver import IWebDriver


class ChromeWebDriver(IWebDriver):
    def __init__(self, path_driver: str,
                 number_attempts_in_case_of_error: int,
                 delay_after_error: int,
                 hide_browser: bool = True) -> None:
        self.__path_driver = path_driver
        self.__number_attempts_in_case_of_error = number_attempts_in_case_of_error
        self.__delay_after_error = delay_after_error
        self.__driver: Union[None, Chrome] = None
        self.__hide_browser = hide_browser

    def get_page_bs(self, url: str) -> BeautifulSoup:
        try:
            if self.__driver is None:
                self.__create()
            self.__driver.get(url)
        except WebDriverException as e:
            print(f"Error - {e}")
            if self.__number_attempts_in_case_of_error > 0:
                self.__number_attempts_in_case_of_error -= 1
                sleep(self.__delay_after_error)
                self.get_page_bs(url)
            else:
                return BeautifulSoup("", "lxml")
        return BeautifulSoup(self.__driver.page_source, "lxml")

    def close(self) -> None:
        self.__driver.close()
        self.__driver = None

    def __create(self) -> None:
        if self.__hide_browser:
            chrome_options = Options()
            chrome_options.add_argument("--headless")
            self.__driver = Chrome(self.__path_driver, chrome_options=chrome_options)
        else:
            self.__driver = Chrome(self.__path_driver)
