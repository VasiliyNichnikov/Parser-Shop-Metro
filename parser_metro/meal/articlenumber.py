from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_base.blockbase import IBlockBase
from convertor.from_string_to_number import get_number_int


class ArticleNumber(IParameter):
    def get(self) -> int:
        return self.__convert_to_number()

    def __init__(self, base: IBlockBase):
        self.__base = base

    def __convert_to_number(self) -> int:
        code: str = self.__base.code
        return get_number_int(code)
