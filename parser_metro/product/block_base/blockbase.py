import re
from typing import Union
from bs4 import Tag, NavigableString
from parser_metro.product.block_base.iblockbase import IBlockBase
from parser_metro.product.block_base.blockbaseerror import NotFindPageSpec, \
    NotFindPageDesc


class BlockBase(IBlockBase):
    @property
    def title(self) -> str:
        return self.__title

    @property
    def code(self) -> str:
        return self.__code

    @property
    def brand(self) -> str:
        return self.__brand

    def __init__(self, block: Union[Tag, NavigableString]) -> None:
        self.__block = block
        self.__title: str = "Not Title"
        self.__code: str = "Not Code"
        self.__brand: str = "Not Brand"

    def search_data(self) -> None:
        self.__find_page_spec()
        self.__find_page_desc()

        self.__title = self.__get_title()
        self.__code = self.__get_code()
        self.__brand = self.__get_brand()

    def __find_page_spec(self) -> None:
        self.__page_spec: Union[Tag, NavigableString] = self.__block.find("div", {"class": "product-page__spec"})
        if self.__page_spec is None:
            raise NotFindPageSpec("Not find spec")

    def __find_page_desc(self) -> None:
        self.__page_desc: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__desc"})
        if self.__page_desc is None:
            raise NotFindPageDesc("Not find desc")

    def __get_title(self) -> str:
        result: str = "0"
        page_title: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__title"})
        if page_title is None:
            return result
        title: Union[Tag, NavigableString] = page_title.find("h1")
        if title is None:
            return result
        result = re.sub(r"\s+", ' ', title.text)
        return result

    def __get_code(self) -> str:
        result: str = "0"
        page_code: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__code"})
        if page_code is None:
            return result
        product_id: Union[Tag, NavigableString] = page_code.find("span", {"itemprop": "productID"})
        if product_id is None:
            return result
        result = product_id.text
        return result

    def __get_brand(self) -> str:
        result: str = "0"
        page_brand: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__brand"})
        if page_brand is None:
            return result
        brand: Union[Tag, NavigableString] = page_brand.find("span")
        if brand is None:
            return result
        result = re.sub(r"\s+", ' ', brand.text)
        return result
