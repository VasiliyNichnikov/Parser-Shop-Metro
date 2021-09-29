import pytest

from tests.workingwithfiles import get_html_code

from bs4 import BeautifulSoup
from parser_metro.product.block_base.blockbase import BlockBase
from parser_metro.product.block_base.blockbaseerror import NotFindPageDesc

main_path_sheepmeat: str = "../../static/html_files/sheepmeat.html"
path_sheepmeat_without_product_page_disc = "../../static/html_files/sheepmeat_without_product_page_desc.html"


@pytest.fixture()
def init_block_base() -> BlockBase:
    html_code: str = get_html_code(main_path_sheepmeat)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_base: BlockBase = BlockBase(bs)
    return block_base


@pytest.fixture()
def init_block_base_without_product_page_disc() -> BlockBase:
    html_code: str = get_html_code(path_sheepmeat_without_product_page_disc)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_base: BlockBase = BlockBase(bs)
    return block_base


def test_get_title(init_block_base) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Баранина для плова охлажденная вакуумная упаковка МЯСО ЕСТЬ!"


def test_get_code(init_block_base) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "563516"


def test_get_brand(init_block_base) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "МЯСО ЕСТЬ!"


def test_catching_error_not_find_page_desc(init_block_base_without_product_page_disc):
    # ARRANGE
    block_base: BlockBase = init_block_base_without_product_page_disc
    # ACT
    with pytest.raises(NotFindPageDesc):
        block_base.search_data()
