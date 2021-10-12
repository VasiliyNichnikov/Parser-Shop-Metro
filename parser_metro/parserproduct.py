from bs4 import BeautifulSoup
from time import sleep
from parser_metro.product.product import Product
from parser_metro.meal.meal import Meal
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.product.productfactory import ProductFactory
from typing import Union
from database import db_session
from database.ad_metro import AdMetro


class ParserProduct:
    def __init__(self, driver: IWebDriver, url: str,
                 number_attempts_in_case_of_error: int,
                 delay_after_error: int) -> None:
        self.__driver = driver
        self.__url = url
        self.__number_attempts_in_case_of_error = number_attempts_in_case_of_error
        self.__delay_after_error = delay_after_error

    def run(self) -> None:
        meal: Meal = self.__get_meal()
        self.upload_product_to_database(meal)

    def __get_meal(self) -> Meal:
        bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(self.__url)

        product: Product = ProductFactory.build(bs)
        meal: Meal = Meal(product)
        meal.init_product()
        if not meal.get_condition_base_block() and self.__number_attempts_in_case_of_error > 0:
            self.__number_attempts_in_case_of_error -= 1
            sleep(self.__delay_after_error)
            meal = self.__get_meal()
        return meal

    @staticmethod
    def __get_str_additional_images(meal) -> str:
        if len(meal.additional_images) > 0:
            result = '\n'.join(meal.additional_images)
            return result
        return "0"

    @staticmethod
    def __get_str_article_images(meal) -> str:
        if len(meal.article_images) > 0:
            result = '\n'.join(meal.article_images)
            return result
        return "0"

    def upload_product_to_database(self, meal: Meal) -> None:
        session = db_session.create_session()

        ad_metro = AdMetro(
            ARTICLE_NUMBER=meal.article_number,
            NAME=meal.name,
            PRICE=meal.price,
            PRICE_WITHOUT_DISCOUNT=meal.price_without_discount,
            WEIGHT=meal.weight,
            PACKING_WIDTH=meal.packing_width,
            PACKING_HEIGHT=meal.packing_height,
            PACKING_LENGTH=meal.packing_length,
            MAIN_IMAGE=meal.main_image,
            ADDITIONAL_IMAGES=self.__get_str_additional_images(meal),
            ARTICLE_IMAGES=self.__get_str_article_images(meal),
            TYPE_PRODUCT=meal.type_product,
            TYPE_OF_PACKAGING=meal.type_of_packaging,
            MINIMUM_STORAGE_TEMPERATURE=meal.minimum_storage_temperature,
            MAXIMUM_STORAGE_TEMPERATURE=meal.maximum_storage_temperature,
            SHELF_LIFE=meal.shelf_life,
            BRAND=meal.brand,
            STRUCTURE=meal.structure,
            ANNOTATION=meal.annotation,
            COUNTRY=meal.country,
            ENERGY_VALUE=meal.energy_value
        )
        session.add(ad_metro)

        session.commit()
        session.close()
