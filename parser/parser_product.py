from bs4 import BeautifulSoup
from parser_metro.product.product import Product
from parser_metro.meal.meal import Meal
from parser_metro.product.productfactory import ProductFactory
from recipient_from_server.chromewebdriver import ChromeWebDriver, IWebDriver
from typing import List


class ParserProduct:
    def __init__(self, url: List[str], path_driver: str):
        self.__url = url
        self.__path_driver = path_driver
        self.__bs = None
        self.__driver: IWebDriver = None

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

    def run(self) -> None:
        product: Product = ProductFactory.build(self.__get_beautiful_soup())
        meal: Meal = Meal(product)
        meal.init_product()
        print(meal.name)
