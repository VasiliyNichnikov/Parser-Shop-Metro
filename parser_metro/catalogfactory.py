from bs4 import BeautifulSoup
from parser_metro.catalog import Catalog
from parser_metro.product_lists.productlist import ProductList, IProductList
from parser_metro.max_page.searchmaxpage import SearchMaxPage, ISearchMaxPage


class CatalogFactory:
    @staticmethod
    def build(bs: BeautifulSoup) -> Catalog:
        product_list: IProductList = ProductList(bs)
        search_max_page: ISearchMaxPage = SearchMaxPage(bs)
        return Catalog(product_list=product_list,
                       max_page=search_max_page)
