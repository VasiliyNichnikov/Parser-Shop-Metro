class BlockImagesError(Exception):
    pass


class NotFindPageSwiper(BlockImagesError):
    pass


class NotPageSlideContainer(BlockImagesError):
    pass


class NotPageSlideNav(BlockImagesError):
    pass