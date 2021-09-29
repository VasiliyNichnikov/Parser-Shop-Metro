import pytest

from parser_metro.product.product import Product
from parser_metro.product.productfactory import ProductFactory
from tests.workingwithfiles import get_html_code

path_pancakes: str = "../../static/html_files/pancakes.html"
path_sheepmeat_without_product_page_disc: str = "../../static/html_files/sheepmeat_without_product_page_desc.html"


def test_initialization_blocks():
    # ARRANGE
    html_code: str = get_html_code(path_pancakes)
    product: Product = ProductFactory.build(html_code)
    # ACT
    product.init_blocks()
    # ASSERT
    assert product.base[0] is True
    assert product.images[0] is True
    assert product.specifications[0] is True
    assert product.price[0] is True


def test_initialization_blocks_with_error_in_base():
    # ARRANGE
    html_code: str = get_html_code(path_sheepmeat_without_product_page_disc)
    product: Product = ProductFactory.build(html_code)
    # ACT
    product.init_blocks()
    # ASSERT
    assert product.base[0] is False
    assert product.images[0] is True
    assert product.specifications[0] is True
    assert product.price[0] is True
