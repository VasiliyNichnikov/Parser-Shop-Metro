import pytest
from tests.workingwithfiles import get_html_code

from parser_metro.product_lists.iproductlist import IProductList
from parser_metro.product_lists.productlistfactory import ProductListFactory
from parser_metro.product_lists.productlisterror import NotFoundMainBlockProduct

main_path = "../../static/html_files/"


def test_search_urls_product_when_html_code_right() -> None:
    # ARRANGE
    global main_path
    html_code_right: str = get_html_code(main_path + "list_product.html")
    product_list: IProductList = ProductListFactory().build(html_code_right)
    # ACT
    product_list.search_urls_product()
    # ACCESS
    assert len(product_list.urls_product) == 30


def test_search_urls_product_when_html_code_without_page_products() -> None:
    # ARRANGE
    global main_path
    html_code_without_page_product: str = get_html_code(main_path + "list_product_without_page_products.html")
    product_list: IProductList = ProductListFactory().build(html_code_without_page_product)
    # ACT
    with pytest.raises(NotFoundMainBlockProduct):
        product_list.search_urls_product()
