import pytest
# noinspection PyUnresolvedReferences
from init_blocks import block_base

from parser_metro.product.block_base.blockbase import IBlockBase
from parser_metro.product.block_base.blockbaseerror import NotFindPageDesc

main_path: str = "../../static/html_files/"


@pytest.mark.parametrize("block_base", [main_path + "sheepmeat.html"], indirect=["block_base"])
def test_get_title(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Баранина для плова охлажденная вакуумная упаковка МЯСО ЕСТЬ!"


@pytest.mark.parametrize("block_base", [main_path + "sheepmeat.html"], indirect=["block_base"])
def test_get_code(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "563516"


@pytest.mark.parametrize("block_base", [main_path + "sheepmeat.html"], indirect=["block_base"])
def test_get_brand(block_base: IBlockBase) -> None:
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "МЯСО ЕСТЬ!"


@pytest.mark.parametrize("block_base", [main_path + "sheepmeat_without_product_page_desc.html"],
                         indirect=["block_base"])
def test_catching_error_not_find_page_desc(block_base: IBlockBase):
    # ACT
    with pytest.raises(NotFindPageDesc):
        block_base.search_data()
