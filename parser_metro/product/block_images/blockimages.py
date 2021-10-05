import typing
from typing import Union, List, Dict
from bs4 import Tag, NavigableString, ResultSet

from parser_metro.product.block_images.iblockimages import IBlockImages
from parser_metro.product.block_images.blockimageserror import NotFindPageSwiper, \
    NotPageSlideContainer, \
    NotFindPageSwiperWrapper, \
    NotFindPageUrlsImages


class BlockImages(IBlockImages):
    @property
    def main_image(self) -> str:
        return self.__main_image

    @property
    def urls_additional(self) -> typing.List[str]:
        return self.__urls_additional

    def __init__(self, block: Union[Tag, NavigableString]) -> None:
        self.__block = block
        self.__main_image: str = ""
        self.__urls_additional: List[str] = []

    def search_data(self) -> None:
        self.__find_page_swiper()
        self.__find_page_slide_container()
        self.__find_page_swiper_wrapper()
        self.__find_page_urls_images()

        images_urls = self.__get_urls()
        self.__main_image = images_urls["main"]
        self.__urls_additional = images_urls["additional"]

    def __find_page_swiper(self) -> None:
        self.__page_swiper: Union[Tag, NavigableString] = self.__block.find("div", {"class": "product-page__swiper"})
        if self.__page_swiper is None:
            raise NotFindPageSwiper("Not find swiper")

    def __find_page_slide_container(self) -> None:
        self.__page_slide_container: Union[Tag, NavigableString] = self.__page_swiper. \
            find("div", {"class": "slide-container"})
        if self.__page_slide_container is None:
            raise NotPageSlideContainer("Not find slide container")

    def __find_page_swiper_wrapper(self) -> None:
        self.__page_swiper_wrapper: Union[Tag, NavigableString] = self.__page_slide_container. \
            find("div", {"class": "swiper-wrapper"})
        if self.__page_swiper_wrapper is None:
            raise NotFindPageSwiperWrapper("Not find page swiper wrapper")

    def __find_page_urls_images(self) -> None:
        self.__urls_images: ResultSet = self.__page_swiper_wrapper. \
            find_all("div", {"class": "product-page__slide"})
        if self.__urls_images is None:
            raise NotFindPageUrlsImages("Not find page urls images")

    def __get_urls(self) -> Dict:
        result: Dict = {"main": "", "additional": []}
        for url_image in self.__urls_images:
            url: Union[Tag, NavigableString] = url_image.find("img", {"class": "product-page__slide-img"})
            if url is not None:
                ready_url = url.get("src")
                if result["main"] == "":
                    result["main"] = ready_url
                else:
                    result["additional"].append(ready_url)
        return result

    # def __find_page_slide_nav(self) -> None:
    #     self.__page_slide_nav: Union[Tag, NavigableString] = self.__page_swiper. \
    #         find("div", {"class": "product-page__slide-nav"})

    # def __get_url_main_image(self) -> str:
    #     result: str = "0"
    #     main_image: Union[Tag, NavigableString] = self.__page_slide_container. \
    #         find("img", {"class": "product-page__slide-img"})
    #     if main_image is None:
    #         return result
    #     result = main_image.get("src")
    #     return result
    #
    # def __get_urls_additional(self) -> List[str]:
    #     urls: List[str] = []
    #     if self.__page_slide_nav is None:
    #         return urls
    #     items: ResultSet = self.__page_slide_nav.find_all("div", {"class": "swiper-slide"})
    #     for item in items:
    #         a: Union[Tag, NavigableString] = item.find("a")
    #         if a is not None:
    #             image: Union[Tag, NavigableString] = a.find("img")
    #             if image is not None:
    #                 urls.append(image.get("src"))
    #     return urls
