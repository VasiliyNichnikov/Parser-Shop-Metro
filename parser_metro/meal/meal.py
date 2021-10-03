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
from parser_metro.meal.expirationdate import ExpirationDate
from parser_metro.meal.informationspecificationkey import InformationSpecificationKey
from parser_metro.meal.packingparameters import PackingParameters


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

    @property
    def type_product(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "тип").get()
        return "0"

    @property
    def minimum_storage_temperature(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "минимальнаятемпературахранения,").get()
        return "0"

    @property
    def maximum_storage_temperature(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "максимальнаятемпературахранения,").get()
        return "0"

    @property
    def structure(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "состав").get()
        return "0"

    @property
    def weight(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "вес,гр").get()
        return "0"

    @property
    def shelf_life(self) -> int:
        condition, specification = self.__product.specifications
        if condition:
            return ExpirationDate(specification, "срокгодности,дн", "срокгодности,мес").get()
        return 0

    @property
    def packing_width(self) -> float:
        condition, specification = self.__product.specifications
        if condition:
            return PackingParameters(specification, "ширинаупаковки,см").get()
        return 0

    @property
    def packing_height(self) -> float:
        condition, specification = self.__product.specifications
        if condition:
            return PackingParameters(specification, "высотаупаковки,см").get()
        return 0

    @property
    def packing_length(self) -> float:
        condition, specification = self.__product.specifications
        if condition:
            return PackingParameters(specification, "длинаупаковки,см").get()
        return 0

    @property
    def country(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "страна").get()
        return "0"

    @property
    def type_of_packaging(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "типупаковки").get()
        return "0"

    @property
    def energy_value(self) -> str:
        condition, specification = self.__product.specifications
        if condition:
            return InformationSpecificationKey(specification, "энергетическаяценность,ккал/100гр").get()
        return "0"

    def __init__(self, product: Product):
        self.__product = product

    def init_product(self):
        self.__product.init_blocks()
