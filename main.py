from database import db_session
from recipient_from_server.chromewebdriver import IWebDriver, ChromeWebDriver
from parser_metro.parser import Parser

path_driver: str = "static/chromedriver.exe"
path_database: str = "static/database/product.db"
url: str = "https://msk.metro-cc.ru/search?q=мясо"

if __name__ == "__main__":
    db_session.global_init(path_database)
    driver: IWebDriver = ChromeWebDriver(path_driver)
    parser = Parser(driver, url, 10, 10)
    parser.run()
    driver.close()
