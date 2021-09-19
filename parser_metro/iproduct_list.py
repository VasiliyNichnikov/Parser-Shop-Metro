from typing import List
from abc import ABC, abstractmethod


class IProductList(ABC):
    @abstractmethod
    def search_urls_products(self) -> List[str]:
        pass
