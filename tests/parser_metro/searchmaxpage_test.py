import pytest
from bs4 import BeautifulSoup

from tests.additional_methods import get_bs

from parser_metro.catalog.max_page.searchmaxpage import SearchMaxPage
from parser_metro.catalog.max_page.isearchmaxpage import ISearchMaxPage

main_path: str = "../../static/html_files/"


@pytest.fixture()
def search_max(request) -> ISearchMaxPage:
    bs: BeautifulSoup = get_bs(request.param)
    search_max: ISearchMaxPage = SearchMaxPage(bs)
    return search_max


@pytest.mark.parametrize("search_max", [main_path + "list_product.html"],
                         indirect=["search_max"])
def test_search_max_page_with_html_code_right(search_max: ISearchMaxPage) -> None:
    # ACT
    search_max.search_data()
    # ASSERT
    assert search_max.max_page == 34


@pytest.mark.parametrize("search_max", [main_path + "list_product_without_catalog_item.html"],
                         indirect=["search_max"])
def test_search_max_page_with_html_code_without_catalog_items(search_max: ISearchMaxPage) -> None:
    # ACT
    search_max.search_data()
    # ASSERT
    assert search_max.max_page == 1


