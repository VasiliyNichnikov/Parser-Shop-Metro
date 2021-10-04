from typing import Union
from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_price.blockprice import IBlockPrice
from convertor.from_string_to_number import get_number_float


class PriceWithoutDiscount(IParameter):
    def __init__(self, price: IBlockPrice):
        self.__price = price

    def get(self) -> Union[float, int]:
        return self.__convert_to_number()

    def __convert_to_number(self) -> Union[float, int]:
        old_price: str = self.__price.old_price
        return get_number_float(old_price)
