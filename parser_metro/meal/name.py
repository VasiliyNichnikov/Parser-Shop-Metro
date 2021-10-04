from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_base.blockbase import IBlockBase


class Name(IParameter):
    def get(self) -> str:
        return self.__base.title

    def __init__(self, base: IBlockBase):
        self.__base = base
