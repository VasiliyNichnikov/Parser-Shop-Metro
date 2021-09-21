from abc import ABC, abstractmethod


class IUrlProduct(ABC):
    @property
    @abstractmethod
    def url(self) -> str:
        pass

    @abstractmethod
    def search_url(self) -> None:
        pass
