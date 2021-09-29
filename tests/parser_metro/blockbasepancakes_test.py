import pytest

from tests.workingwithfiles import get_html_code

from bs4 import BeautifulSoup
from parser_metro.product.block_base.blockbase import BlockBase

main_path_pancakes: str = "../../static/html_files/pancakes.html"
path_pancakes_without_code_and_title: str = "../../static/html_files/pancakes_without_code_and_title.html"


@pytest.fixture()
def init_block_base_pancakes() -> BlockBase:
    html_code: str = get_html_code(main_path_pancakes)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_base: BlockBase = BlockBase(bs)
    return block_base


@pytest.fixture()
def init_block_base_without_code_and_title() -> BlockBase:
    html_code: str = get_html_code(path_pancakes_without_code_and_title)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_base: BlockBase = BlockBase(bs)
    return block_base


def test_get_title(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Блинчики с мясом Metro Chef замороженные, 1кг"


def test_get_code(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "411281"


def test_get_brand(init_block_base_pancakes) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base_pancakes
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "METRO CHEF"


def test_pancakes_without_title(init_block_base_without_code_and_title) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base_without_code_and_title
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Not Title"


def test_pancakes_without_code(init_block_base_without_code_and_title) -> None:
    # ARRANGE
    block_base: BlockBase = init_block_base_without_code_and_title
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "Not Code"
