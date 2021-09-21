from typing import Union
from abc import ABC, abstractmethod
from selenium.webdriver.chrome.options import Options


class IWebDriver(ABC):
    @abstractmethod
    def run(self, options: Options) -> Union[int, list[Union[int, str]]]:
        pass
