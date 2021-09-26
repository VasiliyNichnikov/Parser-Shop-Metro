import pytest

from tests.workingwithfiles import get_html_code

from parser_metro.product.block_base.blockbasefactory import BlockBaseFactory
from parser_metro.product.block_base.iblockbase import IBlockBase
from parser_metro.product.block_base.blockbaseerror import NotFindPageDesc

main_path_sheepmeat: str = "../../static/html_files/sheepmeat.html"
path_sheepmeat_without_product_page_disc = "../../static/html_files/sheepmeat_without_product_page_desc.html"


@pytest.fixture()
def init_block_base_sheepmeat(request) -> IBlockBase:
    html_code: str = get_html_code(main_path_sheepmeat)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    return block_base


@pytest.fixture()
def init_block_base_sheepmeat_without_product_page_disc(request) -> IBlockBase:
    html_code: str = get_html_code(path_sheepmeat_without_product_page_disc)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    return block_base


def test_get_title(init_block_base_sheepmeat) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_sheepmeat
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Баранина для плова охлажденная вакуумная упаковка МЯСО ЕСТЬ!"


def test_get_code(init_block_base_sheepmeat) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_sheepmeat
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "563516"


def test_get_brand(init_block_base_sheepmeat) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_sheepmeat
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "МЯСО ЕСТЬ!"


def test_catching_error_not_find_page_desc(init_block_base_sheepmeat_without_product_page_disc):
    # ARRANGE
    block_base: IBlockBase = init_block_base_sheepmeat_without_product_page_disc
    # ACT
    with pytest.raises(NotFindPageDesc):
        block_base.search_data()
