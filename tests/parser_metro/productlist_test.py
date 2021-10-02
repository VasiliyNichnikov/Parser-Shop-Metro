import pytest
from bs4 import BeautifulSoup
from tests.workingwithfiles import get_html_code

from parser_metro.product_lists.iproductlist import IProductList
from parser_metro.product_lists.productlist import ProductList
# from parser_metro.product_lists.productlistfactory import ProductListFactory
from parser_metro.product_lists.productlisterror import NotFoundMainBlockProduct

main_path = "../../static/html_files/"


@pytest.fixture()
def product_list(request) -> IProductList:
    html_code = get_html_code(request.param)
    bs: BeautifulSoup = BeautifulSoup(html_code)
    product_list: IProductList = ProductList(bs)
    return product_list


@pytest.mark.parametrize('product_list', [main_path + "list_product.html"],
                         indirect=['product_list'])
def test_search_urls_product_when_html_code_right(product_list: IProductList) -> None:
    # ACT
    product_list.search_urls_product()
    # ACCESS
    assert len(product_list.urls_product) == 30


@pytest.mark.parametrize('product_list', [main_path + "list_product_without_page_products.html"],
                         indirect=['product_list'])
def test_search_urls_product_when_html_code_without_page_products(product_list: IProductList) -> None:
    # ACT
    with pytest.raises(NotFoundMainBlockProduct):
        product_list.search_urls_product()
