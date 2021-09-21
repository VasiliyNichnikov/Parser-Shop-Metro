from typing import Union
from bs4 import BeautifulSoup, NavigableString

from parser_metro.product_lists.iurlproduct import IUrlProduct
from parser_metro.product_lists.urlproducterror import NotFoundCatalogItemGroup, NotFoundCatalogItemDefaultImage, \
    NotFoundUrl


class UrlProduct(IUrlProduct):
    @property
    def url(self) -> str:
        return self.__first_part_url + self.__url

    def __init__(self, block: Union[BeautifulSoup, NavigableString]):
        self.__block = block
        self.__first_part_url = "https://msk.metro-cc.ru"
        self.__url = ""

    def search_url(self) -> None:
        self.__find_catalog_item_group()
        self.__find_catalog_item_default_image()
        self.__find_url()

    def __find_catalog_item_group(self) -> None:
        self.__catalog_item_group: Union[BeautifulSoup, NavigableString] = \
            self.__block.find("div", {"class": "catalog-item_group"})
        if self.__catalog_item_group is None:
            raise NotFoundCatalogItemGroup("Not found catalog item group.")

    def __find_catalog_item_default_image(self) -> None:
        self.__catalog_item_default_image: Union[BeautifulSoup, NavigableString] = \
            self.__catalog_item_group.find("div", {"class": "catalog-item_defaut-image"})
        if self.__catalog_item_default_image is None:
            raise NotFoundCatalogItemDefaultImage("Not catalog item default image.")

    def __find_url(self) -> None:
        self.__url: str = self.__catalog_item_default_image.find("a").get("href")
        if self.__url is None:
            raise NotFoundUrl("Not found url.")
