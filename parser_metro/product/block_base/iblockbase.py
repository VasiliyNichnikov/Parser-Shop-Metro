from abc import ABC, abstractmethod


class IBlockBase(ABC):
    @property
    @abstractmethod
    def title(self) -> str:
        pass

    @property
    @abstractmethod
    def code(self) -> str:
        pass

    @property
    @abstractmethod
    def brand(self) -> str:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
