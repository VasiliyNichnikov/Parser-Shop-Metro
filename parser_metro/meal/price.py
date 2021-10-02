from typing import Union
from parser_metro.meal.iparameter import IParameter
from convertor.from_string_to_number import get_number_float
from parser_metro.product.block_price.blockprice import IBlockPrice


class Price(IParameter):
    def __init__(self, price: IBlockPrice) -> None:
        self.__price = price

    def get(self) -> Union[float, int]:
        return self.__convert_to_number()

    def __convert_to_number(self) -> Union[float, int]:
        price: str = self.__price.main_price
        return get_number_float(price)
