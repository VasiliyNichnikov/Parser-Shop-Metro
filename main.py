from parser.parser_package import Parser
from parser.parser_product import ParserProduct


if __name__ == "__main__":
    p = Parser("https://msk.metro-cc.ru/search?q=мясо", "static/chromedriver")
    p.search_data()
    for url in p.urls:
        print(url)
        test_product = ParserProduct(url, "static/chromedriver")
        test_product.run()
