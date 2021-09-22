import typing
from recipient_from_server.iproxy import IProxy


class Proxy(IProxy):
    @property
    def options(self) -> typing.Dict:
        field_for_http_https: str = f"{self.__login}:{self.__password}@{self.__host}:{self.__port}"
        return {
            "proxy": {
                "http": f"http://{field_for_http_https}",
                "https": f"https://{field_for_http_https}",
                "no_proxy": "localhost,127.0.0.1"
            }
        }

    def __init__(self, host: str, port: str, login: str = None, password: str = None):
        self.__host = host
        self.__port = port
        self.__login = login
        self.__password = password
