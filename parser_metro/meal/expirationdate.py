from parser_metro.meal.iparameter import IParameter
from convertor.from_string_to_number import get_number_int
from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications


class ExpirationDate(IParameter):
    def __init__(self, specification: IBlockSpecifications, *args: str):
        self.__specification: IBlockSpecifications = specification
        self.__keys = args

    def get(self) -> int:
        for key in self.__keys:
            if key in self.__specification.specifications.keys():
                value: str = self.__specification.specifications[key]
                if self.__is_need_translate_value(key):
                    return int(self.__transfer_to_days_from_month(value))
                return get_number_int(value)
        return 0

    @staticmethod
    def __is_need_translate_value(key: str) -> bool:
        part_end: str = key.split(',')[-1]
        return "дн" not in part_end

    @staticmethod
    def __transfer_to_days_from_month(value: str) -> float:
        month: int = get_number_int(value)
        return month * 30.437
