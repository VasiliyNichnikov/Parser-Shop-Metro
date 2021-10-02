class UrlProductError(Exception):
    pass


class NotFoundCatalogItemGroup(UrlProductError):
    pass


class NotFoundCatalogItemDefaultImage(UrlProductError):
    pass


class NotFoundUrl(UrlProductError):
    pass
