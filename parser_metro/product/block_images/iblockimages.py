import typing
from abc import ABC, abstractmethod


class IBlockImages(ABC):
    @property
    @abstractmethod
    def main_image(self) -> str:
        pass

    @property
    @abstractmethod
    def urls_additional(self) -> typing.List[str]:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
