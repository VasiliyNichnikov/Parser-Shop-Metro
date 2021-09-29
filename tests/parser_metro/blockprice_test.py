import pytest
from bs4 import BeautifulSoup

from tests.workingwithfiles import get_html_code

from parser_metro.product.block_price.blockprice import BlockPrice
from parser_metro.product.block_price.blockpriceerror import NotFindPriceCardHead

main_path_pancakes: str = "../../static/html_files/pancakes.html"
pancakes_without_old_price: str = "../../static/html_files/pancakes_without_old_price.html"
pancakes_without_price_card_head: str = "../../static/html_files/pancakes_without_price_card_head.html"


@pytest.fixture()
def init_block_price_pancakes() -> BlockPrice:
    html_code: str = get_html_code(main_path_pancakes)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_price: BlockPrice = BlockPrice(bs)
    return block_price


@pytest.fixture()
def init_block_without_old_price() -> BlockPrice:
    html_code: str = get_html_code(pancakes_without_old_price)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_price: BlockPrice = BlockPrice(bs)
    return block_price


@pytest.fixture()
def init_block_without_price_card_head() -> BlockPrice:
    html_code: str = get_html_code(pancakes_without_price_card_head)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_price: BlockPrice = BlockPrice(bs)
    return block_price


def test_get_main_price(init_block_price_pancakes) -> None:
    # ARRANGE
    block_price: BlockPrice = init_block_price_pancakes
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.main_price == "339"


def test_get_old_price(init_block_price_pancakes) -> None:
    # ARRANGE
    block_price: BlockPrice = init_block_price_pancakes
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.old_price == "401.01"


def test_get_old_price_from_html_without_old_price(init_block_without_old_price) -> None:
    # ARRANGE
    block_price: BlockPrice = init_block_without_old_price
    # ACT
    block_price.search_data()
    # ASSERT
    assert block_price.old_price == "Not old price"


def test_catching_error_not_find_price_card_head(init_block_without_price_card_head) -> None:
    # ARRANGE
    block_price: BlockPrice = init_block_without_price_card_head
    # ACT
    with pytest.raises(NotFindPriceCardHead):
        block_price.search_data()
