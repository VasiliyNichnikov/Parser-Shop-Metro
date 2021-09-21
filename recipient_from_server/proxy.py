import typing

from selenium.webdriver.common.desired_capabilities import DesiredCapabilities


class Proxy:
    @property
    def capabilities(self) -> dict:
        return self.__capabilities

    def __init__(self, host: str, port: str, login: str = None, password: str = None):
        self.__proxy: typing.Dict = {
            "address": f"{host}:{port}",
            "username": login,
            "password": password
        }
        self.__capabilities = dict(DesiredCapabilities.CHROME)
        self.__capabilities["proxy"] = {
            "proxyType": "MANUAL",
            "httpProxy": self.__proxy["address"],
            "ftpProxy": self.__proxy["address"],
            "sslProxy": self.__proxy["address"],
            "noProxy": "",
            # "class": "org.openqa.selenium.Proxy",
            "autodetect": False
        }
        self.__capabilities["proxy"]["socksUsername"] = self.__proxy["username"]
        self.__capabilities["proxy"]["socksPassword"] = self.__proxy["password"]
