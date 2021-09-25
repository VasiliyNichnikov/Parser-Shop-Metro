from typing import Union, List
from bs4 import Tag, NavigableString, ResultSet
from parser_metro.product.blockimageserror import NotFindPageSwiper, NotPageSlideContainer, NotPageSlideNav


class BlockImages:
    def __init__(self, block: Union[Tag, NavigableString]) -> None:
        self.__block = block

    def __find_page_swiper(self) -> None:
        self.__page_swiper: Union[Tag, NavigableString] = self.__block.find("div", {"class": "product-page__swiper"})
        if self.__page_swiper is None:
            raise NotFindPageSwiper("Not find swiper")

    def __find_page_slide_container(self) -> None:
        self.__page_slide_container: Union[Tag, NavigableString] = self.__page_swiper. \
            find("div", {"class": "slide-container"})
        if self.__page_slide_container is None:
            raise NotPageSlideContainer("Not find slide container")

    def __find_page_slide_nav(self) -> None:
        self.__page_slide_nav: Union[Tag, NavigableString] = self.__page_swiper. \
            find("div", {"class": "product-page__slide-nav"})
        if self.__page_slide_nav is None:
            raise NotPageSlideNav("Not find slide nav")

    def __get_url_main_image(self) -> str:
        main_image: Union[Tag, NavigableString] = self.__page_slide_container. \
            find("img", {"class": "product-page__slide-img"})
        if main_image is None:
            return "Not main image"
        return main_image.get("src")

    def __get_urls_additional(self) -> List[str]:
        urls: List[str] = []
        items: ResultSet = self.__page_slide_nav.find_all("div", {"class": "swiper-slide"})
        for item in items:
            a: Union[Tag, NavigableString] = item.find("a")
            if a is not None:
                image: Union[Tag, NavigableString] = a.find("img")
                if image is not None:
                    urls.append(image.get("src"))
        return urls
