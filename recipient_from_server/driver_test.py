import time


from seleniumwire import webdriver
# from selenium import webdriver

PROXY_HOST = '176.53.164.160'  # rotating proxy or host
PROXY_PORT = 30001  # port
PROXY_USER = 'v_nichnikov_gmail_co'  # username
PROXY_PASS = '6ffcd8bd7d'  # password


def get_chromedriver(use_proxy=False, user_agent=None):
    path = "../static/chromedriver.exe"
    chrome_options = webdriver.ChromeOptions()

    options = {
        'proxy': {
            'http': f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
            'https': f'https://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
            'no_proxy': 'localhost,127.0.0.1'
        }

        # 'proxy': {
        #     # 'http': f'http://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
        #     'https': f'https://{PROXY_USER}:{PROXY_PASS}@{PROXY_HOST}:{PROXY_PORT}',
        # }
    }
    driver = webdriver.Chrome(path, seleniumwire_options=options)
    return driver


def main():
    driver = get_chromedriver(use_proxy=True)
    driver.get('https://httpbin.org/ip')
    time.sleep(10)


if __name__ == '__main__':
    main()

# import time
#
# from recipient_from_server.proxy import Proxy
# from selenium.webdriver.chrome.options import Options
# from recipient_from_server.iwebdriver import IWebDriver
# from recipient_from_server.chromewebdriver import ChromeWebDriver
#
#
# if __name__ == "__main__":
#     host: str = "213.166.88.149"
#     port: str = "30036"
#     login: str = "v_nichnikov_gmail_co"
#     password: str = "6ffcd8bd7d"
#     proxy: Proxy = Proxy(host, port,login, password)
#
#     options: Options = Options()
#
#     url: str = "https://msk.metro-cc.ru/search?q=Мясо"
#
#     webdriver: IWebDriver = ChromeWebDriver("../static/chromedriver.exe")
#     webdriver.create(options)
#     webdriver.driver.get(url)
#     time.sleep(10)
