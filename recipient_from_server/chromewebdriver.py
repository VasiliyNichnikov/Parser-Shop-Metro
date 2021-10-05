from seleniumwire import webdriver
from recipient_from_server.iproxy import IProxy
from seleniumwire.webdriver import ChromeOptions

from recipient_from_server.iwebdriver import IWebDriver


class ChromeWebDriver(IWebDriver):
    @property
    def driver(self) -> webdriver.Chrome:
        return self.__driver

    def __init__(self, path_driver: str) -> None:
        self.__path_driver = path_driver
        self.__driver = None

    def create(self, options: ChromeOptions, proxy: IProxy = None) -> None:
        if options is None:
            self.__driver = webdriver.Chrome(self.__path_driver)
        else:
            self.__driver = webdriver.Chrome(self.__path_driver, chrome_options=options,
                                             seleniumwire_options=proxy.options)
