import pytest

# noinspection PyUnresolvedReferences
from init_blocks import block_price
from parser_metro.product.block_price.blockprice import IBlockPrice
from parser_metro.product.block_price.blockpriceerror import NotFindPriceCardHead

main_path: str = "../../static/html_files/"


@pytest.mark.parametrize("block_price", [main_path + "pancakes.html"], indirect=["block_price"])
def test_get_main_price(block_price: IBlockPrice) -> None:
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.main_price == "339"


@pytest.mark.parametrize("block_price", [main_path + "pancakes.html"], indirect=["block_price"])
def test_get_old_price(block_price: IBlockPrice) -> None:
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.old_price == "401.01"


@pytest.mark.parametrize("block_price", [main_path + "pancakes_without_old_price.html"], indirect=["block_price"])
def test_get_old_price_from_html_without_old_price(block_price: IBlockPrice) -> None:
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.old_price == "0"


@pytest.mark.parametrize("block_price", [main_path + "pancakes_without_price_card_head.html"], indirect=["block_price"])
def test_catching_error_not_find_price_card_head(block_price: IBlockPrice) -> None:
    # ACT
    with pytest.raises(NotFindPriceCardHead):
        block_price.search_data()
