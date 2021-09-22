import typing
from abc import ABC, abstractmethod


class IProxy(ABC):
    @property
    @abstractmethod
    def options(self) -> typing.Dict:
        pass
