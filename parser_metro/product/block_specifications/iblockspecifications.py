import typing
from abc import ABC, abstractmethod


class IBlockSpecifications(ABC):
    @property
    @abstractmethod
    def specifications(self) -> typing.Dict[str, str]:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
