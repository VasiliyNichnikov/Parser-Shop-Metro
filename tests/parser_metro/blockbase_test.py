from tests.workingwithfiles import get_html_code

from parser_metro.product.block_base.blockbasefactory import BlockBaseFactory
from parser_metro.product.block_base.iblockbase import IBlockBase

main_path_sheepmeat: str = "../../static/html_files/sheepmeat.html"
main_path_pancakes: str = "../../static/html_files/pancakes.html"


def test_get_title_sheepmeat() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_sheepmeat)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Баранина для плова охлажденная вакуумная упаковка МЯСО ЕСТЬ!"


def test_get_code_sheepmeat() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_sheepmeat)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "563516"


def test_get_brand_speepmeat() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_sheepmeat)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "МЯСО ЕСТЬ!"


def test_get_title_pancakes() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_pancakes)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.title == "Блинчики с мясом Metro Chef замороженные, 1кг"


def test_get_code_pancakes() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_pancakes)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.code == "411281"


def test_get_brand_pancakes() -> None:
    # ARRANGE
    html_code: str = get_html_code(main_path_pancakes)
    block_base: IBlockBase = BlockBaseFactory.build(html_code)
    # ACT
    block_base.search_data()
    # ASSERT
    assert block_base.brand == "METRO CHEF"
