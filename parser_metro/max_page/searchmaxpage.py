from typing import Union, List
from bs4 import BeautifulSoup, NavigableString, ResultSet

from parser_metro.max_page.isearchmaxpage import ISearchMaxPage
from parser_metro.max_page.searchmaxpageerror import NotFoundCatalogPagination, \
    NotFoundItemsCatalog, \
    NotFoundMaxPage


class SearchMaxPage(ISearchMaxPage):
    @property
    def max_page(self) -> int:
        return self.__max_page

    def __init__(self, bs: BeautifulSoup) -> None:
        self.__bs = bs
        self.__max_page = 0

    def search_data(self) -> None:
        self.__find_catalog_pagination()
        self.__find_items_catalog()
        self.__max_page: int = self.__find_max_page()

    def __find_catalog_pagination(self) -> None:
        self.__catalog_pagination: Union[BeautifulSoup, NavigableString] = \
            self.__bs.find("ul", {"class": "catalog-pagination"})
        if self.__catalog_pagination is None:
            raise NotFoundCatalogPagination("Not found catalog pagination.")

    def __find_items_catalog(self) -> None:
        self.__items: ResultSet = \
            self.__catalog_pagination.find_all("li", {"class": ["catalog-pagination_item"]})
        if self.__items is None:
            raise NotFoundItemsCatalog("Not found items catalog.")

    def __find_max_page(self) -> int:
        numbers: List[int] = [1]
        for item in self.__items:
            url: Union[BeautifulSoup, NavigableString] = item.find("a")
            if url is not None:
                value: str = url.text
                if value.isdigit():
                    numbers.append(int(value))
            else:
                raise NotFoundMaxPage("Not found max page")
        return max(numbers)
