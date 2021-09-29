from parser_metro.product.block_base.iblockbase import IBlockBase
from parser_metro.product.block_base.blockbaseerror import BlockBaseError

from parser_metro.product.block_images.iblockimages import IBlockImages
from parser_metro.product.block_images.blockimageserror import BlockImagesError

from parser_metro.product.block_specifications.iblockspecifications import IBlockSpecifications
from parser_metro.product.block_specifications.blockspecificationserror import BlockSpecificationsError

from parser_metro.product.block_price.iblockprice import IBlockPrice
from parser_metro.product.block_price.blockpriceerror import BlockPriceError


class Product:
    @property
    def base(self) -> (bool, IBlockBase):
        return self.__is_base, self.__base

    @property
    def images(self) -> (bool, IBlockImages):
        return self.__is_images, self.__images

    @property
    def specifications(self) -> (bool, IBlockSpecifications):
        return self.__is_specifications, self.__specifications

    @property
    def price(self) -> (bool, IBlockPrice):
        return self.__is_price, self.__price

    def __init__(self, block_base: IBlockBase, block_images: IBlockImages, block_specifications: IBlockSpecifications,
                 block_price: IBlockPrice) -> None:
        self.__is_base: bool = False
        self.__is_images: bool = False
        self.__is_specifications: bool = False
        self.__is_price: bool = False

        self.__base = block_base
        self.__images = block_images
        self.__specifications = block_specifications
        self.__price = block_price

    def init_blocks(self) -> None:
        self.__is_base = self.__init_base()
        self.__is_images = self.__init_images()
        self.__is_specifications = self.__init_specifications()
        self.__is_price = self.__init_price()

    def __init_base(self) -> bool:
        try:
            self.__base.search_data()
            return True
        except BlockBaseError as e:
            print(f"Block base - {e}")
            return False

    def __init_images(self) -> bool:
        try:
            self.__images.search_data()
            return True
        except BlockImagesError as e:
            print(f"Block images - {e}")
            return False

    def __init_specifications(self) -> bool:
        try:
            self.__specifications.search_data()
            return True
        except BlockSpecificationsError as e:
            print(f"Block specifications - {e}")
            return True

    def __init_price(self) -> bool:
        try:
            self.__price.search_data()
            return True
        except BlockPriceError as e:
            print(f"Block price - {e}")
            return False
