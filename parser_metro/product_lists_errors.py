class ProductListsErrorsException(Exception):
    pass


class NotFoundMainBlockProduct(ProductListsErrorsException):
    pass


class NotFoundItemsProduct(ProductListsErrorsException):
    pass


class NotFoundUrlsProducts(ProductListsErrorsException):
    pass
