import pytest

# noinspection PyUnresolvedReferences
from init_blocks import block_images

from parser_metro.product.block_images.blockimages import IBlockImages
from parser_metro.product.block_images.blockimageserror import NotFindPageSwiper

main_path: str = "../../static/html_files/"


@pytest.mark.parametrize("block_images", [main_path + "pancakes.html"], indirect=["block_images"])
def test_get_pancakes_main_image(block_images: IBlockImages) -> None:
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.main_image == \
           "https://cdn.metro-cc.ru/ru/ru_pim_502041001001_01.png?maxwidth=480&maxheight=460&format=jpg&quality=80"


@pytest.mark.parametrize("block_images", [main_path + "pancakes.html"], indirect=["block_images"])
def test_get_pancakes_urls_additional(block_images: IBlockImages) -> None:
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.urls_additional == []


@pytest.mark.parametrize("block_images", [main_path + "pancakes_without_page_swiper.html"], indirect=["block_images"])
def test_pancakes_catching_error_not_find_page_swiper(block_images: IBlockImages) -> None:
    # ACT
    with pytest.raises(NotFindPageSwiper):
        block_images.search_data()


@pytest.mark.parametrize("block_images", [main_path + "sheepmeat.html"], indirect=["block_images"])
def test_sheepmeat_urls_additional(block_images: IBlockImages) -> None:
    # ACT
    block_images.search_data()
    # ASSERT
    assert block_images.urls_additional == [
        "https://cdn.metro-cc.ru/ru/ru_pim_382497001001_02.png?maxwidth=480&maxheight=460&format=jpg&quality=80"]
