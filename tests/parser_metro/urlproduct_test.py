import pytest
from bs4 import BeautifulSoup
from parser_metro.catalog.product_lists.urlproducterror import NotFoundCatalogItemDefaultImage
from parser_metro.catalog.product_lists.urlproduct import UrlProduct
from parser_metro.catalog.product_lists.iurlproduct import IUrlProduct
from tests.additional_methods import get_bs

main_path = "../../static/html_files/"


@pytest.fixture()
def url_product(request) -> IUrlProduct:
	bs: BeautifulSoup = get_bs(request.param)
	url_product: IUrlProduct = UrlProduct(bs)
	return url_product


@pytest.mark.parametrize('url_product', [main_path + "url_product.html"], indirect=['url_product'])
def test_search_url_then_html_code_right(url_product: IUrlProduct) -> None:
	# ACT
	url_product.search_url()
	# ACCESS
	assert url_product.url == "https://msk.metro-cc.ru/category/rybnye/krabovoe-myaso-palochki/russkoe-more-200g"


@pytest.mark.parametrize('url_product', [main_path + "url_product_without_catalog_default_image.html"],
						 indirect=['url_product'])
def test_search_url_then_html_code_without_catalog_default_image(url_product: IUrlProduct) -> None:
	# ACT
	with pytest.raises(NotFoundCatalogItemDefaultImage):
		url_product.search_url()
