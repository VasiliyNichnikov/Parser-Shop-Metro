import pytest

from tests.workingwithfiles import get_html_code

from parser_metro.product.block_base.blockbasefactory import BlockBaseFactory
from parser_metro.product.block_base.iblockbase import IBlockBase

main_path_pancakes: str = "../../static/html_files/pancakes.html"
path_pancakes_without_code_and_title: str = "../../static/html_files/pancakes_without_code_and_title.html"


@pytest.fixture()
def init_block_base_pancakes(request) -> IBlockBase:
    html_code: str = get_html_code(main_path_pancakes)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    return block_base


@pytest.fixture()
def init_block_base_without_code_and_title() -> IBlockBase:
    html_code: str = get_html_code(path_pancakes_without_code_and_title)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    return block_base


def test_get_title(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Блинчики с мясом Metro Chef замороженные, 1кг"


def test_get_code(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "411281"


def test_get_brand(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "METRO CHEF"


def test_pancakes_without_title(init_block_base_without_code_and_title) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_without_code_and_title
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Not Title"


def test_pancakes_without_code(init_block_base_without_code_and_title) -> None:
    # ARRANGE
    block_base: IBlockBase = init_block_base_without_code_and_title
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "Not Code"
