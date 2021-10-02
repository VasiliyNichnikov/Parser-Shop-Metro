from parser_metro.meal.iparameter import IParameter
from convertor.from_string_to_number import get_number_float
from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications


class PackingParameters(IParameter):
    def __init__(self, specification: IBlockSpecifications, key: str):
        self.__specification: IBlockSpecifications = specification
        self.__key = key

    def get(self) -> float:
        if self.__key in self.__specification.specifications.keys():
            value: str = self.__specification.specifications[self.__key]
            return self.__conversion_to_mm_from_cm(value)
        return 0

    @staticmethod
    def __conversion_to_mm_from_cm(value: str) -> float:
        cm: float = get_number_float(value)
        return cm * 10
