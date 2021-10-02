from bs4 import BeautifulSoup
from parser_metro.product.block_base.blockbase import BlockBase, IBlockBase
from parser_metro.product.block_images.blockimages import BlockImages, IBlockImages
from parser_metro.product.block_specifications.blockspecifications import BlockSpecifications, IBlockSpecifications
from parser_metro.product.block_price.blockprice import BlockPrice, IBlockPrice
from parser_metro.product.product import Product


class ProductFactory:
    @staticmethod
    def build(bs: BeautifulSoup) -> Product:
        block_base: IBlockBase = BlockBase(bs)
        block_images: IBlockImages = BlockImages(bs)
        block_specifications: IBlockSpecifications = BlockSpecifications(bs)
        block_price: IBlockPrice = BlockPrice(bs)

        return Product(block_base=block_base,
                       block_images=block_images,
                       block_specifications=block_specifications,
                       block_price=block_price)
