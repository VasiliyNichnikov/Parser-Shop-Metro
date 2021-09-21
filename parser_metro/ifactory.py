from typing import Union
from abc import ABC, abstractmethod
from parser_metro.product_lists.iproductlist import IProductList


class IFactory(ABC):
    @abstractmethod
    def build(self) -> Union[IProductList]:
        pass
