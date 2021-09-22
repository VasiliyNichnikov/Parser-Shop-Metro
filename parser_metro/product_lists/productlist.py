from typing import Union, List
from bs4 import BeautifulSoup, NavigableString, ResultSet

from parser_metro.product_lists.urlproduct import UrlProduct
from parser_metro.product_lists.iurlproduct import IUrlProduct
from parser_metro.product_lists.iproductlist import IProductList
from parser_metro.product_lists.productlisterror import NotFoundMainBlockProduct, NotFoundItemsProduct


class ProductList(IProductList):
    @property
    def urls_product(self) -> List[str]:
        return self.__urls_product

    def __init__(self, bs: BeautifulSoup) -> None:
        self.__bs = bs
        self.__urls_product: List = []

    def search_urls_product(self) -> None:
        self.__find_block_products()
        self.__find_items_product()
        self.__urls_product = self.__find_urls_product()

    def __find_block_products(self) -> None:
        self.__block_products: Union[BeautifulSoup, NavigableString] = \
            self.__bs.find("div", {"class": "search-page__products"})
        if self.__block_products is None:
            raise NotFoundMainBlockProduct("Not found main block product.")

    def __find_items_product(self) -> None:
        self.__products: ResultSet = self.__block_products.find_all("div", {"class": "catalog-item"})
        if self.__products is None:
            raise NotFoundItemsProduct("Not found items product.")

    def __find_urls_product(self) -> List[str]:
        urls: List[str] = []
        for p in self.__products:
            product: IUrlProduct = UrlProduct(p)
            product.search_url()
            urls.append(product.url)
        return urls
