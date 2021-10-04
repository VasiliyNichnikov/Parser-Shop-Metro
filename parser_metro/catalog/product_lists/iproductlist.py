from typing import List
from abc import ABC, abstractmethod


class IProductList(ABC):
    @property
    @abstractmethod
    def urls_product(self) -> List[str]:
        pass

    @abstractmethod
    def search_data(self) -> None:
        pass
