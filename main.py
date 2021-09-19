import typing
from requests import get, Response
from parser_metro.product_lists import ProductList
from parser_metro.iproduct_list import IProductList

path_file = "static/search.html"

with open(path_file, "rb") as read:
    b: bytes = read.read()
    text: str = b.decode("UTF-8")

product_list: IProductList = ProductList(text)
urls: typing.List[str] = product_list.search_urls_products()
i: int = 0
for url in urls:
    i += 1
    print(url)
    print(len(url))
print(f"Len: {i}")
