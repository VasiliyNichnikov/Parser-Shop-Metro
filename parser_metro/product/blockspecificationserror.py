class BlockSpecificationsError(Exception):
    pass


class NotFindProductPageContainer(BlockSpecificationsError):
    pass


class NotFindProductPageTab(BlockSpecificationsError):
    pass


class NotFindProductPageFullspec(BlockSpecificationsError):
    pass


class NotFindProductFullspecAll(BlockSpecificationsError):
    pass