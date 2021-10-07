from bs4 import BeautifulSoup
from recipient_from_server.chromewebdriver import ChromeWebDriver
from recipient_from_server.iwebdriver import IWebDriver


url: str = "https://msk.metro-cc.ru/search?q=мясо"
path_driver: str = "../../static/chromedriver"


def test_get_page_bs() -> None:
    # ARRANGE
    driver: IWebDriver = ChromeWebDriver(path_driver)
    # ACT
    bs = driver.get_page_bs(url)
    # ASSERT
    # assert isinstance(bs, BeautifulSoup)

