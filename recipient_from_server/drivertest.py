import time
from selenium.webdriver import Chrome
from recipient_from_server.proxy import Proxy
from recipient_from_server.iproxy import IProxy
from recipient_from_server.iwebdriver import IWebDriver
from recipient_from_server.chromewebdriver import ChromeWebDriver

if __name__ == "__main__":
    host: str = "176.53.164.160"
    port: str = "30001"
    login: str = "v_nichnikov_gmail_co"
    password: str = "6ffcd8bd7d"
    proxy: IProxy = Proxy(host, port, login, password)

    chrome_driver: IWebDriver = ChromeWebDriver("../static/chromedriver.exe")
    chrome_driver.create(options=None, proxy=proxy)
    driver: Chrome = chrome_driver.driver
    driver.get("https://httpbin.org/ip")
    time.sleep(10)