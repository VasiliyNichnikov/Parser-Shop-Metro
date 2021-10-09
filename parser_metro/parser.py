from typing import List
from parser_metro.parserproduct import ParserProduct
from parser_metro.parsercatalog import ParserCatalog
from recipient_from_server.chromewebdriver import IWebDriver


class Parser:
    def __init__(self, driver: IWebDriver, default_url: str) -> None:
        self.__url = default_url
        self.__driver = driver

    def run(self) -> None:
        catalog = ParserCatalog(self.__driver, self.__url)

        for page in range(2, catalog.max_page + 1):
            urls_products: List[str] = catalog.urls
            print(f"Page: {page}; Urls: {urls_products}; Number urls: {len(urls_products)}")
            for url in urls_products:
                print(f"Url product: {url}")
                parser_product = ParserProduct(self.__driver, url)
                parser_product.run()

            url_page = self.__url + f"&page={page}"
            catalog = ParserCatalog(self.__driver, url_page)
