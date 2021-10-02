from bs4 import BeautifulSoup


def get_html_code(path: str) -> str:
    with open(path, "r", encoding="UTF-8") as reading:
        return reading.read()


def get_bs(path: str):
    html_code: str = get_html_code(path)
    return BeautifulSoup(html_code, "lxml")