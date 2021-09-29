import pytest
from tests.workingwithfiles import get_html_code

from bs4 import BeautifulSoup
from parser_metro.product.block_specifications.blockspecifications import BlockSpecifications
from parser_metro.product.block_specifications.blockspecificationserror import NotFindProductPageTab

main_path_pancakes: str = "../../static/html_files/pancakes.html"
path_pancakes_without_product_page_tab: str = "../../static/html_files/pancakes_without_product_page_tab.html"


@pytest.fixture()
def init_block_specifications_pancakes() -> BlockSpecifications:
    html_code: str = get_html_code(main_path_pancakes)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_specifications: BlockSpecifications = BlockSpecifications(bs)
    return block_specifications


@pytest.fixture()
def init_block_specifications_without_product_page_tab() -> BlockSpecifications:
    html_code: str = get_html_code(path_pancakes_without_product_page_tab)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_specifications: BlockSpecifications = BlockSpecifications(bs)
    return block_specifications


def test_get_specifications(init_block_specifications_pancakes) -> None:
    # ARRANGE
    block_specifications: BlockSpecifications = init_block_specifications_pancakes
    # ACT
    block_specifications.search_data()
    # ASSERT
    assert block_specifications.specifications == {'тип': 'блины', 'страна': 'россия'}


def test_get_description(init_block_specifications_pancakes) -> None:
    # ARRANGE
    block_specifications: BlockSpecifications = init_block_specifications_pancakes
    # ACT
    block_specifications.search_data()
    # ASSERT
    assert block_specifications.description.split()[0] == "Блинчики"


def test_catching_error_not_find_product_page_tab(init_block_specifications_without_product_page_tab) -> None:
    # ARRANGE
    block_specifications: BlockSpecifications = init_block_specifications_without_product_page_tab
    # ACT
    with pytest.raises(NotFindProductPageTab):
        block_specifications.search_data()
