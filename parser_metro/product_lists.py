from typing import Union, List
from bs4 import BeautifulSoup, NavigableString, ResultSet

from parser_metro.product import Product
from parser_metro.iproduct import IProduct
from parser_metro.iproduct_list import IProductList
from parser_metro.product_lists_errors import NotFoundMainBlockProduct, NotFoundItemsProduct


class ProductList(IProductList):
    def __init__(self, html_code: str) -> None:
        self.__html_code = html_code
        self.__bs4: BeautifulSoup = BeautifulSoup(self.__html_code, "lxml")

    def search_urls_products(self) -> List[str]:
        self.__find_block_products()
        self.__find_items_product()
        self.__find_urls_products()
        return self.__find_urls_products()

    def __find_block_products(self) -> None:
        self.__block_products: Union[BeautifulSoup, NavigableString] = \
            self.__bs4.find("div", {"class": "search-page__products"})
        if self.__block_products is None:
            raise NotFoundMainBlockProduct("Not found main block product.")

    def __find_items_product(self) -> None:
        self.__products: ResultSet = self.__block_products.find_all("div", {"class": "catalog-item"})
        if self.__products is None:
            raise NotFoundItemsProduct("Not found items product.")

    def __find_urls_products(self) -> List[str]:
        urls: List[str] = []
        for p in self.__products:
            product: IProduct = Product(p)
            product.search_url()
            urls.append(product.url)
        yield urls

