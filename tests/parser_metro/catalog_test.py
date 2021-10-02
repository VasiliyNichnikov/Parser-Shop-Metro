import pytest

from bs4 import BeautifulSoup
from parser_metro.catalog import Catalog
from parser_metro.catalogfactory import CatalogFactory
from tests.additional_methods import get_bs

main_path = "../../static/html_files/"


@pytest.fixture()
def catalog(request) -> Catalog:
    bs: BeautifulSoup = get_bs(request.param)
    catalog: Catalog = CatalogFactory.build(bs)
    return catalog


@pytest.mark.parametrize("catalog", [main_path + "list_product.html"], indirect=["catalog"])
def test_init_max_page_and_product_list(catalog: Catalog) -> None:
    # ACT
    catalog.init_max_page_and_product_list()
    # ASSERT
    assert catalog.max_page[0] is True
    assert catalog.product_list[0] is True


@pytest.mark.parametrize("catalog", [main_path + "list_product_without_page_products.html"], indirect=["catalog"])
def test_init_max_page_and_product_list_with_error_in_product_list(catalog: Catalog) -> None:
    # ACT
    catalog.init_max_page_and_product_list()
    # ASSERT
    assert catalog.max_page[0] is True
    assert catalog.product_list[0] is False
