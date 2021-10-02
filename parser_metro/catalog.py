from parser_metro.max_page.searchmaxpage import ISearchMaxPage
from parser_metro.max_page.searchmaxpageerror import SearchMaxPageError

from parser_metro.product_lists.productlist import IProductList
from parser_metro.product_lists.productlisterror import ProductListError


class Catalog:
    @property
    def max_page(self) -> (bool, ISearchMaxPage):
        return self.__is_max_page, self.__max_page

    @property
    def product_list(self) -> (bool, IProductList):
        return self.__is_product_list, self.__product_list

    def __init__(self, max_page: ISearchMaxPage, product_list: IProductList) -> None:
        self.__is_max_page: bool = False
        self.__is_product_list: bool = False

        self.__max_page = max_page
        self.__product_list = product_list

    def init_max_page_and_product_list(self) -> None:
        self.__is_max_page = self.__init_max_page()
        self.__is_product_list = self.__init_product_list()

    def __init_max_page(self) -> bool:
        try:
            self.__max_page.search_data()
            return True
        except SearchMaxPageError as e:
            print(f"Max page - {e}")
            return False

    def __init_product_list(self) -> bool:
        try:
            self.__product_list.search_data()
            return True
        except ProductListError as e:
            print(f"Product list - {e}")
            return False
