class ProductErrors(Exception):
    pass


class NotFoundCatalogItemGroup(ProductErrors):
    pass


class NotFoundCatalogItemDefaultImage(ProductErrors):
    pass


class NotFoundUrl(ProductErrors):
    pass
