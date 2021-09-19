from requests import get, Response

url: str = "https://msk.metro-cc.ru/category/rybnye/krabovoe-myaso-palochki/myaso-krabovoe-metro-chef-200-g"
response: Response = get(url)
page: str = response.text
print(page)
path_file = "static/meat.html"

with open(path_file, 'wb') as write_file:
    write_file.write(response.content)
