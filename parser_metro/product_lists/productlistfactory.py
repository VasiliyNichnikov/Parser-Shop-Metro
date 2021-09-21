from bs4 import BeautifulSoup
from parser_metro.product_lists.productlist import ProductList
from parser_metro.product_lists.iproductlist import IProductList


class ProductListFactory:
    @staticmethod
    def build(html: str) -> IProductList:
        bs: BeautifulSoup = BeautifulSoup(html, "lxml")
        return ProductList(bs)
