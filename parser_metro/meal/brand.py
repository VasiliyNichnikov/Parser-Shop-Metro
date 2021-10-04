from parser_metro.product.block_base.iblockbase import IBlockBase
from parser_metro.meal.iparameter import IParameter


class Brand(IParameter):
    def __init__(self, base: IBlockBase) -> None:
        self.__base: IBlockBase = base

    def get(self) -> str:
        return self.__base.brand
