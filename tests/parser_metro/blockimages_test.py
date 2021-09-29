import pytest
from bs4 import BeautifulSoup

from tests.workingwithfiles import get_html_code

from parser_metro.product.block_images.blockimages import BlockImages
from parser_metro.product.block_images.blockimageserror import NotFindPageSwiper

main_path_pancakes: str = "../../static/html_files/pancakes.html"
main_path_sheepmeat: str = "../../static/html_files/sheepmeat.html"
path_without_page_swiper: str = "../../static/html_files/pancakes_without_page_swiper.html"


@pytest.fixture()
def init_block_images_pancakes() -> BlockImages:
    html_code: str = get_html_code(main_path_pancakes)
    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")

    block_images: BlockImages = BlockImages(bs)
    return block_images


@pytest.fixture()
def init_block_images_sheepmeat() -> BlockImages:
    html_code: str = get_html_code(main_path_sheepmeat)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_images: BlockImages = BlockImages(bs)
    return block_images


@pytest.fixture()
def init_block_images_without_page_swiper() -> BlockImages:
    html_code: str = get_html_code(path_without_page_swiper)

    bs: BeautifulSoup = BeautifulSoup(html_code, "lxml")
    block_images: BlockImages = BlockImages(bs)
    return block_images


def test_get_pancakes_main_image(init_block_images_pancakes) -> None:
    # ARRANGE
    block_images: BlockImages = init_block_images_pancakes
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.main_image == \
           "https://cdn.metro-cc.ru/ru/ru_pim_502041001001_01.png?maxwidth=480&maxheight=460&format=jpg&quality=80"


def test_get_pancakes_urls_additional(init_block_images_pancakes) -> None:
    # ARRANGE
    block_images: BlockImages = init_block_images_pancakes
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.urls_additional == []


def test_pancakes_catching_error_not_find_page_swiper(init_block_images_without_page_swiper) -> None:
    # ARRANGE
    block_images: BlockImages = init_block_images_without_page_swiper
    # ACT
    with pytest.raises(NotFindPageSwiper):
        block_images.search_data()


def test_sheepmeat_urls_additional(init_block_images_sheepmeat) -> None:
    # ARRANGE
    block_images: BlockImages = init_block_images_sheepmeat
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.urls_additional == [
        "https://cdn.metro-cc.ru/ru/ru_pim_382497001001_01.png?maxheight=64&maxwidth=64&format=jpg&quality=80",
        "https://cdn.metro-cc.ru/ru/ru_pim_382497001001_02.png?maxheight=64&maxwidth=64&format=jpg&quality=80"]
