from abc import ABC, abstractmethod


class ISearchMax(ABC):
    @property
    @abstractmethod
    def max_page(self) -> int:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
