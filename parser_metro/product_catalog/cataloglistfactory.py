from bs4 import BeautifulSoup
from parser_metro.product_catalog.cataloglist import CatalogList
from parser_metro.product_catalog.icataloglist import ICatalogList


class CatalogListFactory:
    @staticmethod
    def build(html: str) -> ICatalogList:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return CatalogList(bs)
