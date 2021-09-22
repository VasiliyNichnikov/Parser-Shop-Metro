class CatalogListError(Exception):
    pass


class NotFoundCatalogPagination(CatalogListError):
    pass


class NotFoundItemsCatalog(CatalogListError):
    pass


class NotFoundMaxPage(CatalogListError):
    pass