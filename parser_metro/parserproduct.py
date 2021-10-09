from bs4 import BeautifulSoup
from parser_metro.product.product import Product
from parser_metro.meal.meal import Meal
from recipient_from_server.iwebdriver import IWebDriver
from parser_metro.product.productfactory import ProductFactory
from typing import Union
from database import db_session
from database.ad_metro import AdMetro
from database.additional_images import AdditionalImages
from database.article_images import ArticleImages


class ParserProduct:
    def __init__(self, driver: IWebDriver, url: str) -> None:
        self.__driver: IWebDriver = driver
        self.__bs: Union[BeautifulSoup, None] = self.__driver.get_page_bs(url)

    def run(self) -> None:
        product: Product = ProductFactory.build(self.__bs)
        meal: Meal = Meal(product)
        meal.init_product()
        self.upload_product_to_database(meal)

    @staticmethod
    def upload_product_to_database(meal: Meal) -> None:
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
        for additional_image in meal.additional_images:
            additional_image_table = AdditionalImages(IMAGE=additional_image)
            ad_metro.ADDITIONAL_IMAGES.append(additional_image_table)

        for article_image in meal.article_images:
            article_image_table = ArticleImages(ARTICLE=article_image)
            ad_metro.ARTICLE_IMAGES.append(article_image_table)

        session.commit()
