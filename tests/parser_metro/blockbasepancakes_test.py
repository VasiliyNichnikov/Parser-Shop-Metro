import pytest
# noinspection PyUnresolvedReferences
from init_blocks import block_base
from parser_metro.product.block_base.blockbase import IBlockBase

main_path: str = "../../static/html_files/"


@pytest.mark.parametrize("block_base", [main_path + "pancakes.html"], indirect=["block_base"])
def test_get_title(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Блинчики с мясом Metro Chef замороженные, 1кг"


@pytest.mark.parametrize("block_base", [main_path + "pancakes.html"], indirect=["block_base"])
def test_get_code(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "411281"


@pytest.mark.parametrize("block_base", [main_path + "pancakes.html"], indirect=["block_base"])
def test_get_brand(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "METRO CHEF"


@pytest.mark.parametrize("block_base", [main_path + "pancakes_without_code_and_title.html"], indirect=["block_base"])
def test_pancakes_without_title(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "0"


@pytest.mark.parametrize("block_base", [main_path + "pancakes_without_code_and_title.html"], indirect=["block_base"])
def test_pancakes_without_code(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "0"
