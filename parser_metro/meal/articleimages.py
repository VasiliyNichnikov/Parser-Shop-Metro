from typing import List
from parser_metro.meal.iparameter import IParameter
from parser_metro.product.block_images.iblockimages import IBlockImages


class ArticleImages(IParameter):
    def __init__(self, images: IBlockImages):
        self.__images = images

    def get(self) -> List[str]:
        urls: List[str] = self.__images.urls_additional.copy()
        urls.append(self.__images.main_image)
        return [self.__get_article_url(url) for url in urls]

    @staticmethod
    def __get_article_url(url: str) -> str:
        parts: List[str] = url.split('_pim_')
        if len(parts) > 1:
            part_two: str = parts[1]
            return part_two.split('_')[0]
        return ""
