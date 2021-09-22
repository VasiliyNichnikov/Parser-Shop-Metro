def get_html_code(path: str) -> str:
    with open(path, "r", encoding="UTF-8") as reading:
        return reading.read()
