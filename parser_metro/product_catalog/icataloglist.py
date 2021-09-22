from abc import ABC, abstractmethod


class ICatalogList(ABC):
    @property
    @abstractmethod
    def max_page(self) -> int:
        pass

    @abstractmethod
    def search_max_page(self) -> None:
        pass
