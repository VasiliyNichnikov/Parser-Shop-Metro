from typing import Union, List, Generator

from bs4 import BeautifulSoup, NavigableString, ResultSet


class ProductList:
    def __init__(self, html_code: str) -> None:
        self.__html_code = html_code
        self.__bs4: BeautifulSoup = BeautifulSoup(self.__html_code, "lxml")

    def __find_block_products(self) -> None:
        self.__block_products: Union[BeautifulSoup, NavigableString] = \
            self.__bs4.find("div", {"class": "search-page__products"})

    def __find_items_product(self) -> None:
        self.__products: ResultSet = self.__block_products.find_all("div", {"class": "catalog-item"})

    def __find_urls_products(self) -> Generator[str]:
        urls: List[str] = []
        for product in self.__products:
            block: Union[BeautifulSoup, NavigableString] = product.find("div", {"class": "catalog-item_group"})
            catalog: Union[BeautifulSoup, NavigableString] = block.find("div", {"class": "catalog-item_defaut-image"})
            url: str = catalog.find("a").get("href")
            urls.append(url)
        yield urls
