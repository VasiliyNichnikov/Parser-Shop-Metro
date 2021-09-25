class BlockPriceError(Exception):
    pass


class NotFindProductPageAside(BlockPriceError):
    pass


class NotFindProductPageCard(BlockPriceError):
    pass


class NotFindPriceCardHead(BlockPriceError):
    pass


class NotFindCardHeadLeft(BlockPriceError):
    pass
