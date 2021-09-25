from selenium import webdriver
from requests import get, Response

url: str = "https://msk.metro-cc.ru/category/myasnye/baranina/baranina-ohlazhdennaya/dlya-plova-vakuumnaya-upakovka-myaso-est"
# response: Response = get(url)
# page: str = response.text
# print(page)
path_file = "static/html_files/sheepmeat.html"


with webdriver.Chrome("static/chromedriver.exe") as driver:
    driver.get(url)
    page: str = driver.page_source

    with open(path_file, 'w', encoding="utf-8") as write_file:
        write_file.write(page)
