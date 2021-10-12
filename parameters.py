import os
from typing import List, Union


class Parameters:
    def __init__(self, data: dict) -> None:
        self.__data = data
        self.__urls: str = "urls"
        self.__number_attempts_in_case_of_error: str = "number_attempts_in_case_of_error"
        self.__delay_after_error: str = "delay_after_error"
        self.__hide_browser: str = "hide_browser"
        self.__path_database: str = "path_database"
        self.__path_excel: str = "path_excel"
        self.__path_webdriver: str = "path_webdriver"
        self.__path_interface: str = "path_interface"

    @property
    def urls(self) -> Union[List[str], None]:
        if self.__check_key(self.__urls):
            return self.__data[self.__urls]
        return None

    @urls.setter
    def urls(self, value: List[str]) -> None:
        if self.__check_key(self.__urls):
            self.__data[self.__urls] = value

    @property
    def number_attempts_in_case_of_error(self) -> Union[int, None]:
        if self.__check_key(self.__number_attempts_in_case_of_error):
            return self.__data[self.__number_attempts_in_case_of_error]
        return None

    @number_attempts_in_case_of_error.setter
    def number_attempts_in_case_of_error(self, value: int) -> None:
        if self.__check_key(self.__number_attempts_in_case_of_error) and isinstance(value, int):
            self.__data[self.__number_attempts_in_case_of_error] = value

    @property
    def delay_after_error(self) -> Union[int, None]:
        if self.__check_key(self.__delay_after_error):
            return self.__data[self.__delay_after_error]
        return None

    @delay_after_error.setter
    def delay_after_error(self, value: int) -> None:
        if self.__check_key(self.__delay_after_error) and isinstance(value, int):
            self.__data[self.__delay_after_error] = value

    @property
    def hide_browser(self) -> bool:
        if self.__check_key(self.__hide_browser):
            return self.__data[self.__hide_browser]
        return False

    @hide_browser.setter
    def hide_browser(self, value: bool) -> None:
        if self.__check_key(self.__hide_browser) and isinstance(value, bool):
            self.__data[self.__hide_browser] = value

    @property
    def path_database(self) -> Union[str, None]:
        if self.__check_key(self.__path_database) and os.path.exists(self.__data[self.__path_database]):
            return self.__data[self.__path_database]
        return None

    @path_database.setter
    def path_database(self, value: str):
        if self.__check_key(self.__path_database) and os.path.exists(value):
            self.__data[self.__path_database] = value

    @property
    def path_excel(self) -> Union[str, None]:
        if self.__check_key(self.__path_excel) and os.path.exists(self.__data[self.__path_excel]):
            return self.__data[self.__path_excel]
        return None

    @path_excel.setter
    def path_excel(self, value: str):
        if self.__check_key(self.__path_excel) and os.path.exists(value):
            self.__data[self.__path_excel] = value

    @property
    def path_webdriver(self) -> Union[str, None]:
        if self.__check_key(self.__path_webdriver) and os.path.exists(self.__data[self.__path_webdriver]):
            return self.__data[self.__path_webdriver]
        return None

    @path_webdriver.setter
    def path_webdriver(self, value: str) -> None:
        if self.__check_key(self.__path_webdriver) and os.path.exists(value):
            self.__data[self.__path_webdriver] = value

    @property
    def path_interface(self) -> Union[str, None]:
        if self.__check_key(self.__path_interface) and os.path.exists(self.__data[self.__path_interface]):
            return self.__data[self.__path_interface]
        return None

    @path_interface.setter
    def path_interface(self, value: str) -> None:
        if self.__check_key(self.__path_interface) and os.path.exists(value):
            self.__data[self.__path_interface] = value

    def __check_key(self, key):
        return key in self.__data.keys()
