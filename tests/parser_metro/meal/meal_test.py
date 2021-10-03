import pytest
from bs4 import BeautifulSoup
from parser_metro.product.productfactory import ProductFactory
from parser_metro.product.product import Product
from parser_metro.meal.meal import Meal
from tests.additional_methods import get_bs

main_path: str = "../../../static/html_products/"


@pytest.fixture()
def meal(request) -> Meal:
    bs: BeautifulSoup = get_bs(request.param)
    product: Product = ProductFactory.build(bs)
    return Meal(product)


@pytest.mark.parametrize("meal", [main_path + "calf_is_shin.html"], indirect=["meal"])
def test_init_product_calf_is_shin(meal: Meal):
    # ACT
    meal.init_product()
    # ARRANGE
    assert meal.article_number == 54768
    assert meal.name == "Оссобуко Мясо есть! из телячьей голяшки на кости, 400г"
    assert meal.price == 379
    assert meal.price_without_discount == 0
    assert meal.main_image == "https://cdn.metro-cc.ru/ru/ru_pim_44128001001_01.png?maxwidth=480&maxheight=460&format=jpg&quality=80"
    assert meal.additional_images == [
        "https://cdn.metro-cc.ru/ru/ru_pim_44128001001_02.png?maxwidth=480&maxheight=460&format=jpg&quality=80"]
    assert meal.article_images == ["44128001001", "44128001001"]
    assert meal.brand == "МЯСО ЕСТЬ!"
    assert meal.annotation == "Оссобуко из телячьей голяшки на кости охлажденное "
    assert meal.type_product == "телятина"
    assert meal.minimum_storage_temperature == "0"
    assert meal.maximum_storage_temperature == "4"
    assert meal.structure == "0"
    assert meal.weight == "400"
    assert meal.shelf_life == "12"
    assert meal.packing_width == 0
    assert meal.packing_height == 0
    assert meal.packing_length == 0


@pytest.mark.parametrize("meal", [main_path + "case_losing_weight_in_week.html"], indirect=["meal"])
def test_init_product_case_losing_weight_in_week(meal: Meal):
    # ACT
    meal.init_product()
    # ARRANGE
    assert meal.article_number == 624996
    assert meal.name == "Кейс ХУДЕЕМ ЗА НЕДЕЛЮ традиционное меню с мясом, 718 г"
    assert meal.price == 679
    assert meal.price_without_discount == 869
    assert meal.main_image == "https://cdn.metro-cc.ru/ru/ru_pim_496763001001_01.png?maxwidth=480&maxheight=460&format=jpg&quality=80"
    assert meal.additional_images == []
    assert meal.article_images == ["496763001001"]
    assert meal.brand == "ХУДЕЕМ ЗА НЕДЕЛЮ"
    assert meal.type_product == "0"
    assert meal.minimum_storage_temperature == "0"
    assert meal.maximum_storage_temperature == "0"
    assert meal.structure == "0"
    assert meal.weight == "0"
    assert meal.shelf_life == "0"
    assert meal.packing_width == 0
    assert meal.packing_height == 0
    assert meal.packing_length == 0


@pytest.mark.parametrize("meal", [main_path + "water_rioba.html"], indirect=["meal"])
def test_init_product_water_rioba(meal: Meal):
    # ACT
    meal.init_product()
    # ARRANGE
    assert meal.article_number == 568823
    assert meal.name == "Вода RIOBA негазированная, 0,33л"
    assert meal.price == 42.90
    assert meal.price_without_discount == 0
    assert meal.main_image == "https://cdn.metro-cc.ru/ru/ru_pim_379361001001_01.png?maxwidth=480&maxheight=460&format=jpg&quality=80"
    assert meal.additional_images == []
    assert meal.article_images == ["379361001001"]
    assert meal.brand == "RIOBA"
    assert meal.type_product == "негазированная"
    assert meal.minimum_storage_temperature == "0"
    assert meal.maximum_storage_temperature == "0"
    assert meal.structure == "0"
    assert meal.weight == "0"
    assert meal.shelf_life == "0"
    assert meal.packing_width == 0
    assert meal.packing_height == 0
    assert meal.packing_length == 0