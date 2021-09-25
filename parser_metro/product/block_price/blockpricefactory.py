from bs4 import BeautifulSoup

from parser_metro.product.block_price.blockprice import BlockPrice
from parser_metro.product.block_price.iblockprice import IBlockPrice


class BlockPriceFactory:
    @staticmethod
    def build(html: str) -> IBlockPrice:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return BlockPrice(bs)
