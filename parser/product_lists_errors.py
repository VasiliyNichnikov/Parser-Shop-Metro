class ProductListsErrorsException(Exception):
    pass


class NotFoundProductLists(ProductListsErrorsException):
    pass


class NotFoundItemsProdictLists(ProductListsErrorsException):
    pass
