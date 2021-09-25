from abc import ABC, abstractmethod


class IBlockPrice(ABC):
    @property
    @abstractmethod
    def main_price(self) -> str:
        pass

    @property
    @abstractmethod
    def old_price(self) -> str:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
