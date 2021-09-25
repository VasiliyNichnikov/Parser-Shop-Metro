class BlockBaseError(Exception):
    pass


class NotFindPageSpec(BlockBaseError):
    pass


class NotFindPageDesc(BlockBaseError):
    pass


class NotFindPageInfo(BlockBaseError):
    pass


class NotFindTitle(BlockBaseError):
    pass


class NotFindCode(BlockBaseError):
    pass


class NotFindBrand(BlockBaseError):
    pass
