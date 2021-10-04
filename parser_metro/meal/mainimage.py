from parser_metro.product.block_images.iblockimages import IBlockImages
from parser_metro.meal.iparameter import IParameter


class MainImage(IParameter):
    def __init__(self, images: IBlockImages):
        self.__images: IBlockImages = images

    def get(self) -> str:
        return self.__images.main_image
