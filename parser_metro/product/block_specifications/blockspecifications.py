import typing
from typing import Union, Dict
from bs4 import Tag, NavigableString, ResultSet

from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications
from parser_metro.product.block_specifications.blockspecificationserror import NotFindProductPageContainer, \
    NotFindProductPageTab, \
    NotFindProductPageFullspec, \
    NotFindProductFullspecAll


class BlockSpecifications(IBlockSpecifications):
    @property
    def specifications(self) -> typing.Dict[str, str]:
        return self.__specifications

    def __init__(self, block: Union[Tag, NavigableString]) -> None:
        self.__block = block
        self.__specifications: Dict[str, str] = {}

    def search_data(self) -> None:
        self.__find_product_page_container()
        self.__find_product_page_tab()
        self.__find_product_page_fullspec()
        self.__find_product_fullspec_all()
        self.__specifications = self.__get_specifications()

    def __find_product_page_container(self) -> None:
        self.__product_page_container: Union[Tag, NavigableString] = self.__block. \
            find("div", {"class": "product-page__container"})
        if self.__product_page_container is None:
            raise NotFindProductPageContainer("Not find product container")

    def __find_product_page_tab(self) -> None:
        self.__product_page_tab: Union[Tag, NavigableString] = self.__product_page_container. \
            find("div", {"class": "product-page__tab"})
        if self.__product_page_tab is None:
            raise NotFindProductPageTab("Not find product tab")

    def __find_product_page_fullspec(self) -> None:
        self.__product_page_fullspec: Union[Tag, NavigableString] = self.__product_page_tab. \
            find("div", {"class": "product-page__fullspec"})
        if self.__product_page_fullspec is None:
            raise NotFindProductPageFullspec("Not find product fullspec")

    def __find_product_fullspec_all(self) -> None:
        self.__product_fullspec_all: ResultSet = self.__product_page_fullspec. \
            find_all("div", {"class": "product-page__fullspec-line"})
        if self.__product_fullspec_all is None:
            raise NotFindProductFullspecAll("Not find product fullspec all")

    def __get_specifications(self) -> Dict[str, str]:
        specifications: Dict[str, str] = {}
        for spec in self.__product_fullspec_all:
            _type: Union[Tag, NavigableString] = spec.find("p")
            _value: Union[Tag, NavigableString] = spec.find("span")
            if _type is not None and _value is not None:
                specifications[_type.text] = _value.text
        return specifications
