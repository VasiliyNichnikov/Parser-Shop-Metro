from typing import List
from parser_metro.product.block_images.iblockimages import IBlockImages
from parser_metro.meal.iparameter import IParameter


class AdditionalImages(IParameter):
    def __init__(self, images: IBlockImages):
        self.__images: IBlockImages = images

    def get(self) -> List[str]:
        return self.__images.urls_additional
