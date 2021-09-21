class ProductListsError(Exception):
    pass


class NotFoundMainBlockProduct(ProductListsError):
    pass


class NotFoundItemsProduct(ProductListsError):
    pass


class NotFoundUrlsProducts(ProductListsError):
    pass
