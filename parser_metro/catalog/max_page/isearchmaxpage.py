from abc import ABC, abstractmethod


class ISearchMaxPage(ABC):
    @property
    @abstractmethod
    def max_page(self) -> int:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
