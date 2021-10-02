import pytest

from tests.additional_methods import get_bs

from bs4 import BeautifulSoup

from parser_metro.product.block_base.blockbase import BlockBase, IBlockBase


@pytest.fixture()
def block_base(request) -> IBlockBase:
    bs: BeautifulSoup = get_bs(request.param)
    block_base: BlockBase = BlockBase(bs)
    return block_base


from parser_metro.product.block_images.blockimages import BlockImages, IBlockImages


@pytest.fixture()
def block_images(request) -> IBlockImages:
    bs: BeautifulSoup = get_bs(request.param)
    block_images: BlockImages = BlockImages(bs)
    return block_images


from parser_metro.product.block_price.blockprice import BlockPrice, IBlockPrice


@pytest.fixture()
def block_price(request) -> IBlockPrice:
    bs: BeautifulSoup = get_bs(request.param)
    block_price: BlockPrice = BlockPrice(bs)
    return block_price


from parser_metro.product.block_specifications.blockspecifications import BlockSpecifications, IBlockSpecifications


@pytest.fixture()
def block_specifications(request) -> IBlockSpecifications:
    bs: BeautifulSoup = get_bs(request.param)
    block_specifications: BlockSpecifications = BlockSpecifications(bs)
    return block_specifications
