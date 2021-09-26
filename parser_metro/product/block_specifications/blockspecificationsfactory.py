from bs4 import BeautifulSoup

from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications
from parser_metro.product.block_specifications.blockspecifications import BlockSpecifications


class BlockSpecificationsFactory:
    @staticmethod
    def build(html: str) -> IBlockSpecifications:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return BlockSpecifications(bs)
