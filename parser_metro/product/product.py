from parser_metro.product.block_base.iblockbase import IBlockBase
from parser_metro.product.block_base.blockbaseerror import BlockBaseError

from parser_metro.product.block_images.iblockimages import IBlockImages
from parser_metro.product.block_images.blockimageserror import BlockImagesError

from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications
from parser_metro.product.block_specifications.blockspecificationserror import BlockSpecificationsError

from parser_metro.product.block_price.iblockprice import IBlockPrice
from parser_metro.product.block_price.blockpriceerror import BlockPriceError


class Product:
    def __init__(self, block_base: IBlockBase, block_images: IBlockImages, block_specifications: IBlockSpecifications,
                 block_price: IBlockPrice) -> None:
        self.__base = block_base
        self.__images = block_images
        self.__specifications = block_specifications
        self.__price = block_price

    def init_blocks(self) -> None:
        self.__init_base()
        self.__init_images()
        self.__init_specifications()
        self.__init_price()

    def __init_base(self) -> None:
        try:
            self.__base.search_data()
        except BlockBaseError as e:
            print(f"Block base - {e}")

    def __init_images(self) -> None:
        try:
            self.__images.search_data()
        except BlockImagesError as e:
            print(f"Block images - {e}")

    def __init_specifications(self) -> None:
        try:
            self.__specifications.search_data()
        except BlockSpecificationsError as e:
            print(f"Block specifications - {e}")

    def __init_price(self) -> None:
        try:
            self.__price.search_data()
        except BlockPriceError as e:
            print(f"Block price - {e}")
