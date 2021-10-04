def is_digit(str_number: str) -> bool:
    if str_number.isdigit():
        return True
    else:
        try:
            float(str_number)
            return True
        except ValueError:
            return False


def get_number_float(str_number: str) -> float:
    if ',' in str_number:
        str_number = str_number.replace(',', '.')
    if is_digit(str_number):
        return float(str_number)
    return 0


def get_number_int(str_number: str) -> int:
    if str_number.isdigit():
        return int(str_number)
    return 0
