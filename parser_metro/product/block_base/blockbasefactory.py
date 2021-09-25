from bs4 import BeautifulSoup
from parser_metro.product.block_base.blockbase import BlockBase
from parser_metro.product.block_base.iblockbase import IBlockBase


class BlockBaseFactory:
    @staticmethod
    def build(html: str) -> IBlockBase:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return BlockBase(bs)

