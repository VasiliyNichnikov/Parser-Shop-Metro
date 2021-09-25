from tests.workingwithfiles import get_html_code

from parser_metro.product_catalog.cataloglistfactory import CatalogListFactory
from parser_metro.product_catalog.icataloglist import ICatalogList


main_path: str = "../../static/html_files/"


def test_search_max_page_with_html_code_right() -> None:
    # ARRANGE
    html_code_right: str = get_html_code(main_path + "list_product.html")
    catalog_list: ICatalogList = CatalogListFactory().build(html_code_right)
    # ACT
    catalog_list.search_max_page()
    # ASSERT
    assert catalog_list.max_page == 34


def test_search_max_page_with_html_code_without_catalog_items() -> None:
    # ARRANGE
    html_code_without_catalog_items: str = get_html_code(main_path + "list_product_without_catalog_item.html")
    catalog_list: ICatalogList = CatalogListFactory().build(html_code_without_catalog_items)
    # ACT
    catalog_list.search_max_page()
    # ASSERT
    assert catalog_list.max_page == 1