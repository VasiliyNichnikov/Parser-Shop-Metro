from bs4 import BeautifulSoup
from abc import ABC, abstractmethod


class IWebDriver(ABC):
    @abstractmethod
    def get_page_bs(self, url: str) -> BeautifulSoup:
        pass

    @abstractmethod
    def close(self) -> None:
        pass
