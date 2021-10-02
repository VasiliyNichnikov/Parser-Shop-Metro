import pytest

from bs4 import BeautifulSoup
from parser_metro.product.product import Product
from parser_metro.product.productfactory import ProductFactory
from tests.additional_methods import get_bs

main_path: str = "../../static/html_files/"


@pytest.fixture()
def product(request) -> Product:
    bs: BeautifulSoup = get_bs(request.param)
    product: Product = ProductFactory.build(bs)
    return product


@pytest.mark.parametrize("product", [main_path + "pancakes.html"], indirect=["product"])
def test_initialization_blocks(product: Product):
    # ACT
    product.init_blocks()
    # ASSERT
    assert product.base[0] is True
    assert product.images[0] is True
    assert product.specifications[0] is True
    assert product.price[0] is True


@pytest.mark.parametrize("product", [main_path + "sheepmeat_without_product_page_desc.html"], indirect=["product"])
def test_initialization_blocks_with_error_in_base(product: Product):
    # ACT
    product.init_blocks()
    # ASSERT
    assert product.base[0] is False
    assert product.images[0] is True
    assert product.specifications[0] is True
    assert product.price[0] is True
