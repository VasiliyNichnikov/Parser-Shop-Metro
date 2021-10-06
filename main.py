from recipient_from_server.chromewebdriver import IWebDriver, ChromeWebDriver
from parser_metro.parser import Parser

path_driver: str = "static/chromedriver.exe"
url: str = "https://msk.metro-cc.ru/search?q=мясо"


if __name__ == "__main__":
    driver: IWebDriver = ChromeWebDriver(path_driver)
    parser = Parser(driver, url)
    parser.run()
    driver.close()
