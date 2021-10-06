from bs4 import BeautifulSoup
from parser_metro.product.product import Product
from parser_metro.meal.meal import Meal
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.product.productfactory import ProductFactory
from typing import Union


class ParserProduct:
    def __init__(self, driver: IWebDriver, url: str) -> None:
        self.__driver: IWebDriver = driver
        self.__bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(url)

    def run(self) -> None:
        product: Product = ProductFactory.build(self.__bs)
        meal: Meal = Meal(product)
        meal.init_product()

        print("---------------")
        print(meal.name)
        print(meal.energy_value)
        print(meal.country)
