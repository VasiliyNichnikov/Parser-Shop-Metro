from selenium import webdriver
from abc import ABC, abstractmethod
from seleniumwire.webdriver import ChromeOptions
from recipient_from_server.iproxy import IProxy


class IWebDriver(ABC):
    @property
    @abstractmethod
    def driver(self) -> webdriver.Chrome:
        pass

    @abstractmethod
    def create(self, options: ChromeOptions, proxy: IProxy = None) -> None:
        pass
