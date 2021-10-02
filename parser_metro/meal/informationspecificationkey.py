from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications


class InformationSpecificationKey(IParameter):
    def __init__(self, specification: IBlockSpecifications, key: str):
        self.__specification: IBlockSpecifications = specification
        self.__key = key

    def get(self) -> str:
        if self.__key in self.__specification.specifications.keys():
            value: str = self.__specification.specifications[self.__key]
            return value
        return "0"
