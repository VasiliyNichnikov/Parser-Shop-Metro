from bs4 import BeautifulSoup
from parser_metro.product.block_images.blockimages import BlockImages
from parser_metro.product.block_images.iblockimages import IBlockImages


class BlockImagesFactory:
    @staticmethod
    def build(html: str) -> IBlockImages:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return BlockImages(bs)
