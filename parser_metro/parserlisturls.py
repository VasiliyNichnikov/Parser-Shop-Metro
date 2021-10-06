from bs4 import BeautifulSoup
from typing import List, Union
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.catalog.catalogfactory import CatalogFactory, Catalog


class ParserListUrls:
    def __init__(self, driver: IWebDriver, url: str) -> None:
        self.__driver: IWebDriver = driver
        self.__bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(url)
        self.__catalog: Catalog = CatalogFactory.build(self.__bs)
        self.__catalog.init_max_page_and_product_list()

    @property
    def max_page(self) -> int:
        condition, search_max_page = self.__catalog.max_page
        if condition:
            return search_max_page.max_page
        return 0

    @property
    def urls(self) -> List[str]:
        condition, product_list = self.__catalog.product_list
        if condition:
            return product_list.urls_product
        return []
