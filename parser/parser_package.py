from bs4 import BeautifulSoup
from typing import List
from parser_metro.catalog.product_lists.productlist import IProductList, ProductList
from recipient_from_server.chromewebdriver import ChromeWebDriver, IWebDriver
from parser_metro.catalog.max_page.searchmaxpage import ISearchMaxPage, SearchMaxPage


class Parser:
    def __init__(self, url: str, path_driver: str) -> None:
        self.__url = url
        self.__path_driver = path_driver
        self.__driver: IWebDriver = None
        self.__bs: BeautifulSoup = None
        self.__max_page = 0
        self.__urls = []

    @property
    def max_page(self) -> int:
        return self.__max_page

    @property
    def urls(self) -> List[str]:
        return self.__urls

    def __get_beautiful_soup(self) -> BeautifulSoup:
        if self.__bs is None:
            self.__bs = BeautifulSoup(self.__get_html_code(), "lxml")
        return self.__bs

    def __get_html_code(self) -> str:
        if self.__driver is None:
            self.__creating_webdriver()
        with self.__driver.driver as driver:
            driver.get(self.__url)
            return driver.page_source

    def __creating_webdriver(self) -> None:
        self.__driver = ChromeWebDriver(self.__path_driver)
        self.__driver.create(options=None)

    def __get_max_page(self) -> int:
        search_max_page: ISearchMaxPage = SearchMaxPage(self.__get_beautiful_soup())
        search_max_page.search_data()
        return search_max_page.max_page

    def __get_list_products(self) -> List[str]:
        product_list: IProductList = ProductList(self.__get_beautiful_soup())
        product_list.search_data()
        return product_list.urls_product

    def search_data(self):
        self.__max_page = self.__get_max_page()
        self.__urls = self.__get_list_products()
