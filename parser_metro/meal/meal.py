from typing import Union, List

from parser_metro.product.product import Product

from parser_metro.meal.articlenumber import ArticleNumber
from parser_metro.meal.name import Name
from parser_metro.meal.price import Price
from parser_metro.meal.pricewithoutdiscount import PriceWithoutDiscount
from parser_metro.meal.mainimage import MainImage
from parser_metro.meal.additionalimages import AdditionalImages
from parser_metro.meal.articleimages import ArticleImages
from parser_metro.meal.brand import Brand
from parser_metro.meal.annotation import Annotation


class Meal:
    @property
    def article_number(self) -> int:
        condition, base = self.__product.base
        if condition:
            return ArticleNumber(base).get()
        return 0

    @property
    def name(self) -> str:
        condition, base = self.__product.base
        if condition:
            return Name(base).get()
        return "0"

    @property
    def price(self) -> Union[int, float]:
        condition, price = self.__product.price
        if condition:
            return Price(price).get()
        return 0

    @property
    def price_without_discount(self) -> Union[int, float]:
        condition, price = self.__product.price
        if condition:
            return PriceWithoutDiscount(price).get()
        return 0

    @property
    def main_image(self) -> str:
        condition, images = self.__product.images
        if condition:
            return MainImage(images).get()
        return "0"

    @property
    def additional_images(self) -> List[str]:
        condition, images = self.__product.images
        if condition:
            return AdditionalImages(images).get()
        return []

    @property
    def article_images(self) -> List[str]:
        condition, images = self.__product.images
        if condition:
            return ArticleImages(images).get()
        return []

    @property
    def brand(self) -> str:
        condition, base = self.__product.base
        if base:
            return Brand(base).get()
        return "0"

    @property
    def annotation(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return Annotation(specification).get()
        return "0"

    def __init__(self, product: Product):
        self.__product = product

    def init_product(self):
        self.__product.init_blocks()
