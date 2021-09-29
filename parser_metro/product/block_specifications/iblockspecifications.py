import typing
from abc import ABC, abstractmethod


class IBlockSpecifications(ABC):
    @property
    @abstractmethod
    def specifications(self) -> typing.Dict[str, str]:
        pass

    @property
    @abstractmethod
    def description(self) -> str:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
