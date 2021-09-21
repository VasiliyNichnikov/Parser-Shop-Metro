from bs4 import BeautifulSoup
from parser_metro.ifactory import IFactory
from parser_metro.product_lists.productlist import ProductList
from parser_metro.product_lists.iproductlist import IProductList


class ProductListFactory(IFactory):
    def __init__(self, html: str):
        self.__html = html

    def build(self) -> IProductList:
        bs: BeautifulSoup = BeautifulSoup(self.__html, "lxml")
        return ProductList(bs)
