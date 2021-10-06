from bs4 import BeautifulSoup
from typing import List, Union
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.catalog.product_lists.productlist import IProductList, ProductList
from parser_metro.catalog.max_page.searchmaxpage import ISearchMaxPage, SearchMaxPage


class ParserListUrls:
    def __init__(self, driver: IWebDriver, url: str) -> None:
        self.__driver: IWebDriver = driver
        self.__bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(url)
        self.__search_max_page: ISearchMaxPage = SearchMaxPage(self.__bs)
        self.__search_max_page.search_data()

        self.__product_list: IProductList = ProductList(self.__bs)
        self.__product_list.search_data()

    @property
    def max_page(self) -> int:
        return self.__search_max_page.max_page

    @property
    def urls(self) -> List[str]:
        return self.__product_list.urls_product
