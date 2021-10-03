from selenium import webdriver
from requests import get, Response

url: str = "https://msk.metro-cc.ru/category/bezalkogolnye-napitki/pityevaya-voda-kulery/rioba-negazirovannaya-033-l"
# response: Response = get(url)
# page: str = response.text
# print(page)
path_file = "static/html_products/water_rioba.html"


with webdriver.Chrome("static/chromedriver.exe") as driver:
    driver.get(url)
    page: str = driver.page_source

    with open(path_file, 'w', encoding="utf-8") as write_file:
        write_file.write(page)
