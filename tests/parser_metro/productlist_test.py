import pytest

from parser_metro.product_lists.iproductlist import IProductList
from parser_metro.product_lists.productlistfactory import ProductListFactory
from parser_metro.product_lists.productlistserror import NotFoundMainBlockProduct

main_path = "../../static/html_files/"


def get_html_code(name: str) -> str:
    global main_path
    with open(main_path + name, "r", encoding="UTF-8") as reading:
        return reading.read()


def test_search_urls_product_when_html_code_right() -> None:
    # ARRANGE
    html_code_right: str = get_html_code("list_product.html")
    product_list: IProductList = ProductListFactory().build(html_code_right)
    # ACT
    product_list.search_urls_product()
    # ACCESS
    assert len(product_list.urls_product) == 30


def test_search_urls_product_when_html_code_without_page_products() -> None:
    # ARRANGE
    html_code_without_page_product: str = get_html_code("list_product_without_catalog_item.html")
    product_list: IProductList = ProductListFactory().build(html_code_without_page_product)
    # ACT
    with pytest.raises(NotFoundMainBlockProduct):
        product_list.search_urls_product()
