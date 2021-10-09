from time import sleep
from bs4 import BeautifulSoup
from typing import List, Union
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.catalog.catalogfactory import CatalogFactory, Catalog


class ParserCatalog:
    def __init__(self, driver: IWebDriver, url: str, number_attempts_in_case_of_error: int,
                 delay_after_error: int) -> None:
        self.__driver: IWebDriver = driver
        self.__url = url
        self.__number_attempts_in_case_of_error = number_attempts_in_case_of_error
        self.__delay_after_error = delay_after_error
        self.__init_catalog()

    def __init_catalog(self) -> None:
        self.__bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(self.__url)
        self.__catalog: Catalog = CatalogFactory.build(self.__bs)
        self.__catalog.init_max_page_and_product_list()

    @property
    def max_page(self) -> int:
        condition, search_max_page = self.__catalog.max_page
        if condition:
            return search_max_page.max_page
        return self.__checking_for_errors(max_page=True)

    @property
    def urls(self) -> List[str]:
        condition, product_list = self.__catalog.product_list
        if condition:
            return product_list.urls_product
        return self.__checking_for_errors(urls=True)

    def __checking_for_errors(self, max_page: bool = False, urls: bool = False) -> Union[int, List[str]]:
        for attempt in range(self.__number_attempts_in_case_of_error):
            self.__init_catalog()
            condition_max_page = self.__catalog.max_page[0]
            condition_product_list = self.__catalog.product_list[0]

            if condition_max_page and max_page:
                return self.__catalog.max_page[1].max_page

            if condition_product_list and urls:
                return self.__catalog.product_list[1].urls_product
            sleep(self.__delay_after_error)

        if max_page:
            return 0

        if urls:
            return []
