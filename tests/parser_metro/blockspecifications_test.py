import pytest

# noinspection PyUnresolvedReferences
from init_blocks import block_specifications

from parser_metro.product.block_specifications.blockspecifications import IBlockSpecifications
from parser_metro.product.block_specifications.blockspecificationserror import NotFindProductPageTab

main_path: str = "../../static/html_files/"


@pytest.mark.parametrize("block_specifications", [main_path + "pancakes.html"], indirect=["block_specifications"])
def test_get_specifications(block_specifications: IBlockSpecifications) -> None:
    # ACT
    block_specifications.search_data()
    # ASSERT
    assert block_specifications.specifications == {'тип': 'блины', 'страна': 'россия'}


@pytest.mark.parametrize("block_specifications", [main_path + "pancakes.html"], indirect=["block_specifications"])
def test_get_description(block_specifications: IBlockSpecifications) -> None:
    # ACT
    block_specifications.search_data()
    # ASSERT
    assert block_specifications.description.split()[0] == "Блинчики"


@pytest.mark.parametrize("block_specifications", [main_path + "pancakes_without_product_page_tab.html"],
                         indirect=["block_specifications"])
def test_catching_error_not_find_product_page_tab(block_specifications: IBlockSpecifications) -> None:
    # ACT
    with pytest.raises(NotFindProductPageTab):
        block_specifications.search_data()
