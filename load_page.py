from selenium import webdriver
from requests import get, Response

url: str = "https://msk.metro-cc.ru/search?q=Мясо"
# response: Response = get(url)
# page: str = response.text
# print(page)
path_file = "static/list_product.html"



with webdriver.Chrome("static/chromedriver.exe") as driver:
    driver.get(url)
    page: str = driver.page_source

    with open(path_file, 'w', encoding="utf-8") as write_file:
        write_file.write(page)
