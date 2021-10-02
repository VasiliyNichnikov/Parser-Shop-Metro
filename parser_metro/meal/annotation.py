from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications


class Annotation(IParameter):
    def __init__(self, specifications: IBlockSpecifications) -> None:
        self.__specifications = specifications

    def get(self) -> str:
        return self.__specifications.description
