class SearchMaxPageError(Exception):
    pass


class NotFoundCatalogPagination(SearchMaxPageError):
    pass


class NotFoundItemsCatalog(SearchMaxPageError):
    pass


class NotFoundMaxPage(SearchMaxPageError):
    pass