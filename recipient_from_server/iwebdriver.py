from typing import Any
from selenium import webdriver
from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class IWebDriver(ABC):
    @property
    @abstractmethod
    def driver(self) -> webdriver.Chrome:
        pass

    @abstractmethod
    def create(self, options: Options, dc: DesiredCapabilities=None) -> None:
        pass
