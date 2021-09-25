from typing import Union
from bs4 import Tag, NavigableString
from parser_metro.product.blockbaseerror import NotFindPageSpec, \
    NotFindPageDesc, \
    NotFindPageInfo, \
    NotFindTitle, \
    NotFindCode, \
    NotFindBrand


class BlockBase:
    def __init__(self, block: Union[Tag, NavigableString]):
        self.__block = block

    def __find_page_spec(self) -> None:
        self.__page_spec: Union[Tag, NavigableString] = self.__block.find("div", {"class": "product-page__spec"})
        if self.__page_spec is None:
            raise NotFindPageSpec("Not find spec")

    def __find_page_desc(self) -> None:
        self.__page_desc: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__desc"})
        if self.__page_desc is None:
            raise NotFindPageDesc("Not find desc")

    def __find_page_info(self) -> None:
        self.__page_info: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__info"})
        if self.__page_info is None:
            raise NotFindPageInfo("Not find info")

    def __get_title(self) -> str:
        page_title: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__title"})
        title: Union[Tag, NavigableString] = page_title.find("h1")
        if title is None:
            raise NotFindTitle("Not find title")
        return title.text

    def __get_code(self) -> str:
        page_code: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__code"})
        product_id: Union[Tag, NavigableString] = page_code.find("span", {"itemprop": "productID"})
        if product_id is None:
            raise NotFindCode("Not find code")
        return product_id.text

    def __get_brand(self) -> str:
        page_brand: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__brand"})
        brand: Union[Tag, NavigableString] = page_brand.find("span")
        if brand is None:
            raise NotFindBrand("Not find brand")
        return brand.text
