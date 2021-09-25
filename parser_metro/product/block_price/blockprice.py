from typing import Union
from bs4 import Tag, NavigableString
from parser_metro.product.block_price.iblockprice import IBlockPrice
from parser_metro.product.block_price.blockpriceerror import NotFindProductPageAside, \
    NotFindProductPageCard, \
    NotFindPriceCardHead, \
    NotFindCardHeadLeft


class BlockPrice(IBlockPrice):
    @property
    def main_price(self) -> str:
        return self.__main_price

    @property
    def old_price(self) -> str:
        return self.__old_price

    def __init__(self, block: Union[Tag, NavigableString]) -> None:
        self.__block = block
        self.__main_price = "0"
        self.__old_price = "0"

    def search_data(self) -> None:
        self.__find_product_page_aside()
        self.__find_product_page_card()
        self.__find_price_card_head()
        self.__find_price_card_head_left()

        self.__main_price = self.__get_main_price()
        self.__old_price = self.__get_old_price()

    def __find_product_page_aside(self) -> None:
        self.__product_page_aside: Union[Tag, NavigableString] = self.__block. \
            find("aside", {"id": "product-page__aside", "class": "product-page__aside"})
        if self.__product_page_aside is None:
            raise NotFindProductPageAside("Not find product aside")

    def __find_product_page_card(self) -> None:
        self.__product_page_card: Union[Tag, NavigableString] = self.__product_page_aside. \
            find("div", {"class": ["product-page__card vue-affix", "affix-top"]})
        if self.__product_page_card is None:
            raise NotFindProductPageCard("Not find product card")

    def __find_price_card_head(self) -> None:
        self.__price_card_head: Union[Tag, NavigableString] = self.__product_page_card. \
            find("div", {"class": "price-card__head"})
        if self.__price_card_head is None:
            raise NotFindPriceCardHead("Not find price card head")

    def __find_price_card_head_left(self) -> None:
        self.__price_card_head_left: Union[Tag, NavigableString] = self.__price_card_head. \
            find("div", {"class": "price-card__head-left"})
        if self.__price_card_head_left is None:
            raise NotFindCardHeadLeft("Not find card head left")

    def __get_main_price(self) -> str:
        price_card: Union[Tag, NavigableString] = self.__price_card_head_left. \
            find("div", {"class": ["price-card__price", "price-card__price--promo"]})
        if price_card is None:
            return "Not main price"
        price: Union[Tag, NavigableString] = price_card.find("span", {"itemprop": "price"})
        if price is None:
            return "0"
        return price.text

    def __get_old_price(self) -> str:
        price_card: Union[Tag, NavigableString] = self.__price_card_head_left. \
            find("div", {"class": "price-card__oldprice"})
        if price_card is None:
            return "Not old price"
        price: Union[Tag, NavigableString] = price_card.find("span")
        if price is None:
            return "0"
        return price.text
