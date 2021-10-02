import pytest
from bs4 import BeautifulSoup

from tests.additional_methods import get_bs

from parser_metro.product_catalog.searchmaxpage import SearchMaxPage
from parser_metro.product_catalog.isearchmax import ISearchMax

main_path: str = "../../static/html_files/"


@pytest.fixture()
def search_max(request) -> ISearchMax:
    bs: BeautifulSoup = get_bs(request.param)
    search_max: ISearchMax = SearchMaxPage(bs)
    return search_max


@pytest.mark.parametrize("search_max", [main_path + "list_product.html"],
                         indirect=["search_max"])
def test_search_max_page_with_html_code_right(search_max: ISearchMax) -> None:
    # ACT
    search_max.search_data()
    # ASSERT
    assert search_max.max_page == 34


@pytest.mark.parametrize("search_max", [main_path + "list_product_without_catalog_item.html"],
                         indirect=["search_max"])
def test_search_max_page_with_html_code_without_catalog_items(search_max: ISearchMax) -> None:
    # ACT
    search_max.search_data()
    # ASSERT
    assert search_max.max_page == 1


