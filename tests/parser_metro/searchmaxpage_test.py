import pytest
from bs4 import BeautifulSoup

from tests.workingwithfiles import get_html_code

from parser_metro.product_catalog.searchmaxpage import SearchMaxPage
from parser_metro.product_catalog.isearchmax import ISearchMax

main_path: str = "../../static/html_files/"


@pytest.fixture()
def search_max_page(request) -> ISearchMax:
    html_code: str = get_html_code(request.param)
    bs: BeautifulSoup = BeautifulSoup(html_code)
    search_max: ISearchMax = SearchMaxPage(bs)
    return search_max


@pytest.mark.parametrize('search_max_page', [main_path + "pancakes_without_old_price.html"],
                         indirect=['search_max_page'])
def test_search_max_page_with_html_code_right(search_max_page: ISearchMax) -> None:
    # ACT
    search_max_page.search_data()
    # ASSERT
    assert search_max_page.max_page == 34


@pytest.mark.parametrize('search_max_page', [main_path + "pancakes_without_old_price.html"],
                         indirect=['search_max_page'])
def test_search_max_page_with_html_code_without_catalog_items(search_max_page: ISearchMax) -> None:
    # ACT
    search_max_page.search_data()
    # ASSERT
    assert search_max_page.max_page == 1
