from typing import List
from parser_metro.parserproduct import ParserProduct
from parser_metro.parserlisturls import ParserListUrls
from recipient_from_server.chromewebdriver import IWebDriver


class Parser:
    def __init__(self, driver: IWebDriver, default_url: str) -> None:
        self.__url = default_url
        self.__driver = driver
        self.__max_page = ParserListUrls(driver, default_url).max_page

    def run(self) -> None:
        for page in range(1, self.__max_page + 1):
            url_page = self.__url + f"&page={page}"
            urls_products: List[str] = ParserListUrls(self.__driver, url_page).urls
            print(f"Page: {page}; Urls: {urls_products}; Number urls: {len(urls_products)}")
            for url in urls_products:
                print(f"Url product: {url}")
                parser_product = ParserProduct(self.__driver, url)
                parser_product.run()
