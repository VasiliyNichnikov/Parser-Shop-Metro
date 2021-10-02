import pytest
from bs4 import BeautifulSoup
from parser_metro.product_lists.urlproducterror import NotFoundCatalogItemDefaultImage
from parser_metro.product_lists.urlproduct import UrlProduct
from parser_metro.product_lists.iurlproduct import IUrlProduct

html_code_right: str = """<div data-productid="641098" class="catalog-item">
                                                <div class="catalog-item__block">
                                                    <div class="catalog-item__top">
                                                        <div class="catalog-item_text"><a
                                                                href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                class="catalog-item_name">
                                                            Мясо крабовое Metro Chef, 200 г
                                                        </a>
                                                            <div class="catalog-item_article">
                                                                Арт. 641098
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item_group"><!---->
                                                            <div class="catalog-item_icons"></div>
                                                            <div class="catalog-item_defaut-image"><a
                                                                    href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                    class="catalog-item_image"
                                                                    data-src="https://cdn.metro-cc.ru/ru/ru_pim_528235001001_01.png?maxwidth=230&amp;maxheight=160&amp;format=jpg&amp;quality=80"
                                                                    lazy="loaded"
                                                                    style="background-image: url(&quot;https://cdn.metro-cc.ru/ru/ru_pim_528235001001_01.png?maxwidth=230&amp;maxheight=160&amp;format=jpg&amp;quality=80&quot;);"></a>
                                                            </div>
                                                            <div class="catalog-item_block"><!---->
                                                                <div class="catalog-item_bottom">
                                                                    <div class="catalog-item_cost">
                                                                        <div class="catalog-item_price"><!---->
                                                                            <div class="catalog-item_price-current">
                                                                                <!---->
                                                                                130 <i class="ruble-symbol">₽</i><span>/шт</span>
                                                                                <span class="catalog-item_price-hint">
					?
					<span class="catalog-item_price-tooltip"><p>Указанная цена действует <br> только при заказе онлайн</p></span></span>
                                                                                <!----></div>
                                                                        </div> <!----> <!----></div>
                                                                    <div class="catalog-item_in-pack catalog-item_mobile-stock"><span
                                                                            class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                                    </div>
                                                                    <div class="catalog-item_buy catalog-item_buy_btn--dark">
                                                                        <button type="button"
                                                                                class="catalog-item_buy_btn gtm_fam_click_catalog">
                                                                            <svg xmlns="http://www.w3.org/2000/svg"
                                                                                 width="26" height="24"
                                                                                 viewBox="0 0 26 24"
                                                                                 class="catalog-item_buy_btn-icon">
                                                                                <path data-name="Forma 1 copy 2"
                                                                                      d="M10.8 18.376a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.829-1.87zm7.406 0a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.832-1.87zm4.665-10.555H8.953l-.038.012v-.012s-.2-1.73-.313-2.448-1.867-1.614-5.644-3.434c-.889-.38-1.632 1.278 0 2.149L5.936 5.51a1.62 1.62 0 01.752.962c.06.553 1.267 9.71 1.267 9.71a1.263 1.263 0 001.179 1.271H20.5a1.221 1.221 0 001.136-1.015L23.884 9.6s.669-1.779-1.013-1.779zm-2.776 7.429H9.816l-.226-1.84h11.039zm1.038-3.586H9.375L9.134 9.7H21.7z"
                                                                                      fill="#fff"
                                                                                      fill-rule="evenodd"></path>
                                                                            </svg>
                                                                            <span>В корзину</span></button>
                                                                    </div> <!----></div>
                                                                <div class="catalog-item_in-pack catalog-item_desktop-stock"><span
                                                                        class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="catalog-item__hidden">
                                                        <div class="catalog-item__hidden-content"><!----> <!---->
                                                            <div class="catalog-item_title-tc"><p>В центре оптовой
                                                                торговли</p> <a href="#">
                                                                ?
                                                                <span class="catalog-item_tooltip"><p>Цены многоуровневого ценника<br> действуют только при покупке товара<br> в торговом центре</p></span></a>
                                                            </div>
                                                            <div class="catalog-item_cost _yellow">
                                                                <div class="catalog-item_price-lvl"><!---->
                                                                    <div class="catalog-item_price-lvl_current"><!---->
                                                                        130 <i class="ruble-symbol">₽</i><!----> <!---->
                                                                        <!----></div>
                                                                </div>
                                                                <div class="catalog-item_discount-lvl">
                                                                    от
                                                                    <b>
                                                                        1 шт
                                                                    </b></div>
                                                                <div class="catalog-item_available catalog-item_available--mobile">
                                                                    <a href="#"
                                                                       class="catalog-line-item__no-request"><span><svg
                                                                            width="16" height="16" viewBox="0 0 16 16"
                                                                            fill="none"
                                                                            xmlns="http://www.w3.org/2000/svg"><path
                                                                            d="M13.174 10.263V7.08c0-2.142-1.4-3.937-3.348-4.632C9.704 1.637 8.913 1 8 1s-1.643.637-1.826 1.447c-1.948.695-3.348 2.49-3.348 4.632v3.184C2.826 11.247 2.035 12 1 12h14c-1.035 0-1.826-.753-1.826-1.737z"
                                                                            stroke="#fff" stroke-width="2"
                                                                            stroke-miterlimit="10"
                                                                            stroke-linecap="round"
                                                                            stroke-linejoin="round"></path><path
                                                                            d="M10 13a1 1 0 10-2 0 1 1 0 10-2 0c0 1.119.881 2 2 2s2-.881 2-2z"
                                                                            stroke="#fff" stroke-width="2"
                                                                            stroke-miterlimit="10"
                                                                            stroke-linecap="round"
                                                                            stroke-linejoin="round"></path></svg></span>
                                                                        <p>Сообщить о поступлении</p></a></div>
                                                            </div> <!---->
                                                            <div class="catalog-item_stock">
                                                                <div class="catalog-item_stock-scale _ends"><span
                                                                        class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                </div>
                                                                <a href="#" class="catalog-item_stock-status">Заканчивается</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="catalog-item__mobile">
                                                    <div class="catalog-item__mobile-top">
                                                        <div class="catalog-item__mobile-img"><!---->
                                                            <div class="catalog-item_defaut-image"><a
                                                                    href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                    class="catalog-item_image"
                                                                    data-src="https://cdn.metro-cc.ru/ru/ru_pim_528235001001_01.png?maxwidth=230&amp;maxheight=160&amp;format=jpg&amp;quality=80"
                                                                    lazy="loading"
                                                                    style="background-image: url(&quot;/_nuxt/img/preloader.e23aafd.gif&quot;);"></a>
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item__mobile-info"><!----> <a
                                                                href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                class="catalog-item_name">
                                                            Мясо крабовое Metro Chef, 200 г
                                                        </a>
                                                            <div class="catalog-item_article">
                                                                Арт. 641098
                                                            </div>
                                                            <div class="catalog-item_icons"></div>
                                                        </div>
                                                    </div>
                                                    <div class="catalog-item__mobile-bottom">
                                                        <div class="catalog-item__mobile-price">
                                                            <div class="catalog-item_cost">
                                                                <div class="catalog-item_price"><!---->
                                                                    <div class="catalog-item_price-current"><!---->
                                                                        130
                                                                        <i class="ruble-symbol">₽</i><span>/шт</span>
                                                                        <span class="catalog-item_price-hint">
					?
					<span class="catalog-item_price-tooltip"><p>Указанная цена действует <br> только при заказе онлайн</p></span></span>
                                                                        <!----></div>
                                                                </div> <!----> <!----></div>
                                                            <div class="catalog-item_in-pack catalog-item_mobile-stock"><span
                                                                    class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item__mobile-btn">
                                                            <div class="catalog-item_buy catalog-item_buy_btn--dark">
                                                                <button type="button"
                                                                        class="catalog-item_buy_btn gtm_fam_click_catalog">
                                                                    <svg xmlns="http://www.w3.org/2000/svg" width="26"
                                                                         height="24" viewBox="0 0 26 24"
                                                                         class="catalog-item_buy_btn-icon">
                                                                        <path data-name="Forma 1 copy 2"
                                                                              d="M10.8 18.376a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.829-1.87zm7.406 0a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.832-1.87zm4.665-10.555H8.953l-.038.012v-.012s-.2-1.73-.313-2.448-1.867-1.614-5.644-3.434c-.889-.38-1.632 1.278 0 2.149L5.936 5.51a1.62 1.62 0 01.752.962c.06.553 1.267 9.71 1.267 9.71a1.263 1.263 0 001.179 1.271H20.5a1.221 1.221 0 001.136-1.015L23.884 9.6s.669-1.779-1.013-1.779zm-2.776 7.429H9.816l-.226-1.84h11.039zm1.038-3.586H9.375L9.134 9.7H21.7z"
                                                                              fill="#fff" fill-rule="evenodd"></path>
                                                                    </svg>
                                                                    <span>В корзину</span></button>
                                                            </div> <!----> <!----></div>
                                                    </div> <!----></div>
                                            </div>"""
html_code_without_catalog_default_image: str = """<div data-productid="641098" class="catalog-item">
                                                <div class="catalog-item__block">
                                                    <div class="catalog-item__top">
                                                        <div class="catalog-item_text"><a
                                                                href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                class="catalog-item_name">
                                                            Мясо крабовое Metro Chef, 200 г
                                                        </a>
                                                            <div class="catalog-item_article">
                                                                Арт. 641098
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item_group"><!---->
                                                            <div class="catalog-item_icons"></div>
                                                            
                                                            <div class="catalog-item_block"><!---->
                                                                <div class="catalog-item_bottom">
                                                                    <div class="catalog-item_cost">
                                                                        <div class="catalog-item_price"><!---->
                                                                            <div class="catalog-item_price-current">
                                                                                <!---->
                                                                                130 <i class="ruble-symbol">₽</i><span>/шт</span>
                                                                                <span class="catalog-item_price-hint">
					?
					<span class="catalog-item_price-tooltip"><p>Указанная цена действует <br> только при заказе онлайн</p></span></span>
                                                                                <!----></div>
                                                                        </div> <!----> <!----></div>
                                                                    <div class="catalog-item_in-pack catalog-item_mobile-stock"><span
                                                                            class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                                    </div>
                                                                    <div class="catalog-item_buy catalog-item_buy_btn--dark">
                                                                        <button type="button"
                                                                                class="catalog-item_buy_btn gtm_fam_click_catalog">
                                                                            <svg xmlns="http://www.w3.org/2000/svg"
                                                                                 width="26" height="24"
                                                                                 viewBox="0 0 26 24"
                                                                                 class="catalog-item_buy_btn-icon">
                                                                                <path data-name="Forma 1 copy 2"
                                                                                      d="M10.8 18.376a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.829-1.87zm7.406 0a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.832-1.87zm4.665-10.555H8.953l-.038.012v-.012s-.2-1.73-.313-2.448-1.867-1.614-5.644-3.434c-.889-.38-1.632 1.278 0 2.149L5.936 5.51a1.62 1.62 0 01.752.962c.06.553 1.267 9.71 1.267 9.71a1.263 1.263 0 001.179 1.271H20.5a1.221 1.221 0 001.136-1.015L23.884 9.6s.669-1.779-1.013-1.779zm-2.776 7.429H9.816l-.226-1.84h11.039zm1.038-3.586H9.375L9.134 9.7H21.7z"
                                                                                      fill="#fff"
                                                                                      fill-rule="evenodd"></path>
                                                                            </svg>
                                                                            <span>В корзину</span></button>
                                                                    </div> <!----></div>
                                                                <div class="catalog-item_in-pack catalog-item_desktop-stock"><span
                                                                        class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                                </div>
                                                            </div>
                                                        </div>
                                                    </div>
                                                    <div class="catalog-item__hidden">
                                                        <div class="catalog-item__hidden-content"><!----> <!---->
                                                            <div class="catalog-item_title-tc"><p>В центре оптовой
                                                                торговли</p> <a href="#">
                                                                ?
                                                                <span class="catalog-item_tooltip"><p>Цены многоуровневого ценника<br> действуют только при покупке товара<br> в торговом центре</p></span></a>
                                                            </div>
                                                            <div class="catalog-item_cost _yellow">
                                                                <div class="catalog-item_price-lvl"><!---->
                                                                    <div class="catalog-item_price-lvl_current"><!---->
                                                                        130 <i class="ruble-symbol">₽</i><!----> <!---->
                                                                        <!----></div>
                                                                </div>
                                                                <div class="catalog-item_discount-lvl">
                                                                    от
                                                                    <b>
                                                                        1 шт
                                                                    </b></div>
                                                                <div class="catalog-item_available catalog-item_available--mobile">
                                                                    <a href="#"
                                                                       class="catalog-line-item__no-request"><span><svg
                                                                            width="16" height="16" viewBox="0 0 16 16"
                                                                            fill="none"
                                                                            xmlns="http://www.w3.org/2000/svg"><path
                                                                            d="M13.174 10.263V7.08c0-2.142-1.4-3.937-3.348-4.632C9.704 1.637 8.913 1 8 1s-1.643.637-1.826 1.447c-1.948.695-3.348 2.49-3.348 4.632v3.184C2.826 11.247 2.035 12 1 12h14c-1.035 0-1.826-.753-1.826-1.737z"
                                                                            stroke="#fff" stroke-width="2"
                                                                            stroke-miterlimit="10"
                                                                            stroke-linecap="round"
                                                                            stroke-linejoin="round"></path><path
                                                                            d="M10 13a1 1 0 10-2 0 1 1 0 10-2 0c0 1.119.881 2 2 2s2-.881 2-2z"
                                                                            stroke="#fff" stroke-width="2"
                                                                            stroke-miterlimit="10"
                                                                            stroke-linecap="round"
                                                                            stroke-linejoin="round"></path></svg></span>
                                                                        <p>Сообщить о поступлении</p></a></div>
                                                            </div> <!---->
                                                            <div class="catalog-item_stock">
                                                                <div class="catalog-item_stock-scale _ends"><span
                                                                        class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                    <span class="catalog-item_stock-scale_item"></span>
                                                                </div>
                                                                <a href="#" class="catalog-item_stock-status">Заканчивается</a>
                                                            </div>
                                                        </div>
                                                    </div>
                                                </div>
                                                <div class="catalog-item__mobile">
                                                    <div class="catalog-item__mobile-top">
                                                        <div class="catalog-item__mobile-img"><!---->
                                                            <div class="catalog-item_defaut-image"><a
                                                                    href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                    class="catalog-item_image"
                                                                    data-src="https://cdn.metro-cc.ru/ru/ru_pim_528235001001_01.png?maxwidth=230&amp;maxheight=160&amp;format=jpg&amp;quality=80"
                                                                    lazy="loading"
                                                                    style="background-image: url(&quot;/_nuxt/img/preloader.e23aafd.gif&quot;);"></a>
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item__mobile-info"><!----> <a
                                                                href="/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
                                                                class="catalog-item_name">
                                                            Мясо крабовое Metro Chef, 200 г
                                                        </a>
                                                            <div class="catalog-item_article">
                                                                Арт. 641098
                                                            </div>
                                                            <div class="catalog-item_icons"></div>
                                                        </div>
                                                    </div>
                                                    <div class="catalog-item__mobile-bottom">
                                                        <div class="catalog-item__mobile-price">
                                                            <div class="catalog-item_cost">
                                                                <div class="catalog-item_price"><!---->
                                                                    <div class="catalog-item_price-current"><!---->
                                                                        130
                                                                        <i class="ruble-symbol">₽</i><span>/шт</span>
                                                                        <span class="catalog-item_price-hint">
					?
					<span class="catalog-item_price-tooltip"><p>Указанная цена действует <br> только при заказе онлайн</p></span></span>
                                                                        <!----></div>
                                                                </div> <!----> <!----></div>
                                                            <div class="catalog-item_in-pack catalog-item_mobile-stock"><span
                                                                    class="catalog-item_in-pack_total-price">
    130&nbsp;<i class="ruble-symbol">₽</i></span> / 1 шт
                                                            </div>
                                                        </div>
                                                        <div class="catalog-item__mobile-btn">
                                                            <div class="catalog-item_buy catalog-item_buy_btn--dark">
                                                                <button type="button"
                                                                        class="catalog-item_buy_btn gtm_fam_click_catalog">
                                                                    <svg xmlns="http://www.w3.org/2000/svg" width="26"
                                                                         height="24" viewBox="0 0 26 24"
                                                                         class="catalog-item_buy_btn-icon">
                                                                        <path data-name="Forma 1 copy 2"
                                                                              d="M10.8 18.376a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.829-1.87zm7.406 0a1.87 1.87 0 11-1.829 1.87 1.849 1.849 0 011.832-1.87zm4.665-10.555H8.953l-.038.012v-.012s-.2-1.73-.313-2.448-1.867-1.614-5.644-3.434c-.889-.38-1.632 1.278 0 2.149L5.936 5.51a1.62 1.62 0 01.752.962c.06.553 1.267 9.71 1.267 9.71a1.263 1.263 0 001.179 1.271H20.5a1.221 1.221 0 001.136-1.015L23.884 9.6s.669-1.779-1.013-1.779zm-2.776 7.429H9.816l-.226-1.84h11.039zm1.038-3.586H9.375L9.134 9.7H21.7z"
                                                                              fill="#fff" fill-rule="evenodd"></path>
                                                                    </svg>
                                                                    <span>В корзину</span></button>
                                                            </div> <!----> <!----></div>
                                                    </div> <!----></div>
                                            </div>"""
ready_url: str = "https://msk.metro-cc.ru/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"


@pytest.fixture()
def url_product(request) -> IUrlProduct:
    bs4: BeautifulSoup = BeautifulSoup(request.param, "lxml")
    url_product: IUrlProduct = UrlProduct(bs4)
    return url_product


@pytest.mark.parametrize('url_product', [html_code_right],
                         indirect=['url_product'])
def test_search_url_then_html_code_right(url_product: IUrlProduct) -> None:
    # ACT
    url_product.search_url()
    # ACCESS
    assert url_product.url == ready_url


@pytest.mark.parametrize('url_product', [html_code_without_catalog_default_image],
                         indirect=['url_product'])
def test_search_url_then_html_code_without_catalog_default_image(url_product: IUrlProduct) -> None:
    # ACT
    with pytest.raises(NotFoundCatalogItemDefaultImage):
        url_product.search_url()
