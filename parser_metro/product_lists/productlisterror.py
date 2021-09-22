class ProductListError(Exception):
    pass


class NotFoundMainBlockProduct(ProductListError):
    pass


class NotFoundItemsProduct(ProductListError):
    pass


class NotFoundUrlsProducts(ProductListError):
    pass
