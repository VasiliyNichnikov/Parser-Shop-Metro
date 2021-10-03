class BlockImagesError(Exception):
    pass


class NotFindPageSwiper(BlockImagesError):
    pass


class NotPageSlideContainer(BlockImagesError):
    pass


class NotFindPageSwiperWrapper(BlockImagesError):
    pass


class NotFindPageUrlsImages(BlockImagesError):
    pass
