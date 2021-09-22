from typing import Union
from bs4 import BeautifulSoup, Tag, NavigableString


class BlockBase:
    def __init__(self, block: Union[Tag, NavigableString]):
        self.__block = block

    def __find_page_spec(self) -> None:
        self.__page_spec: Union[Tag, NavigableString] = self.__block.find("div", {"class": "product-page__spec"})
        if self.__page_spec is None:
            pass  # FIXME Error

    def __find_page_desc(self) -> None:
        self.__page_desc: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__desc"})
        if self.__page_desc is None:
            pass  # FIXME Error

    def __find_page_info(self) -> None:
        self.__page_info: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__info"})
        if self.__page_info is None:
            pass  # FIXME

    def __get_title(self) -> str:
        page_title: Union[Tag, NavigableString] = self.__page_spec.find("div", {"class": "product-page__title"})
        title: Union[Tag, NavigableString] = page_title.find("h1")
        if title is None:
            pass  # FIXME Error
        return title.text

    def __get_code(self) -> str:
        page_code: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__code"})
        product_id: Union[Tag, NavigableString] = page_code.find("span", {"itemprop": "productID"})
        if product_id is None:
            pass  # FIXME Error
        return product_id.text

    def __get_brand(self) -> str:
        page_brand: Union[Tag, NavigableString] = self.__page_desc.find("div", {"class": "product-page__brand"})
        brand: Union[Tag, NavigableString] = page_brand.find("span")
        if brand is None:
            pass  # FIXME Error
        return brand.text
